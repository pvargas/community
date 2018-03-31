<template>
<div class="w_posts">
<h1 class="section">TRENDING</h1>
<b-row>
    <b-col md="6" sm="12">
        <div class="post-box">
            <div class="img-box" style="background-image: url(https://placehold.it/250x250);">
            </div>
            
            <div class="card-custom title">
                <div class="card-content-area">
                    <h3><a href="#">Going Back to Reddit</a></h3>
                    <div class="text-muted">
                        Posted Nov 11 by <a href="#">Mario</a>
                    </div>
                    <p class="card-text mb-auto">This is a wider card with supporting text below as a natural lead-in to additional content.</p>
                    <strong class="text-danger mr-2">-9 votes</strong>
                    <span class="badge badge-info">Tags</span>
                </div>
            </div>
        </div>
    </b-col>
    <b-col md="6" sm="12">
        <div class="post-box">
            <div class="img-box" style="background-image: url(https://placehold.it/250x250);">
            </div>
            
            <div class="card-custom title">
                <div class="card-content-area">
                    <h3><a href="#">Going Back to Reddit</a></h3>
                    <div class="text-muted">
                        Posted Nov 11 by <a href="#">Mario</a>
                    </div>
                    <p class="card-text mb-auto">This is a wider card with supporting text below as a natural lead-in to additional content.</p>
                    <strong class="text-danger mr-2">-9 votes</strong>
                    <span class="badge badge-info">Tags</span>
                </div>
            </div>
        </div>
    </b-col>
</b-row>
<b-row>
    <b-col md="6" sm="12">
        <div class="post-box">
            <div class="img-box" style="background-image: url(https://placehold.it/250x250);">
            </div>
            
            <div class="card-custom title">
                <div class="card-content-area">
                    <h3><a href="#">Going Back to Reddit</a></h3>
                    <div class="text-muted">
                        Posted Nov 11 by <a href="#">Mario</a>
                    </div>
                    <p class="card-text mb-auto">This is a wider card with supporting text below as a natural lead-in to additional content.</p>
                    <strong class="text-danger mr-2">-9 votes</strong>
                    <span class="badge badge-info">Tags</span>
                </div>
            </div>
        </div>
    </b-col>
    <b-col md="6" sm="12">
        <div class="post-box">
            <div class="img-box" style="background-image: url(https://placehold.it/250x250);">
            </div>
            
            <div class="card-custom title">
                <div class="card-content-area">
                    <h3><a href="#">Going Back to Reddit</a></h3>
                    <div class="text-muted">
                        Posted Nov 11 by <a href="#">Mario</a>
                    </div>
                    <p class="card-text mb-auto">This is a wider card with supporting text below as a natural lead-in to additional content.</p>
                    <strong class="text-danger mr-2">-9 votes</strong>
                    <span class="badge badge-info">Tags</span>
                </div>
            </div>
        </div>
    </b-col>
</b-row>

<h1 class="section">ALL POSTS</h1>
<PostsList></PostsList>

</div>
</template>

<script>
import PostsList from './PostsList.vue'
export default {
    name: 'Posts',
    components: {
        PostsList
    }
}
</script>

<style>
@media screen and (max-width: 768px){
  .card-custom {
      flex-direction: row;
      flex-wrap: nowrap;
  }

  .card-img-area {
      height: 0px;
      width: 0px;
  }
}

.post-box {
    display: flex;
    flex-direction: row;
    align-content: center;
    flex-wrap: nowrap;
    margin-bottom: 1rem;
}

.img-box {
    height: auto;
    width: 50%;
    background-size: cover;
    background-position: 50% 50%;
}

.card-custom {
    max-width: 35em;
    height: auto;
    display: flex;
    border: 1px solid #dddddd;
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