<template>
  <div >
    <div @click="open" class="card h-100">
      <img :src="movie.poster_path" class="card-img-top img-thumbnail rounded" alt="poster img">
      <div class="card-body">
        <h5 class="card-title">{{ movie.title }}</h5>
        <i class="fa-solid fa-heart"></i>
        {{ movie.wished_count }}
      </div>
      <div class="card-footer">
        <small class="text-muted">{{ movie.release_date }}</small>
      </div>
    </div>

    <modal :name='movie.title' height="auto" width="70%" :scrollable="true">
      <MovieDetail/>
    </modal>
  </div> 
</template>

<script>
  import MovieDetail from './MovieDetail.vue'
  import Vue from 'vue'
  import VModal from 'vue-js-modal'
  import 'vue-js-modal/dist/styles.css'
  import { mapActions } from 'vuex'

  Vue.use(VModal)

  export default {
    name: 'MovieListItem',
    props: { movie: Object },
    components: { MovieDetail },
    methods: {
      ...mapActions(['fetchMovie']),
      open () {
        this.fetchMovie(this.movie.pk)
        this.$modal.show(this.movie.title)
      },
    },
  }
</script>

<style>
  
</style>