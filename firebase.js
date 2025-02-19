// Import the functions you need from the SDKs you need
import { initializeApp } from "firebase/app";
import { getAnalytics } from "firebase/analytics";
// TODO: Add SDKs for Firebase products that you want to use
// https://firebase.google.com/docs/web/setup#available-libraries

// Your web app's Firebase configuration
// For Firebase JS SDK v7.20.0 and later, measurementId is optional
const firebaseConfig = {
  apiKey: "AIzaSyAhBA0jaS8krV3tVj43trTzWBt8rTiDbKw",
  authDomain: "chatbot-a8da4.firebaseapp.com",
  projectId: "chatbot-a8da4",
  storageBucket: "chatbot-a8da4.firebasestorage.app",
  messagingSenderId: "232473748823",
  appId: "1:232473748823:web:61422775846aa29dec4a12",
  measurementId: "G-L6TEQHJV0L"
};

// Initialize Firebase
const app = initializeApp(firebaseConfig);
const analytics = getAnalytics(app);