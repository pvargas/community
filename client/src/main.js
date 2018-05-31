// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import Vue from 'vue'
import App from './App'
import BootstrapVue from 'bootstrap-vue'
import VueLocalStorage from 'vue-localstorage'
import Vuelidate from 'vuelidate'

import router from './router/index.js'
import VueResource from 'vue-resource'
import 'bootstrap/dist/css/bootstrap.css'
import 'bootstrap-vue/dist/bootstrap-vue.css'

import { UV_UDP_REUSEADDR } from 'constants';
import {http} from './services/http'

Vue.use(VueResource)
Vue.use(BootstrapVue)
Vue.use(Vuelidate)

Vue.use(VueLocalStorage, {
    name: 'ls',
    bind: true
})

Vue.prototype.$axios = http
Vue.prototype.$eventHub = new Vue();

Vue.http.options.xhr = {withCredentials: true}
Vue.config.productionTip = false

//eslint-disable no-new 
new Vue({
    el: '#app',
    router,
    components: { App },
    template: '<App/>'
}).$mount('#app')
