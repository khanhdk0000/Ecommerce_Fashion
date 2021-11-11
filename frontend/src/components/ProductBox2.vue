<template>
  <div class="product">
    <div class="product-header">
      <img v-bind:src="product.image_link" alt="product" />
    </div>
    <div class="product-footer">
      <h3 class="title is-size-6">{{ product.product_name }}</h3>
      <div class="rating">
        <i class="fas fa-star"></i>
        <i class="fas fa-star"></i>
        <i class="fas fa-star"></i>
        <i class="fas fa-star"></i>
        <i class="fas fa-star"></i>
      </div>
      <div class="product-price">
        <h4>${{ product.product_price }}</h4>
      </div>
    </div>
    <ul>
      <li>
        <!-- <a href="#">
          <i class="far fa-eye"></i>
        </a> -->
        <router-link
          v-bind:to="{ name: 'Product', params: { id: product.product_id } }"
          ><i class="far fa-eye"></i
        ></router-link>
      </li>
      <li>
        <div class="custom-product-button" @click="addFavorite(product.product_id)">
          <i class="far fa-heart"></i>
        </div>
      </li>
      <li>
        <a href="#">
          <i class="fas fa-shopping-cart"></i>
        </a>
      </li>
    </ul>
  </div>
</template>

<script>
import axios from "axios";
import { getAuth, onAuthStateChanged } from "firebase/auth";
import { toast } from "bulma-toast";

export default {
  name: "ProductBox2",
  props: {
    product: Object,
  },
  setup() {
    const addFavorite = (id) => {
      console.log("add to favorite " + id);

      const auth = getAuth();
      onAuthStateChanged(auth, (user) => {
        if (user) {
          console.log(user.uid);

          // Add to favorite list
          axios
            .post(`/api/contains/${id}/${user.uid}`)
            .then((response) => {
              console.log(response);
            })
            .catch((error) => {
              console.log(error);
            });

          toast({
            message: "Product added to favorite",
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
    return { addFavorite };
  },
  mounted() {
    console.log(this.product.product_name);
  },
};
</script>

<style lang="scss" scoped>
h3 {
  margin-top: 5px;
  white-space: nowrap;
  overflow: hidden;
  text-overflow: ellipsis;
  max-width: 200px;
}

.product-center {
  display: grid;
  grid-template-columns: repeat(4, 1fr);
  gap: 1rem;
}

.product {
  text-align: center;
  position: relative;
  padding: 0 3rem;
  margin-top: 1rem;
}

.product-header {
  display: flex;
  align-items: center;
  justify-content: center;
  height: 20rem;
}

.product-header img.small {
  max-height: 10rem;
}

.product-footer h3 {
  font-weight: 500;
  font-size: 1.2rem;
  color: #444;
}

.rating {
  color: #ffd800;
  font-size: 0.7rem;
}

.product-price h4 {
  font-weight: 500;
}

.product ul {
  position: absolute;
  display: flex;
  align-items: center;
  justify-content: center;
  top: 50%;
  left: 50%;
  width: 10rem;
  height: 2.5rem;
  background-color: rgba(255, 255, 255, 0.5);
  opacity: 0;
  visibility: hidden;
  transform: translate(-50%, -50%) scale(0.7);
  transition: all 0.5s ease-in-out;
}

.product:hover ul {
  opacity: 1;
  visibility: visible;
  transform: translate(-50%, -50%) scale(1);
}

.product:hover ul i {
  color: #fff;
}

.product ul li:not(:last-child) {
  margin-right: 0.8rem;
}

.product ul a {
  position: relative;
  display: flex;
  align-items: center;
  justify-content: center;
  background-color: #8e94f2;
  width: 2.7rem;
  height: 2.7rem;
  cursor: pointer;
  transition: 0.5s;
}

.custom-product-button {
  position: relative;
  display: flex;
  align-items: center;
  justify-content: center;
  background-color: #8e94f2;
  width: 2.7rem;
  height: 2.7rem;
  cursor: pointer;
  transition: 0.5s;
}

.custom-product-button:hover {
  background-color: #222;
}

.custom-product-button::before {
  content: "";
  position: absolute;
  top: -0.6rem;
  left: -0.6rem;
  height: 0;
  width: 0;
  border-top: 3px solid #8e94f2;
  border-left: 3px solid #8e94f2;
  transition: 0.5s;
  opacity: 0;
  z-index: 1;
}

.custom-product-button::after {
  content: "";
  position: absolute;
  bottom: -0.6rem;
  right: -0.6rem;
  width: 0;
  height: 0;
  border-bottom: 3px solid #8e94f2;
  border-right: 3px solid #8e94f2;
  z-index: 1;
  opacity: 0;
  transition: 0.5s;
}

.custom-product-button:hover::before {
  width: 126%;
  height: 126%;
  border-top: 3px solid #222;
  border-left: 3px solid #222;
  opacity: 1;
}

.custom-product-button:hover::after {
  width: 126%;
  height: 126%;
  border-bottom: 3px solid #222;
  border-right: 3px solid #222;
  opacity: 1;
}


///////
.product ul a:hover {
  background-color: #222;
}

.product ul a::before {
  content: "";
  position: absolute;
  top: -0.6rem;
  left: -0.6rem;
  height: 0;
  width: 0;
  border-top: 3px solid #8e94f2;
  border-left: 3px solid #8e94f2;
  transition: 0.5s;
  opacity: 0;
  z-index: 1;
}

.product ul a::after {
  content: "";
  position: absolute;
  bottom: -0.6rem;
  right: -0.6rem;
  width: 0;
  height: 0;
  border-bottom: 3px solid #8e94f2;
  border-right: 3px solid #8e94f2;
  z-index: 1;
  opacity: 0;
  transition: 0.5s;
}

.product ul a:hover::before {
  width: 126%;
  height: 126%;
  border-top: 3px solid #222;
  border-left: 3px solid #222;
  opacity: 1;
}

.product ul a:hover::after {
  width: 126%;
  height: 126%;
  border-bottom: 3px solid #222;
  border-right: 3px solid #222;
  opacity: 1;
}

@media only screen and (max-width: 998px) {
  .product-center {
    grid-template-columns: repeat(3, 1fr);
  }
}

@media only screen and (max-width: 768px) {
  .product-center {
    grid-template-columns: repeat(2, 1fr);
  }

  .product-header {
    height: 20rem;
  }

  .product-header img.small {
    max-height: 20rem;
  }
}

@media only screen and (max-width: 567px) {
  .product-header {
    height: 15rem;
  }
}
</style>