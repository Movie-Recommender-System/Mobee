<template>
  <div>
    <h3>ReviewList</h3>
    <ul v-if="reviews===[]">
      <li class="text-muted">리뷰가 존재하지 않습니다.</li>
    </ul>
    <ul class="list-group">
      <ReviewListItem v-for="review in reviews" :key="review.pk" :review='review'/>
    </ul>
    
  </div>
</template>

<script>
  import ReviewListItem from './ReviewListItem.vue'

  export default {
    name: 'ReviewList',  
    components: { ReviewListItem },
    props: {reviews: Array },
  }
</script>

<style>
  
</style>