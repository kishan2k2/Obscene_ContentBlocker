

chrome.storage.local.get(['userEmail', 'deviceId'], function(data) {
    if (data.userEmail && data.deviceId) {
        // Data exists, show the relevant elements
        document.getElementById('InDeviceId').textContent = data.deviceId;
        document.getElementById('InUserEmail').textContent = data.userEmail;
        document.getElementById('individualDiv').classList.remove('hidden');
        console.log("it have data")
    } else {
        // Data doesn't exist, redirect to start.html
        console.log("it does not have data");
        window.location.href = 'start.html';
        
    }
});
