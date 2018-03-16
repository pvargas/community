<template>
  <div id="app">
    <Navbar></Navbar>
    <b-container fluid>
      <router-view></router-view>
    </b-container>
  </div>
</template>

<script>
import Navbar from './components/Navbar.vue'
export default {
  name: 'App',
  components: {
    Navbar
  }
}
</script>

<style>

body {
  font-family: 'Roboto', sans-serif;
  font-size: 16px;
  background-color: #F8F8F8;
}
footer {
  position: fixed;
  width: 100%;
  bottom: 0;
  line-height: 50px;
}
</style>
