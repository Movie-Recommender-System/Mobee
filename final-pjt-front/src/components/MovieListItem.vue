<template>
  <div class="col">
    <div class="card h-100">
      <img :src="movie.poster_path" class="card-img-top img-thumbnail rounded" :alt="`${movie.title} poster img`">
      <div class="card-body">
        <h5 class="card-title">{{ movie.title }}</h5>
        <h4>wished_count:{{ movie.wished_count }}</h4>
        <MovieDetailModal>
        </MovieDetailModal>
      </div>
      <div class="card-footer">
        <small class="text-muted">{{ movie.release_date }}</small>
      </div>
    </div>
  </div> 
</template>

<script>
  import MovieDetailModal from './MovieDetailModal.vue'
  export default {
    name: 'MovieListItem',
    props: { movie: Object },
    components: { MovieDetailModal },
  }
</script>

<style>
  
</style>