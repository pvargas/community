<template>
<div class="w_sidebar">
    <hUserSidebar></hUserSidebar>
    <b-btn block class="mb-4" :to="'/makepost'">Submit a post</b-btn>
    <TagsSidebar></TagsSidebar>
    
</div>
</template>
<script>
import hUserSidebar from './hUserPageSidebar.vue'
import TagsSidebar from './TagsSidebar.vue'
export default {
    components: {
        hUserSidebar,
        TagsSidebar
    }
}
</script>

<style scoped>
</style>