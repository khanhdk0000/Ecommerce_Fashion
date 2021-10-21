<template>
  <!-- <div class="column is-3">
    <div class="box">
      <figure class="image mb-4">
        <div class=""><img v-bind:src="product.image_link" /></div>
      </figure>

      <h3 class="is-size-4">{{ product.product_name }}</h3>
      <p class="is-size-6 has-text-grey">${{ product.product_price }}</p>

      <router-link to="#" class="button is-dark mt-4">View details</router-link>
    </div>
  </div> -->
  <div class="column is-4-tablet is-3-desktop">
    <div class="card">
      <div class="card-image has-text-centered px-2">
        <figure class="image is-4by3 product-crop">
          <img
            class="product-crop"
            v-bind:src="product.image_link"
            alt="Placeholder image"
          />
        </figure>
      </div>
      <div class="card-content">
        <p class="title is-size-6">{{ product.product_name }}</p>
        <p>{{ product.product_price }}</p>
      </div>
      <footer class="card-footer">
        <p class="card-footer-item">
          <router-link v-bind:to="{name: 'Product', params: {id: product.product_id}}" class="has-text-centered">View Details</router-link>
        </p>
      </footer>
    </div>
  </div>
</template>

<script>
export default {
  name: "ProductBox",
  props: {
    product: Object,
  },
  mounted() {
    console.log(this.product);
  },
};
</script>

<style  lang="scss" scoped>
/* .image {
  margin-top: -1.25rem;
  margin-left: -1.25rem;
  margin-right: -1.25rem;
}
.crop {
  width: 100%;
  height: 200px;
  overflow: cover;
} */

.product-crop {
  object-fit: cover;
}

.card:hover {
  transition: transform 0.5s;

  &::after {
    position: absolute;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    transition: opacity 2s cubic-bezier(0.165, 0.84, 0.44, 1);
    box-shadow: 0 8px 17px 0 rgba(0, 0, 0, 0.2),
      0 6px 20px 0 rgba(0, 0, 0, 0.15);
    content: "";
    opacity: 0;
    z-index: -1;
  }

  &:hover,
  &:focus {
    transform: scale3d(1.006, 1.006, 1);

    &::after {
      opacity: 1;
    }
  }
}

.txt-hover:hover {
  //   text-decoration: underline;
  color: white;
}

p {
  white-space: nowrap;
  overflow: hidden;
  text-overflow: ellipsis;
  max-width: 200px;
}
.card-footer:hover {
  background-color: hsl(0, 0%, 29%);
  p {
    a {
      color: white;
    }
  }
}
</style>