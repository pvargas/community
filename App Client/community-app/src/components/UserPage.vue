<template>
<div class="w-userpage">
<b-row>
    <b-col sm="2"></b-col>
    <b-col sm="4">
        <b-button variant="outline-primary">Posts</b-button>
        <b-button variant="outline-secondary">Comments</b-button>
    </b-col>
    <b-col sm="4">
    </b-col>
    <b-col sm="2"></b-col>
</b-row>
<b-row class="comments" v-for="comment in comments" v-bind:key="comment.id">
    <b-col cols="3" class="my-auto">
        <a href="#">
            <img class="img rounded mt-center" src="http://placehold.it/156x94" alt="">
        </a>
    </b-col>
    <b-col cols="9" class="my-auto">
        <p>{{comment.content}}</p>
        <a class="btn btn-default" href="#">View comments<span class="badge badge-info ml-2">231</span></a>
    </b-col>
</b-row>
</div>
</template>

<script>
export default {
    name: 'userpage',
    data() {
        return {
            comments: [],
            posts: [],
            user: {}
        }
    },
     created: function() {
        
    }
}
</script>

<style>
</style>