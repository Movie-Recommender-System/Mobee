<template>
  <div>
    <h3>MovieDetailModal</h3>
    <ReviewList/>
  </div>
</template>

<script>
  import ReviewList from './ReviewList.vue'

  export default {
    name: 'MovieDetailModal',
    components: { ReviewList },
  }
</script>

<style>
  
</style>