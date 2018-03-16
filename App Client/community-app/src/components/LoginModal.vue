<template>
<!--Login Modal Stuff-->
<div class="modal fade" id="login-modal">
  <div class="modal-dialog">
    <div class="modal-content">

    <!-- Modal Header -->
    <div class="modal-header ">
        <h4 class="modal-title">Log in</h4>
        <button type="button" class="close" data-dismiss="modal">&times;</button>
    </div>

    <!-- Modal body -->
    <div class="modal-body">
        <form>
        <div class="form-group row">
            <div class="col-2">
            <label for="uname-input" class="col-form-label">Username:</label>
            </div>
            <div class="col-10 input-group">
            <span class="input-group-addon">
                <i class="fas fa-user"></i>
            </span>
            <input name="user" class="form-control" type="text" id="uname-input">
            </div>
        </div>
        <div class="form-group row">
            <div class="col-2">
            <label for="pw-input" class="col-form-label">Password:</label>
            </div>
            <div class="col-10 input-group">
            <span class="input-group-addon">
                <i class="fas fa-key"></i>
            </span>
            <input name="pass" class="form-control" type="password" id="pw-input">
            </div>
        </div>
        <input type="submit" class="btn btn-primary btn-block" name="login" value="Login">
        </form>
    </div>

    <!-- Modal footer -->
    <div class="modal-footer">
        <p>Don't have an account? Register
        <a href="#">here</a>
        </p>
    </div>

    </div>
  </div>
</div>
</template>

<script>
export default {
    name: 'loginmodal'
}
</script>

<style scoped>

</style>