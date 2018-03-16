<template>
<div class="w_posts">
<h1 class="section">TRENDING</h1>
<b-row>
    <b-col md="6" sm="12">
      <div class="card-custom title">
          <div class="card-img-area">
          </div>
          <div class="card-content-area">
            <h3>
                <a href="#">Going Back to Reddit</a>
            </h3>
            <div class="text-muted">
            Posted Nov 11 by <a href="#">Mario</a>
            </div>
            <p class="card-text mb-auto">This is a wider card with supporting text below as a natural lead-in to additional content.</p>
            <strong class="text-danger mr-2">-9 votes</strong>
            <span class="badge badge-info">Tags</span>
          </div>
      </div>
    </b-col>
    <b-col md="6" sm="12">
      <div class="card-custom">
          <div class="card-img-area" style="background-image:url(https://mdbootstrap.com/img/Photos/Horizontal/Nature/4-col/img%20%282%29.jpg)">
          </div>
          <div class="card-content-area">
            <h3>
              <a href="#">Going Back to Reddit</a>
            </h3>
            <div class="text-muted">
              Posted Nov 11 by <a href="#">Mario</a>
            </div>
            <p class="card-text mb-auto">This is a wider card with supporting text below as a natural lead-in to additional content.</p>
            <strong class="text-danger mr-2">-9 votes</strong>
            <span class="badge badge-info">Tags</span>
          </div>
      </div>
    </b-col>
</b-row>
<b-row>
    <b-col md="6" sm="12">
      <div class="card-custom">
          <div class="card-img-area" style="background-image:url(https://mdbootstrap.com/img/Photos/Horizontal/Nature/4-col/img%20%282%29.jpg)">
          </div>
          <div class="card-content-area">
            <h3>
              <a href="#">Going Back to Reddit</a>
            </h3>
            <div class="text-muted">
              Posted Nov 11 by <a href="#">Mario</a>
            </div>
            <p class="card-text mb-auto">This is a wider card with supporting text below as a natural lead-in to additional content.</p>
            <strong class="text-danger mr-2">-9 votes</strong>
            <span class="badge badge-info">Tags</span>
          </div>
      </div>
    </b-col>
    <b-col md="6" sm="12">
      <div class="card-custom">
          <div class="card-img-area" style="background-image:url(https://mdbootstrap.com/img/Photos/Horizontal/Nature/4-col/img%20%282%29.jpg)">
          </div>
          <div class="card-content-area">
            <h3>
              <a href="#">Going Back to Reddit</a>
            </h3>
            <div class="text-muted">
              Posted Nov 11 by <a href="#">Mario</a>
            </div>
            <p class="card-text mb-auto">This is a wider card with supporting text below as a natural lead-in to additional content.</p>
            <strong class="text-danger mr-2">-9 votes</strong>
            <span class="badge badge-info">Tags</span>
          </div>
      </div>
    </b-col>
</b-row>

<hr>

<!--row-->
<b-row v-for="post in allPosts" v-bind:key="post.id" class="post-row">
    <b-col cols="3" class="my-auto">
        <a href="#">
            <img class="img rounded mt-center" src="http://placehold.it/156x94" alt="">
        </a>
    </b-col>
    <b-col cols="9" class="my-auto">
        <h4>{{post.title}}</h4>
        <p class="tag">Tags: 
            <span class="badge badge-pill badge-primary">sports</span>
            <span class="badge badge-pill badge-default">football</span>
            <span class="badge badge-pill badge-default">nfl</span>
            <span class="ml-1">Posted on: <span class="badge badge-success">2/5/18</span></span>
        </p>
        <a class="btn btn-default" href="#">View comments<span class="badge badge-info ml-2">231</span></a>
    </b-col>
</b-row>
<!--row-->

</div>
</template>

<script>
export default {
  name: 'App',

  data() {
      return {
          allPosts: []
      }
  },
  created: function() {
      //actual endpoint http://community.io/api/v1/posts  
      this.$http.get('https://jsonplaceholder.typicode.com/posts')
        .then(function(response){
            if(response.status == "200"){
                let list = response.data
                for (var i = 0; i < list.length; i++){
                    var item = list[i]
                    this.allPosts.push({
                        author: item.userId,//author: item.author, 
                        content: item.body,//content: item.content,
                        title: item.title,
                        id: item.id
                        //created_at: item.created_at,
                        //is_url: item.is_url,
                        //last_modified: item.last_modified
                        
                    })
                }
            }
        })
  }
}
</script>

<style>
/*@media screen and (min-width: 768px){
  .card-custom {
      flex-direction: row;
      flex-wrap: nowrap;
  }

  .card-img-area {
      height: 0px;
      width: 0px;
  }
}*/

.card-custom {
  width: 100%;
  height: auto;
  min-height: 10rem;
  display: flex;
  flex-direction: column;
  flex-wrap: wrap;
  margin-bottom: 1rem;
  border: 1px solid #dddddd;
}

/*.card-img-area {
  width: 100%;
  height: auto;
  background-size: cover;
  background-position: 50% 50%;
}*/

.card-content-area {
    padding: 1rem;
}

h3 a {
  font-family: 'Merriweather', serif;
  font-size: 0.9em;  
  text-decoration: none;
  color: black;
}

h3 a:hover {
  color: black;
  text-decoration-color: #dfdfdf !important;
}

h3 a:visited {
  text-decoration: none;
  color: black;
}

.section {
  font-size: 0.9em;  
  color: #4d4d4d;
  border-top: 0.1em solid #dddddd;  
  margin-bottom: 1em;
}

</style>