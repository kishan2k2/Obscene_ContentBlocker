





// let variableValue = true; // Default value


// // Listen for messages from other scripts

// chrome.runtime.onMessage.addListener(function(message, sender, sendResponse) {

//     if (message.type === 'getVariableValue') {
//         sendResponse({ variableValue });
//     } 
  
// });


// chrome.runtime.onMessage.addListener(function(message, sender, sendResponse) {
//     if (message.type === 'updateVariableValue') {
//         // Update variableValue based on the message received from the background script
//         console.log("working")
//         variableValue= message.variableValue;
//         url=message.url;
       

//     }
// });

console.log("this is background")
// Define the initial value for the excluded_sites list
const initialExcludedSites = [];

// Store the initial value in Chrome storage
chrome.storage.sync.set({ excluded_sites: initialExcludedSites }, function() {
    if (chrome.runtime.lastError) {
        console.error('Error setting initial value:', chrome.runtime.lastError);
    } else {
        
        console.log('Initial value for excluded_sites set successfully.');
    }
});


let variableValue = false;
chrome.runtime.onMessage.addListener(function(message, sender, sendResponse) {
    if (message.type === 'getVariableValue') {
        // Send variableValue to content script
        variableValue=message.variableValue;
        sendResponse({ variableValue });
    } else if (message.type === 'openAlertPage') {
        // Open alert.html within the extension
        // chrome.tabs.create({ url: chrome.runtime.getURL('alert.html') });
        chrome.tabs.update({ url: `alert.html?url=${encodeURIComponent(message.url)}` });

    }
});
