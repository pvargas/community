<template>
<div class="w_tagsidebar">
    <h4>Your tags</h4>
    <b-input class="tag-input mb-2" v-model="tagNameInput" v-on:keyup.native.enter="addTag"></b-input>
    <div class="tags-list">
        <span class="badge badge-info tag mr-2"  v-for="tag in tagsList" :key="tag.name">
            <div v-on:click="removeTag(tag)">{{tag}}</div>
        </span>
    </div>
</div>
</template>

<script>
export default {
    data() {
        return {
            tagsList: [],
            tagNameInput: ''
        }
    },
    methods: {
        addTag: function() {
            if(this.tagsList.indexOf(this.tagNameInput) <= -1) {
                this.tagsList.push(this.tagNameInput.toLowerCase())
                this.tagNameInput = ''
            }
        },
        removeTag: function(tag) {
            var index = this.tagsList.indexOf(tag)
            if(index != -1) {
                this.tagsList.splice(index, 1)
            }
        }
    }
}
</script>

<style scoped>

.tags-list {
    display: flex;
    flex-direction: row;
    flex-wrap: wrap;
}

.tag {
    cursor: pointer;

}

.tag:hover {
    transform: scale(1.1);
}

.tag-input {
    border-radius: 5px;
    
}

</style>