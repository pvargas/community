<template>
    <div class="w_comment" >
        <b-row v-if="depth>0" :style="indent" class="custom mb-2">
            <b-col xs="12" sm="12">
                <div class="media mb-2" style="margin-left: -3em;">
                    <img class="mr-3 rounded-circle" v-bind:src="'https://api.adorable.io/avatars/50/' + authorId" alt="">
                    <div class="media-body">
                        <p style="margin-bottom: -.1em;">{{content}}</p> 
                        <span class="user-text mr-2">user{{authorId}}</span><span class="user-text">posted on {{createdAt}}</span>
                    </div>
                </div>
            </b-col>

        </b-row>

        <comment 
        v-for="child in children"
        :children="child.children" 
        :id="child.model.id"
        :authorId="child.model.author_id"
        :createdAt="child.model.created_at"
        :content="child.model.content"
        :depth="depth + 1"
        :key="child.model.id"
        >
        </comment>
    </div>
</template>

<script>
export default {
    name: 'comment',
    props: ['id', 'children', 'content', 'authorId', 'createdAt', 'depth'],
    computed: {
        indent() {
            return {
                transform: `translate(${this.depth * 50}px)` 
            }
        }
    }
}
</script>

<style scoped>

.custom {
    font-size: .9em;
    color: grey;
}

.user-text {
    color: darkgrey;
}
</style>