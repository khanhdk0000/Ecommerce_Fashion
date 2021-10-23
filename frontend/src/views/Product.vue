<template>
  <div class="page-product">
    <div class="columns is-multiline">
      <div class="column is-7">
        <figure class="image mb-6 mr-6 is-4by5">
          <img class="product-crop" v-bind:src="product.image_link" />
        </figure>
      </div>

      <div class="column is-5">
        <h1 class="title">{{ product.product_name }}</h1>

        <h2 class="subtitle">Information</h2>
        <p>{{ product.product_type }}</p>
        <p><strong>Price: </strong>${{ product.product_price }}</p>

        <div class="field has-addons mt-6">
          <div class="control">
            <input type="number" class="input" min="1" v-model="quantity" />
          </div>

          <div class="control">
            <a class="button is-dark" @click="addToCart()">Add to cart</a>
          </div>
        </div>
      </div>
    </div>
    <!-- cards -->
    <hr/>
    <section class="section is-hidden-mobile">
      <div class="container">
        <h3 class="title has-text-centered is-size-4">Related Products</h3>
        <div class="mt-5 columns is-centered is-8 is-variable features">
          <div class="column is-4-tablet is-3-desktop">
            <div class="card">
              <div class="card-image has-text-centered px-4">
                <figure class="image is-4by3 product-crop">
                  <img
                    class="product-crop"
                    src="../assets/wristwatch-1149669.jpg"
                    alt="Placeholder image"
                  />
                </figure>
              </div>
              <div class="card-content">
                <p>£12.95</p>
                <p class="title is-size-5">Cortardo Cup</p>
              </div>
              <footer class="card-footer">
                <p class="card-footer-item">
                  <a href="#" class="has-text-grey">View</a>
                </p>
              </footer>
            </div>
          </div>
          <div class="column is-4-tablet is-3-desktop">
            <div class="card">
              <div class="card-image has-text-centered px-4">
                <figure class="image is-4by3">
                  <img
                    class="product-crop"
                    src="../assets/tie-690084.jpg"
                    alt="Placeholder image"
                  />
                </figure>
              </div>
              <div class="card-content">
                <p>£12.95</p>
                <p class="title is-size-5">Cortardo Cup</p>
              </div>
              <footer class="card-footer">
                <p class="card-footer-item">
                  <a href="#" class="has-text-grey">View</a>
                </p>
              </footer>
            </div>
          </div>
          <div class="column is-4-tablet is-3-desktop">
            <div class="card">
              <div class="card-image has-text-centered px-4">
                <figure class="image is-4by3">
                  <img
                    class="product-crop"
                    src="../assets/logo.png"
                    alt="Placeholder image"
                  />
                </figure>
              </div>
              <div class="card-content">
                <p>£12.95</p>
                <p class="title is-size-5">Cortardo Cup</p>
              </div>
              <footer class="card-footer">
                <p class="card-footer-item">
                  <a href="#" class="txt-hover has-text-grey">View</a>
                </p>
              </footer>
            </div>
          </div>
        </div>
      </div>
    </section>
  </div>
</template>

<script>
import axios from "axios";
import { toast } from "bulma-toast";
import getUser from '../composables/getUser';

export default {
  name: "Product",
  data() {
    return {
      product: {},
      quantity: 1,
      order: {},
      order_detail: {}
    };
  },
  mounted() {
    this.getProduct();
  },
  methods: {
    async getProduct() {
      this.$store.commit("setIsLoading", true);

      const id = this.$route.params.id;
      // const product_slug = this.$route.params.product_slug;

      await axios
        .get(`/api/product/${id}`)

        .then((response) => {
          this.product = response.data;
          console.log(response);

          document.title = this.product.name;
        })
        .catch((error) => {
          console.log(error);
        });

      this.$store.commit("setIsLoading", false);
    },
    async addToCart() {
      if (isNaN(this.quantity) || this.quantity < 1) {
        this.quantity = 1;
      }

      const {user} = getUser();

      // console.log(this.product);
      //* Config database field
      let ordered_date = new Date();

      let required_date = ordered_date; //? 3 day from ordered date
      required_date.setDate(required_date.getDate() + 3);

      ordered_date = ordered_date.toISOString().slice(0, 19).replace('T', ' ');
      required_date = required_date.toISOString().slice(0, 19).replace('T', ' ');

      console.log(`ordered_date: ${ordered_date}`);
      console.log(`required_date: ${required_date}`);

      console.log(`current user: ${user.value.displayName}`);
      console.log(`current user's id: ${user.value.uid}`);

      //* Put order to the db
      await axios
        .post("api/checkout/order/", {
          "ordered_date":ordered_date,
          "required_date":required_date,
          "customer_id": user.value.uid,
        })
        .then(response => {
          this.order = response.data;
          // console.log(response.data);
        })
        .catch(error => {
          console.log(error);
        });

      //* Put order_detail to the db
      let price = this.product.product_price * this.quantity;
      // console.log(`order_id: ${this.order.order_id}`)
      // console.log(`product_id: ${this.product.product_id}`)
      // console.log(`price: ${price}`)
      // console.log(`product price: ${this.product.product_price}`)
      // console.log(`quantity: ${this.quantity}`)
      await axios
        .post("api/checkout/cart/", {
          "order_id": this.order.order_id,
          "product_id": this.product.product_id,
          "quantity": this.quantity,
          "price": price,
        })
        .then(response => {
          this.order_detail = response.data;
          console.log(response.data);
        })
        .catch(error => {
          if (error.response){

          //do something
          console.log(`Error response: ${JSON.stringify(error.response)}`);

          }else if(error.request){

          //do something else
          console.log(`Error request: ${error.request}`);

          }else if(error.message){

          //do something other than the other two
          console.log(`Error message: ${error.message}`);

          }
        });

      // * Commit to store and show message

      this.$store.commit("addToCart", {product:this.product, quantity:this.quantity});

      toast({
        message: "The product was added to the cart",
        type: "is-success",
        dismissible: true,
        pauseOnHover: true,
        duration: 2000,
        position: "bottom-right",
      });
    },
  },
};
</script>

<style lang="scss" scoped>
.product-image {
  max-height: 200px;
}

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
  text-decoration: underline;
}
</style>