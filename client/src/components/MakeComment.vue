<template>
<div class="w_makecomment">
    <div class="card my-4">
        <h5 class="card-header">reply</h5>
        <div class="card-body">
            <form>
                <div class="form-group">
                    <textarea v-model="textField" class="form-control" rows="3"></textarea>
                </div>
                <b-btn class="btn btn-primary" v-on:click="postComment">Submit</b-btn>
            </form>
        </div>
    </div>
</div>
</template>

<script>
import {tokenedAxios} from '../services/http'
import {EventBus} from '../Events.js'

export default {
    name: 'makecomment',
    props: ['parent', 'postId'],
    data() {
        return {
            textField: '',
            comment: {
                parent_id : -1,
                post_id : -1,
                author : '',
                content : ''
            },
            errors:[]
        }
    },
    methods: {
        postComment: function(){
            var self = this

            if(self.$ls.get('Token') && self.$ls.get('CUser')){
                var http = tokenedAxios(self.$ls.get('Token'))
            
                self.comment.parent_id = self.parent
                self.comment.post_id = self.$route.params.postid
                self.comment.author = self.$ls.get('CUser')
                self.comment.content = self.textField


                http.post('/comments', self.comment)
                .then(function(response) {
                    if(response.status == "200"){
                        console.log('successfully posted')
                        EventBus.$emit('makecomment', self.comment)
                        //location.reload()
                    }
                }).catch(function(e) {
                    console.log(e)
                })
            }
        }
    }
}
</script>

<style scoped>
.card {
    width: 100%;
}
</style>