<template>
<div class="w-postlist">
<b-row>
    <b-col sm="6" md="4" v-for="post in allPosts" v-bind:key="post.id" >
        <b-card class="card-text"
                :img-src="'https://picsum.photos/250/250?image=' + (post.id + 10)"
                img-fluid
                img-alt="image"
                img-top>
            <div class="card-text">
                <router-link :to="'/posts/' + post.id">
                    <span class="card-title">{{post.title}}</span>
                </router-link>

                <div class="text-muted">
                    Posted on 3/17/18 by:
                    <a href="#">Author{{post.author}}</a>
                </div>
                <div class="badge badge-info">
                    Tags
                </div>
            </div>
        </b-card>
    </b-col>
</b-row>
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
                    for (var i = 0; i < 3; i++){
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