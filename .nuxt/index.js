import Vue from 'vue'

import Meta from 'vue-meta'
import ClientOnly from 'vue-client-only'
import NoSsr from 'vue-no-ssr'
import { createRouter } from './router.js'
import NuxtChild from './components/nuxt-child.js'
import NuxtError from '..\\layouts\\error.vue'
import Nuxt from './components/nuxt.js'
import App from './App.js'
import { setContext, getLocation, getRouteData, normalizeError } from './utils'

/* Plugins */

import nuxt_plugin_vuescrollto_540aedc0 from 'nuxt_plugin_vuescrollto_540aedc0' // Source: .\\vue-scrollto.js (mode: 'client')
import nuxt_plugin_cookieuniversalnuxt_09bea671 from 'nuxt_plugin_cookieuniversalnuxt_09bea671' // Source: .\\cookie-universal-nuxt.js (mode: 'all')
import nuxt_plugin_pluginutils_43737e76 from 'nuxt_plugin_pluginutils_43737e76' // Source: .\\nuxt-i18n\\plugin.utils.js (mode: 'all')
import nuxt_plugin_pluginseo_03b9a159 from 'nuxt_plugin_pluginseo_03b9a159' // Source: .\\nuxt-i18n\\plugin.seo.js (mode: 'all')
import nuxt_plugin_pluginrouting_1bb9b0d0 from 'nuxt_plugin_pluginrouting_1bb9b0d0' // Source: .\\nuxt-i18n\\plugin.routing.js (mode: 'all')
import nuxt_plugin_pluginmain_2f096c9f from 'nuxt_plugin_pluginmain_2f096c9f' // Source: .\\nuxt-i18n\\plugin.main.js (mode: 'all')
import nuxt_plugin_nuxtplugin50e62083_70e7be5a from 'nuxt_plugin_nuxtplugin50e62083_70e7be5a' // Source: .\\nuxt.plugin.50e62083.js (mode: 'all')
import nuxt_plugin_plugin_744235b7 from 'nuxt_plugin_plugin_744235b7' // Source: .\\composition-api\\plugin.js (mode: 'all')
import nuxt_plugin_pluginsi18ncookiesf96dcce6_756fa02d from 'nuxt_plugin_pluginsi18ncookiesf96dcce6_756fa02d' // Source: .\\plugins.i18n-cookies.f96dcce6.js (mode: 'all')
import nuxt_plugin_pluginse2etestingc40295f4_125da65e from 'nuxt_plugin_pluginse2etestingc40295f4_125da65e' // Source: .\\plugins.e2e-testing.c40295f4.js (mode: 'all')
import nuxt_plugin_pluginsloggerd44a8f46_f5a12a3c from 'nuxt_plugin_pluginsloggerd44a8f46_f5a12a3c' // Source: .\\plugins.logger.d44a8f46.js (mode: 'all')
import nuxt_plugin_pluginsssrbdc4ff22_d766711c from 'nuxt_plugin_pluginsssrbdc4ff22_d766711c' // Source: .\\plugins.ssr.bdc4ff22.js (mode: 'all')
import nuxt_plugin_pluginscontext163412b2_63c89f4b from 'nuxt_plugin_pluginscontext163412b2_63c89f4b' // Source: .\\plugins.context.163412b2.js (mode: 'all')
import nuxt_plugin_workbox_55c9c0b6 from 'nuxt_plugin_workbox_55c9c0b6' // Source: .\\workbox.js (mode: 'client')
import nuxt_plugin_metaplugin_1edac1b6 from 'nuxt_plugin_metaplugin_1edac1b6' // Source: .\\pwa\\meta.plugin.js (mode: 'all')
import nuxt_plugin_iconplugin_158b76ce from 'nuxt_plugin_iconplugin_158b76ce' // Source: .\\pwa\\icon.plugin.js (mode: 'all')
import nuxt_plugin_scrollToTopclient_6f28b416 from 'nuxt_plugin_scrollToTopclient_6f28b416' // Source: ..\\plugins\\scrollToTop.client.js (mode: 'client')

// Component: <ClientOnly>
Vue.component(ClientOnly.name, ClientOnly)

// TODO: Remove in Nuxt 3: <NoSsr>
Vue.component(NoSsr.name, {
  ...NoSsr,
  render (h, ctx) {
    if (process.client && !NoSsr._warned) {
      NoSsr._warned = true

      console.warn('<no-ssr> has been deprecated and will be removed in Nuxt 3, please use <client-only> instead')
    }
    return NoSsr.render(h, ctx)
  }
})

// Component: <NuxtChild>
Vue.component(NuxtChild.name, NuxtChild)
Vue.component('NChild', NuxtChild)

// Component NuxtLink is imported in server.js or client.js

// Component: <Nuxt>
Vue.component(Nuxt.name, Nuxt)

Object.defineProperty(Vue.prototype, '$nuxt', {
  get() {
    const globalNuxt = this.$root.$options.$nuxt
    if (process.client && !globalNuxt && typeof window !== 'undefined') {
      return window.$nuxt
    }
    return globalNuxt
  },
  configurable: true
})

Vue.use(Meta, {"keyName":"head","attribute":"data-n-head","ssrAttribute":"data-n-head-ssr","tagIDKeyName":"hid"})

const defaultTransition = {"name":"page","mode":"out-in","appear":false,"appearClass":"appear","appearActiveClass":"appear-active","appearToClass":"appear-to"}

async function createApp(ssrContext, config = {}) {
  const router = await createRouter(ssrContext, config)

  // Create Root instance

  // here we inject the router and store to all child components,
  // making them available everywhere as `this.$router` and `this.$store`.
  const app = {
    head: {"title":"Shopify | Vue Storefront Next","meta":[{"charset":"utf-8"},{"name":"viewport","content":"width=device-width, initial-scale=1"},{"name":"theme-color","content":"#5ece7b"},{"hid":"description","name":"description","content":"Vue Storefront 2 template for Shopify."},{"name":"generator","content":"Vue Storefront 2"},{"hid":"charset","charset":"utf-8"},{"hid":"mobile-web-app-capable","name":"mobile-web-app-capable","content":"yes"},{"hid":"apple-mobile-web-app-title","name":"apple-mobile-web-app-title","content":"VSF Next: Shopify APP"},{"hid":"author","name":"author","content":"Aureate labs"},{"hid":"og:type","name":"og:type","property":"og:type","content":"website"},{"hid":"og:title","name":"og:title","property":"og:title","content":"VSF Next: Shopify APP"},{"hid":"og:site_name","name":"og:site_name","property":"og:site_name","content":"VSF Next: Shopify APP"},{"hid":"og:description","name":"og:description","property":"og:description","content":"This is the Shopify PWA app for VSF Next - Developed by Aureate labs"},{"hid":"og:url","name":"og:url","property":"og:url","content":"shopify-pwa-beta.aureatelabs.com"},{"hid":"og:image","name":"og:image","property":"og:image","content":"shopify-pwa-beta.aureatelabs.com\u002F_nuxt\u002Ficons\u002Ficon_512x512.03acdc.png"},{"hid":"og:image:width","name":"og:image:width","property":"og:image:width","content":512},{"hid":"og:image:height","name":"og:image:height","property":"og:image:height","content":512},{"hid":"og:image:type","name":"og:image:type","property":"og:image:type","content":"image\u002Fpng"}],"link":[{"rel":"icon","type":"image\u002Fx-icon","href":"\u002Ffavicon.ico"},{"rel":"preconnect","href":"https:\u002F\u002Ffonts.gstatic.com","crossorigin":"crossorigin"},{"rel":"preload","href":"https:\u002F\u002Ffonts.googleapis.com\u002Fcss?family=Raleway:300,400,400i,500,600,700|Roboto:300,300i,400,400i,500,700&display=swap","as":"style"},{"rel":"stylesheet","href":"https:\u002F\u002Ffonts.googleapis.com\u002Fcss?family=Raleway:300,400,400i,500,600,700|Roboto:300,300i,400,400i,500,700&display=swap","media":"print","onload":"this.media='all'"},{"hid":"shortcut-icon","rel":"shortcut icon","href":"\u002Ficons\u002Fandroid-icon-48x48.png"},{"hid":"apple-touch-icon","rel":"apple-touch-icon","href":"\u002F_nuxt\u002Ficons\u002Ficon_512x512.03acdc.png","sizes":"512x512"},{"rel":"manifest","href":"\u002F_nuxt\u002Fmanifest.244f73ab.json","hid":"manifest"}],"style":[],"script":[],"htmlAttrs":{"lang":"en"}},

    router,
    nuxt: {
      defaultTransition,
      transitions: [defaultTransition],
      setTransitions (transitions) {
        if (!Array.isArray(transitions)) {
          transitions = [transitions]
        }
        transitions = transitions.map((transition) => {
          if (!transition) {
            transition = defaultTransition
          } else if (typeof transition === 'string') {
            transition = Object.assign({}, defaultTransition, { name: transition })
          } else {
            transition = Object.assign({}, defaultTransition, transition)
          }
          return transition
        })
        this.$options.nuxt.transitions = transitions
        return transitions
      },

      err: null,
      dateErr: null,
      error (err) {
        err = err || null
        app.context._errored = Boolean(err)
        err = err ? normalizeError(err) : null
        let nuxt = app.nuxt // to work with @vue/composition-api, see https://github.com/nuxt/nuxt.js/issues/6517#issuecomment-573280207
        if (this) {
          nuxt = this.nuxt || this.$options.nuxt
        }
        nuxt.dateErr = Date.now()
        nuxt.err = err
        // Used in src/server.js
        if (ssrContext) {
          ssrContext.nuxt.error = err
        }
        return err
      }
    },
    ...App
  }

  const next = ssrContext ? ssrContext.next : location => app.router.push(location)
  // Resolve route
  let route
  if (ssrContext) {
    route = router.resolve(ssrContext.url).route
  } else {
    const path = getLocation(router.options.base, router.options.mode)
    route = router.resolve(path).route
  }

  // Set context to app.context
  await setContext(app, {
    route,
    next,
    error: app.nuxt.error.bind(app),
    payload: ssrContext ? ssrContext.payload : undefined,
    req: ssrContext ? ssrContext.req : undefined,
    res: ssrContext ? ssrContext.res : undefined,
    beforeRenderFns: ssrContext ? ssrContext.beforeRenderFns : undefined,
    ssrContext
  })

  function inject(key, value) {
    if (!key) {
      throw new Error('inject(key, value) has no key provided')
    }
    if (value === undefined) {
      throw new Error(`inject('${key}', value) has no value provided`)
    }

    key = '$' + key
    // Add into app
    app[key] = value
    // Add into context
    if (!app.context[key]) {
      app.context[key] = value
    }

    // Check if plugin not already installed
    const installKey = '__nuxt_' + key + '_installed__'
    if (Vue[installKey]) {
      return
    }
    Vue[installKey] = true
    // Call Vue.use() to install the plugin into vm
    Vue.use(() => {
      if (!Object.prototype.hasOwnProperty.call(Vue.prototype, key)) {
        Object.defineProperty(Vue.prototype, key, {
          get () {
            return this.$root.$options[key]
          }
        })
      }
    })
  }

  // Inject runtime config as $config
  inject('config', config)

  // Add enablePreview(previewData = {}) in context for plugins
  if (process.static && process.client) {
    app.context.enablePreview = function (previewData = {}) {
      app.previewData = Object.assign({}, previewData)
      inject('preview', previewData)
    }
  }
  // Plugin execution

  if (process.client && typeof nuxt_plugin_vuescrollto_540aedc0 === 'function') {
    await nuxt_plugin_vuescrollto_540aedc0(app.context, inject)
  }

  if (typeof nuxt_plugin_cookieuniversalnuxt_09bea671 === 'function') {
    await nuxt_plugin_cookieuniversalnuxt_09bea671(app.context, inject)
  }

  if (typeof nuxt_plugin_pluginutils_43737e76 === 'function') {
    await nuxt_plugin_pluginutils_43737e76(app.context, inject)
  }

  if (typeof nuxt_plugin_pluginseo_03b9a159 === 'function') {
    await nuxt_plugin_pluginseo_03b9a159(app.context, inject)
  }

  if (typeof nuxt_plugin_pluginrouting_1bb9b0d0 === 'function') {
    await nuxt_plugin_pluginrouting_1bb9b0d0(app.context, inject)
  }

  if (typeof nuxt_plugin_pluginmain_2f096c9f === 'function') {
    await nuxt_plugin_pluginmain_2f096c9f(app.context, inject)
  }

  if (typeof nuxt_plugin_nuxtplugin50e62083_70e7be5a === 'function') {
    await nuxt_plugin_nuxtplugin50e62083_70e7be5a(app.context, inject)
  }

  if (typeof nuxt_plugin_plugin_744235b7 === 'function') {
    await nuxt_plugin_plugin_744235b7(app.context, inject)
  }

  if (typeof nuxt_plugin_pluginsi18ncookiesf96dcce6_756fa02d === 'function') {
    await nuxt_plugin_pluginsi18ncookiesf96dcce6_756fa02d(app.context, inject)
  }

  if (typeof nuxt_plugin_pluginse2etestingc40295f4_125da65e === 'function') {
    await nuxt_plugin_pluginse2etestingc40295f4_125da65e(app.context, inject)
  }

  if (typeof nuxt_plugin_pluginsloggerd44a8f46_f5a12a3c === 'function') {
    await nuxt_plugin_pluginsloggerd44a8f46_f5a12a3c(app.context, inject)
  }

  if (typeof nuxt_plugin_pluginsssrbdc4ff22_d766711c === 'function') {
    await nuxt_plugin_pluginsssrbdc4ff22_d766711c(app.context, inject)
  }

  if (typeof nuxt_plugin_pluginscontext163412b2_63c89f4b === 'function') {
    await nuxt_plugin_pluginscontext163412b2_63c89f4b(app.context, inject)
  }

  if (process.client && typeof nuxt_plugin_workbox_55c9c0b6 === 'function') {
    await nuxt_plugin_workbox_55c9c0b6(app.context, inject)
  }

  if (typeof nuxt_plugin_metaplugin_1edac1b6 === 'function') {
    await nuxt_plugin_metaplugin_1edac1b6(app.context, inject)
  }

  if (typeof nuxt_plugin_iconplugin_158b76ce === 'function') {
    await nuxt_plugin_iconplugin_158b76ce(app.context, inject)
  }

  if (process.client && typeof nuxt_plugin_scrollToTopclient_6f28b416 === 'function') {
    await nuxt_plugin_scrollToTopclient_6f28b416(app.context, inject)
  }

  // Lock enablePreview in context
  if (process.static && process.client) {
    app.context.enablePreview = function () {
      console.warn('You cannot call enablePreview() outside a plugin.')
    }
  }

  // Wait for async component to be resolved first
  await new Promise((resolve, reject) => {
    // Ignore 404s rather than blindly replacing URL in browser
    if (process.client) {
      const { route } = router.resolve(app.context.route.fullPath)
      if (!route.matched.length) {
        return resolve()
      }
    }
    router.replace(app.context.route.fullPath, resolve, (err) => {
      // https://github.com/vuejs/vue-router/blob/v3.4.3/src/util/errors.js
      if (!err._isRouter) return reject(err)
      if (err.type !== 2 /* NavigationFailureType.redirected */) return resolve()

      // navigated to a different route in router guard
      const unregister = router.afterEach(async (to, from) => {
        if (process.server && ssrContext && ssrContext.url) {
          ssrContext.url = to.fullPath
        }
        app.context.route = await getRouteData(to)
        app.context.params = to.params || {}
        app.context.query = to.query || {}
        unregister()
        resolve()
      })
    })
  })

  return {
    app,
    router
  }
}

export { createApp, NuxtError }
