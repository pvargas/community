<template>
<div class="w_posts">

<h1 class="section">TOP POSTS</h1>
<div v-if="loading" style="color: darkgrey; font-size: 1.5em; text-align: center;">
    <div class="loader"></div>
</div>

<div class="error" v-if="error" style="text-align: center;">
    <h4>Server error</h4>
    <h6>{{errorText}}</h6>
</div>

<div v-if="!error && !loading"><span @click="toggleNewest" :class="{'selected': newest, 'not-selected': !newest}">Newest</span> 
                     <span @click="toggleNewest" :class="{'selected': !newest, 'not-selected': newest}">Oldest</span>
</div>
<b-row v-if="!loading">
    
    <b-col id="column" v-for="post in filteredPosts" :key="post.id" lg="4" md="6" sm="12">
        <router-link :to="'/posts/' + post.id">
            <div class="post-box">
                <div class="img-box" 
                    :style="'background-image: url(https://picsum.photos/250/250?image=' + 
                    (post.id + 1) + ');'">
                </div>
                
                <div class="card-custom">
                    <div class="card-content-area">

                        <router-link v-if="post.is_url == false" :to="'/posts/' + post.id">
                            <div class="post-header">{{post.title}}</div>
                        </router-link>

                        <a v-if="post.is_url == true" :href="post.content">
                            <div class="post-header">{{post.title}}</div>
                        </a>

                        <div class="text-muted">Posted on {{toSimpleDate(post.created_at)}}</div>
                        <span>
                            <span class="text-muted">Author: </span>
                            <a :to="'/users/' + post.name">{{post.author.name}}</a>
                        </span>
                        
                        <div v-for="tag in post.tags" :key="tag.id" 
                            class="badge badge-info mr-1">{{tag.name}}</div>

                    </div>
                </div>
            </div>
        </router-link>
    </b-col>
</b-row>


</div>
</template>

<script>
import PostsList from './PostsList.vue'
import {EventBus} from '../Events.js'
export default {
    name: 'Posts',
    data() {
        return  {
            posts: [],
            filteredPosts: [],
            loading: false,
            newest: true,
            error: false,
            errorText: ''
        }
    },
    components: {
        PostsList
    },
    created() {
        let self = this
        self.updatePosts()
        EventBus.$on('tagfilter', function(tag) {
            self.setPostsByFilter()
        }) 
        
    },
    methods: {

        /*must first send get for /posts to find number of posts and their id's
          then get request per post to get every post's tag 
          this is the reason for the slow front page*/
        updatePosts() {
            let self = this
            self.loading = true
            self.$axios.get('/posts')
            .then(function(response){
                let data = response.data.posts
                let wait = 0
                for (var i = 0; i < data.length; i++){
                    self.$axios.get('/posts/' + data[i].id) 
                    .then(function(response2){
                        self.posts.push(response2.data.post)
                        wait+= 1
                        if(wait >= data.length) {
                            self.setPostsByFilter()
                            self.loading = false
                        }
                    })
                }
            }).catch(function(e) {
                self.error = true
                self.errorText = e.response.data.message
                self.loading = false 
            })
        },
        setPostsByFilter() {
            let self = this
            let lsTags = JSON.parse(self.$ls.get('Tags'))
            self.filteredPosts = []
            for(let i = 0; i < lsTags.length; i++){
                if(lsTags[i].selected == true) {
                    for(let j = 0; j < self.posts.length; j++) {
                        let post = self.posts[j]
                        if(self.containsTag(post.tags, lsTags[i].name) && !self.existsInFilteredPosts(post)) {
                            self.filteredPosts.push(post)
                        }
                    }
                }
            }
            self.filteredPosts.sort(function(postA, postB) {
                return postB.created_at.localeCompare(postA.created_at)
            })
        },
        containsTag(tags, tagName) {
            for(let i = 0; i < tags.length; i++) {
                if(tags[i].name.toLowerCase() == tagName.toLowerCase()) {
                    return true
                }
            }
            return false
        },
        postMatchesFilters(post) {
            let self = this
            for(let i = 0; i < post.tags.length; i++){
                if(self.tagIsSelected(post.tags[i].name)){
                    return true
                }
            }
            return false
        },
        existsInFilteredPosts(post) {
            for(let i = 0; i < this.filteredPosts.length; i++) {
                if(post.id == this.filteredPosts[i].id) {
                    return true
                }
            }
            return false
        },
        toSimpleDate(date) {
            let str = ''
            str += date.substr(0, 10)
            return str
        },
        toggleNewest() {
            if(this.newest == true) {
                this.newest = false
                this.filteredPosts.sort(function(postA, postB) {
                    return postA.created_at.localeCompare(postB.created_at)
                })
            } else {
                this.newest = true
                this.filteredPosts.sort(function(postA, postB) {
                    return postB.created_at.localeCompare(postA.created_at)
                })
            }
        }
    }
}
</script>

<style>

.post-box {
    display: flex;
    flex-direction: row;
    align-content: center;
    margin-bottom: 1rem;
    min-height: 9em;
    transition: .1s;
}

a:hover {
    text-decoration: none;
}

.card-custom {
    border: 1px solid lightgrey;
    padding: 1rem;
    width: 50%;
    height: auto;
    transition: .2s;
    word-wrap: break-word;
    overflow: hidden;
}

.post-box:hover {
    transform: scale(1.02);
    background-color: rgba(82, 73, 172, 0.13);
}

.img-box {
    width: 50%;
    height: auto;
    background-size: cover;
    background-position: 50% 50%;
}

.post-header {
    font-family: 'Merriweather', serif;
    font-size: 0.85em;  
    text-decoration: none;
    color: black;
}

.post-header:hover {
  color: black;
  text-decoration-color: grey !important;
}

.post-header:visited {
    text-decoration: none;
    color: black;
}

.text-muted {
    font-size: .8em;
}

.section {
    font-size: 0.9em;  
    color: #4d4d4d;
    border-top: 0.1em solid #dddddd;  
    margin-bottom: 1em;
}

.selected {
    color: black;
    cursor: pointer;
}


.loader {
    border: 16px solid #f3f3f3; 
    border-top: 16px solid tan; 
    border-radius: 50%;
    width: 90px;
    height: 90px;
    animation: spin 2s linear infinite;
    margin: auto;
}

@keyframes spin {
    0% { transform: rotate(0deg); }
    100% { transform: rotate(360deg); }
}

.not-selected {
    color: grey;
    cursor: pointer;
}

router-link, a {
    text-decoration: none;
}

.error {
    color: rgb(197, 40, 40);
}

@media screen and (min-width: 576px){
    .card-custom {
        width: 100%;
        display: flex;
        align-items: flex-start;
        height: 9em;
    }

    .post-box {
        flex-direction: column;
        width: 100%;
        margin-bottom: 2rem;
    }

    .img-box {
        width: 100%;
        height: 10em;
    }
    
}

</style>