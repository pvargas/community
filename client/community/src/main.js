// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import Vue from 'vue'
import App from './App'
import BootstrapVue from 'bootstrap-vue'

import VueRouter from 'vue-router'
import VueResource from 'vue-resource'
import 'bootstrap/dist/css/bootstrap.css'
import 'bootstrap-vue/dist/bootstrap-vue.css'

import Posts from './components/Posts.vue'
import PostContent from './components/PostContent.vue'
import UserPage from './components/UserPage.vue'

Vue.use(VueRouter)
Vue.use(VueResource)
Vue.use(BootstrapVue)
Vue.http.options.xhr = {withCredentials: true}
Vue.config.productionTip = false

const routes = [
  
    {
        path: '/',
        redirect: {
            name: 'posts'
        }
    },
    {
        path: '/posts',
        name: 'posts',
        component: Posts
    },
    { 
        path: '/posts/:postid',
        name: 'post',
        component: PostContent
    },
    {
        path: '/users',
        name: 'users'
    },
    {
        path: '/users/:userName',
        name: 'user',
        component: UserPage
    }
]

const router = new VueRouter({
  routes,
  mode: 'history'
})


//eslint-disable no-new 
new Vue({
  el: '#app',
  router,
  components: { App },
  template: '<App/>'
}).$mount('#app')
