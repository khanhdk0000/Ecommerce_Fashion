import Vue from 'vue'
import Router from 'vue-router'
import { normalizeURL, decode } from 'ufo'
import { interopDefault } from './utils'
import scrollBehavior from './router.scrollBehavior.js'

const _645e80cd = () => interopDefault(import('..\\pages\\Category.vue' /* webpackChunkName: "pages/Category" */))
const _b3f8c95a = () => interopDefault(import('..\\pages\\Checkout.vue' /* webpackChunkName: "" */))
const _79323352 = () => interopDefault(import('..\\pages\\Checkout\\Billing.vue' /* webpackChunkName: "" */))
const _17e1855d = () => interopDefault(import('..\\pages\\Checkout\\Payment.vue' /* webpackChunkName: "" */))
const _26632532 = () => interopDefault(import('..\\pages\\Checkout\\Shipping.vue' /* webpackChunkName: "" */))
const _53478de4 = () => interopDefault(import('..\\pages\\Checkout\\ThankYou.vue' /* webpackChunkName: "" */))
const _bbb4a5d6 = () => interopDefault(import('..\\pages\\Checkout.vue' /* webpackChunkName: "pages/Checkout" */))
const _9c65e3d4 = () => interopDefault(import('..\\pages\\Checkout\\Billing.vue' /* webpackChunkName: "pages/Checkout/Billing" */))
const _507c6021 = () => interopDefault(import('..\\pages\\Checkout\\Payment.vue' /* webpackChunkName: "pages/Checkout/Payment" */))
const _70e229ba = () => interopDefault(import('..\\pages\\Checkout\\Shipping.vue' /* webpackChunkName: "pages/Checkout/Shipping" */))
const _9dc6926c = () => interopDefault(import('..\\pages\\Checkout\\ThankYou.vue' /* webpackChunkName: "pages/Checkout/ThankYou" */))
const _3dfb011f = () => interopDefault(import('..\\pages\\ContactUs.vue' /* webpackChunkName: "pages/ContactUs" */))
const _287550ec = () => interopDefault(import('..\\pages\\Home.vue' /* webpackChunkName: "" */))
const _1b4ad8a4 = () => interopDefault(import('..\\pages\\Home.vue' /* webpackChunkName: "pages/Home" */))
const _44ab88bc = () => interopDefault(import('..\\pages\\MyAccount.vue' /* webpackChunkName: "pages/MyAccount" */))
const _66c87f41 = () => interopDefault(import('..\\pages\\MyAccount\\AdressBook.vue' /* webpackChunkName: "pages/MyAccount/AdressBook" */))
const _f488e9ee = () => interopDefault(import('..\\pages\\MyAccount\\BillingDetails.vue' /* webpackChunkName: "pages/MyAccount/BillingDetails" */))
const _7646dba4 = () => interopDefault(import('..\\pages\\MyAccount\\LoyaltyCard.vue' /* webpackChunkName: "pages/MyAccount/LoyaltyCard" */))
const _a31b2272 = () => interopDefault(import('..\\pages\\MyAccount\\MyNewsletter.vue' /* webpackChunkName: "pages/MyAccount/MyNewsletter" */))
const _c84810ea = () => interopDefault(import('..\\pages\\MyAccount\\MyProfile.vue' /* webpackChunkName: "pages/MyAccount/MyProfile" */))
const _39424e06 = () => interopDefault(import('..\\pages\\MyAccount\\MyReviews.vue' /* webpackChunkName: "pages/MyAccount/MyReviews" */))
const _ec90dfb0 = () => interopDefault(import('..\\pages\\MyAccount\\OrderHistory.vue' /* webpackChunkName: "pages/MyAccount/OrderHistory" */))
const _3cdd843c = () => interopDefault(import('..\\pages\\MyAccount\\ShippingDetails.vue' /* webpackChunkName: "pages/MyAccount/ShippingDetails" */))
const _6b0b6620 = () => interopDefault(import('..\\pages\\Product.vue' /* webpackChunkName: "pages/Product" */))
const _e372a566 = () => interopDefault(import('..\\pages\\ResetPassword.vue' /* webpackChunkName: "" */))
const _24d364cb = () => interopDefault(import('..\\pages\\ResetPassword.vue' /* webpackChunkName: "pages/ResetPassword" */))
const _558a1524 = () => interopDefault(import('..\\pages\\MyAccount.vue' /* webpackChunkName: "" */))
const _07b2c21c = () => interopDefault(import('..\\pages\\Product.vue' /* webpackChunkName: "" */))
const _683c6f0b = () => interopDefault(import('..\\pages\\Category.vue' /* webpackChunkName: "" */))

const emptyFn = () => {}

Vue.use(Router)

export const routerOptions = {
  mode: 'history',
  base: '/',
  linkActiveClass: 'nuxt-link-active',
  linkExactActiveClass: 'nuxt-link-exact-active',
  scrollBehavior,

  routes: [{
    path: "/Category",
    component: _645e80cd,
    name: "Category___en"
  }, {
    path: "/checkout",
    component: _b3f8c95a,
    name: "checkout___en",
    children: [{
      path: "billing",
      component: _79323352,
      name: "billing___en"
    }, {
      path: "payment",
      component: _17e1855d,
      name: "payment___en"
    }, {
      path: "shipping",
      component: _26632532,
      name: "shipping___en"
    }, {
      path: "thank-you",
      component: _53478de4,
      name: "thank-you___en"
    }]
  }, {
    path: "/Checkout",
    component: _bbb4a5d6,
    name: "Checkout___en",
    children: [{
      path: "Billing",
      component: _9c65e3d4,
      name: "Checkout-Billing___en"
    }, {
      path: "Payment",
      component: _507c6021,
      name: "Checkout-Payment___en"
    }, {
      path: "Shipping",
      component: _70e229ba,
      name: "Checkout-Shipping___en"
    }, {
      path: "ThankYou",
      component: _9dc6926c,
      name: "Checkout-ThankYou___en"
    }]
  }, {
    path: "/ContactUs",
    component: _3dfb011f,
    name: "ContactUs___en"
  }, {
    path: "/de",
    component: _287550ec,
    name: "home___de"
  }, {
    path: "/Home",
    component: _1b4ad8a4,
    name: "Home___en"
  }, {
    path: "/MyAccount",
    component: _44ab88bc,
    name: "MyAccount___en",
    children: [{
      path: "AdressBook",
      component: _66c87f41,
      name: "MyAccount-AdressBook___en"
    }, {
      path: "BillingDetails",
      component: _f488e9ee,
      name: "MyAccount-BillingDetails___en"
    }, {
      path: "LoyaltyCard",
      component: _7646dba4,
      name: "MyAccount-LoyaltyCard___en"
    }, {
      path: "MyNewsletter",
      component: _a31b2272,
      name: "MyAccount-MyNewsletter___en"
    }, {
      path: "MyProfile",
      component: _c84810ea,
      name: "MyAccount-MyProfile___en"
    }, {
      path: "MyReviews",
      component: _39424e06,
      name: "MyAccount-MyReviews___en"
    }, {
      path: "OrderHistory",
      component: _ec90dfb0,
      name: "MyAccount-OrderHistory___en"
    }, {
      path: "ShippingDetails",
      component: _3cdd843c,
      name: "MyAccount-ShippingDetails___en"
    }]
  }, {
    path: "/Product",
    component: _6b0b6620,
    name: "Product___en"
  }, {
    path: "/reset-password",
    component: _e372a566,
    name: "reset-password___en"
  }, {
    path: "/ResetPassword",
    component: _24d364cb,
    name: "ResetPassword___en"
  }, {
    path: "/de/Category",
    component: _645e80cd,
    name: "Category___de"
  }, {
    path: "/de/checkout",
    component: _b3f8c95a,
    name: "checkout___de",
    children: [{
      path: "billing",
      component: _79323352,
      name: "billing___de"
    }, {
      path: "payment",
      component: _17e1855d,
      name: "payment___de"
    }, {
      path: "shipping",
      component: _26632532,
      name: "shipping___de"
    }, {
      path: "thank-you",
      component: _53478de4,
      name: "thank-you___de"
    }]
  }, {
    path: "/de/Checkout",
    component: _bbb4a5d6,
    name: "Checkout___de",
    children: [{
      path: "Billing",
      component: _9c65e3d4,
      name: "Checkout-Billing___de"
    }, {
      path: "Payment",
      component: _507c6021,
      name: "Checkout-Payment___de"
    }, {
      path: "Shipping",
      component: _70e229ba,
      name: "Checkout-Shipping___de"
    }, {
      path: "ThankYou",
      component: _9dc6926c,
      name: "Checkout-ThankYou___de"
    }]
  }, {
    path: "/de/ContactUs",
    component: _3dfb011f,
    name: "ContactUs___de"
  }, {
    path: "/de/Home",
    component: _1b4ad8a4,
    name: "Home___de"
  }, {
    path: "/de/MyAccount",
    component: _44ab88bc,
    name: "MyAccount___de",
    children: [{
      path: "AdressBook",
      component: _66c87f41,
      name: "MyAccount-AdressBook___de"
    }, {
      path: "BillingDetails",
      component: _f488e9ee,
      name: "MyAccount-BillingDetails___de"
    }, {
      path: "LoyaltyCard",
      component: _7646dba4,
      name: "MyAccount-LoyaltyCard___de"
    }, {
      path: "MyNewsletter",
      component: _a31b2272,
      name: "MyAccount-MyNewsletter___de"
    }, {
      path: "MyProfile",
      component: _c84810ea,
      name: "MyAccount-MyProfile___de"
    }, {
      path: "MyReviews",
      component: _39424e06,
      name: "MyAccount-MyReviews___de"
    }, {
      path: "OrderHistory",
      component: _ec90dfb0,
      name: "MyAccount-OrderHistory___de"
    }, {
      path: "ShippingDetails",
      component: _3cdd843c,
      name: "MyAccount-ShippingDetails___de"
    }]
  }, {
    path: "/de/Product",
    component: _6b0b6620,
    name: "Product___de"
  }, {
    path: "/de/reset-password",
    component: _e372a566,
    name: "reset-password___de"
  }, {
    path: "/de/ResetPassword",
    component: _24d364cb,
    name: "ResetPassword___de"
  }, {
    path: "/de/my-account/:pageName?",
    component: _558a1524,
    name: "my-account___de"
  }, {
    path: "/de/p/:id/:slug",
    component: _07b2c21c,
    name: "product___de"
  }, {
    path: "/de/c/:slug_1/:slug_2?/:slug_3?/:slug_4?/:slug_5?",
    component: _683c6f0b,
    name: "category___de"
  }, {
    path: "/my-account/:pageName?",
    component: _558a1524,
    name: "my-account___en"
  }, {
    path: "/p/:id/:slug",
    component: _07b2c21c,
    name: "product___en"
  }, {
    path: "/c/:slug_1/:slug_2?/:slug_3?/:slug_4?/:slug_5?",
    component: _683c6f0b,
    name: "category___en"
  }, {
    path: "/",
    component: _287550ec,
    name: "home___en"
  }],

  fallback: false
}

export function createRouter (ssrContext, config) {
  const base = (config._app && config._app.basePath) || routerOptions.base
  const router = new Router({ ...routerOptions, base  })

  // TODO: remove in Nuxt 3
  const originalPush = router.push
  router.push = function push (location, onComplete = emptyFn, onAbort) {
    return originalPush.call(this, location, onComplete, onAbort)
  }

  const resolve = router.resolve.bind(router)
  router.resolve = (to, current, append) => {
    if (typeof to === 'string') {
      to = normalizeURL(to)
    }
    return resolve(to, current, append)
  }

  return router
}
