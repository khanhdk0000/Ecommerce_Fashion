<template>
  <div class="page-log-in">
    <div class="columns">
      <div class="column is-4 is-offset-4">
        <h1 class="title">Log in</h1>

        <form @submit.prevent="handleSubmit">
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

          <div class="notification is-danger" v-if="error">
            <p>{{ error }}</p>
          </div>

          <div class="field">
            <div class="control">
              <button v-if="!isPending" class="button is-dark">Log in</button>
              <button v-if="isPending" disabled class="button">Loading</button>
            </div>
          </div>

          <hr />

          Or <router-link to="/sign-up">click here</router-link> to sign up!
        </form>
      </div>
    </div>
  </div>
</template>

<script>
import axios from "axios";

import { useStore } from "vuex";
import useLogin from "../composables/useLogin";
import { ref } from "vue";
import { useRouter } from "vue-router";
import loadItems from '../composables/loadItems';

export default {
  setup() {
    const { error, login, isPending } = useLogin();
    const router = useRouter();
    const email = ref("");
    const password = ref("");
    const store = useStore();

    const handleSubmit = async () => {
      const res = await login(email.value, password.value);
      if (!error.value) {
        console.log("Logged in successfully");
        const user = res.user;
        const userInfo = {
          'customer_id': user.uid,
          'name': user.displayName,
          'email': user.email,
        };
        store.commit("setUser", userInfo);
        router.push({ name: "Home" });

        // ? Setup tokens
        const userToken = await user.getIdToken()
        store.commit("setToken", userToken);
        globalThis.localStorage.setItem('token', userToken);

        // ? Crawl data from database
        store.commit('clearCart');
        store.state.cart.items = await loadItems(userInfo.customer_id);

        globalThis.localStorage.setItem('cart', JSON.stringify(store.state.cart))
      }
    };

    return { email, password, handleSubmit, error, isPending };
  },
};

// export default {
//     name: 'LogIn',
//     data() {
//         return {
//             username: '',
//             password: '',
//             errors: []
//         }
//     },
//     mounted() {
//         document.title = 'Log In'
//     },
//     methods: {
//         async submitForm() {
//             axios.defaults.headers.common["Authorization"] = ""

//             localStorage.removeItem("token")

//             const formData = {
//                 username: this.username,
//                 password: this.password
//             }

//             await axios
//                 .post("/api/v1/token/login/", formData)
//                 .then(response => {
//                     const token = response.data.auth_token

//                     this.$store.commit('setToken', token)

//                     axios.defaults.headers.common["Authorization"] = "Token " + token

//                     localStorage.setItem("token", token)

//                     const toPath = this.$route.query.to || '/cart'

//                     this.$router.push(toPath)
//                 })
//                 .catch(error => {
//                     if (error.response) {
//                         for (const property in error.response.data) {
//                             this.errors.push(`${property}: ${error.response.data[property]}`)
//                         }
//                     } else {
//                         this.errors.push('Something went wrong. Please try again')

//                         console.log(JSON.stringify(error))
//                     }
//                 })
//         }
//     }
// }
</script>