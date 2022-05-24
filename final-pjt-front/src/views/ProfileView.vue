<template>
  <div class="container">
    <h2>{{ profile.username }}'s Profile</h2>
    <div class="d-flex my-5">
      <div class="container">
        <h4>남긴 리뷰</h4>
        <ul class="list-group">
          <li class="list-group-item" v-for="review in profile.reviews" :key="review.pk">
            <h5>영화 제목 : {{ review.movie.title }}</h5>
            <p>리뷰 : {{ review.content }}</p>
            <div>
              <span>평점: </span>
              <i v-if="review.score > 0.5" class="fa-solid fa-star"></i>
              <i v-if="review.score > 1.5" class="fa-solid fa-star"></i>
              <i v-if="review.score > 2.5" class="fa-solid fa-star"></i>
              <i v-if="review.score > 3.5" class="fa-solid fa-star"></i>
              <i v-if="review.score > 4.5" class="fa-solid fa-star"></i>
            </div>
            <p><i class="fa-solid fa-heart"></i> {{ review.like_count }}</p>
          </li>
        </ul>
      </div>
      <div class="container">
        <h4>Wish List</h4>
        <div class="row row-cols-1 row-cols-md-3 g-4">
          <div class="col" v-for="movie in profile.wish_movie_list" :key="movie.pk">
            <div class="card h-100">
              <img :src="movie.poster_path" 
              class="card-img-top img-thumbnail rounded" alt="poster img">
              <div class="card-body">
                <h5 class="card-title">{{ movie.title }}</h5>
              </div>
            </div>
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
      ...mapGetters(['profile', 'currentUser'])
    },
    methods: {
      ...mapActions(['fetchProfile'])
    },
    created () {
      setTimeout(() => this.fetchProfile({ username : this.currentUser.username }), 1000)
    }
  }
</script>

<style>
  
</style>