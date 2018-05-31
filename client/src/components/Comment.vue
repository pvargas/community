<template>
    <div class="w_comment" >
        <b-row v-if="depth>0" :style="indent" class="custom mb-2">
            <b-col cols="12" sm="12">
                <div class="media mb-2" style="margin-left: -3em;">
                    <img class="mr-3 rounded-circle" v-bind:src="'https://api.adorable.io/avatars/50/' + author.id" alt="">
                    <div class="media-body">
                        <p v-if="!edit" style="margin-bottom: -.1em;">{{content}}</p>
                        <router-link :to="'/users/' + author.id" class="username mr-2">
                            <span v-if="author.name">{{author.name}}</span>
                            <span v-if="!author.name">{{author}}</span>
                        </router-link><span v-if="createdAt" class="user-text">posted on {{toSimpleDate(createdAt)}}</span>
                        <div v-if="loggedIn">
                            <span v-if="!sameUser" class="cursor ml-2" v-on:click="toggleShowForm">reply</span>
                            <div v-if="sameUser">
                                <span v-if="!edit" class="cursor ml-1" v-on:click="editComment">edit</span>
                                <span v-if="edit" class="cursor ml-1" v-on:click="editComment">cancel</span>
                                <span v-if="edit" class="cursor ml-1" v-on:click="saveCommentEdit()">save</span>
                            </div>
                        </div>
                        <br>
                        <textarea class="edit-comment" v-if="edit" v-model="content"></textarea>               
                    </div>
                </div>
            </b-col>
            <b-col cols="12" sm="12">
                <MakeComment v-show="showForm" :parent="id" :postId="postId"></MakeComment>
            </b-col>
        </b-row>

        <comment v-for="child in children"
                 :children="child.children" 
                 :id="child.model.id"
                 :author="child.model.author"
                 :createdAt="child.model.created_at"
                 :content="child.model.content"
                 :depth="depth + 1"
                 :postId="child.model.post_id"
                 :key="child.model.id"
        >
        </comment>
    </div>
</template>

<script>
import MakeComment from './MakeComment.vue'
import {tokenedAxios} from '../services/http'

export default {
    name: 'comment',
    data: function() {
        return {
            showForm: false,
            edit: false,
            sameUser: false,
            loggedIn: false
        }
    },
    components: {
        MakeComment
    },
    props: ['children', 'id', 'content', 'author', 'createdAt', 'depth', 'postId'],
    computed: {
        indent() {
            return {
                transform: `translate(${this.depth * 30}px)` 
            }
        }
    },
    created() {
        if(this.depth != 0) {
            if(this.$ls.get('CUser') && this.$ls.get('Token')) {
                this.loggedIn = true
            }

            if(this.$ls.get('CUser') == this.author.name) {
                this.sameUser = true
            }
        }
    },
    methods: {
        toggleShowForm: function() {
            if(this.showForm == false){
                this.showForm = true;
            }
            else {
                this.showForm = false;
            }
        },
        toSimpleDate(date) {
            return date.substr(0, 10)
        },
        editComment() {
            if(this.edit == false){
                this.edit = true;
            }
            else {
                this.edit = false;
            }
        },
        saveCommentEdit() {
            let self = this
            self.edit = false

            if(self.$ls.get('Token') && self.$ls.get('CUser')){
                var http = tokenedAxios(self.$ls.get('Token'))

                http.put('/comments/' + self.id, {content: self.content})
                .then(function(response) {
                    console.log('successfully posted')
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

.custom {
    font-size: .9em;
    color: grey;
    width: 100%;
}

.user-text {
    color: darkgrey;
}

.username {
    text-decoration: none;
}

.cursor {
    cursor: pointer;
}

.edit-comment {
    max-width: 100%;
}

</style>