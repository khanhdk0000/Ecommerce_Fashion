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
      user_instance: {},
      order: {},
      order_detail: {},
      is_customer_order_exist: false,
      is_order_detail_exist: false,
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

      let required_date = new Date(); //? 3 day from ordered date
      required_date.setDate(required_date.getDate() + 3);

      ordered_date = ordered_date.toISOString().slice(0, 19).replace('T', ' ');
      required_date = required_date.toISOString().slice(0, 19).replace('T', ' ');

      console.log(`ordered_date: ${ordered_date}`);
      console.log(`required_date: ${required_date}`);

      console.log(`current user: ${user.value.displayName}`);
      console.log(`current user's id: ${user.value.uid}`);

      this.user_instance = {
        'customer_id': user.value.uid,
        'name': user.value.displayName,
        'email': user.value.email
      }

      // ? Put order to the db if not already exist
      // * Check if the order is already exist by the customer
      await this.isExistOrder();
      if (!this.is_customer_order_exist){
        console.log('Adding order');
        await axios
          .post("api/checkout/order/", {
            "ordered_date":ordered_date,
            "required_date":required_date,
            "customer": this.user_instance,
          })
          .then(response => {
            this.order = response.data;
            console.log(`Order added: ${this.order}`);
          })
          .catch(error => {
            console.log(error);
          });
      }
      // * Hard update the local order
      await this.isExistOrder();
      // * Dont care the above

      // ? Put order_detail to the db
      // * Check whether the order_detail with product_id is already in the database
      await this.isExistOrderDetail();
      if (!this.is_order_detail_exist){
        await axios
          .post("api/checkout/cart/", {
            "order": this.order,
            "product": this.product,
            "quantity": this.quantity,
            "price": this.product.product_price * this.quantity,
          })
          .then(response => {
            this.order_detail = response.data;
            console.log(`Added order's detail: ${this.order_detail}`);
          })
          .catch(error => {
            if (error.response){
              console.log(`Error response: ${JSON.stringify(error.response)}`);
            }else if(error.request){
              console.log(`Error request: ${error.request}`);
            }else if(error.message){
              console.log(`Error message: ${error.message}`);
            }
          });
      }
      else{
        // * Update the quantity and price of order's detail
        const new_content = {
          'quantity': this.order_detail.quantity + this.quantity,
          'price': this.product.product_price * (this.order_detail.quantity + this.quantity)
        }
        console.log(`Before updated order's detail:`);
        console.log(this.order_detail)

        await axios
            .put(`api/checkout/cart/${this.order.order_id}/${this.product.product_id}/`, new_content)
            .then(response => {
              this.order_detail = response.data;
              console.log(`Newly updated order's detail:`);
              console.log(this.order_detail)
            })
            .catch(error => {
              if (error.response){
                console.log(`Error response: ${JSON.stringify(error.response)}`);
              }else if(error.request){
                console.log(`Error request: ${error.request}`);
              }else if(error.message){
                console.log(`Error message: ${error.message}`);
              }
            });
      }

      // * Commit to store and show message

      this.$store.commit("addToCart", {product:this.product, quantity:this.quantity, order: this.order});

      toast({
        message: "The product was added to the cart",
        type: "is-success",
        dismissible: true,
        pauseOnHover: true,
        duration: 2000,
        position: "bottom-right",
      });
    },

    async isExistOrder(){
      try {
        await axios
          .get(`api/checkout/order/customer/${this.user_instance.customer_id}`)
          .then(response => {
            this.order = response.data[response.data.length-1]; // Get the latest order of user
            this.is_customer_order_exist=true?this.order:false; // In case no found result.

            console.log(`Get order by customer's id:`);
            console.log(response.data);
          })
          .catch(error => {
            this.is_customer_order_exist=false;
            if (error.response){
              console.log(`Error response: ${JSON.stringify(error.response)}`);
            }else if(error.request){
              console.log(`Error request: ${error.request}`);
            }else if(error.message){
              console.log(`Error message: ${error.message}`);
            }
          })
      } catch (error) {
        console.log(`Error Type: ${typeof(error)}`);
        if (error.response){
          console.log(`Error response: ${JSON.stringify(error.response)}`);
        }else if(error.request){
          console.log(`Error request: ${error.request}`);
        }else if(error.message){
          console.log(`Error message: ${error.message}`);
        }
      }
    },

    async isExistOrderDetail(){
      try {
        await axios
          .get(`api/checkout/cart/${this.order.order_id}/${this.product.product_id}`)
          .then(response => {
            this.is_order_detail_exist=true;
            this.order_detail=response.data;
            console.log(`Get order's detail by order_id and product_id:`);
            console.log(response);
          })
          .catch(error => {
            this.is_order_detail_exist=false;
            if (error.response){
              console.log(`Error response: ${JSON.stringify(error.response)}`);
            }else if(error.request){
              console.log(`Error request: ${error.request}`);
            }else if(error.message){
              console.log(`Error message: ${error.message}`);
            }
          })
      } catch (error) {
        console.log(`Error Type: ${typeof(error)}`);
        if (error.response){
          console.log(`Error response: ${JSON.stringify(error.response)}`);
        }else if(error.request){
          console.log(`Error request: ${error.request}`);
        }else if(error.message){
          console.log(`Error message: ${error.message}`);
        }
      }
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