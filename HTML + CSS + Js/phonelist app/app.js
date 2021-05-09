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
}

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
        // Add book to list
        ui.addBookToList(phone);

        // Show success
        ui.showAlert('Phone List Added!', 'success');

        // Clear fields
        ui.clearFields();
    }

    e.preventDefault();
});
