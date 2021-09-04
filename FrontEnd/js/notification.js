
// Import the functions you need from the SDKs you need
   import { initializeApp } from "https://www.gstatic.com/firebasejs/9.0.1/firebase-app.js";
import  { getMessaging, onMessage , getToken  }  from "https://www.gstatic.com/firebasejs/9.0.1/firebase-messaging.js";
// TODO: Add SDKs for Firebase products that you want to use
// https://firebase.google.com/docs/web/setup#available-libraries

// Your web app's Firebase configuration
// For Firebase JS SDK v7.20.0 and later, measurementId is optional
const firebaseConfig = {
    apiKey: "AIzaSyAErLujF4YTpHuLcIoN_QH9bNjmbV7O5sM",
    authDomain: "notificationtask-d17db.firebaseapp.com",
    projectId: "notificationtask-d17db",
    storageBucket: "notificationtask-d17db.appspot.com",
    messagingSenderId: "609671336612",
    appId: "1:609671336612:web:1103f1735097510a0f0c31",
    measurementId: "G-0P5S0WD4QV"
};

const app = initializeApp(firebaseConfig);
const messaging = getMessaging(app);
getToken(messaging, { vapidKey: 'BLIBhRtKT4-7OGBdm0zWJxP_CdnPhQ3UT4wAqGC8X1gT-G8frqTuDA7-LO8Uujnlw43nncJbAV8MKWOzx2ZWCwg' }).then((currentToken) => {
if (currentToken) {
// Send the token to your server and update the UI if necessary
// ...
} else {
  // Show permission request UI
  console.log('No registration token available. Request permission to generate one.');
  // ...
  }
}).catch((err) => {
                    console.log('An error occurred while retrieving token. ', err);
                // ...
                });
