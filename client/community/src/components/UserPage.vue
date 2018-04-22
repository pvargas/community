<template>
<div class="w-userpage">
<h1 class="section"></h1>


<b-row class="mb-4">
    <b-col sm="4" xs="12">
        <b-button v-on:click="showCommentList = false" class="full-btn" variant="outline-primary">Posts</b-button>
    </b-col>
    <b-col sm="4" xs="12">
        <b-button v-on:click="showCommentList = true" class="full-btn" variant="outline-secondary">Comments</b-button>
    </b-col> 
</b-row>


<b-row>
    
    <b-col sm="9" class="display">

        <!--Show all comments-->
        <div v-show="showCommentList" class="comments" v-for="comment in comments" v-bind:key="comment.id">
            <b-row>
                <b-col cols="12">
                    <h5>{{getPostTitleById(comment.postid)}}</h5>
                </b-col>
            </b-row>
            <b-row>
                <b-col cols="12" class="my-auto">
                    <p>{{comment.content}}</p>
                </b-col>
            </b-row>
            <b-row>
                <b-col cols="5" offset="1">
                    <b-btn class="full-btn" variant="secondary" size="sm" href="#">View post<span class="badge badge-light ml-2">231</span></b-btn>
                </b-col>
            </b-row> 
            <hr>     
        </div>

        <!--Show all posts-->
        <div v-show="showCommentList == false" class="posts" v-for="post in posts" v-bind:key="post.id">
            <b-row>
                <b-col cols="12">
                    <h5 style="color: cornflowerblue;">{{post.title}}</h5>
                </b-col>
            </b-row>
            <b-row>
                <b-col cols="12" class="my-auto">
                    <p>{{post.content}}</p>
                </b-col>
            </b-row>
            <b-row>
                <b-col cols="5" offset="1">
                    <b-btn class="full-btn" variant="primary" size="sm" href="#">View post<span class="badge badge-success ml-2">231</span></b-btn>
                </b-col>
            </b-row>
            <hr>     
        </div>
    </b-col>

    <b-col sm="3">
        <UserSidebar></UserSidebar>
    </b-col>
</b-row>

</div>
</template>

<script>
import UserSidebar from './hUserPageSidebar.vue'
export default {
    name: 'userpage',
    components: {
        UserSidebar
    },
    data() {
        return {
            comments: [],
            posts: [],
            user: {},
            showCommentList: true
        }
    },
    created: function() {
        //actual endpoint http://community.io/api/v1/posts  
        this.$http.get('https://jsonplaceholder.typicode.com/comments')
            .then(function(response){
                if(response.status == "200"){
                    let list = response.data
                    for (var i = 0; i < list.length; i++){
                        var item = list[i]
                        this.comments.push({
                            author: item.email,//author: item.author, 
                            content: item.body,//content: item.content,
                            commentid: item.id,
                            postid: item.postId
                            //created_at: item.created_at,
                            //is_url: item.is_url,
                            //last_modified: item.last_modified
                            
                        })
                    }
                }
            })

        this.$http.get('https://jsonplaceholder.typicode.com/posts')
            .then(function(response){
                if(response.status == "200"){
                    let list = response.data
                    for (var i = 0; i < list.length; i++){
                        var item = list[i]
                        this.posts.push({
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
    },
    methods: {
        getPostTitleById: function(searchId){
            for(var i = 0; i < this.posts.length; i++){
                var temp = this.posts[i];
                if(temp.id == searchId){
                    return temp.title;
                }
            }
            return 0;
        }
    },
}
</script>

<style>

.display {
    display: flex;
    flex-direction: column;
    background-color: whitesmoke;
    border-radius: 5px;
    height: auto;
}

h4 {
    color: cornflowerblue;
    font-family: 'Roboto', sans-serif;
    font-weight: 500;
}

.btn:focus {
    outline: none;
    box-shadow: none;
    
}
.full-btn {
    width: 100%;
}

.section {
  font-size: 0.9em;  
  color: #4d4d4d;
  border-top: 0.1em solid #dddddd;  
  margin-bottom: 1em;
}

</style>