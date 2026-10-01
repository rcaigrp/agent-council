document.getElementById('waste-form').addEventListener('submit', async (e) => {
    e.preventDefault();
    
    const name = document.getElementById('item-name').value;
    const quantity = document.getElementById('quantity').value;
    const category = document.getElementById('category').value;
    
    const response = await fetch('/api/waste', {
        method: 'POST',
        headers: {'Content-Type': 'application/json'},
        body: JSON.stringify({name, quantity, category})
    });
    
    if (response.ok) {
        loadWasteData();
        document.getElementById('waste-form').reset();
    }
});

async function loadWasteData() {
    const response = await fetch('/api/waste');
    const data = await response.json();
    
    const listElement = document.getElementById('waste-list');
    listElement.innerHTML = '';
    
    data.forEach(item => {
        const itemElement = document.createElement('div');
        itemElement.textContent = `${item.name}: ${item.quantity} (${item.category})`;
        listElement.appendChild(itemElement);
    });
}

loadWasteData();