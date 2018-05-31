<template>
<div class="w-userpage">
<h1 class="section"></h1>


<div class="mb-4 buttons">
        <button @click="showCommentList = false" 
        :class="{'full-btn selected': !showCommentList, 'full-btn': showCommentList}"
         variant="outline-secondary">Posts</button>

        <button @click="showCommentList = true" 
        :class="{'full-btn selected': showCommentList, 'full-btn': !showCommentList}" 
        variant="outline-secondary">Comments</button>
</div>

<b-row>
    
    <b-col sm="9" class="">

        <!--Show all comments-->
        <div v-show="showCommentList" class="posts" 
                v-for="comment in comments" v-bind:key="comment.id">
                <router-link :to="'/posts/' + comment.post_id">
                    <div class="box mb-2">
                        <div class="title"><h5>{{comment.title}}</h5></div>
                        <div class="date">
                            {{toSimpleDate(comment.created_at)}}
                        </div>
                        <div class="comment-text">
                            {{comment.content}}
                        </div>
                    </div>
                </router-link>
        </div>

        <!--Show all posts-->
        <div v-show="!showCommentList" class="posts" 
                v-for="post in posts" v-bind:key="post.id">
                <router-link :to="'/posts/' + post.id">
                    <div class="box mb-2">
                        <div class="title"><h5>{{post.title}}</h5></div>
                        <div class="date">
                            {{toSimpleDate(post.created_at)}}
                        </div>
                    </div>
                </router-link>
        </div>
    </b-col>

    <b-col sm="3">
        <UserSidebar :commentCount="commentCount" 
                     :postCount="postCount">
        </UserSidebar>
    </b-col>
</b-row>

</div>
</template>

<script>
import UserSidebar from './UserPageSidebar.vue'
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
            commentCount: '',
            postCount: '',
            showCommentList: false
        }
    },
    created: function() {
        let self = this
        self.$axios.get('/users/' + self.$route.params.userName + '/posts' )
            .then(function(response){
                if(response.status == "200"){
                    let data = response.data.posts
                    self.postCount = response.data.count
                    for (var i = 0; i < data.length; i++){
                        self.posts.push({
                            author: data[i].author,
                            content: data[i].content,
                            id: data[i].id,
                            created_at: data[i].created_at,
                            last_modified: data[i].last_modified,
                            title: data[i].title,
                            is_url: data[i].is_url 
                        })
                    }
                }
            })

        self.$axios.get('/users/' + self.$route.params.userName + '/comments' )
            .then(function(response){
                if(response.status == "200"){
                    let data = response.data.comments
                    self.commentCount = response.data.count
                    for (var i = 0; i < data.length; i++){
                        self.comments.push({
                            author: data[i].author,
                            content: data[i].content,
                            id: data[i].id,
                            created_at: data[i].created_at,
                            last_modified: data[i].last_modified, 
                            title: data[i].post.title,
                            post_id: data[i].post_id
                        })
                    }
                }
                console.log(self.comments)
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
        },
        toSimpleDate(date) {
            return date.substr(0, 10)
        }
    }
}
</script>

<style scoped>

.display {
    display: flex;
    flex-direction: column;
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
    background-color: #F8EEE4;
    cursor: pointer;
    border: none;
}

.full-btn:hover {
    background-color: #F2E5D2;
}

.box {
    display: flex;
    flex-direction: column;
    min-height: 5em;
    width: 100%;
    background-color: whitesmoke;
    padding: 1em;
    transition: .2s;
}

.box:hover {
    background-color: tan;
    transform: scale(1.05)
}

a:hover {
    text-decoration: none;
}

.title {
    display: flex;
    flex-direction: row;
    min-height: 2em;
    font-size: 1em;
    color: black;
}

.date {
    display: flex;
    flex-direction: row;
    color: darkgrey;
}

.section {
  font-size: 0.9em;  
  color: #4d4d4d;
  border-top: 0.1em solid #dddddd;  
  margin-bottom: 1em;
}

.btn {
    background-color: tan;
    max-width: 15em;
}

.buttons {
    margin-left: 30px;
    width: 40%;
}

.selected {
    background-color: tan;
}

.comment-text {
    color: black;
}

@media screen and (max-width: 576px){
    .buttons {
        margin-left: 0px;
        width: 100%;
    }

    .btn {
        max-width: 100%;
        margin-bottom: .5em;
    }


}

</style>