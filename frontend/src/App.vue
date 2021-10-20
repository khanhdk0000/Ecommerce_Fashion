<template>
  <div id="wrapper">
    <nav class="navbar has-shadow">
      <!-- Container is for pushing out of the border -->
      <div class="container">
        <div class="navbar-brand">
          <!-- Start logo -->
          <router-link to="/" class="navbar-item">
            <div class="is-size-2 has-text-weight-medium">Fashion</div>
          </router-link>
          <!-- End logo -->

          <a
            class="navbar-burger"
            aria-label="menu"
            aria-expanded="false"
            data-target="navbar-menu"
            @click="showMobileMenu = !showMobileMenu"
          >
            <span aria-hidden="true"></span>
            <span aria-hidden="true"></span>
            <span aria-hidden="true"></span>
          </a>
        </div>

        <div
          class="navbar-menu"
          id="navbar-menu"
          v-bind:class="{ 'is-active': showMobileMenu }"
        >
          <div class="navbar-start">
            <!-- Start menu item -->
            <router-link to="/summer" class="navbar-item">Men</router-link>
            <router-link to="/winter" class="navbar-item">Women</router-link>

            <!-- Start Drop down big menu  -->
            <div class="navbar-item has-dropdown is-hoverable is-mega">
              <div class="navbar-link">Categories</div>
              <div id="blogDropdown" class="navbar-dropdown">
                <div class="container is-fluid">
                  <div class="columns">
                    <div class="column">
                      <h1 class="title is-6 is-mega-menu-title">Apparel</h1>
                      <a class="navbar-item" href="#">
                        <div class="navbar-content">
                          <p>Topwear</p>
                        </div>
                      </a>
                      <a class="navbar-item" href="#">
                        <div class="navbar-content">
                          <p>Bottomwear</p>
                        </div>
                      </a>
                      <a class="navbar-item" href="#">
                        <div class="navbar-content">
                          <p>Socks</p>
                        </div>
                      </a>
                      <a class="navbar-item" href="#">
                        <div class="navbar-content">
                          <p>Innerwear</p>
                        </div>
                      </a>
                      <a class="navbar-item" href="#">
                        <div class="navbar-content">
                          <p>Dress</p>
                        </div>
                      </a>

                      <a class="navbar-item" href="#">
                        <div class="navbar-content">
                          <p>Loungewear and Nightwear</p>
                        </div>
                      </a>

                      <a class="navbar-item" href="#">
                        <div class="navbar-content">
                          <p>Saree</p>
                        </div>
                      </a>

                      <a class="navbar-item" href="#">
                        <div class="navbar-content">
                          <p>Apparel Set</p>
                        </div>
                      </a>
                    </div>

                    <div class="column">
                      <h1 class="title is-6 is-mega-menu-title">Accessories</h1>
                      <a class="navbar-item" href="#">
                        <div class="navbar-content">
                          <p>Watches</p>
                        </div>
                      </a>
                      <a class="navbar-item" href="#">
                        <div class="navbar-content">
                          <p>Socks</p>
                        </div>
                      </a>
                      <a class="navbar-item" href="#">
                        <div class="navbar-content">
                          <p>Belts</p>
                        </div>
                      </a>
                      <a class="navbar-item" href="#">
                        <div class="navbar-content">
                          <p>Bags</p>
                        </div>
                      </a>
                      <a class="navbar-item" href="#">
                        <div class="navbar-content">
                          <p>Shoe Accessories</p>
                        </div>
                      </a>

                      <a class="navbar-item" href="#">
                        <div class="navbar-content">
                          <p>Jewellery</p>
                        </div>
                      </a>

                      <a class="navbar-item" href="#">
                        <div class="navbar-content">
                          <p>Eyewear</p>
                        </div>
                      </a>

                      <a class="navbar-item" href="#">
                        <div class="navbar-content">
                          <p>Scarves</p>
                        </div>
                      </a>

                      <a class="navbar-item" href="#">
                        <div class="navbar-content">
                          <p>Wallets</p>
                        </div>
                      </a>

                      <a class="navbar-item" href="#">
                        <div class="navbar-content">
                          <p>Headwear</p>
                        </div>
                      </a>

                      <a class="navbar-item" href="#">
                        <div class="navbar-content">
                          <p>Mufflers</p>
                        </div>
                      </a>

                      <a class="navbar-item" href="#">
                        <div class="navbar-content">
                          <p>Ties</p>
                        </div>
                      </a>

                      <a class="navbar-item" href="#">
                        <div class="navbar-content">
                          <p>Wallets</p>
                        </div>
                      </a>

                      <a class="navbar-item" href="#">
                        <div class="navbar-content">
                          <p>Perfume</p>
                        </div>
                      </a>
                    </div>

                    <div class="column">
                      <h1 class="title is-6 is-mega-menu-title">Footwear</h1>
                      <a class="navbar-item" href="#">
                        <div class="navbar-content">
                          <p>Shoes</p>
                        </div>
                      </a>
                      <a class="navbar-item" href="#">
                        <div class="navbar-content">
                          <p>Flip Flops</p>
                        </div>
                      </a>
                      <a class="navbar-item" href="#">
                        <div class="navbar-content">
                          <p>Sandal</p>
                        </div>
                      </a>
                    </div>

                    <div class="column">
                      <h1 class="title is-6 is-mega-menu-title">
                        Personal Care
                      </h1>
                      <a class="navbar-item" href="#">
                        <div class="navbar-content">
                          <p>Fragrance</p>
                        </div>
                      </a>
                      <a class="navbar-item" href="#">
                        <div class="navbar-content">
                          <p>Lips</p>
                        </div>
                      </a>
                      <a class="navbar-item" href="#">
                        <div class="navbar-content">
                          <p>Skin Care</p>
                        </div>
                      </a>
                      <a class="navbar-item" href="#">
                        <div class="navbar-content">
                          <p>Makeup</p>
                        </div>
                      </a>
                      <a class="navbar-item" href="#">
                        <div class="navbar-content">
                          <p>Nails</p>
                        </div>
                      </a>
                      <a class="navbar-item" href="#">
                        <div class="navbar-content">
                          <p>Beauty Accessories</p>
                        </div>
                      </a>
                      <a class="navbar-item" href="#">
                        <div class="navbar-content">
                          <p>Skin</p>
                        </div>
                      </a>
                      <a class="navbar-item" href="#">
                        <div class="navbar-content">
                          <p>Eyes</p>
                        </div>
                      </a>
                      <a class="navbar-item" href="#">
                        <div class="navbar-content">
                          <p>Bath and Body</p>
                        </div>
                      </a>
                      <a class="navbar-item" href="#">
                        <div class="navbar-content">
                          <p>Hair</p>
                        </div>
                      </a>
                      <a class="navbar-item" href="#">
                        <div class="navbar-content">
                          <p>Perfume</p>
                        </div>
                      </a>
                    </div>

                    <div class="column">
                      <h1 class="title is-6 is-mega-menu-title">
                        Sporting Goods
                      </h1>
                      <a class="navbar-item" href="#">
                        <div class="navbar-content">
                          <p>Sports Equipment</p>
                        </div>
                      </a>
                      <a class="navbar-item" href="#">
                        <div class="navbar-content">
                          <p>Wristbands</p>
                        </div>
                      </a>
                    </div>
                  </div>
                </div>
              </div>
            </div>

            <!-- End big dropdown menu-->
          </div>

          <div class="navbar-end">
            <div class="navbar-item">
              <!-- Start search bar  -->
              <form method="get" action="/search">
                <div class="field has-addons">
                  <div class="control">
                    <input
                      type="text"
                      class="input"
                      placeholder="What are you looking for?"
                      name="query"
                    />
                  </div>

                  <div class="control">
                    <button class="button is-dark">
                      <span class="icon">
                        <i class="fas fa-search"></i>
                      </span>
                    </button>
                  </div>
                </div>
              </form>
              <!-- End Search bar  -->
            </div>

            <!-- <div class="buttons">
                <template v-if="$store.state.isAuthenticated">
                  <router-link to="/my-account" class="button is-light"
                    >My account</router-link
                  >
                </template>

                <template v-else>
                  <router-link to="/log-in" class="button is-light"
                    >Log in</router-link
                  >
                </template>

              </div> -->

            <!-- User login  -->
            <!-- <router-link to="/log-in" class="navbar-item">
              <span class="icon mx-4">
                <i class="far fa-user"></i>
              </span>
            </router-link> -->

            <!-- Wishlist  -->
            <router-link to="/cart" class="navbar-item">
              <span class="icon mx-4">
                <i class="far fa-heart"></i>
              </span>
            </router-link>

            <!-- Cart  -->
            <router-link to="/cart" class="navbar-item">
              <span class="icon mx-4"
                ><i class="fas fa-shopping-cart"></i
              ></span>
            </router-link>

            <div class="navbar-item dropdown is-hoverable">
              <div class="dropdown-trigger">
                <div v-if="user">
                  <figure class="image is-24x24">
                    <img :src="avatarUrl" />
                  </figure>
                </div>
                <div v-else>
                  <span class="icon mx-4">
                    <i class="far fa-user"></i>
                  </span>
                </div>
              </div>
              <div class="dropdown-menu" id="dropdown-menu" role="menu">
                <div class="dropdown-content">
                  <div v-if="user">
                    <router-link to="/my-account" class="dropdown-item">
                      My Account
                    </router-link>
                    <hr class="dropdown-divider" />
                    <button
                      class="button is-white is-small"
                      @click="handleClick"
                    >
                      Log Out
                    </button>
                  </div>
                  <div v-else>
                    <router-link to="/log-in" class="dropdown-item">
                      Log In
                    </router-link>
                    <router-link to="/sign-up" class="dropdown-item">
                      Sign Up
                    </router-link>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </nav>

    <div
      class="is-loading-bar has-text-centered"
      v-bind:class="{ 'is-loading': $store.state.isLoading }"
    >
      <div class="lds-dual-ring"></div>
    </div>

    <section class="section">
      <router-view />
    </section>

    <footer class="footer">
      <p class="has-text-centered">Copyright (c) 2021</p>
    </footer>
  </div>
</template>

<script>
import axios from "axios";
import getUser from "./composables/getUser";
import useLogout from "./composables/useLogout";
import { useRouter } from "vue-router";
import { computed } from "vue";

export default {
  setup() {
    const { user } = getUser();
    const { logout } = useLogout();
    const router = useRouter();

    const handleClick = async () => {
      await logout();
      console.log("logged out");
      router.push({ name: "LogIn" });
    };

    const avatarUrl = computed(()=> {
      let url = `https://avatars.dicebear.com/api/micah/${user.value.displayName}.svg`
      return url
    })

    return { handleClick, user, avatarUrl };
  },
  data() {
    return {
      showMobileMenu: false,
      cart: {
        items: [],
      },
    };
  },
  beforeCreate() {
    this.$store.commit("initializeStore");

    const token = this.$store.state.token;

    if (token) {
      axios.defaults.headers.common["Authorization"] = "Token " + token;
    } else {
      axios.defaults.headers.common["Authorization"] = "";
    }
  },
  mounted() {
    this.cart = this.$store.state.cart;
  },
  computed: {
    cartTotalLength() {
      let totalLength = 0;

      for (let i = 0; i < this.cart.items.length; i++) {
        totalLength += this.cart.items[i].quantity;
      }

      return totalLength;
    },
  },
};
</script>

<style lang="scss">
@import "../node_modules/bulma";

.lds-dual-ring {
  display: inline-block;
  width: 80px;
  height: 80px;
}
.lds-dual-ring:after {
  content: " ";
  display: block;
  width: 64px;
  height: 64px;
  margin: 8px;
  border-radius: 50%;
  border: 6px solid #ccc;
  border-color: #ccc transparent #ccc transparent;
  animation: lds-dual-ring 1.2s linear infinite;
}
@keyframes lds-dual-ring {
  0% {
    transform: rotate(0deg);
  }
  100% {
    transform: rotate(360deg);
  }
}

.is-loading-bar {
  height: 0;
  overflow: hidden;

  -webkit-transition: all 0.3s;
  transition: all 0.3s;

  &.is-loading {
    height: 80px;
  }
}

.navbar-item.is-mega {
  position: static;
  z-index: 5000;

  .is-mega-menu-title {
    margin-bottom: 0;
    padding: 0.375rem 1rem;
  }
}
</style>
