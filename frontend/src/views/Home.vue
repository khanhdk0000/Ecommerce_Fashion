<template>
  <div class="home">
    <TestHero />

    <!-- Category -->
    <CategorySection/>

    <!-- New cards -->
    <section class="sort-category">
      <div class="title-container">
        <div class="section-titles">
          <div class="section-title active filter-btn" data-id="trend">
            <span class="dot"></span>
            <h1 class="primary-title">Trending Products</h1>
          </div>
        </div>
      </div>

      <div class="product-center container">
        <ProductBox2
          v-for="product in latestProducts.slice(20, 24)"
          v-bind:key="product.product_id"
          v-bind:product="product"
        />
      </div>
    </section>

    <Gallery />
  </div>
</template>

<script>
import axios from "axios";

import ProductBox from "../components/ProductBox.vue";
import TestHero from "../components/TestHero.vue";
import ProductBox2 from "../components/ProductBox2.vue";
import CategorySection from "../components/CategorySection.vue";
import Gallery from "../components/Gallery.vue";

export default {
  name: "Home",
  data() {
    return {
      latestProducts: [],
    };
  },
  components: {
    ProductBox,
    TestHero,
    ProductBox2,
    CategorySection,
    Gallery
  },
  mounted() {
    this.getLatestProducts();

    document.title = "Home";
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
.title-container {
  display: flex;
  align-items: center;
  justify-content: center;
  padding: 1rem 0;
  margin-bottom: 1rem;
  background-color: #dfe7fd;
}

.section-titles:not(:last-child) {
  margin-right: 0.75rem;
}

.section-title {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  cursor: pointer;
}

.section-title h1 {
  font-size: 1.2rem;
  font-weight: inherit;
}

.section-title:hover .primary-title,
.section-title:hover span.dot,
.section-title:hover span.dot::before {
  opacity: 1;
}

.section-title .primary-title {
  opacity: 0.6;
  padding-left: 0.25rem;
  transition: opacity 0.3s ease-in-out;
}

span.dot {
  opacity: 0.6;
  padding: 0.27rem;
  position: relative;
  border: 1px solid #222;
  cursor: pointer;
  transition: opacity 0.3s ease-in-out;
}

span.dot::before {
  content: "";
  position: absolute;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  border: 1px solid #222;
  background-color: #222;
  margin: 1px;
  opacity: 0.6;
}

.section-title.active span.dot {
  opacity: 1;
}

.section-title.active span.dot::before {
  opacity: 1;
}

.section-title.active .primary-title {
  opacity: 1;
}

@media only screen and (max-width: 567px) {
  .title-container {
    flex-direction: column;
  }

  .section-titles:not(:last-child) {
    margin: 0 0 0.7rem;
  }
}

/* ========= product center ========= */
.product-center {
  display: grid;
  grid-template-columns: repeat(4, 1fr);
  gap: 1rem;
}

</style>