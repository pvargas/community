<template>
<!--Login Modal Stuff-->
<b-modal @hidden="createUser = false" hide-footer ref="loginModalRef" id="login-modal" centered>
<div v-show="!createUser" slot="modal-title">Log in</div>
<div v-show="createUser" slot="modal-title">Create an Account</div>
<b-form v-show="!createUser">
    <b-form-group>
        <b-row class="mb-2">
            <b-col sm="2" xs="2" class="my-auto">
                <label for="uname">Username:</label>
            </b-col>
                
            <b-col sm="10" xs="10" class="my-auto">
                <b-input-group>
                    <b-input-group-prepend is-text><span><i class="fas fa-user"></i></span></b-input-group-prepend>
                    <b-form-input class="input" v-model="user" type="text"></b-form-input>
                </b-input-group>
            </b-col>
        </b-row>
        <b-row>
            <b-col sm="2" xs="2" class="my-auto">
                <label for="pass">Password:</label>
            </b-col>
                
            <b-col sm="10" xs="10" class="my-auto">
                <b-input-group>
                    <b-input-group-prepend is-text><span><i class="fas fa-key"></i></span></b-input-group-prepend>
                    <b-form-input class="input" v-model="pass" type="password"></b-form-input>
                </b-input-group>
            </b-col>
        </b-row>
    </b-form-group>
    <div>
        <p>Don't have an account? Register
            <span class="text-btn" @click="createUser = true">here</span>
        </p>
    </div>
    <b-btn v-on:click="sendRequest" variant="btn-primary" class="btn btn-primary">Login</b-btn>
</b-form>


<div>
    
</div>

<CreateUserModal @closemodal="accountCreated" v-show="createUser"></CreateUserModal>

</b-modal>

</template>

<script>
import axios from 'axios' 
import CreateUserModal from './CreateUserModal.vue'
export default {
    name: 'loginmodal',
    data() {
        return {
            user: '',
            pass: '',
            err: [],
            createUser: false
        }
    },
    components: {
        CreateUserModal
    },
    methods: {
        closeModal() {
            this.$refs.loginModalRef.hide()
        },
        sendRequest() {
            let self = this
            let authString = self.user + ':' + self.pass
            authString = btoa(authString)
            self.closeModal()

            var axiosReq = axios.create({
                baseURL: 'https://www.pvargapi.win',
                headers: {'Authorization': 'Basic ' + authString}
            })
            
            
            axiosReq.get(`/account/login`)
            .then(function(response) {
                let data = response.data
                self.$ls.set('Token', data.token)
                self.$ls.set('CUser', data.name)
                location.reload()
            })
            .catch(function(e) {
                window.alert('Invalid username or password')
            })
        },
        accountCreated(user, pass){
            let self = this
            self.user = user
            self.pass = pass
            self.sendRequest()
        },
    }
}
</script>

<style scoped>
.btn {
  float: right;
}

.input:active,
.input:focus,
.input {
    box-shadow: none;
    outline: 0px !important;
    -webkit-appearance:none;
}

.text-btn {
    color: dodgerblue;
    cursor: pointer;
}

.text-btn:hover {
    color: rgb(24, 104, 185);
}

</style>