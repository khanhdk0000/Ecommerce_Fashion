<template>
    <tr>
        <td><router-link v-bind:to="{name: 'Product', params: {id: item.product.product_id}}">{{ item.product.product_name }}</router-link></td>
        <td>${{ item.product.product_price }}</td>
        <td>
            {{ item.quantity }}
            <a @click="decrementQuantity(item)">-</a>
            <a @click="incrementQuantity(item)">+</a>
        </td>
        <td>${{ getItemTotal(item).toFixed(2) }}</td>
        <td><button class="delete" @click="removeFromCart(item)"></button></td>
    </tr>
</template>

<script>
import axios from 'axios'
export default {
  name: 'CartItem',
  props: {
      initialItem: Object
  },
  data() {
      return {
          item: this.initialItem
      }
  },
  methods: {
      getItemTotal(item) {
        return item.quantity * item.product.product_price
      },
      decrementQuantity(item) {
        item.quantity -= 1

        if (item.quantity === 0) {
            this.$emit('removeFromCart', item)
        }

        this.updateCart()
      },
      incrementQuantity(item) {
        item.quantity += 1

        this.updateCart()
      },
    async updateCart() {
      localStorage.setItem('cart', JSON.stringify(this.$store.state.cart))

      // * Update the cart with new quantity, price

      const new_content = {
      'quantity': this.item.quantity,
      'price': this.getItemTotal(this.item)
      }
      console.log(this.item)

      await axios
      .put(`api/checkout/cart/${this.item.order.order_id}/${this.item.product.product_id}/`, new_content)
      .then(response => {
        console.log(`Newly updated order's detail:`);
        console.log(response.data)
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
    async removeFromCart(item) {
      this.$emit('removeFromCart', item)

      //* Get order_id bind with this product_id
      // await axios
      //     .get(`api/checkout/cart/${item.product.product_id}`)
      //     .then(response => {
      //         console.log(response)
      //     })
      //     .catch(error => {
      //         if (error.response){
      //             console.log(`Error response: ${JSON.stringify(error.response)}`);
      //         }else if(error.request){
      //             console.log(`Error request: ${error.request}`);
      //         }else if(error.message){
      //             console.log(`Error message: ${error.message}`);
      //         }
      //     })
      //* Remove the item from cart and any of its order_details


      this.updateCart()
    },
  },
}
</script>