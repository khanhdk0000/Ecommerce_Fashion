<template>
  <div id="category">
    <Breadcrumb />
    <div class="navbar section">
      <div
        class="navbar__aside is-size-3 has-text-centered has-text-weight-bold"
      >
        Filter
      </div>
      <div class="navbar__main">
        <div class="navbar__sort">
          <span class="navbar__label">Sort by:</span>

          <!-- Dropdown button -->
          <div v-bind:class="{ 'is-active': isActive }" class="dropdown">
            <div class="dropdown-trigger">
              <button
                class="button"
                aria-haspopup="true"
                aria-controls="dropdown-menu"
                v-on:click="isActive = !isActive"
              >
                <span> {{ categoryFilter }} </span>
                <span class="icon is-small">
                  <i class="fas fa-angle-down" aria-hidden="true"></i>
                </span>
              </button>
            </div>
            <div class="dropdown-menu" id="dropdown-menu" role="menu">
              <div class="dropdown-content">
                <a
                  href="#"
                  class="dropdown-item"
                  v-on:click="testClick('Latest')"
                >
                  Latest
                </a>
                <a
                  class="dropdown-item"
                  v-on:click="testClick('Price from low to high')"
                >
                  Price from low to high
                </a>
                <a
                  href="#"
                  class="dropdown-item"
                  v-on:click="testClick('Price from high to low')"
                >
                  Price from high to low
                </a>
              </div>
            </div>
          </div>
          <!-- End dropdown button -->
        </div>

        <div class="navbar__counter">
          <span class="navbar__label">Products found: </span>
          <span class="">280</span>
        </div>
      </div>
    </div>
    <div class="main section">
      <div class="sidebar">
        <Accordion v-for="i in sidebar_content" :key="i">
          <AccordionItem :trigger="i.trigger" :contents="i.content" />
        </Accordion>
      </div>

      <div class="products">
        <div class="products__grid">
          <ProductBox
            v-for="product in category.products"
            v-bind:key="product.id"
            v-bind:product="product"
            class=""
          />
          <ProductBox
            v-for="product in category.products"
            v-bind:key="product.id"
            v-bind:product="product"
            class=""
          />
          <ProductBox
            v-for="product in category.products"
            v-bind:key="product.id"
            v-bind:product="product"
            class=""
          />
        </div>

        <nav class="pagination custom_pagination" role="navigation" aria-label="pagination">
        <a
          class="pagination-previous is-disabled"
          title="This is the first page"
          >Previous</a
        >
        <a class="pagination-next">Next page</a>
        <ul class="pagination-list">
          <li>
            <a
              class="pagination-link is-current"
              aria-label="Page 1"
              aria-current="page"
              >1</a
            >
          </li>
          <li>
            <a class="pagination-link" aria-label="Goto page 2">2</a>
          </li>
          <li>
            <a class="pagination-link" aria-label="Goto page 3">3</a>
          </li>
        </ul>
      </nav>
      </div>

      
    </div>
  </div>
</template>

<script>
import axios from "axios";
import { toast } from "bulma-toast";

import ProductBox from "@/components/ProductBox";
import Breadcrumb from "../components/Breadcrumb.vue";
import Accordion from "../components/Accordion.vue";
import AccordionItem from "../components/accordion-item.vue";

export default {
  name: "Category",
  components: {
    ProductBox,
    Breadcrumb,
    Accordion,
    AccordionItem,
  },
  data() {
    return {
      category: {
        products: [],
      },
      isActive: false,
      categoryFilter: "Latest",
      sidebar_content: [
        {
          trigger: "Color",
          content: ["Red", "Green", "Blue"],
        },
        {
          trigger: "Category",
          content: [
            "Apparel",
            "Accessories",
            "Footwear",
            "Personal Care",
            "Sporting Goods",
          ],
        },
      ],
    };
  },
  mounted() {
    this.getCategory();
  },
  watch: {
    $route(to, from) {
      if (to.name === "Category") {
        this.getCategory();
      }
    },
  },
  methods: {
    async getCategory() {
      const categorySlug = this.$route.params.category_slug;

      this.$store.commit("setIsLoading", true);

      axios
        .get(`/api/v1/products/${categorySlug}/`)
        .then((response) => {
          this.category = response.data;

          document.title = this.category.name + " | Djackets";
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
    testClick(cate) {
      console.log("Click");
      this.categoryFilter = cate;
      this.isActive = !this.isActive;
    },
  },
};
</script>

<style scoped lang='scss'>
.custom_pagination{
  background-color: white;

}

hr.solid {
  border-top: 0.5px solid rgb(218, 218, 218);
}

.vertical {
  border-left: 0.5px solid rgb(218, 218, 218);
  min-height: 500px;
  height: 100%;
}

.navbar {
  z-index: 1;
  position: relative;
  display: flex;
  border: 1px solid #f1f2f3;
  border-width: 1px 0 1px 0;
  &.section {
    padding: 0;
  }
  &__main {
    display: flex;
    align-items: center;
    padding: 16px 0;
  }
  &__aside {
    flex: 0 0 15%;
    padding: 16px 16px;
    border: 1px solid #f1f2f3;
    border-width: 0 1px 0 0;
  }
  &__main {
    flex: 1;
    display: flex;
    padding: 0;
  }
  &__title {
    --heading-title-font-weight: 600;
    --heading-title-font-size: 18px;
  }
  &__filters-icon {
    margin: 0 0 0 4px;
    order: 1;
  }
  &__label {
    font-weight: 400;
    color: #72757e;
    margin: 0 16px 0 0;
  }
  &__sort {
    display: flex;
    align-items: center;
    margin: 0 auto 0 80px;
  }
  &__counter {
    margin: auto;
  }
  &__view {
    display: flex;
    order: -1;
    align-items: center;
    margin: 0;
    &-icon {
      cursor: pointer;
      margin: 0 24px 0 16px;
      &:last-child {
        margin: 0;
      }
    }
    &-label {
      margin: 0 16px 0 0;
      font: 400 16px / 1.6 Raleway;
      text-decoration: none;
      color: #43464e;
    }
  }
}

.breadcrumbs {
  padding: 24px 24px 24px 16px;
}

.main {
  &.section {
    padding: 0;
  }
}

.main {
  display: flex;
}
.sidebar {
  flex: 0 0 15%;
  padding: 16px;
  border: 1px solid #f1f2f3;
  border-width: 0 1px 0 0;
}

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