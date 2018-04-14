<template>
<div class="w_navbar">

  <b-navbar toggleable variant="default" type="light">

    <b-navbar-brand v-bind:to="'/posts'" class="font-header">Community</b-navbar-brand>

    <b-navbar-toggle target="hamburger-btn"></b-navbar-toggle>

    <b-collapse is-nav id="hamburger-btn">
        <b-navbar-nav class="ml-auto nav-form">
            <b-nav-form class="mr-3 my-auto">
                <b-form-input class="search-bar" type="text" placeholder="Search"></b-form-input>
            </b-nav-form>

            <LoginModal></LoginModal>
            <b-btn class="nav-btn my-auto" v-b-modal="'login-modal'" variant="outline-success" type="button">Log in</b-btn>

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
  <h1 class="section"></h1>
</div>
</template>

<script>
import LoginModal from './LoginModal.vue'
export default {
    name: 'navigator',
    data: function(){
      return {
        //pretty sure I DON'T need this
        searchExpand: false
      }
    },
    methods: {
      search: function(e) {
        e.preventDefault()
        searchExpand = true //nor this
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
    font-size: .8em;
    border: 0;
    outline: 0;
    padding: .3em .6em;
    height: 100%;
    border-radius: 5px;
}


.nav-btn:focus {
    outline: none;
    border: 0;
    box-shadow: none;
}

.search-bar {
    font-size: .8em;
    height: 100%;
    border: .5px solid lightgrey;
}

.search-bar:focus {
    box-shadow: none;
    border: .5px solid lightgrey;
}

.w_navbar {
    width: 80%;
    margin: auto;
}

.section {
  font-size: 0.9em;  
  color: #4d4d4d;
  border-top: 0.1em solid #dddddd;  
  margin-bottom: 1em;
}

#nav2 {
    margin-top: -.4rem;
}
</style>