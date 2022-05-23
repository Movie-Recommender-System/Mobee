<template>
  <div @click="open" class="col">
    <div class="card h-100">
      <img :src="movie.poster_path" class="card-img-top img-thumbnail rounded" alt="poster img">
      <div class="card-body">
        <h5 class="card-title">{{ movie.title }}</h5>
        <h4>wished_count:{{ movie.wished_count }}</h4>
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

  //componentName: 'Modal'}, 
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
      }
    }
  }
</script>

<style>
  
</style>