
<template>
<div class="w-usersidebar">

        <b-row class="sidebar-header">
            <b-col sm="12" xs="12">
                <div class="box1">
                    <b-img class="profile-pic" style="align-self: center;" src="http://placehold.it/80x80"></b-img>
                    <h4 style="align-self: center;">{{usr.name}}</h4>
                    <h6>{{usr.email}}</h6>
                </div>
            </b-col>
            <b-col sm="12" xs="12">
                <p class="text-muted">Posts</p>
                <p class="text-muted">Comments</p>
                <p class="text-muted">Points</p>
            </b-col>
        </b-row>

        <p class="text-muted text-member">
            Member since: {{usr.memberSince}}
        </p>
</div>
</template>

<script>
export default {
    name: 'user-sidebar',
    data() {
        return {
            usr: {
                name: '',
                email: '',
                isMod: false,
                memberSince: '',
                id: -1
            }
        }
    },
    created: function() {
        this.$http.get('http://127.0.0.1:5000/api/v1/users/user1')
            .then(function(response){
                if(response.status == "200"){
                    let temp = response.data
                    this.usr.name = temp.user.name, 
                    this.usr.email = temp.user.email,
                    this.usr.isMod = temp.user.is_moderator,
                    this.usr.memberSince = temp.user.member_since,
                    this.usr.id = temp.user.id,
                    console.log(temp)
                    
                }
            })
    }

}
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