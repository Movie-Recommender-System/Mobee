<template>
  <div>
    <h3>MovieListView</h3>
    <MovieListItem/>
  </div>
</template>

<script>
  import MovieListItem from '@/components/MovieListItem.vue'
  import { mapActions, mapGetters } from 'vuex'
  
  export default {
    name: 'MovieListView',
    components: { MovieListItem },
  }
</script>

<style>
  
</style>