<template>
  <div class="home">
    <section class="hero is-medium is-dark mb-6">
        <div class="hero-body has-text-centered">
            <p class="title mb-6">
                Welcome to Djacket
            </p>
            <p class="subtitle">
                The best jacket store online
            </p>
        </div>
    </section>

    <div class="columns is-multiline">
      <div class="column is-12">
          <h2 class="is-size-2 has-text-centered">Latest products</h2>
      </div>
      
      <div 
        class="column is-3" 
        v-for="product in latestProducts"
        v-bind:key="product.id"
      >
      <div class="box">
        <figure class="image mb-4">
          <img :src="product.get_thumbnail">
        </figure>
        
        <h3 class="is-size-4">{{ product.name }}</h3>
        <p class="is-size-6 has-text-gray">{{ product.price }}</p>
        
        <router-link v-bind:to="product.get_absolute_url" class="button is-dark mt-4">View Details</router-link>
      </div>
      </div>
  
    </div>
  </div>
</template>

<script>
import axios from 'axios'
//import { response } from 'express'

//import ProductBox from '@/components/ProductBox'

export default {
  name: 'Home',
  data() {
    return {
      latestProducts: []
    }
  },
  components: {
    //ProductBox
  },
  mounted() {
    this.getLatestProducts()

    document.title = 'Home | Djackets'
  },
  methods: {
    async getLatestProducts() {
      this.$store.commit('setIsLoading', true)

      await axios
        .get('/api/v1/latest-products/')
        .then(response => {
          this.latestProducts = response.data
        })
        .catch(error => {
          console.log(error)
        })

      this.$store.commit('setIsLoading', false)
    }
  }
}
</script>