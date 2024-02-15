const urlParams = new URLSearchParams(window.location.search);
const url = urlParams.get("url");
document
  .getElementById("backButtonInject")
  .addEventListener("click", function () {
    window.close();
  });
document
  .getElementById("proceedButtonInject")
  .addEventListener("click", function () {
    // Open the new URL in a new tab
    const variableValue = false;
    
    function appendToExcludedSites(url, variableValue) {
      return new Promise((resolve, reject) => {
        chrome.storage.sync.get({ excluded_sites: [] }, function (data) {
          // Append the new key-value pair to the list
          data.excluded_sites.push({ url: url, variableValue: variableValue });
    
          // Store the updated list back in Chrome storage
          chrome.storage.sync.set(
            { excluded_sites: data.excluded_sites },
            function () {
              if (chrome.runtime.lastError) {
                reject("Error appending to excluded_sites: " + chrome.runtime.lastError);
              } else {
                resolve("URL and boolean value appended to excluded_sites successfully.");
              }
            }
          );
        });
      });
    }
    
    function getUserData() {
      return new Promise((resolve, reject) => {
        chrome.storage.local.get(["userEmail", "deviceId"], function (data) {
          if (data.userEmail && data.deviceId) {
            // Data exists, resolve with relevant data
          
            resolve({ deviceId: data.deviceId, userEmail: data.userEmail });
          } else {
            // Data doesn't exist, reject with an error
            reject("User data not found");
          }
        });
      });
    }
    
    function sendEmailAndOpenURL(deviceId, userEmail) {
      return new Promise((resolve, reject) => {
        
        var emailBody = {
          "id": deviceId,
          "url": url,
          "email": userEmail
        };
        // alert("before sending mail")
        // alert(deviceId)
        // alert(url)
        // alert(userEmail)
        fetch("http://localhost:5000/send-email", {
          mode: "cors",
          method: "POST",
          headers: {
            "Content-type": "application/json",
            // "Origin": "*"
          },
          body: JSON.stringify(emailBody),
        })
        .then((res) => {
          if (!res.ok) {
            alert("email not working")
            reject("Error while sending the email");
          } else {
              alert("email send")
              return res.json();
            }
          })
          .then((data) => {
            if (data.result) {
              // alert("alert.js data")
              resolve("Email sent successfully");
              window.open(url, "_self");
             
            } else {
              reject("Email not sent successfully");
            }
          })
          .catch((error) => {
            reject(error);
          });
          
        // Open URL after sending email
        
        
      });
    }
    
    // Usage: Chain the promises to ensure sequential execution
    appendToExcludedSites(url, variableValue)
      .then(() => {
        return getUserData();
      })
      .then((userData) => {
        const { deviceId, userEmail } = userData;
        return sendEmailAndOpenURL(deviceId, userEmail);
      })
      .then((message) => {
        console.log(message);
      })
      .catch((error) => {
        console.error("Error:", error);
      });
    
  });