<template>
<div class="w_navbar">
  
  <b-navbar toggleable variant="default" type="light">

    <b-navbar-brand v-bind:to="'/posts'" class="font-header">Community</b-navbar-brand>

    <b-navbar-toggle target="hamburger-btn"></b-navbar-toggle>

    <b-collapse is-nav id="hamburger-btn">
        <b-navbar-nav class="ml-auto nav-form">
            <b-nav-form class="mr-3">
                <b-form-input class="search-bar" type="text" placeholder="Search"></b-form-input>
                <span class="input-group-btn">
                <b-button class="nav-btn" variant="outline-success" type="submit" v-on:click="search">
                    <i class="fas fa-search"></i>
                </b-button>
                </span>
            </b-nav-form>

            <LoginModal></LoginModal>
            <b-btn class="nav-btn" v-b-modal="'login-modal'" variant="outline-success" type="button">Log in</b-btn>

        </b-navbar-nav>
    </b-collapse>
  </b-navbar>
  <b-navbar id="nav2">
      <ul class="generic-tags">
          <li>Technology</li>
          <li>Science</li>
          <li>Politics</li>
          <li>Business</li>
          <li>Media</li>
          <li>Pop Culture</li>
          <li>World News</li>
      </ul>
  </b-navbar>
  
</div>
</template>

<script>
import LoginModal from './LoginModal.vue'
export default {
    name: 'navigator',
    data: function(){
      return {
        searchExpand: false
      }
    },
    methods: {
      search: function(e) {
        e.preventDefault()
        searchExpand = true
        //TODO: add functionality for searching website
      }
    },
    components: {
      LoginModal
    }
}
</script>

<style>
.font-header {
    font-family: 'Abril Fatface', cursive;  
    font-size: 2.2em !important;  
}

.generic-tags {
    margin: auto;
    list-style-type: none;
    display: flex;
    flex-direction: row;
    overflow: auto;
}

.generic-tags li{
    margin-right: 3rem;
}

.nav-btn {
    font-size: .9em;
}

.search-bar {
    font-size: .9em;
}

#nav2 {
    margin-top: -.4rem;
}
</style>