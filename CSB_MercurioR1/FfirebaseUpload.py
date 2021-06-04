import firebase


firebase.initializeApp({
    apiKey: "AIzaSyAlBn9vALCkHI0wwqWPrBvEOmlW56dD5FA",
    authDomain: "pi-tempsensor.firebaseapp.com",
    databaseURL: "https://pi-tempsensor-default-rtdb.firebaseio.com",
    projectId: "pi-tempsensor",
    storageBucket: "pi-tempsensor.appspot.com",
    messagingSenderId: "500750341004",
    appId: "1:500750341004:web:898fae7b81023c7b32fca9",
    measurementId: "G-J1FNHCXDMZ"
})


messaging = firebase.messaging()

database = firebase.FirebaseDatabase.getInstance()
myRef = firebase.FirebaseDatabase.getReference("message");