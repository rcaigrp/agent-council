document.addEventListener('DOMContentLoaded', function() {
    var map = L.map('map').setView([0, 0], 2);
    L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
        maxZoom: 19,
        attribution: '© OpenStreetMap'
    }).addTo(map);

    fetch('/api/devices')
        .then(r => r.json())
        .then(devices => {
            devices.forEach(dev => {
                var lat = Math.random() * 180 - 90;
                var lng = Math.random() * 360 - 180;
                L.marker([lat, lng]).addTo(map)
                    .bindPopup(`IP: ${dev.ip}<br>Latency: ${dev.latency_ms.toFixed(1)} ms`);
            });
        })
        .catch(err => console.error('Failed to load devices', err));
});