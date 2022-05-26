<template>
  <form @submit.prevent="onSubmit" class="bg-black">
    <div class="container">
      <div class="row p-3">
        <p>평점</p>
        <div class="d-flex py-2">
        <span @click='onStar(0)'>
          <span v-if="stars[0]" class="material-symbols-outlined 
          text-warning">hexagon</span>
          <span v-else class="material-symbols-outlined">hexagon</span>
        </span>
        <span @click='onStar(1)'>
          <span v-if="stars[1]" class="material-symbols-outlined 
          text-warning">hexagon</span>
          <span v-else class="material-symbols-outlined">hexagon</span>
        </span>
        <span @click='onStar(2)'>
          <span v-if="stars[2]" class="material-symbols-outlined 
          text-warning">hexagon</span>
          <span v-else class="material-symbols-outlined">hexagon</span>
        </span>
        <span @click='onStar(3)'>
          <span v-if="stars[3]" class="material-symbols-outlined 
          text-warning">hexagon</span>
          <span v-else class="material-symbols-outlined">hexagon</span>
        </span>
        <span @click='onStar(4)'>
          <span v-if="stars[4]" class="material-symbols-outlined 
          text-warning">hexagon</span>
          <span v-else class="material-symbols-outlined">hexagon</span>
        </span>
      </div>
      </div>
      
      <div>
        <label for="content">content: </label>
        <textarea placeholder="리뷰를 수정해 주세요." v-model.trim="editReview.content" type="text" id="content" />
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
      modalName: String,
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
        this.$modal.hide(this.modalName)
      } 
    }
  }
</script>

<style>
  
</style>