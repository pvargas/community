<template>
<div class="w-postlist">

<b-card-group columns>
    <b-card class="card-text" v-for="post in allPosts" v-bind:key="post.id" 
            img-src="http://placehold.it/200x150"
            img-fluid
            img-alt="image"
            img-top>
        <router-link :to="'/posts/' + post.id"><span class="card-title">{{post.title}}</span></router-link>
        <p class="text-muted">
            Posted on 3/17/18 by:
            <a href="#">Author{{post.author}}</a>
        </p>
        <p class="badge badge-info">
            Tags
        </p>
        <p class="card-text">
            {{post.content}}
        </p>
    </b-card>
</b-card-group>
</div>
</template>

<script>
export default {

    name: 'Posts',
    data() {
        return {
            allPosts: []
        }
    },

    created: function() {
        //actual endpoint http://community.io/api/v1/posts  
        this.$http.get('https://jsonplaceholder.typicode.com/posts').then(function(response){
                if(response.status == "200"){
                    let list = response.data
                    for (var i = 0; i < list.length; i++){
                        var item = list[i]
                        this.allPosts.push({
                            author: item.userId,//author: item.author, 
                            content: item.body,//content: item.content,
                            title: item.title,
                            id: item.id
                            //created_at: item.created_at,
                            //is_url: item.is_url,
                            //last_modified: item.last_modified
                            
                        })
                    }
                }
            })
    }
}
</script>

<style scoped>
.card-text {
  font-family: 'Merriweather', serif;
  text-decoration: none;
  color: black;
}

.card-title {
    font-size: 1.5rem; 
    text-decoration: none;
    color: black;
}
</style>