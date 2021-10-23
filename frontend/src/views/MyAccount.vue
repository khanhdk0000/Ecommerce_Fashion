<template>
    <div class="page-my-account">
        <div class="columns is-multiline">
            <div class="column is-12">
                <h1 class="title">My account</h1>
            </div>

            <div class="column is-12">
                <button @click="handleClick" class="button is-danger">Log out</button>
            </div>

            <hr>

            <div class="column is-12">
                <h2 class="subtitle">My orders</h2>

                <OrderSummary
                    v-for="order in orders"
                    v-bind:key="order.id"
                    v-bind:order="order" />
            </div>
        </div>
    </div>
</template>

<script>
import axios from 'axios'

import OrderSummary from '@/components/OrderSummary.vue'
import useLogout from '../composables/useLogout'
import { useRouter } from 'vue-router'

export default {
    name: 'MyAccount',
    components: {
        OrderSummary
    },
    setup() {
        const {logout} = useLogout();
        const router = useRouter();

        const handleClick = async () => {
            await logout();
            console.log("logged out");
            router.push('/log-in');
        };

        return {handleClick};
    },
    data() {
        return {
            orders: []
        }
    },
    mounted() {
        document.title = 'My account | Djackets'

        this.getMyOrders()
    },
    methods: {
        async getMyOrders() {
            this.$store.commit('setIsLoading', true)

            await axios
                .get('/api/checkout/order/')
                .then(response => {
                    // this.orders = response.data
                    console.log(response)
                })
                .catch(error => {
                    console.log(error)
                })

            this.$store.commit('setIsLoading', false)
        }
    }
}
</script>