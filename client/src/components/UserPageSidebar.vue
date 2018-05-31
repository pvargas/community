
<template>
<div class="w-usersidebar">
        <b-row v-if="!loading" class="sidebar-header">
            <b-col sm="12" xs="12">
                <div class="box1">
                    <b-img class="profile-pic" style="align-self: center;"
                     :src="'https://api.adorable.io/avatars/50/' + user.id"></b-img>
                    <h4 style="align-self: center;">{{user.name}}</h4>
                </div>
            </b-col>
            <b-col sm="12" xs="12">
                <p class="text-muted">Posts: {{postCount}}</p>
                <p class="text-muted">Comments {{commentCount}}</p>
            </b-col>
        </b-row>

        <p class="text-muted text-member">
            Member since: {{toSimpleDate(user.createdAt)}}
        </p>
</div>
</template>

<script>
export default {
    name: 'user-sidebar',
    data() {
        return {
            user: {
                name: '',
                createdAt: '',
                id: ''
            },
            loading: true
        }
    },
    props: ['postCount', 'commentCount'],
    created: function() {
        let self = this

        self.$axios.get('/users/' + self.$route.params.userName)
            .then(function(response){
                let data = response.data.user
                self.user.createdAt = data.member_since,
                self.user.id = data.id,
                self.user.name = data.name
                self.loading = false
            })
    },
    methods: {
        toSimpleDate(date) {
            return date.substr(0, 10)
        }
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

.w-usersidebar {
    background-color: whitesmoke;
    padding: 1em;
    height: 22em;
    border-radius: 10px;
}

</style>