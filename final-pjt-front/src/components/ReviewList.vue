<template>
  <div>
    <h3 class="text-light text-center py-4">ReviewList</h3>
    <ul v-if="reviews.length === 0">
      <li class="text-muted">리뷰가 존재하지 않습니다.</li>
    </ul>
    <ul v-else class="list-group box">
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
  .box {
    height: 600px;
    overflow: auto;
  }
</style>