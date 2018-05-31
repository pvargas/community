<template>
    <div id="app">
        <Navbar></Navbar>
        <b-container>
            <b-row>
                <b-col sm="12">
                <router-view :key="$route.path"></router-view>
                </b-col>

            </b-row>
        </b-container>
    </div>
</template>

<script>
import Navbar from './components/Navbar.vue'
import TagsSidebar from './components/TagsSidebar.vue'
export default {
  name: 'App',
  components: {
    Navbar,
    TagsSidebar
  }
}
</script>

<style>
/* fonts used: Roboto:400/500 , Abril Fatface, Merriweather*/
#app {
    font-family: 'Roboto', sans-serif;
    font-size: 16px;
}
.page-footer {
    position: fixed;
    bottom: 0%;
    margin: auto;
    display: flex;
    width: 100%;
    justify-content: center;
}

.btn {
    background-color: rgba(24, 27, 51, 0.795);
    border: none;
}

.btn:hover {
    background-color: #181B33;
}

</style>
