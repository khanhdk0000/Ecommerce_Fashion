<template>
  <div class="page-sign-up">
    <div class="columns">
      <div class="column is-4 is-offset-4">
        <h1 class="title">Sign up</h1>

        <form @submit.prevent="handleSubmit">
          <div class="field">
            <label>User Name</label>
            <div class="control">
              <input type="text" class="input" v-model="displayName" />
            </div>
          </div>

          <div class="field">
            <label>Email</label>
            <div class="control">
              <input type="text" class="input" v-model="email" />
            </div>
          </div>

          <div class="field">
            <label>Password</label>
            <div class="control">
              <input type="password" class="input" v-model="password" />
            </div>
          </div>

          <!-- <div class="field">
            <label>Repeat password</label>
            <div class="control">
              <input type="password" class="input" v-model="password2" />
            </div>
          </div> -->

          <div class="notification is-danger" v-if="error">
            <p>{{ error }}</p>
          </div>

          <div class="field">
            <div class="control">
              <button v-if="!isPending" class="button is-dark">Sign Up</button>
              <button v-if="isPending" disabled class="button">Loading</button>
            </div>
          </div>

          <hr />

          Or <router-link to="/log-in">click here</router-link> to log in!
        </form>
      </div>
    </div>
  </div>
</template>

<script>
import axios from "axios";
import { toast } from "bulma-toast";

import useSignup from "../composables/useSignup";
import { ref } from "vue";
import { useRouter } from "vue-router";

export default {
  setup() {
    const { error, signup, isPending } = useSignup();
    const email = ref("");
    const password = ref("");
    const displayName = ref("");
    const router = useRouter();

    const handleSubmit = async () => {
      const res = await signup(email.value, password.value, displayName.value);
      if (!error.value) {
        console.log("Sign up success");
        toast({
          message: "Account created, now you can gain access to the page!",
          type: "is-success",
          dismissible: true,
          pauseOnHover: true,
          duration: 2000,
          position: "bottom-right",
        });
        // router.push({ name: "UserPlaylists" });
        router.push('/')

        //* Put user into the database
        const user = res.user;
        const userInfo = {
          'customer_id':user.uid,
          'name':user.displayName,
          'email':user.email
        };

        // console.log(userInfo);
        await axios.post('/api/user/', {
          customer_id: userInfo.customer_id,
          name: userInfo.name,
          email: userInfo.email
        })
        .then(response => {
          console.log(userInfo);
        })
        .catch(error => {
          console.log(error);
        });

      }
    };

    return {
      email,
      password,
      displayName,
      isPending,
      error,
      handleSubmit,
    };
  },
};

// export default {
//     name: 'SignUp',
//     data() {
//         return {
//             username: '',
//             password: '',
//             password2: '',
//             errors: []
//         }
//     },
//     methods: {
//         submitForm() {
//             this.errors = []

//             if (this.username === '') {
//                 this.errors.push('The username is missing')
//             }

//             if (this.password === '') {
//                 this.errors.push('The password is too short')
//             }

//             if (this.password !== this.password2) {
//                 this.errors.push('The passwords doesn\'t match')
//             }

//             if (!this.errors.length) {
//                 const formData = {
//                     username: this.username,
//                     password: this.password
//                 }

//                 axios
//                     .post("/api/v1/users/", formData)
//                     .then(response => {
//                         toast({
//                             message: 'Account created, please log in!',
//                             type: 'is-success',
//                             dismissible: true,
//                             pauseOnHover: true,
//                             duration: 2000,
//                             position: 'bottom-right',
//                         })

//                         this.$router.push('/log-in')
//                     })
//                     .catch(error => {
//                         if (error.response) {
//                             for (const property in error.response.data) {
//                                 this.errors.push(`${property}: ${error.response.data[property]}`)
//                             }

//                             console.log(JSON.stringify(error.response.data))
//                         } else if (error.message) {
//                             this.errors.push('Something went wrong. Please try again')

//                             console.log(JSON.stringify(error))
//                         }
//                     })
//             }
//         }
//     }
// }
</script>