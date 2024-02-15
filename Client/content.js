var variableValue = false;

let url = window.location.href;

fetch("http://localhost:5000/check-url", {
  method: "POST",
  mode: "cors",
  headers: {
    "Content-type": "application/json",
    // "Origin": "*"
  },
  body: JSON.stringify({ url: url }),
})
  .then((res) => {
    if (!res.ok) console.log("Could not check the url");
    return res.json();
  })
  .then((data) => {
    // alert(data)
    // for (let key in data) {
    //   alert(`${key}: ${data[key]}`);
    // }
    if (data.result == true) {
      variableValue = true;
      // alert(variableValue);

      // alert(variableValue);
      function processExcludedSites() {
        return new Promise((resolve, reject) => {
          // Check if excluded_sites exists in storage
          chrome.storage.sync.get(null, function (data) {
            if (!data.hasOwnProperty("excluded_sites")) {
              // If excluded_sites doesn't exist, resolve the promise immediately
              resolve();
              return;
            }

            const excludedSites = data.excluded_sites;
            const dataSize = excludedSites.length;

            // Iterate over each object in the excluded_sites list
            excludedSites.forEach(function (site) {
              if (url == site.url) {
                variableValue = false;
              }
            });

            // Resolve the promise when processing is completed
            resolve();
          });
        });
      }

      function sendMessageToBackground(url, variableValue) {
        return new Promise((resolve, reject) => {
          chrome.runtime.sendMessage(
            {
              type: "getVariableValue",
              url: url,
              variableValue: variableValue,
            },
            (response) => {
              if (response && response.variableValue) {
                variableValue = response.variableValue;
                if (variableValue) {
                  // Send message to background script to open alert.html
                  chrome.runtime.sendMessage({
                    type: "openAlertPage",
                    url: url,
                  });
                }
              }
              // Resolve the promise after sending the message
              resolve();
            }
          );
        });
      }

      // Usage
      processExcludedSites()
        .then(() => {
          // Once processing is completed, call sendMessageToBackground()
          return sendMessageToBackground(url, variableValue);
        })
        .catch((error) => {
          // Handle errors if any
          console.error("Error:", error);
        });
    }
  });
