<template>
  <div id="app">
    <Navbar></Navbar>
    <b-container>
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
/* fonts used: Roboto:400/500 , Abril Fatface, Merriweather*/
body {
  font-family: 'Roboto', sans-serif;
  font-size: 16px;
  background-color: #F8F8F8;
}
.page-footer {
  position: fixed;
  width: 100%;
  bottom: 0;
  line-height: 50px;
}
</style>
