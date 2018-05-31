import Vue from 'vue'
import VueRouter from 'vue-router'

import Posts from './../components/Posts.vue'
import PostContent from './../components/PostContent.vue'
import UserPage from './../components/UserPage.vue'
import MakePost from './../components/MakePost.vue'
import LandingPage from './../components/LandingPage.vue'

Vue.use(VueRouter)

export default new VueRouter({
    routes: [
       /* {
            path: '/',
            name: 'landing',
            component: LandingPage
        },*/
        {
            path: '/',
            redirect: '/posts'
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
        },
        {
            path: '/makepost',
            name: 'makepost',
            component: MakePost
        }
    ],
    scrollBehavior (to, from, savedPosition) {
        return {
            x: 0,
            y: 0
        }
      },
      mode: 'history'
})