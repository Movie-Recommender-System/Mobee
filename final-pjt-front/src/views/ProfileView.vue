<template>
  <div class="container px-5">
    <div class="container px-5">
    <h1 class="text-center my-5">{{ profile.username }}'s Profile</h1>
    <div v-if="currentUser.is_staff == true">
      <button v-if="isDownload" class="btn btn-warning" type="button" disabled>
        <span class="spinner-border spinner-border-sm" role="status" aria-hidden="true"></span>
        Loading...
      </button>
      <form v-else>
        <label for="page">page:</label>
        <input id="page" type="text" v-model.trim="page">
        <button  class="btn btn-warning"
        @click.prevent="download('now_playing')">TMDB Now Playing Movie Update</button>
        <button  class="btn btn-warning"
        @click.prevent="download('popular')">TMDB Famous Movie Update</button>
      </form>
    </div>
    <div class="row my-5">
      <div class="col-4 box ">
        <h4 class="text-center">장르 선호도</h4>
        <div class="p-3">
          <Bar
          :chart-options="chartOptions"
          :chart-data="chartData"
          :chart-id="chartId"
          :dataset-id-key="datasetIdKey"
          :plugins="plugins"
          :css-classes="cssClasses"
          :styles="styles"
          :width="width"
          :height="height"
          />
        </div>
        
        <br>
        <h5 class="text-center my-2">{{ profile.username }}님이 좋아하는 장르입니다.</h5>
        <div class="container text-center">
          <div class=" d-inline " v-for="best_genre in profile.preferred_genres.best_genres" :key="best_genre">
          <span class=" badge bg-warning">{{ best_genre }}</span> 
        </div>
        </div>
        
      </div>
      <div class="honeymovies col-8 text-center">
        <h4 >내 꿀단지 영화</h4>
        <div class="p-3 box row row-cols-1 row-cols-sm-2 row-cols-md-3 row-cols-lg-4">
          <div class="col py-1" v-for="movie in profile.wish_movie_list" :key="movie.pk">
            <div class="card h-100">
              <p class="card-header">{{ movie.title }}</p>
              <img :src="`https://image.tmdb.org/t/p/w500/${movie.poster_key}`" 
              class="cover d-block  " alt="poster img" />
            </div> 
          </div>
        </div>
      </div>

    <div class="row my-5">
      <div class="col-4">
      <h4 class="text-center">남긴 리뷰</h4>
        <ul class="box list-group m-3">
          <li class="list-group-item" v-for="review in profile.reviews" :key="review.pk">
            <h5>영화 제목 : {{ review.movie.title }}</h5>
            <p>리뷰 : {{ review.content }}</p>
            <div>
              <span v-if="review.score > 0.5" class="material-symbols-outlined text-warning">hexagon</span>
              <span v-if="review.score > 1.5" class="material-symbols-outlined text-warning">hexagon</span>
              <span v-if="review.score > 2.5" class="material-symbols-outlined text-warning">hexagon</span>
              <span v-if="review.score > 3.5" class="material-symbols-outlined text-warning">hexagon</span>
              <span v-if="review.score > 4.5" class="material-symbols-outlined text-warning">hexagon</span>
            </div>
            <p><i class="fa-solid fa-heart"></i> {{ review.like_count }}</p>
          </li>
        </ul>
      </div>
      <div class="col-4">
        <h4 class="text-center">작성한 게시글 모음</h4>
        <div class="box list-group">
          <li class="list-group-item" v-for="article in profile.articles" :key="article.pk">
            <h5> {{ article.title }}</h5>
            <p>{{ article.content }}</p>
            <p><i class="fa-solid fa-heart"></i> {{ article.like_count }}</p>
          </li>
        </div>
      </div>
      <div class="col-4">
        <h4 class="text-center">작성한 댓글 모음</h4>
        <div>
          <ul class=" box list-group">
          <li class="list-group-item" v-for="comment in profile.comments" :key="comment.pk">
            <h5> {{ comment.article.title }}</h5>
            <p> {{ comment.content }}</p>
          </li>
        </ul>
        </div>
        </div>
      </div>
    </div>
    </div>
  </div>
</template>

<script>
  import { mapActions, mapGetters } from 'vuex'
  import { Bar } from 'vue-chartjs/legacy'
  import { Chart as ChartJS, Title, Tooltip, Legend, BarElement, CategoryScale, LinearScale } from 'chart.js'

  ChartJS.register(Title, Tooltip, Legend, BarElement, CategoryScale, LinearScale)

  export default {
    name: 'ProfileView',
    components: { Bar },
    data() {
      return {
        page: 0,
        chartData: {
          labels: [ 'a', 'b', 'c', 'd' ],
          datasets: [ { 
            data: [0, 1, 2, 3],
            // backgroundColor: '#f87979',
            backgroundColor: 'rgb(255, 220, 106)',
            label: '선호도',
            } ],
        },
        chartOptions: {
          responsive: true
        },
      }
    },
    props: {
      chartId: {
        type: String,
        default: 'bar-chart'
      },
      datasetIdKey: {
        type: String,
        default: 'label'
      },
      width: {
        type: Number,
        default: 400
      },
      height: {
        type: Number,
        default: 400
      },
      cssClasses: {
        default: '',
        type: String
      },
      styles: {
        type: Object,
        default: () => {}
      },
      plugins: {
        type: Array,
        default: () => []
      }
    },
    computed: {
      ...mapGetters(['profile', 'currentUser', 'isDownload']),
    },
    methods: {
      ...mapActions(['fetchProfile', 'createMovies']),
      download(kind) {
        setTimeout(() => {      
        this.createMovies({'kind': kind, 'page': this.page})
        }, 500)
      }
    },
    created () {
      setTimeout(() => {      
        this.fetchProfile({ username : this.currentUser.username })
      }, 500)        
      setTimeout(() => {
        this.chartData.labels = this.profile.preferred_genres.genres
        this.chartData.datasets[0].data = this.profile.preferred_genres.scores
      }, 1000)
    }
  }
</script>

<style scoped>
@font-face {
    font-family: 'KOHIBaeumOTF';
    src: url('https://cdn.jsdelivr.net/gh/projectnoonnu/noonfonts_2201-2@1.0/KOHIBaeumOTF.woff') format('woff');
    font-weight: normal;
    font-style: normal;
}
  .box {
    height: 600px;
    overflow: auto;
  }
  h1{
    font-family: 'KOHIBaeumOTF';
  }

  /* .honeymovies > p {
    font-family: 'KOHIBaeumOTF';
  } */

  h1:hover, h2:hover, h3:hover, h4:hover, h5:hover, h6:hover, a:hover {
    background-color: #ffdc6a;
  }
</style>