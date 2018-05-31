export default {

    login(email, pass, cb) {
        cb = arguments[arguments.length - 1]
        if (localStorage.token) {
            if(cb) 
            cb(true) 
                this.onChange(true)
            
        }
    }
}