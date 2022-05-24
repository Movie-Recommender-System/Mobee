<template>
  <div>
    <div class="btn-group" role="group" aria-label="Button group with nested dropdown">
      <button type="button" class="btn btn-primary" @click='fetchMovies("recent")'>최신 영화</button>
      <button type="button" class="btn btn-primary" 
      @click='fetchMovies("wish")'>유저들이 가장 많이 찜한 영화</button>
      <button type="button" class="btn btn-primary" 
      v-if="isLoggedIn" @click='fetchRecommendMovies'>사용자 맞춤 추천 영화</button>
      <div class="btn-group" role="group">
        <button id="btnGroupDrop1" type="button" class="btn btn-primary dropdown-toggle"
         data-bs-toggle="dropdown" aria-expanded="false">장르별 추천 영화
        </button>
        <ul class="dropdown-menu" aria-labelledby="btnGroupDrop1">
          <li v-for="genre in genres" :key="genre.pk" @click='fetchMovies(genre.name)'>
            <a class="dropdown-item" href="#">{{ genre.name }}</a>
          </li>
        </ul>
      </div>
    </div>
    <ul>
      <div>
        <h1> {{moviesKind}}</h1>
      </div>
      <div v-if="!isMovies">
        <h3>사용자 데이터가 부족합니다.</h3>
      </div>
      <div v-else class="row row-cols-1 row-cols-md-3 g-4">
        <MovieListItem v-for="movie in movies" :key="movie.pk" :movie="movie"/>
      </div>
    </ul>
  </div>
</template>

<script>
  import MovieListItem from '@/components/MovieListItem.vue'
  import { mapActions, mapGetters } from 'vuex'


  export default {
    name: 'MovieListView',
    components: { MovieListItem },
    computed: {
      ...mapGetters(['movies', 'isLoggedIn', 'isMovies', 'genres', 'moviesKind'])
    },
    methods: {
      ...mapActions(['fetchMovies', 'fetchRecommendMovies'])
    },
    created() {
      this.fetchMovies('recent')
    }
  }
</script>

<style>
  
</style>