<template>
  <div class="page-cart">
    <div class="columns is-multiline">
      <div class="column is-12">
        <h1 class="title">Cart</h1>
      </div>

      <div class="column is-12 box">
        <table class="table is-fullwidth" v-if="cartTotalLength">
          <thead>
            <tr>
              <th>Product</th>
              <th>Price</th>
              <th>Quantity</th>
              <th>Total</th>
              <th></th>
            </tr>
          </thead>

          <tbody>
            <CartItem
              v-for="item in cart.items"
              v-bind:key="item.product.product_id"
              v-bind:initialItem="item"
              v-on:removeFromCart="removeFromCart" />
          </tbody>
        </table>

        <p v-else>You don't have any products in your cart...</p>
      </div>

      <div class="column is-12 box">
        <h2 class="subtitle">Summary</h2>

        <strong>${{ cartTotalPrice.toFixed(2) }}</strong>, {{ cartTotalLength }} items

        <hr>

        <router-link to="/cart/checkout" class="button is-dark">Proceed to checkout</router-link>
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios'
import CartItem from '@/components/CartItem.vue'
import getUser from '../composables/getUser'

export default {
    name: 'Cart',
    components: {
        CartItem
    },
    data() {
      return {
        cart: {
          items: []
        },
      }
    },
    mounted() {
      this.cart = this.$store.state.cart;
      console.log(this.cart);
      this.cart.items.forEach(element => {
          console.log(element);
      });
      // console.log(this.cart.items)
    },
    methods: {
      async removeFromCart(item) {
        this.cart.items = this.cart.items.filter(i => i.product.product_id !== item.product.product_id)

        // ! Remove this product_id from the order_detail
        console.log("Removing item:")
        console.log(item)

        const order_id = item.order.order_id;
        const product_id = item.product.product_id;

        await axios
          .delete(`api/checkout/cart/${order_id}/${product_id}`)
          .then(response => {
            console.log(response.data + " Item has been deleted");
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
      },

    },
    computed: {
        cartTotalLength() {
          return this.cart.items.reduce((acc, curVal) => {
            return acc += curVal.quantity
          }, 0)
        },
        cartTotalPrice() {
          return this.cart.items.reduce((acc, curVal) => {
            return acc += curVal.product.product_price * curVal.quantity
          }, 0)
        },
    }
}
</script>