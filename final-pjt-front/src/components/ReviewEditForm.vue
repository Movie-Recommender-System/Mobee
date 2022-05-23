<template>
  <form @submit.prevent="onSubmit">
    <div>
      <div class="d-flex">
        <span @click='onStar(0)'>
          <i v-if="stars[0]" class="fa-solid fa-star"></i>
          <i v-else class="fa-regular fa-star"></i>
        </span>
        <span @click='onStar(1)'>
          <i v-if="stars[1]" class="fa-solid fa-star"></i>
          <i v-else class="fa-regular fa-star"></i>
        </span>
        <span @click='onStar(2)'>
          <i v-if="stars[2]" class="fa-solid fa-star"></i>
          <i v-else class="fa-regular fa-star"></i>
        </span>
        <span @click='onStar(3)'>
          <i v-if="stars[3]" class="fa-solid fa-star"></i>
          <i v-else class="fa-regular fa-star"></i>
        </span>
        <span @click='onStar(4)'>
          <i v-if="stars[4]" class="fa-solid fa-star"></i>
          <i v-else class="fa-regular fa-star"></i>
        </span>
      </div>
      <div>
        <label for="content">content: </label>
        <textarea v-model.trim="editReview.content" type="text" id="content" />
      </div>
    </div>
    <div>
      <button>수정</button>
    </div>
  </form>
</template>

<script>
  import { mapActions } from 'vuex'

  export default {
    name: 'ReviewEditForm',
    props: { 
      review : Object,
    },
    data () {
      return {
        editReview: {
          content: this.review.content,
          score: 0,
        },
        stars: [false, false, false, false, false],
      }
    },
    methods: {
      ...mapActions([ 'updateReview' ]),
      onStar ( num ) {
        if ( num == 0 ) {
          this.stars = [true, false, false, false, false]
          this.editReview.score = 1
        }
        else if ( num == 1 ) {
          this.stars = [true, true, false, false, false]
          this.editReview.score = 2
        }
        else if ( num == 2 ) {
          this.stars = [true, true, true, false, false]
          this.editReview.score = 3
        }
        else if ( num == 3 ) {
          this.stars = [true, true, true, true, false]
          this.editReview.score = 4
        }
        else if ( num == 4 ) {
          this.stars = [true, true, true, true, true]
          this.editReview.score = 5
        }
      },
      onSubmit() {
        if ( this.editReview.score > 0 ) {
          this.updateReview({ moviePk: this.review.movie, reviewPk: this.review.pk,
            content: this.editReview.content, score: this.editReview.score })
        } else {
          alert('평점을 넣어주세요.')
        }
        this.editReview.content = this.review.content
        this.stars = [false, false, false, false, false]
        this.$modal.hide('updateModal')
      } 
    }
  }
</script>

<style>
  
</style>