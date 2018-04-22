<template>
<div class="w_content">
<h1 class="section"></h1>
<b-row>
    <b-col sm="1" xs="12">
        <div class="score mt-4">
            <b-button v-on:click="toggleDown = false" :pressed.sync="toggleUp" class="vote-btn" variant="outline-success"><i class="fas fa-angle-up"></i></b-button>
            <span>44.5k</span>
            <b-button v-on:click="toggleUp = false" :pressed.sync="toggleDown" class="vote-btn" variant="outline-success"><i class="fas fa-angle-down"></i></b-button>
        </div>
        <hr>
    
    </b-col>
    <b-col sm="11" xs="12">
        <b-row>
            <b-col sm="12">
                <span><h1 class="post-title">Post Title</h1> by <a href="#">Author</a></span>
        
            <b-img fluid class="rounded-circle mx-2" src="http://placehold.it/50x50"/>
            </b-col>
        </b-row>
        
        
        <p class="badge badge-info">Tags</p>

        <p class="text-muted">Posted on 11/11/11</p>

        <hr>

        <b-img fluid class="rounded" src="http://placehold.it/900x300"/>

        <hr>

        <p class="lead">Lorem ipsum dolor sit amet, consectetur adipisicing elit. 
            Ut, tenetur natus doloremque laborum quos iste ipsum rerum obcaecati
             impedit odit illo dolorum ab tempora nihil dicta earum fugiat. 
             Temporibus, voluptatibus.
        </p>

        <p>Lorem ipsum dolor sit amet, consectetur adipisicing elit. 
            Ut, tenetur natus doloremque laborum quos iste ipsum rerum obcaecati
             impedit odit illo dolorum ab tempora nihil dicta earum fugiat. 
             Temporibus, voluptatibus.
        </p>

        <blockquote class="blockquote mb-0">
            <p>
                Lorem ipsum dolor sit amet,
                consectetur adipiscing elit.
                Integer posuere erat a ante.
            </p>
            <footer class="blockquote-footer">
                Someone famous in <cite title="Source Title">Source Title</cite>
            </footer>
        </blockquote>

        <p>
            Lorem ipsum dolor sit amet, consectetur adipisicing elit.
            Error, nostrum, aliquid, animi, ut quas placeat totam sunt tempora
            commodi nihil ullam alias modi dicta saepe minima ab quo voluptatem obcaecati?
        </p>

        <p>
            Lorem ipsum dolor sit amet, consectetur adipisicing elit. Harum, dolor quis.
            Sunt, ut, explicabo, aliquam tenetur ratione tempore quidem voluptates cupiditate
            voluptas illo saepe quaerat numquam recusandae? Qui, necessitatibus, est!
        </p>
        <!--End of Post-->
        <hr>

        <div class="card my-4">
            <h5 class="card-header">Leave a Comment:</h5>
            <div class="card-body">
              <form>
                <div class="form-group">
                  <textarea class="form-control" rows="3"></textarea>
                </div>
                <button type="submit" class="btn btn-primary">Submit</button>
              </form>
            </div>
          </div>

        <!-- Single Comment -->
        <div class="media mb-4">
            <img class="d-flex mr-3 rounded-circle" src="http://placehold.it/50x50" alt="">
            <div class="media-body">
                <h5 class="mt-0">Commenter Name</h5>
                Cras sit amet nibh libero, in gravida nulla. Nulla vel metus scelerisque ante sollicitudin. Cras purus odio, vestibulum in vulputate at, tempus viverra turpis. Fusce condimentum nunc ac nisi vulputate fringilla. Donec lacinia congue felis in faucibus.
            </div>
        </div>

        <!-- Comment with nested comments -->
        <div class="media mb-4">
            <img class="d-flex mr-3 rounded-circle" src="http://placehold.it/50x50" alt="">
            <div class="media-body">
                <h5 class="mt-0">Commenter Name</h5>
                Cras sit amet nibh libero, in gravida nulla. Nulla vel metus scelerisque ante sollicitudin. Cras purus odio, vestibulum in vulputate at, tempus viverra turpis. Fusce condimentum nunc ac nisi vulputate fringilla. Donec lacinia congue felis in faucibus.

                <div class="media mt-4">
                    <img class="d-flex mr-3 rounded-circle" src="http://placehold.it/50x50" alt="">
                    <div class="media-body">
                        <h5 class="mt-0">Commenter Name</h5>
                        Cras sit amet nibh libero, in gravida nulla. Nulla vel metus scelerisque ante sollicitudin. Cras purus odio, vestibulum in vulputate at, tempus viverra turpis. Fusce condimentum nunc ac nisi vulputate fringilla. Donec lacinia congue felis in faucibus.
                    </div>
                </div>

                <div class="media mt-4">
                    <img class="d-flex mr-3 rounded-circle" src="http://placehold.it/50x50" alt="">
                    <div class="media-body">
                        <h5 class="mt-0">Commenter Name</h5>
                        Cras sit amet nibh libero, in gravida nulla. Nulla vel metus scelerisque ante sollicitudin. Cras purus odio, vestibulum in vulputate at, tempus viverra turpis. Fusce condimentum nunc ac nisi vulputate fringilla. Donec lacinia congue felis in faucibus.
                    </div>
                </div>
            </div>
        </div>
        </b-col>
        
</b-row>
</div>
</template>

<script>
export default {
    name: 'postcontent',
    data() {
        return {
            post: {
                author: '',
                content: '',
                title: '',
                id: ''
            },
            comments: [],
            toggleUp: false,
            toggleDown: false
        }
    },
    created: function() {
        var theURL = 'https://jsonplaceholder.typicode.com/posts/' + this.$route.params.postid
        this.$http.get(theURL)
            .then(function(response){
                if(response.status == "200"){
                    let thePost = response.data
                    this.post.author = thePost.userId//author: item.author, 
                    this.post.content = thePost.body,//content: item.content,
                    this.post.title = thePost.title,
                    this.post.id = thePost.id
                    //created_at: item.created_at,
                    //is_url: item.is_url,
                    //last_modified: item.last_modified
                
                }
            })

        theURL += '/comments'
        this.$http.get(theURL)
            .then(function(response){
                if(response.status == '200'){
                    let theComments = response.data
                    for(var i = 0; i < theComments.length; i++){
                        var temp = theComments[i]
                        this.comments.push({
                            id: temp.id,
                            author: temp.email,
                            content: temp.body 
                        })
                    }
                }
                
            })
    }
}
</script>

<style scoped>
.score {
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
}

.vote-btn {
    width: 2.5rem;
    height: 2.2rem;
    border: 0px;
}

.post-title {
  font-family: 'Merriweather', serif;
  font-size: 2.2em;  
  text-decoration: none;
  color: black;
}

.btn:focus {
    outline: none;
    box-shadow: none;
}

.section {
  font-size: 0.9em;  
  color: #4d4d4d;
  border-top: 0.1em solid #dddddd;  
  margin-bottom: 1em;
}

</style>