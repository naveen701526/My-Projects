// Phone Constructor
class Phone {
    constructor(name, number, relation) {
        this.name = name;
        this.number = number;
        this.relation = relation;
    }
}

// UI Constructor
class UI {
    // Clear Fields
    clearFields() {
        document.getElementById('relation').value = 'Sister';
        document.getElementById('number').value = '';
        document.getElementById('name').value = '';
    }

    addPhoneToList(phone) {
        const list = document.getElementById('number-list');
        // Create tr element
        const row = document.createElement('tr');
        // Insert cols
        row.innerHTML = `
    <td>${phone.name}</td>
    <td>${phone.number}</td>
    <td>${phone.relation}</td>
    <td><a href="#" class="delete"><i class="fas fa-times-circle"></i><a></td>
  `;

        list.appendChild(row);
    }

    // Show Alert
    showAlert(message, className) {
        // Create div
        const div = document.createElement('div');
        // Add classes
        div.className = `alert ${className} text-center`;

        // Add Attribute
        div.setAttribute('role', 'alert');
        // Add text
        div.appendChild(document.createTextNode(message));
        // Get parent
        const container = document.querySelector('.container');
        // Get form
        const form = document.querySelector('#number-form');
        // Insert alert
        container.insertBefore(div, form);

        // Timeout after 3 sec
        setTimeout(function () {
            document.querySelector('.alert').remove();
        }, 3000);
    }

    // Delete Book
    deletePhone(target) {
        if (target.parentElement.className == 'delete') {
            target.parentElement.parentElement.parentElement.remove();
        }
    }
}

// Local Storage Class
class Store {
    static getPhone() {
        let phones;
        if (localStorage.getItem('phones') === null) {
            phones = [];
        } else {
            phones = JSON.parse(localStorage.getItem('phones'));
        }

        return phones;
    }

    static displayPhones() {
        const phones = Store.getPhone();

        phones.forEach(function (phone) {
            const ui = new UI();

            // Add phone to UI
            ui.addPhoneToList(phone);
        });
    }

    static addPhone(phone) {
        const phones = Store.getPhone();

        phones.push(phone);

        localStorage.setItem('phones', JSON.stringify(phones));
    }

    static removePhone(relation) {
        const phones = Store.getPhone();

        phones.forEach(function (book, index) {
            if (book.relation === relation) {
                phones.splice(index, 1);
            }
        });

        localStorage.setItem('phones', JSON.stringify(phones));
    }
}

// DOM Load Event
document.addEventListener('DOMContentLoaded', Store.displayPhones);

// Event Listeners
document.getElementById('number-form').addEventListener('submit', function (e) {
    // // Get form values
    const name = document.getElementById('name').value,
        number = document.getElementById('number').value,
        relation = document.getElementById('relation').value;

    // // Instantiate phone
    const phone = new Phone(name, number, relation);

    // // Instantiate UI
    const ui = new UI();

    // Validate
    if (name === '' || number === '') {
        // Error alert
        ui.showAlert('Please fill in all fields', 'alert-danger');
    } else {
        // Add phone content to list
        ui.addPhoneToList(phone);

        // Add to LS
        Store.addPhone(phone);

        // Show success
        ui.showAlert('Phone List Added!', 'alert-success');

        // Clear fields
        ui.clearFields();
    }

    e.preventDefault();
});

// Event Listener for delete
document.getElementById('number-list').addEventListener('click', (e) => {
    // Instantiate UI
    const ui = new UI();

    // Delete phone
    ui.deletePhone(e.target);

    // Remove from LS
    Store.removePhone(
        e.target.parentElement.parentElement.previousElementSibling.textContent
    );

    // Show message
    ui.showAlert('Phone Entry Removed!', 'alert-success');

    e.preventDefault();
});
