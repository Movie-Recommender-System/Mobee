<template>
  <div class="container">
    <h1 class="text-center my-5">{{ moviesKind }}</h1>
    <div class="row">
      <div id="buttons" class="btn-group my-5" role="group" aria-label="Button group with nested dropdown">

        <button  type="button" class="btn btn-primary" @click='fetchMovies("recent")'>최신 영화</button>
        <button type="button" class="btn btn-primary" @click='fetchMovies("wish")'>꿀단지에 가장 많이 담긴 영화</button>
        <button type="button" class="btn btn-primary" data-bs-toggle="tooltip" data-bs-placement="bottom" title="회원님이 남기신 리뷰와 꿀단지에 넣은 영화 정보를 혼합하여
        맟춤 추천 영화를 알려드려요!" @click='fetchRecommendMovies' v-if="isLoggedIn" >꿀단지 알고리즘 추천영화</button>
        
        <div class="button btn-group" role="group">
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
    </div>
    <ul>
      <br>
      <br>
      <div v-if="!isMovies">
        <div v-if="moviesKind=='recommend'">
          <h3>사용자 데이터가 부족합니다.</h3>
        </div>
        <div v-else>
          <h3>관련 장르의 영화가 존재하지 않습니다.</h3>
        </div>
      </div>
      <div v-else class="row row-cols-1 align-content-center">
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

<style scoped>


</style>