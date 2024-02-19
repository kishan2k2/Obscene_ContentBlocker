document.getElementById('myForm').addEventListener('submit', function(event) {
    event.preventDefault();
    const userEmail = document.getElementById('userEmail').value;
    const deviceId = document.getElementById('deviceId').value;
    chrome.storage.local.set({ 'userEmail': userEmail, 'deviceId': deviceId }, function() {
        console.log('Data saved:', { 'userEmail': userEmail, 'deviceId': deviceId });
        window.location.href = 'main.html';
        
    });
});
