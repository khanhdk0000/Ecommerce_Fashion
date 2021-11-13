<template>
  <div class="column is-4-tablet is-3-desktop" v-if="isValid">
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
          <router-link
            v-bind:to="{ name: 'Product', params: { id: product.product_id } }"
            >View Details</router-link
          >
        </p>
        <p class="card-footer-item" @click="addFavorite(product.product_id)">
          Delete
        </p>
      </footer>
    </div>
  </div>
</template>

<script>
import axios from "axios";
import { getAuth, onAuthStateChanged } from "firebase/auth";
import { toast } from "bulma-toast";
import { ref } from "vue";

export default {
  name: "ProductBoxDelete",
  props: {
    product: Object,
  },
  setup() {
    const isValid = ref(true);
    const addFavorite = (id) => {
      console.log("Delete " + id);
      isValid.value = false;
      const auth = getAuth();
      onAuthStateChanged(auth, (user) => {
        if (user) {
          console.log(user.uid);

          // Add to favorite list
          axios
            .delete(`/api/contains/${id}/${user.uid}`)
            .then((response) => {
              console.log(response);
            })
            .catch((error) => {
              console.log(error);
            });

          toast({
            message: "Product removed from favorite",
            type: "is-primary",
            dismissible: true,
            pauseOnHover: true,
            duration: 2000,
            position: "bottom-right",
          });
        } else {
          console.log("no user");
        }
      });
    };
    return { addFavorite, isValid };
  },
  mounted() {
    console.log(this.product.product_name);
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
.card-footer-item:hover {
  background-color: hsl(0, 0%, 29%);
  color: white;
  cursor: pointer;
  p {
    router-link {
      color: white;
    }
  }
}
</style>