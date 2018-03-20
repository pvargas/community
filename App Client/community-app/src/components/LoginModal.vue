<template>
<!--Login Modal Stuff-->
<b-modal id="login-modal" title="Log in">
    
        <b-form>
            <b-form-group>
                <b-row>
                    <b-col sm="2" xs="2">
                        <label for="uname">Username:</label>
                    </b-col>
                        
                    <b-col sm="10" xs="10">
                        <b-input-group>
                            <b-input-group-prepend is-text><span><i class="fas fa-user"></i></span></b-input-group-prepend>
                            <b-form-input :id="uname" type="text"></b-form-input>
                        </b-input-group>
                    </b-col>
                </b-row>
                <b-row>
                    <b-col sm="2" xs="2">
                        <label for="pass">Password:</label>
                    </b-col>
                        
                    <b-col sm="10" xs="10">
                        <b-input-group>
                            <b-input-group-prepend is-text><span><i class="fas fa-key"></i></span></b-input-group-prepend>
                            <b-form-input :id="pass" type="text"></b-form-input>
                        </b-input-group>
                    </b-col>
                </b-row>

                <input type="submit" class="btn btn-primary btn-block" name="login" value="Login">
            </b-form-group>
            
        </b-form>


    
    <div>
        <p>Don't have an account? Register
        <a href="#">here</a>
        </p>
    </div>
</b-modal>

</template>

<script>
export default {
    name: 'loginmodal',
    data() {
        return {
            uname: '',
            pass: ''
        }
    }
}
</script>

<style scoped>

</style>