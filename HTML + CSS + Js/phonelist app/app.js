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
        document.getElementById('relation').value = '';
        document.getElementById('number').value = '';
        document.getElementById('name').value = '';
    }

    addPhoneToList() {
        const list = document.getElementById('number-list');
        // Create tr element
        const row = document.createElement('tr');
        // Insert cols
        row.innerHTML = `
    <td>${phone.name}</td>
    <td>${phone.number}</td>
    <td>${phone.relation}</td>
    <td><a href="#" class="delete">X<a></td>
  `;

        list.appendChild(row);
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

    // // Add phone to list
    ui.addPhoneToList(phone);

    // // Clear fields
    ui.clearFields();

    e.preventDefault();
});
