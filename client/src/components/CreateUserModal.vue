<template>
<div class="w_createuser">
    
    <label for="uname">Username:</label>
    <b-input v-model.trim="user.name" class="input" id="uname"></b-input>
    <p class="error" v-if="!$v.user.name.required">* Required</p>
    <p class="error" v-if="!$v.user.name.alphaNum">Only letters and numbers allowed</p>

    <label for="email">Email</label>
    <b-input v-model.trim="user.email" class="input" id="email"></b-input>
    <p class="error" v-if="!$v.user.email.required">* Required</p>
    <p class="error" v-if="!$v.user.email.email">Enter a valid email</p>

    <label for="pass">Password</label>
    <b-input class="input" 
             type="password" 
             id="pass1"
             v-model.trim="user.password"
             @input="$v.user.password.$touch()">
    </b-input>
    <p class="error" v-if="!$v.user.password.required">* Required</p>

    <label for="pass2">Verify password</label>
    <b-input class="input" 
             type="password" 
             id="pass2"
             v-model.trim="user.repeatPassword"
             @input="$v.user.repeatPassword.$touch()">
    </b-input>
    <p class="error" v-if="!$v.user.repeatPassword.sameAsPassword">
        Passwords must match
    </p>

    <b-btn @click="register" slot="modal-footer" class="mt-4">Register</b-btn>
</div>
</template>

<script>
import {required, sameAs, alphaNum, email} from 'vuelidate/lib/validators'

export default {
    name: 'createuser',
    data() {
        return {
            user: {
                name: '',
                email: '',
                password: '',
                repeatPassword: ''
            },
        }
    },
    validations: {
        user: {
            name: {
                required,
                alphaNum
            },
            email: {
                required,
                email
            },
            password: {
                required
            },
            repeatPassword: {
                sameAsPassword: sameAs('password')
            }
        }
    },
    methods: {
        register() {
            let self = this
            if(self.$v.user.$invalid == false){
                self.$axios.post('/users', self.user)
                .then(function(response) {
                    if(response.status == "200") {
                        self.$emit('closemodal', self.user.name, self.user.password)
                    } else {
                        window.alert(response.status)
                        
                    }
                    console.log(response)
                })
                .catch(function(e) {
                    window.alert(e.response.data.message)
                })
                
            } else {
                window.alert('Missing or incorrect fields')
            }
        }
    }
}
</script>

<style scoped>
.input {
    box-shadow: none;
    outline: 0px !important;
    -webkit-appearance:none;
}

.error {
    color: lightcoral;
    font-size: .8em;
}
</style>