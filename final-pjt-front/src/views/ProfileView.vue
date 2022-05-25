<template>
  <div class="container">
    <h2 class="text-center my-5">{{ profile.username }}'s Profile</h2>
    <div class="row my-5">

      <div class="col-4 box">
        <h4>남긴 리뷰</h4>
        <ul class="list-group">
          <li class="list-group-item" v-for="review in profile.reviews" :key="review.pk">
            <h5>영화 제목 : {{ review.movie.title }}</h5>
            <p>리뷰 : {{ review.content }}</p>
            <div>
              <span v-if="review.score > 0.5" class="material-symbols-outlined text-warning">hexagon</span>
              <span v-if="review.score > 1.5" class="material-symbols-outlined text-warning">hexagon</span>
              <span v-if="review.score > 2.5" class="material-symbols-outlined text-warning">hexagon</span>
              <span v-if="review.score > 3.5" class="material-symbols-outlined text-warning">hexagon</span>
              <span v-if="review.score > 4.5" class="material-symbols-outlined text-warning">hexagon</span>
            </div>
            <p><i class="fa-solid fa-heart"></i> {{ review.like_count }}</p>
          </li>
        </ul>
      </div>
      
      <div class="col-8 box">
        <h4>Wish List</h4>
        <div class="row row-cols-1 row-cols-md-3 g-4">
          <div class="col" v-for="movie in profile.wish_movie_list" :key="movie.pk">
            <div class="card h-100">
              <img :src="`https://image.tmdb.org/t/p/w500/${movie.poster_key}`" 
              class="card-img-top img-thumbnail rounded" alt="poster img">
              <div class="card-body">
                <h5 class="card-title">{{ movie.title }}</h5>
              </div>
            </div>
          </div> 
        </div>
      </div>

    <div class="row">
      <div class="col-6">
        <h4>작성한 게시글 모음</h4>
        <div class="box list-group">
          <li class="list-group-item" v-for="article in profile.articles" :key="article.pk">
            <h5> {{ article.title }}</h5>
            <p>{{ article.content }}</p>
            <p><i class="fa-solid fa-heart"></i> {{ article.like_count }}</p>
          </li>
        </div>
      </div>
      <div class="col-6">
        <h4>작성한 댓글 모음</h4>
        <div>
          <ul class=" box list-group">
          <li class="list-group-item" v-for="comment in profile.comments" :key="comment.pk">
            <h5> {{ comment.article.title }}</h5>
            <p> {{ comment.content }}</p>
          </li>
        </ul>
        </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import { mapActions, mapGetters } from 'vuex'
  export default {
    name: 'ProfileView',
    computed: {
      ...mapGetters(['profile', 'currentUser']),
    },
    methods: {
      ...mapActions(['fetchProfile'])
    },
    created () {

      setTimeout(() => this.fetchProfile({ username : this.currentUser.username }), 100)
    }
  }
</script>

<style scoped>
  .box {
    height: 600px;
    overflow: auto;
  }
</style>