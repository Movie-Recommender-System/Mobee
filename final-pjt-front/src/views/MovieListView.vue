<template>
  <div>
    
    <div class="pagetitle">
        <h1 class="text-center my-5">MovieListView</h1>
        <div class=" text-align-between justify-content-between align-items-center">
          <ol class=" text-align-between justify-content-between align-items-center">
            <button type="button" class="btn btn-primary" @click='fetchMovies("recent")'>최신 영화</button>
            <button type="button" class="btn btn-primary" @click='fetchMovies("wish")'>인기 영화</button>
            <button type="button" class="btn btn-primary" v-if="isLoggedIn" @click='fetchRecommendMovies'>사용자 추천 영화</button>
            <button id="btnGroupDrop1" type="button" class="btn btn-primary dropdown-toggle" data-bs-toggle="dropdown" aria-expanded="false">장르별 영화</button>
            <ul class="dropdown-menu" aria-labelledby="btnGroupDrop1">
              <li>
                <a class="dropdown-item" href="#">SF</a>
                <a class="dropdown-item" href="#">TV 영화</a>
                <a class="dropdown-item" href="#">가족</a>
                <a class="dropdown-item" href="#">공포</a>
                <a class="dropdown-item" href="#">다큐멘터리</a>
                <a class="dropdown-item" href="#">드라마</a>
                <a class="dropdown-item" href="#">로맨스</a>
                <a class="dropdown-item" href="#">모험</a>
                <a class="dropdown-item" href="#">미스터리</a>
                <a class="dropdown-item" href="#">범죄</a>
                <a class="dropdown-item" href="#">서부</a>
                <a class="dropdown-item" href="#">스릴러</a>
                <a class="dropdown-item" href="#">애니메이션</a>
                <a class="dropdown-item" href="#">액션</a>
                <a class="dropdown-item" href="#">역사</a>
                <a class="dropdown-item" href="#">음악</a>
                <a class="dropdown-item" href="#">전쟁</a>
                <a class="dropdown-item" href="#">코미디</a>
                <a class="dropdown-item" href="#">판타지</a>
              </li>
            </ul>
          </ol>
        </div>
      </div>
    <ul>
      <div class="row row-cols-1 row-cols-sm-2 row-cols-md-3 row-cols-lg-4 row-cols-xl-5 row-cols-xxl-6 g-4">
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
      ...mapGetters(['movies', 'isLoggedIn'])
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
  .breadcrumb > li:hover {
    cursor: pointer;
  }
</style>