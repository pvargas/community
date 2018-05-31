<template>
<div class="w_loggedin my-auto">
    <div class="c-navbar-user">
        <b-img fluid class="userimage my-auto" 
                :src="'https://api.adorable.io/avatars/25/' + user.id"/>
        <router-link :to="'/makepost'"><button  class="btn btn1">Make a post</button></router-link>
        <b-nav-item-dropdown class="user-dropdown" right>
            <b-dropdown-header class="username">
                Signed in as: 
                <router-link :to="'/users/' + user.name">{{user.name}}</router-link>
            </b-dropdown-header>
            <b-dropdown-divider></b-dropdown-divider>
            <b-dropdown-item :to="'/makepost'">Submit a Post</b-dropdown-item>
            <b-dropdown-item @click="logout">Logout</b-dropdown-item>
        </b-nav-item-dropdown>

    </div>
</div>
</template>

<script>
export default {
    data() {
        return {
            user: {
                name: '',
                id: ''
            }
        }
    },
    created() {
        let self = this
        self.user.name = self.$ls.get('CUser')
        self.$axios.get('/users/' + self.user.name)
        .then(function(response){
            let data = response.data.user
            self.user.id = data.id
        })
    },
    methods: {
        logout() {
            let self = this
            self.$ls.remove('Token')
            self.$ls.remove('CUser')
            location.reload()
        }
    }
}
</script>

<style scoped>

.userbox {
    display: flex;
    flex-direction: row;
    justify-content: flex-end;
    height: 100%;
    width: 124.17px;
}

.usercol {
    display: flex;
    flex-direction: column;
    text-align: center;
    max-width: 4em;
}
.dropdown-item {
    font-size: .9em;
}

.username {
    overflow: hidden;
    width: 100%;
}

.userimage {
    max-height: 2.5em;
    max-width: 2.5em;
    padding-right: 0px;
    border-radius: 10px;
    margin-right: 3px;
}
li {
    list-style: none;
}
.user-dropdown {
    z-index: 1;
    position: absolute;
    right: 0;
    margin-top: 30px;
    margin-right: 3px;
}

a.nav-link {
    padding: 0px!important;
}
.c-navbar-user {
    display: flex;
    justify-content: flex-end;
    width: 124.17px;
}

.btn1 {
    position: absolute;
    right: 0;
    margin-right: 50px;
    margin-top: 5.5px;
    width: 8em;
    font-size: .8em;
    color: white;
    background-color: tan;
}

.btn1:hover {
    background-color: #AC9473;
}

@media screen and (max-width: 576px) {
    .c-navbar-user {
        width: 100%;
    }

    .btn1 {
        display: none;
    }
}

</style>