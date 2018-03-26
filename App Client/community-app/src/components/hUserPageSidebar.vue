
<template>
<div class="w-usersidebar">

        <b-row class="sidebar-header">
            <b-col sm="12" xs="12">
                <div class="box1">
                    <b-img class="profile-pic" style="align-self: center;" src="http://placehold.it/80x80"></b-img>
                    <h4 style="align-self: center;">fsdf</h4>
                </div>
            </b-col>
            <b-col sm="12" xs="12">
                <p class="text-muted">Posts</p>
                <p class="text-muted">Comments</p>
                <p class="text-muted">Points</p>
            </b-col>
        </b-row>

        <p class="text-muted text-member">
            Member since: 11/11/11
        </p>
</div>
</template>

<script>
</script>

<style>

.box1 {
    display: flex;
    flex-direction: column;
    align-items: flex-start;
}

.text-member {
    font-size: .8em
}

.profile-pic {
    border-radius: 5px;
}

</style>