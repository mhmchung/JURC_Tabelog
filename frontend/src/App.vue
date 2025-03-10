<template>
  <div class="bg-gray-100 min-h-screen">
    <!-- Header -->
    <header class="bg-white shadow-md p-4 flex justify-between items-center">
      <h1 class="text-2xl font-extrabold text-gray-800">🍽️ Tabelog</h1>
      <nav>
        <ul class="flex space-x-6">
          <li><router-link to="/" class="hover:text-red-500 font-semibold">Home</router-link></li>
          <li><router-link to="/restaurants" class="hover:text-red-500 font-semibold">Restaurants</router-link></li>
          <li><router-link to="/profile" class="hover:text-red-500 font-semibold">Profile</router-link></li>
        </ul>
      </nav>
    </header>

    <!-- Hero Section -->
    <section class="relative w-full h-[50vh] bg-cover bg-center flex items-center justify-center" style="background-image: url('https://source.unsplash.com/1600x900/?restaurant,food');">
      <div class="bg-black bg-opacity-50 p-10 text-white text-center rounded-lg">
        <h2 class="text-4xl font-bold">Discover the Best Restaurants 🍜</h2>
        <p class="mt-3 text-lg">Find the best dining experiences tailored to your taste.</p>
      </div>
    </section>

    <!-- Restaurant Listings -->
    <main class="p-10">
      <h3 class="text-3xl font-bold text-gray-800 mb-6">Top Restaurants</h3>
      <div class="grid grid-cols-1 sm:grid-cols-2 md:grid-cols-3 gap-6">
        <div v-for="restaurant in restaurants" :key="restaurant.id" class="bg-white p-5 rounded-xl shadow-lg transition-transform transform hover:scale-105">
          <img :src="restaurant.image || 'https://source.unsplash.com/400x300/?food,dish'" alt="Restaurant Image" class="w-full h-40 object-cover rounded-lg">
          <h4 class="text-xl font-semibold mt-3">{{ restaurant.name }}</h4>
          <p class="text-gray-600 text-sm mt-1">{{ restaurant.category }}</p>
          <p class="mt-2 font-bold text-yellow-500">⭐ {{ restaurant.rating }} / 5</p>
          <router-link :to="`/restaurants/${restaurant.id}`" class="inline-block mt-4 text-red-500 font-bold hover:underline">View Details →</router-link>
        </div>
      </div>
    </main>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  data() {
    return {
      restaurants: []
    };
  },
  mounted() {
    this.fetchRestaurants();
  },
  methods: {
    async fetchRestaurants() {
      try {
        const response = await axios.get('http://localhost:8000/restaurants/');
        this.restaurants = response.data;
      } catch (error) {
        console.error('Error fetching restaurants:', error);
      }
    }
  }
};
</script>

<style>
body {
  font-family: 'Arial', sans-serif;
  background-color: #f8f8f8;
}
</style>
