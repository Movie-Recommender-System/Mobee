<template>
  <div>
    <h3>MovieListView</h3>
    <ul>
      <li>
        <button>유저들이 가장 많이 보고 싶어하는 영화</button>
        </li>
      <li><button>최신 영화</button></li>
      <li><button>사용자 맞춤 추천 영화</button></li>
    </ul>
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
      ...mapGetters(['movies'])
    },
    methods: {
      ...mapActions(['fetchMovies'])
    },
    created() {
      this.fetchMovies('recent')
    }
  }
</script>

<style>
  
</style>