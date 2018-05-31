<template>
<div class="w_makepost">
<b-row>
    <b-col xs="12" sm="12" offset-md="1" md="10">
    <div class="tabs">
        <div v-on:click="textPost" :class="{'tab tab-inactive': post.is_url,  
                'tab tab-active': !post.is_url}"
                >Text</div>

        <div v-on:click="linkPost" :class="{'tab tab-active': post.is_url,  
                'tab tab-inactive': !post.is_url}"
                >Link</div>
    </div>
    <div class="post-items">
        <label for="title">Title</label>
        <b-input id="title" v-model="post.title" class="input"></b-input>
        <p class="error" v-if="!$v.post.title.required">* Required</p>

        <div class="navbar-tags-box">
            <div v-for="tag in tagsList" @click="toggleTag(tag)" :key="tag.name" 
            :class="{'tag mr-4 mt-1': tag.selected, 'tag not-tag mr-4 mt-1': !tag.selected}">
                {{tag.name}}
            </div>
        </div>

        <div v-if="post.is_url">
            <label for="url">URL</label>
            <b-form-input type="text" id="url" v-model="post.content" class="input"/>
            <p class="error" v-if="!$v.post.content.required">* Required</p>
        </div>

        <div v-if="!post.is_url">
            <label for="post-text">Content</label>
            <b-textarea id="post-text"
                        class="text-area"
                        v-model="post.content"
                        placeholder="Post text"
                        :rows="5"
                        :max-rows="20"
                        style="white-space: pre-wrap;">
            </b-textarea>
            <p class="error" v-if="!$v.post.content.required">* Required</p>
        </div>


        <b-btn class="create-btn" v-on:click="createPost()">Create</b-btn>
    </div>

    
    </b-col>
</b-row>
</div>
</template>

<script>
import {tokenedAxios} from '../services/http'
import {required, alphaNum} from 'vuelidate/lib/validators'
export default {
    data() {
        return {
            tagsList:  [{name: 'Technology', selected: false},
                        {name: 'Science', selected: false},
                        {name: 'Politics', selected: false},
                        {name: 'Business', selected: false},
                        {name: 'Media', selected: false},
                        {name: 'Culture', selected: false},
                        {name: 'News', selected: false}, 
                        {name: 'Art', selected: false}, 
                        {name: 'Other', selected: false}],
            post: {
                title: '',
                content: '',
                tags: [],
                author: '',
                is_url: false
            }
        }
    },
    validations: {
        post: {
            title: {
                required
            },
            content: {
                required
            }
        }
    },
    methods: {
        createPost() {
            var self = this
            if(self.$v.post.$invalid == false){
                for(let i = 0; i < self.tagsList.length; i++) {
                    if(self.tagsList[i].selected == true) {
                        self.post.tags.push({name: self.tagsList[i].name})
                        console.log(self.post.tags)
                    }
                }
                if(self.$ls.get('Token') && self.$ls.get('CUser')){
                    var http = tokenedAxios(self.$ls.get('Token'))
                    self.post.author = self.$ls.get('CUser')

                    http.post('/posts', self.post)
                    .then(function(response) {
                        if(response.status == "200"){
                            console.log('successfully posted')
                            self.$router.push('/posts/' + response.data.post.id)
                        }
                    })
                    .catch(function(e) {
                        console.log(e.data.response)
                    })
                }else {
                    window.alert('You are not logged in')
                }
            } else {
                window.alert('Fill in required fields')
            }
        },
        removeTag(tag) {
            var index = this.post.tags.indexOf(tag)
            if(index != -1) {
                this.post.tags.splice(index, 1)
            }
        },
        textPost() {
            if(this.post.is_url == true) {
                this.post.is_url = false
            } 
        },
        linkPost() {
            if(this.post.is_url == false) {
                this.post.is_url = true
            }
        },
        capitalizeFirstLetter(string) {
            return string.charAt(0).toUpperCase() + string.slice(1);
        },
        toggleTag(tag){
            if(tag.selected == true) {
                tag.selected = false
            } else {
                tag.selected = true
            }
        }
    }
}
</script>

<style scoped>

.tabs {
    display: flex;
    flex-direction: row;
    width:40%;
}

@media screen and (max-width: 576px){
    .tabs {
        width: 100%;
    }
}

.tab {
    font-size: .85em;
    border-top-right-radius: 5px;
    border-top-left-radius: 5px;
    text-align: center;
    width: 100%;
}
.tab-inactive {
    background-color:#F2E5D2;
}
.tab-active {
    background-color: #BF8D72;
}

.tab:hover {
    cursor: pointer;
}


.post-items {
    border: 1px solid rgb(209, 167, 144);
    background: white;
    padding: 1em;
    padding-bottom: 1.5em;
    display: flex;
    flex-direction: column;
}

.text-area:focus,
.text-area:active,
.text-area,
.input {
    box-shadow: none;
    outline: 0px !important;
    -webkit-appearance:none;
}
.navbar-tags-box {
    background-color: inherit;
    display: flex;
    flex-direction: row;
    flex-wrap: wrap;
    width: 100%;
    justify-content: center;
    margin-bottom: 1em;
}

.tag {
    font-size: .8em;
    background-color: tan;
    cursor: pointer;
    border-radius: 25px;
    padding: .5em;
    transition: .2s;
    text-align: center;
}

.tag:hover {
    transform: scale(1.1);
}

.not-tag {
    background-color: #F8EEE4;
}


#title {
    margin-left: .5em;
    width: 90%;
    border-radius: 20px;
}

#tag-input {
    margin-left: .5em;
    width: 30%;
    border-radius: 20px;
}

#post-text {
    margin-left: .5em;
    width: 95%;
    border-radius: 10px;
}

#url {
    margin-left: .5em;
    width: 90%;
    border-radius: 20px;
}

label {
    margin-left: .5em;    
}

.create-btn {
    margin-top: 1em;
    margin-left: 0;
    width: 8em;
    margin-left: .5em;
}

.error {
    color: lightcoral;
    font-size: .8em;
    margin-left: 2.3%;
    margin-top: .3em;
}


</style>