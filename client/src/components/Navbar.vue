<template>
<div class="w_navbar">
    <div class="c-navbar">
        <div class="c-navbar-placeholder"></div>
        <router-link class="c-navbar-brand" v-bind:to="'/posts'">Community</router-link>
        <div class="my-auto c-nav" v-if="!$ls.get('Token')">
            <div class="c-nav-item" v-b-modal="'login-modal'"><div>Login</div></div>  
            <LoginModal></LoginModal>
        </div>
        <LoggedIn v-if="$ls.get('Token')"></LoggedIn>
    </div>
    
    <div class="navbar navs-box">
        <div class="tags-box">
            <div v-for="tag in tagsList" @click="toggleTag(tag)" :key="tag.name" 
            :class="{'tag mr-4 mt-1': tag.selected, 'tag not-tag mr-4 mt-1': !tag.selected}">{{tag.name}}</div>
        </div>
    </div>
    <h1 class="section"></h1>
</div>
</template>

<script>
import LoginModal from './LoginModal.vue'
import LoggedIn from './LoggedIn.vue'
import {EventBus} from '../Events.js'

export default {
    name: 'navigator',
    data() {
        return {
            tagsList: [{name: 'Technology', selected: true},
                    {name: 'Science', selected: true},
                    {name: 'Politics', selected: true},
                    {name: 'Business', selected: true},
                    {name: 'Media', selected: true},
                    {name: 'Culture', selected: true},
                    {name: 'News', selected: true}, 
                    {name: 'Art', selected: true}, 
                    {name: 'Other', selected: true}],
            tagNameInput: ''
        }
    },
    components: {
        LoginModal,
        LoggedIn
    },
    created() {
        let self = this
        self.initialTags()
        if(!self.$ls.get('Tags')) {
            self.saveTagsToLS()
        }
    },
    methods: {
        initialTags() {
            let self = this
            if(self.$ls.get('Tags') != null) {
                self.pullTagsFromLS()
            } 
        },
        saveTagsToLS() {
            this.$ls.set('Tags', JSON.stringify(this.tagsList))
        },
        pullTagsFromLS() {
            let self = this
            self.tagsList = JSON.parse(self.$ls.get('Tags'))
        },
        hasTag() {
            let self = this
            for(var i = 0; i < self.tagsList.length; i++) {
                if(self.tagsList[i].name == self.tagNameInput) {
                    return true
                }
            }
            return false
        },
        hasTagName(tagName) {
            let self = this
            for(let i = 0; i < self.tagsList.length; i++) {
                if(self.tagsList[i].name == tagName) {
                    return true
                }
            }
            return false
        },
        toggleTag(tag){

            if(tag.selected == true) {
                tag.selected = false
            } else {
                tag.selected = true
            }
            this.saveTagsToLS()
            EventBus.$emit('tagfilter', tag)
        }
    }
}
</script>

<style>
.c-navbar {
    display: flex;
    flex-direction: row;
    justify-content: space-between;
    height: 4em;
    background-color:#F2E5D2;
    width: 100%;
}

.c-navbar-brand {
    font-family: 'Abril Fatface', cursive;  
    font-size: 2.2em !important;  
    color:#425268 !important;
}

.c-navbar-brand:hover {
    text-decoration: none;
}

.c-navbar-placeholder {
    width: 124.18px;
}

.c-nav {
    display: flex;
    flex-direction: row;
    margin-right: 1em;
}

.c-nav-item {
    margin-right: 1em;
    cursor: pointer;
    margin-left: 68.74px;
}

.c-nav-item div {
    color: #8892a1;
}
.c-nav-item div:hover {
    color: #192c47
}

.section {
    font-size: 0.9em;  
    color: #4d4d4d;
    border-top: 0.1em solid #dddddd;  
    margin-bottom: 1em;
}

/*navbar 2 stuff*/
.navs-box {
    background-color: #F8EEE4;
    width: 100%;
    text-align: center;
}

.tags-box {
    margin: auto;
}

.tag {
    display: inline-block;
    font-size: .8em;
    background-color: tan;
    cursor: pointer;
    border-radius: 25px;
    padding: .5em;
    transition: .2s;
    text-align: center;
    margin-right: -20px;
}

.not-tag {
    background-color: #F8EEE4;
}

.tag:hover {
    transform: scale(1.1);
    backface-visibility: hidden;
    -webkit-backface-visibility: hidden;
    -moz-backface-visibility: hidden;
    -ms-backface-visibility: hidden;
}

.tag-input {
    width: 7em;
    height: 2em;
    font-size: .8em;
}

@media screen and (max-width: 576px) {
    .c-navbar-brand {
        margin-right: auto;
        margin-left: 10px;
        margin-right: 0px;
    }

    .c-navbar-placeholder {
        width: 0px;
    }

    .c-navbar-explore {
        width: 0px;
        display: none;
    }

    .tag-input {
        width: 100%;
    }

    .c-nav-item {
        margin-left: 0px;
    }
    

}
</style>