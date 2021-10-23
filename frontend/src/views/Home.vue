<template>
  <div class="home">
    <CarouselHero />

    <!-- <div class="columns is-multiline">
      <div class="column is-12">
        <h2 class="is-size-2 has-text-centered">Latest products</h2>
      </div>

      <ProductBox
        v-for="product in latestProducts.slice(0, 4)"
        v-bind:key="product.product_id"
        v-bind:product="product"
      />
    </div> -->
    <!-- cards -->
    <section class="section is-hidden-mobile">
      <div class="container">
        <h3 class="title has-text-centered is-size-4">Latest Products</h3>
        <div class="mt-5 columns is-centered is-8 is-variable features">

      <ProductBox
        v-for="product in latestProducts.slice(0, 4)"
        v-bind:key="product.product_id"
        v-bind:product="product"
      />
        </div>
      </div>
    </section>
  </div>
</template>

<script>
import axios from "axios";

import ProductBox from "../components/ProductBox.vue";
import CarouselHero from "../components/CarouselHero.vue";

export default {
  name: "Home",
  data() {
    return {
      latestProducts: [],
    };
  },
  components: {
    ProductBox,
    CarouselHero,
  },
  mounted() {
    this.getLatestProducts();

    document.title = "Home | Djackets";
  },
  methods: {
    async getLatestProducts() {
      this.$store.commit("setIsLoading", true);

      await axios
        .get("/api/product/search/")
        .then((response) => {
          this.latestProducts = response.data;
        })
        .catch((error) => {
          console.log(error);
        });

      // console.log(this.latestProducts[0].product_name);

      this.$store.commit("setIsLoading", false);
    },
  },
};
</script>

<style lang="scss" scoped>

</style>