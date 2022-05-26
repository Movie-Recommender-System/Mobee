<template>
  <div>
    
    <br>
    <br>
    <div class="container">
      <div class="d-flex">
        <div v-for="(movie,index) in movies" :key="index">
          <img v-if="index < 3" :src="`https://image.tmdb.org/t/p/w500/${movie.poster_key}`">
        </div>
      </div>
    </div>

    <h1 v-if="moviesKind == 'recent'" class="text-center m-5 p-5">최신 Movies</h1>
    <h1 v-else-if="moviesKind == 'wish'" class="text-center m-5 p-5">꿀단지에 가장 많이 담긴 Movies</h1>
    <h1 v-else-if="moviesKind == 'recommend'" class="text-center m-5 p-5">꿀단지 알고리즘 추천 Movies</h1>
    <h1 v-else class="text-center m-5 p-5">{{ moviesKind }}</h1>


    <div class="text-center container justify-contents-items">
      <div class="row justify-contents-items">
        <div class="btn-group" role="group" aria-label="Basic radio toggle button group">

        <input type="radio" class="btn-check" @click='fetchMovies("recent")' name="btnradio" id="btnradio1" autocomplete="off" checked="">
        <label class="btn btn-outline-primary" for="btnradio1">최신 영화</label>

        <input type="radio" class="btn-check"  @click='fetchMovies("wish")' name="btnradio" id="btnradio2" autocomplete="off" checked="">
        <label class="btn btn-outline-primary" for="btnradio2">꿀단지에 가장 많이 담긴 영화</label>
        
        <input type="radio" class="btn-check" name="btnradio" id="btnradio3" autocomplete="off" checked="" data-bs-toggle="tooltip" data-bs-placement="bottom" title="회원님이 남기신 리뷰와 꿀단지에 넣은 영화 정보를 혼합하여
        맟춤 추천 영화를 알려드려요!" @click='fetchRecommendMovies' v-if="isLoggedIn">
        <label class="btn btn-outline-primary" for="btnradio3">꿀단지 알고리즘 추천 영화</label>
         
        <div class="button btn-group" role="group">
          <button id="btnGroupDrop1" type="button" class="btn btn-outline-primary dropdown-toggle"
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
      
    </div>

    <div>
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
        <div v-else>
          <div class="row row-cols-1 align-content-center justify-content-center">
            <div v-for="movie in movies" :key="movie.pk">
              <MovieListItem v-if="movie.title.replace(/ /gi, '').includes(query)"  :movie="movie"/>
            </div>
          </div>
        </div>
      </ul>
    </div>
  </div>
</template>

<script>
  import MovieListItem from '@/components/MovieListItem.vue'
  import { mapActions, mapGetters } from 'vuex'


  export default {
    name: 'MovieListView',
    components: { MovieListItem },
    computed: {
      ...mapGetters(['movies', 'isLoggedIn', 'isMovies', 
      'genres', 'moviesKind', 'query'])
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

.body {
  background-color: rgb(33, 33, 33);
} 

img {
  --_g: no-repeat linear-gradient(#000 0 0);
  --_s: 10% /45% 45%;
  --m:
    var(--_g) left   var(--_i,0%) top    var(--_s),
    var(--_g) bottom var(--_i,0%) left   var(--_s),
    var(--_g) top    var(--_i,0%) right  var(--_s),
    var(--_g) right  var(--_i,0%) bottom var(--_s);
  -webkit-mask: var(--m);
          mask: var(--m);
  filter: grayscale();
  transition: .3s linear;
  cursor: pointer;
}
img:hover {
  --_i: 10%;
  filter: grayscale(0);
}

body {
  margin: 0;
  background: #c9697a;
  display: grid;
  min-height: 100vh;
  grid-auto-flow :column;
  place-content: center;
  gap: 40px;
}

/* .container {
  width: 70%;
  height: 200px;
  overflow: hidden;
}

.container img {
  max-width: 100%;
  height: auto;
  display: block;
} */

img {
  max-width: 100%;
  width: auto !important;
  height: auto !important;
}

</style>