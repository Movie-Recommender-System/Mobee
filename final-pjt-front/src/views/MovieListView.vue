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
                <a class="dropdown-item" href="#">Dropdown link</a>
              </li>
            </ul>
          </ol>
        </div>
      </div>

    
    <ul>
      <div class="row row-cols-1 row-cols-md-3 g-4">
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