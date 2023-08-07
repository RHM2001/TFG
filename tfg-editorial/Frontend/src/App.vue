<script setup>
import Header from './components/Header.vue';
import Footer from './components/Footer.vue';

</script>

<template>
  
  <div id="app">
    <Header />
    <router-view></router-view>
    <Footer />
  </div>
</template>

export default {
  name: 'App',
}