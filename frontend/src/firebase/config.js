import firebase from 'firebase/compat/app';
import 'firebase/compat/auth';


// For Firebase JS SDK v7.20.0 and later, measurementId is optional

const firebaseConfig = {
  apiKey: "AIzaSyCM3SF8xOL5b3_s1jaC2fKLmO-0UrY4eG0",
  authDomain: "fashion-c165e.firebaseapp.com",
  projectId: "fashion-c165e",
  storageBucket: "fashion-c165e.appspot.com",
  messagingSenderId: "752732965965",
  appId: "1:752732965965:web:a6c0974f2c1e10971f6004"
};

// init firebase
firebase.initializeApp(firebaseConfig)

// init service
// const projectFirestore = firebase.firestore()
const projectAuth = firebase.auth()
// const projectStorage = firebase.storage()

// timestamp 
// const timestamp = firebase.firestore.FieldValue.serverTimestamp

export {projectAuth}

