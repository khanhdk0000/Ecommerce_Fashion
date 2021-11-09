import axios from 'axios';


const loadItems = async(user_id) => {
  /*
  * Load all the items from current user
  */

  // ? Get the latest order of the current user

  let orders = this;
  await axios
    .get(`api/checkout/order/customer/${user_id}`)
    .then(response => {
      orders = JSON.parse(JSON.stringify(response.data));

      console.log(`Get orders by customer's id:`);
      console.log(response.data);
    })
    .catch(error => {
      if (error.response){
        console.log(`Error response: ${JSON.stringify(error.response)}`);
      }else if(error.request){
        console.log(`Error request: ${error.request}`);
      }else if(error.message){
        console.log(`Error message: ${error.message}`);
      }
    })

  const current_order = orders[orders.length-1];

  // ? Get the items in the current order
  let items = this;
  try {
    await axios
      .get(`api/checkout/cart/order/${current_order.order_id}`)
      .then(response => {
        console.log(`Get order's detail by order_id and product_id:`);
        console.log(response);
        items = JSON.parse(JSON.stringify(response.data));
        items['order_id']=current_order.order_id;
      })
      .catch((error) => {
        if (error.response) {
          console.log(`Error response: ${JSON.stringify(error.response)}`);
        } else if (error.request) {
          console.log(`Error request: ${error.request}`);
        } else if (error.message) {
          console.log(`Error message: ${error.message}`);
        }
      })
  } catch (error) {
    console.log("User has no item in cart yet!")
  }

  return items;
};

export default loadItems;