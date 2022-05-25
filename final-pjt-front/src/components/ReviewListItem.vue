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

    <div class="d-flex mb-5">
      <div>
        <h4>
          <a v-if="isLoggedIn" @click='likeReview(
            {moviePk : review.movie, reviewPk : review.pk})'>
            <i v-if="review.is_liked" class="fa-solid fa-heart text-danger"></i>
            <i v-else class="fa-regular fa-heart"></i>
          </a>
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
          <li><button class="dropdown-item" type="button" @click="open">
          수정</button></li>
        </ul>
      </div>
    </div>
    <modal name='updateModal' height="auto" width="50%">
      <ReviewEditForm :review="review"/>
    </modal>
  </li>
</template>

<script>
  import ReviewEditForm from './ReviewEditForm.vue'
  import { mapGetters, mapActions } from 'vuex'
  import Vue from 'vue'
  import VModal from 'vue-js-modal'
  import 'vue-js-modal/dist/styles.css'

  Vue.use(VModal)

  export default {
    name: 'ReviewListItem',
    components: { ReviewEditForm },
    props: {review: Object },
    computed: {
      ...mapGetters([ 'isLoggedIn' ])
    },
    methods: {
      ...mapActions([ 'likeReview', 'deleteReview' ]),
      open () {
        this.$modal.show('updateModal')
      }
    }
  }
</script>

<style>
</style>