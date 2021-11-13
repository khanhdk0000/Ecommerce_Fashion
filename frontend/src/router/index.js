import { createRouter, createWebHistory } from 'vue-router'

import store from '../store'

import Home from '../views/Home.vue'

import Product from '../views/Product.vue'
import Category from '../views/Category.vue'
import Search from '../views/Search.vue'
import Cart from '../views/Cart.vue'
import SignUp from '../views/SignUp.vue'
import LogIn from '../views/LogIn.vue'
import MyAccount from '../views/MyAccount.vue'
import Checkout from '../views/Checkout.vue'
import Success from '../views/Success.vue'
import Favorite from '../views/Favorite.vue'
import Test from "../views/Test.vue";

const routes = [
  {
    path: '/',
    name: 'Home',
    component: Home
  },
  {
    path: '/sign-up',
    name: 'SignUp',
    component: SignUp
  },
  {
    path: '/log-in',
    name: 'LogIn',
    component: LogIn
  },
  {
    path: '/my-account',
    name: 'MyAccount',
    component: MyAccount,
    // meta: {
    //     requireLogin: true
    // }
  },
  {
    path: '/search',
    name: 'Search',
    component: Category
  },
  {
    path: '/cart',
    name: 'Cart',
    component: Cart
  },
  {
    path: '/cart/success',
    name: 'Success',
    component: Success
  },
  {
    path: '/cart/checkout',
    name: 'Checkout',
    component: Checkout,
    // meta: {
    //     requireLogin: true
    // }
  },
  {
    path: '/product/:id',
    name: 'Product',
    component: Product
  },
  {
    path: '/wishlist',
    name: 'Wishlist',
    component: Favorite
  },
  {
    path: '/test',
    name: 'Test',
    component: Test
  }
  // {
  //   path: '/category/:category_slug',
  //   name: 'Category',
  //   component: Category
  // },
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

// router.beforeEach((to, from, next) => {
//   if (to.matched.some(record => record.meta.requireLogin) && !store.state.isAuthenticated) {
//     next({ name: 'LogIn', query: { to: to.path } });
//   } else {
//     next()
//   }
// })

export default router
