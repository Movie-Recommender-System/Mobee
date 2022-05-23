<template>
  <li class="list-group-item d-flex justify-content-between align-items-center">
    <div class="align-top">
      <i class="fa-solid fa-star"></i>
      <i v-if="review.score >= 2" class="fa-solid fa-star"></i>
      <i v-if="review.score >= 3" class="fa-solid fa-star"></i>
      <i v-if="review.score >= 4" class="fa-solid fa-star"></i>
      <i v-if="review.score == 5" class="fa-solid fa-star"></i>
      <p>내용 : {{ review.content }}</p>
    </div>
    
    <div class="d-flex">
      <div>
        <h4>
          <button v-if="isLoggedIn" @click='likeReview(
            {moviePk : review.movie, reviewPk : review.pk})'>
            <i v-if="review.is_liked" class="fa-solid fa-heart"></i>
            <i v-else class="fa-regular fa-heart"></i>
          </button>
          <i v-else class="fa-solid fa-heart"></i>
          {{ review.like_count }}
        </h4>
        <span class="m-2">작성자 : {{ review.user.username }}</span>
      </div>
      <div class="dropdown">
        <button class="btn btn-secondary dropdown-toggle" type="button" 
        id="dropdownMenu2" data-bs-toggle="dropdown" aria-expanded="false">
          <i class="fa-solid fa-gear"></i>
        </button>
        <ul class="dropdown-menu" aria-labelledby="dropdownMenu2">
          <li><button class="dropdown-item" type="button"
          @click='deleteReview({moviePk : review.movie, reviewPk : review.pk})'>
          삭제</button></li>
          <li><button class="dropdown-item" type="button">
          수정</button></li>
        </ul>
      </div>
    </div>
  </li>
</template>

<script>
  import { mapGetters, mapActions } from 'vuex'
  export default {
    name: 'ReviewListItem',
    props: {review: Object },
    computed: {
      ...mapGetters([ 'isLoggedIn' ])
    },
    methods: {
      ...mapActions([ 'likeReview', 'deleteReview' ])
    }
  }
</script>

<style>
</style>