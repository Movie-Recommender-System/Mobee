<template>
  <div v-if="movie.credits">
    <img class="window-header" :src="movie.poster_path" alt="poster img">
    <h3 class='text-wrap'>{{ movie.title }}</h3>
    <h4>
      <button v-if="isLoggedIn" @click='wishMovie(movie.pk)'>
        <p>{{ movie.is_wished }}</p>
        <i v-if="movie.is_wished" class="fa-solid fa-heart"></i>
        <i v-else class="fa-regular fa-heart"></i>
      </button>
      <i v-else class="fa-solid fa-heart"></i>
      {{ movie.wished_count }}
    </h4>
    <p>
      <i v-if="movie.score_avg > 0.5" class="fa-solid fa-star"></i>
      <i v-if="movie.score_avg > 1.5" class="fa-solid fa-star"></i>
      <i v-if="movie.score_avg > 2.5" class="fa-solid fa-star"></i>
      <i v-if="movie.score_avg > 3.5" class="fa-solid fa-star"></i>
      <i v-if="movie.score_avg > 4.5" class="fa-solid fa-star"></i>
      <span v-if="movie.score_avg">{{ movie.score_avg }}</span>
      <span v-else class="text-muted">데이터가 없습니다.</span>
    </p>
    <p>내용 : {{ movie.overview }}</p>
    <p>출시일 : {{ movie.release_date }}</p>

    <div class="row row-cols-1 row-cols-md-4 g-6">
      <div class="col" v-for="director in directors" :key="director.name">
        <div class="card h-100">
          <img :src="director.profile_path" class="card-img-top" alt="director profile img">
          <div class="card-body">
            {{ director.name }}
          </div>
          <div class="card-footer">
            <small class="text-muted">director</small>
          </div>
        </div>
      </div>
      <div class="col" v-for="actor in actors" :key="actor.name">
        <div class="card h-100">
          <img :src="actor.profile_path" class="card-img-top" alt="actor profile img">
          <div class="card-body">
            {{ actor.name }}
          </div>
          <div class="card-footer">
            <small class="text-muted">{{ actor.character }}</small>
          </div>
        </div>
      </div>
    </div>

    <p>장르 : 
      <ul v-for="genre in movie.genres" :key="genre.pk">
        <li>
          <p>{{ genre.name }}</p>
        </li>
      </ul>
    </p>

    <p>리뷰 수 : {{ movie.reviews_count }}</p>
    <ReviewList :reviews="movie.reviews"/>
    <ReviewCreateForm :moviePk="movie.pk" />
  </div>
      
</template>

<script>
  import { mapGetters, mapActions } from 'vuex'
  import ReviewList from './ReviewList.vue'
  import ReviewCreateForm from './ReviewCreateForm.vue'

  export default {
    name: 'MovieDetail',
    components: { ReviewList, ReviewCreateForm },
    computed: {
      ...mapGetters(['movie', 'isLoggedIn']),
      actors() {
        return this.movie.credits.actors
      },
      directors() {
        return this.movie.credits.directors
      }
    },
    methods: {
      ...mapActions(['wishMovie'])
    }
    
  }
</script>

<style>
  
</style>