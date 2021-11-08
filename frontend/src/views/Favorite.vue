<template>
  <div>
    <div class="products">
      <div class="products__grid">
        <ProductBoxDelete
          v-for="product in products"
          v-bind:key="product.id"
          v-bind:product="product"
          class=""
        />
      </div>
    </div>
  </div>
</template>

<script>
import axios from "axios";
import { toast } from "bulma-toast";

import ProductBox from "@/components/ProductBox";
import ProductBoxDelete from "../components/ProductBoxDelete.vue";
import getUser from "../composables/getUser";
import { onMounted, ref } from "vue";
import { useStore } from "vuex";
import { projectAuth, firebase } from "../firebase/config";
import { getAuth, onAuthStateChanged } from "firebase/auth";

export default {
  name: "Favorite",
  components: {
    ProductBox,
    ProductBoxDelete
  },
  setup() {
    const products = ref("");
    const store = useStore();

    onMounted(async () => {
      console.log("Component is mounted!");
      await getFavorite();
    });

    const getFavorite = async () => {
      store.commit("setIsLoading", true);
      const auth = getAuth();
      onAuthStateChanged(auth, (user) => {
        if (user) {
          console.log(user.uid);
          axios
            .get(`/api/wishlist/${user.uid}`)
            .then((response) => {
              products.value = response.data;

              document.title = "Favorite";
            })
            .catch((error) => {
              console.log(error);

              toast({
                message: "Something went wrong. Please try again.",
                type: "is-danger",
                dismissible: true,
                pauseOnHover: true,
                duration: 2000,
                position: "bottom-right",
              });
            });
          // ...
        } else {
          console.log("no user");
        }
      });

      store.commit("setIsLoading", false);
    };

    return { products };
  },
  data() {
    return {
      category: {
        products: [],
      },
    };
  },
  mounted() {
    // this.getCategory();
  },
  methods: {
    async getCategory() {
      this.$store.commit("setIsLoading", true);
      console.log(this.$route.query);

      axios
        .get(`/api/product/search`)
        .then((response) => {
          this.category.products = response.data;

          document.title = "Favorite";
        })
        .catch((error) => {
          console.log(error);

          toast({
            message: "Something went wrong. Please try again.",
            type: "is-danger",
            dismissible: true,
            pauseOnHover: true,
            duration: 2000,
            position: "bottom-right",
          });
        });

      this.$store.commit("setIsLoading", false);
    },
  },
};
</script>

<style scoped lang="scss">
.products {
  box-sizing: border-box;
  flex: 1;
  margin: 0;
  &__grid,
  &__list {
    display: flex;
    flex-wrap: wrap;
  }
  &__grid {
    justify-content: flex-start;
  }
  &__product-card {
    --product-card-max-width: 11rem;
    --product-card-title-margin: 4px 0 0 0;
    --price-regular-font-line-height: 1;
    margin-bottom: 16px;
    ::v-deep .sf-product-card__price {
      margin: 4px 0 8px;
    }
    flex: 1 1 50%;
  }
  &__product-card-horizontal {
    margin-bottom: 16px;
    flex: 0 0 100%;
    ::v-deep .sf-product-card-horizontal__wishlist-icon {
      .sf-icon {
        width: 1.5rem;
        height: 1.5rem;
      }
    }
  }
  &__slide-enter {
    opacity: 0;
    transform: scale(0.5);
  }
  &__slide-enter-active {
    transition: all 0.2s ease;
  }
  &__pagination {
    display: flex;
    justify-content: center;
    margin: 24px 0;
  }
  &__show-on-page {
    display: flex;
    justify-content: flex-end;
    align-items: baseline;
    &__label {
      font-family: Raleway;
      font-size: 14px;
    }
  }
}
</style>