<template>
<div class="w_content">

<b-row v-if="!loading" class="mb-4">
    <b-col sm="12" offset-md="1" md="10" cols="12">
        <b-row class="post-info-outer">
            <b-col sm="10" cols="10" class="my-auto post-info">
                <h6 class="post-title my-auto">{{post.title}}</h6> 
                
                <div class="tags">
                    <div v-for="tag in post.tags" :key="tag.name" class="badge badge-info mr-1">
                        {{tag.name}}
                    </div>
                </div>
                <div class="media my-auto">                    
                    <b-img fluid class="rounded-circle mx-2 my-auto" 
                    :src="'https://api.adorable.io/avatars/50/' + post.author_id" alt=""/>
                    <div class="media-body my-auto">
                        <router-link class="my-auto" :to="'/users/' + post.author">{{post.author}}</router-link>
                        <p class="text-muted date my-auto">posted on {{toSimpleDate(post.created_at)}}</p>
                    </div>
                </div>
                
            </b-col>
            <b-col sm="2" cols="2" class="my-auto">
                <div class="score">
                    <button @click="upvote()" :pressed.sync="toggleUp"
                     :class="{'btn btn-clicked': myVoteValue == 1, 'btn': myVoteValue != 1}">
                        <i class="fas fa-angle-up mx-auto"></i>
                     </button>

                    <div class="mx-auto votes">{{voteValue}}</div>

                    <button @click="downvote()" :pressed.sync="toggleDown" 
                     :class="{'btn btn-clicked': myVoteValue == parseInt(-1), 'btn': myVoteValue != -1}">
                        <i class="fas fa-angle-down mx-auto"></i>
                     </button>
                </div>
            </b-col>
            <div v-if="sameUser">
                <span v-if="!deleteMenu" @click="toggleDeleteMenu()" class="ml-4 mt-1 text-muted delete-post">delete post</span>
                <span v-if="deleteMenu" class="ml-4 mt-1 text-muted delete-post">Really delete post?</span>
                <span v-if="deleteMenu"  @click="deletePost()" class="ml-4 mt-1 text-muted delete-post">yes</span>
                <span v-if="deleteMenu" @click="toggleDeleteMenu()" class="ml-4 mt-1 text-muted delete-post">no</span>
            </div>
        </b-row>
        <hr>

        <div class="img-box" 
        :style="'background-image: url(https://picsum.photos/900/300?image='+ (post.id + 1) +');'"></div>

        <hr>
        <div class="content-area">
            <p v-if="post.is_url == false">
                {{post.content}}
            </p>
            <a v-if="post.is_url" :href="post.content">{{post.content}}</a>
        </div>
        <hr>
    
        <MakeComment :parent="null" :postId="$route.params.postid"></MakeComment>
        
        <Comment :depth="0" :children="this.commentTree.children"></Comment>
        
    </b-col>
        
</b-row>
</div>
</template>

<script>
import Comment from './Comment.vue'
import MakeComment from './MakeComment.vue'
import {tokenedAxios} from '../services/http'
import {EventBus} from '../Events.js'
var TreeModel = require("tree-model")

export default {
    name: 'postcontent',
    components: {
        Comment,
        MakeComment
    },
    data() {
        return {
            post: {
                author: '',
                author_id: '',
                id: '',
                title: '',
                content: '',
                is_url: false,
                created_at: '',
                last_modified: '',
                tags: []
            },
            commentTree: {},
            loading: false,
            toggleUp: false,
            toggleDown: false,
            deleteMenu: false,
            sameUser: false,
            myVoteValue: 0,
            voteValue: 0,
            votes: []
        }
    },
    created: function() {
        let self = this
        let wait = 0
        self.loading = true

        

        //logic for immediately displaying comment rather than making api call again
        EventBus.$on('makecomment', function(comment) {
            let temp = new TreeModel()
            var parent = self.commentTree.first(function(node) {
                return node.model.id == comment.parent_id
            })

            if(parent) {
                parent.addChild(temp.parse(comment))
                parent.children[parent.children.length - 1].model.created_at = 'Just now'
                parent.children.splice(0, 0, parent.children[parent.children.length -1])
                parent.children.splice(parent.children.length - 1, 1)
                location.reload()
            } 
        })
        
        //populate post with info
        self.$axios.get('/posts/' + self.$route.params.postid)
        .then(function(response){
            let post = response.data.post
            self.post.id = post.id
            self.post.content = post.content,
            self.post.title = post.title,
            self.post.created_at = post.created_at,
            self.post.last_modified = post.last_modified,
            self.post.is_url = post.is_url
            self.post.author = post.author.name
            self.post.author_id = post.author.id

            if(self.$ls.get('CUser') == self.post.author) {
                self.sameUser = true
            }

            wait +=1
            if(wait >= 4)
                self.loading = false
            self.updateTree()
            
        })

        //if user logged in, get data ready for making comments
        if(self.$ls.get('CUser') && self.$ls.get('Token')) {
            self.$axios.get('/users/' + self.$ls.get('CUser'))
            .then(function(response) {
                self.userId = response.data.user.id
                wait +=1
                if(wait >= 4)
                    self.loading = false
            }).catch(function(e) {
                console.log(e.response.data.message)
            })
        } else {
            wait +=1
            if(wait >= 4)
                self.loading = false
        }
        
        //get vote info
        self.$axios.get('/posts/' + self.$route.params.postid + '/votes')
        .then(function(response) {
            let data = response.data
            self.voteValue = data.total
            self.votes = data.votes
            
            let theVote = self.getUserVoteFromList()
            if(theVote != null) {
                self.myVoteValue = theVote.value
            }

            wait +=1
            if(wait >= 4)
                self.loading = false
                
        
        })

        //get tag info for post
        self.$axios.get('/posts/' + self.$route.params.postid + '/tags')
        .then(function(response){
            let tags = response.data.tags
            self.post.tags = tags

            wait +=1
            if(wait >= 4)
                self.loading = false
        })
    },
    methods: {
        updateTree() {
            var self = this

            //populate comments
            self.$axios.get('/posts/' + self.$route.params.postid + '/comments')
            .then(function(response) {
            if (response.status == "200") {
                let data = response.data.comments;

                data.sort(function(a, b) {
                    return a.id - b.id
                });

                var tree = new TreeModel();
                var root = tree.parse({});

                for (var i = 0; i < data.length; i++) {
                    var node = tree.parse(data[i]);
                    //direct child of root
                    if (node.model.parent_id == null) {
                        root.addChild(node);
                    } else {
                        //find the parent node
                        var existingNode = root.first(function(parent) {
                            return parent.model.id == node.model.parent_id;
                        });
                        existingNode.addChild(node);
                    }
                }
            self.commentTree = root;
            self.$forceUpdate
            }
            });
        },
        vote(){
            let self = this
            if(self.$ls.get('Token') && self.$ls.get('CUser')){
                var http = tokenedAxios(self.$ls.get('Token'))

                let voter = self.$ls.get('CUser')
                let theVote = this.getUserVoteFromList()

                if(theVote != null) {
                    if(theVote.value != this.myVoteValue) {
                        this.voteValue -= theVote.value //subtract old vote
                        theVote.value = this.myVoteValue //find user value, change it to new value
                        this.voteValue += this.myVoteValue //add new value to total
                    } else {
                        this.voteValue -= theVote.value
                        console.log('removed')
                        this.myVoteValue = 0
                        theVote.value = 0
                    }
                } else {
                    this.voteValue += this.myVoteValue  //add new value to total
                    this.votes.push({value: this.myVoteValue, voter: {name: voter}}) //add basic vote info to votes array
                }

                http.post('/posts/' + self.$route.params.postid + '/votes', 
                {voter: self.$ls.get('CUser'), value: self.myVoteValue})
                .then(function(response) {
                    console.log(response.status)
                }).catch(function(e) {
                    console.log(e)
                })
            } else {
                window.alert('You are not logged in')
            }
        },
        getUserVoteFromList(){
            let voter = this.$ls.get('CUser')
            for(let i = 0; i < this.votes.length; i++) {
                if(this.votes[i].voter.name == voter ) {
                    return this.votes[i]
                }
            }
            return null
        },
        toSimpleDate(date) {
            return date.substr(0, 10)
        },
        upvote() {
            this.myVoteValue = 1
            this.vote()
        },
        downvote() {
            this.myVoteValue = -1
            this.vote()
        },
        toggleDeleteMenu() {
            if(this.deleteMenu == true){
                this.deleteMenu = false
            } else {
                this.deleteMenu = true
            }
        },
        deletePost() {
            let self = this

            if(self.$ls.get('CUser') && self.$ls.get('Token')) {
                let http = tokenedAxios(self.$ls.get('Token'))

                http.delete('/posts/' + self.post.id)
                .then(function(response) {
                    self.$router.push('/posts', function() {window.alert('successfully deleted post')})
                }).catch(function(e) {
                    console.log(e.response.data.message)
                })
            } else {
                window.alert('You are not logged in')
            }
        }
    }
}
</script>

<style scoped>

.score {
    display: flex;
    flex-direction: column;
    align-items: center;
}

.votes {
    padding-right: 1.3px;
}

.post-info-outer {
    background-color: whitesmoke;
    border-radius: 5px;
    padding: .5em;
}

.media {
    padding-top: .5em;
}

.content-area {
    background: whitesmoke;
    border-radius: 10px;
    padding-left: 1em;
    padding-right: 1em;
    padding-bottom: 1em;
    word-break: break-word;
    white-space: pre-line;
}

.btn {
    color: rgba(24, 27, 51, 0.795);;
    background-color: inherit;
    border-radius: 25px;
}

.btn:hover,
.btn:active {
    color: white;
    background-color: none;
    outline: none!important;
    box-shadow: none!important;
    
}

.btn-clicked {
    color: white!important;
    background-color: grey;
    
}

.btn:focus {
    box-shadow: none!important;
    outline: none!important;
}

.post-title {
    font-size: 1.6em;
    text-decoration: none;
    color: #11142C;
}

.btn:focus {
    outline: none;
    box-shadow: none;
}

.user-text {
    color: grey;
    font-size: 0.9em;
}

.img-box {
    height: 15em;
    width: 100%;
    background-size: cover;
    background-position: 50% 50%;
}

.date {
    font-size: 0.9em;
}

.tags {
    display: flex;
    flex-direction: row;
}

.delete-post {
    font-size: .8em;
}

.delete-post:hover {
    color: black!important;
    transform: scale(1.01)!important;
    cursor: pointer;
}

a {
    text-decoration: none;
}

router-link {
    text-decoration: none;
}
</style>