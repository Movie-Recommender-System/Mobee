<template>
  <div class="movislistitem col">
          <div class="movie_card" id="bright" @click="open">
            <div class="info_section">
              <div class="movie_header">
                <img class="locandina" :src="posterURL"/>
                <h4>{{ movie.title }}</h4>
                <h6>{{ movie.release_date }}, David Ayer <i class="fa-solid fa-heart"></i>   {{ movie.wished_count }}</h6> 
                <span class="minutes">117 min</span>
                <span v-for="genre in movie.genres" :key="genre.pk">{{ genre.name }}</span>
                
                 
              </div>
              <div class="movie_desc">
                <p class="text">
                  {{ movie.overview }}
                </p>
              </div>
            </div>
            <div class="blur_back bright_back" :style="`background-image: url(${backdropURL});`"></div>
          </div>

    <modal :name='movie.title' height="auto" width="70%"  :scrollable="true">
      <br><br>
      <MovieDetail/>
    </modal>

  </div>
</template>

<script src="https://cdnjs.cloudflare.com/ajax/libs/jquery/3.3.1/jquery.min.js"></script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/color-thief/2.0.1/color-thief.min.js"></script>

<script>
  import MovieDetail from './MovieDetail.vue'
  import Vue from 'vue'
  import VModal from 'vue-js-modal'
  import 'vue-js-modal/dist/styles.css'
  import { mapActions } from 'vuex'

  Vue.use(VModal)

  export default {
    name: 'MovieListItem',
    props: { movie: Object },
    components: { MovieDetail },
    computed: {
      backdropURL() {
        return `https://image.tmdb.org/t/p/w500/${this.movie.backdrop_key}`
      },
      posterURL() {
        return `https://image.tmdb.org/t/p/w200/${this.movie.poster_key}`
      },
    },
    methods: {
      ...mapActions(['fetchMovie']),
      open () {
        this.fetchMovie(this.movie.pk)
        setTimeout(() => this.$modal.show(this.movie.title), 500)
      }
    },
  }
</script>

<style scoped>

@import url("https://fonts.googleapis.com/css?family=Montserrat:300,400,700,800");
* {
  box-sizing: border-box;
  margin: 0;
}


.movie_desc > p {
  overflow: hidden;
  text-overflow: ellipsis;
  /* word-wrap:break-word; 
  line-height: 1.2em;
  height: 3.6em;  */
  display: -webkit-box;
  -webkit-line-clamp: 6; /* 라인수 */
  -webkit-box-orient: vertical;
  }
.link {
  display: block;
  text-align: center;
  color: #777;
  text-decoration: none;
  padding: 10px;
}

.movie_card {
  position: relative;
  display: block;
  width: 950px;
  height: 320px;
  margin: 30px auto;
  z-index: 1;
  overflow: hidden;
  border-radius: 10px;
  transition: all 0.4s;
  box-shadow: 0px 0px 120px -25px rgba(0, 0, 0, 0.5);
  overflow: hidden;
  text-overflow: ellipsis;
}

.movie_card:hover {
  transform: scale(1.02);
  box-shadow: 0px 0px 80px -25px rgba(0, 0, 0, 0.5);
  transition: all 0.4s;

}


.movie_card .info_section {
  position: relative;
  width: 100%;
  height: 100%;
  background-blend-mode: multiply;
  z-index: 2;
  border-radius: 10px;
}
.movie_card .info_section .movie_header {
  position: relative;
  padding: 25px;
  height: 40%;
}
.movie_card .info_section .movie_header h4 {
  color: black;
  font-weight: 700;
}
.movie_card .info_section .movie_header h6 {
  color: #555;
  font-weight: 500;
}
.movie_card .info_section .movie_header .minutes {
  display: inline-block;
  margin-top: 13px;
  color: #555;
  padding: 5px;
  border-radius: 5px;
  border: 1px solid rgba(0, 0, 0, 0.05);
}
.movie_card .info_section .movie_header .type {
  display: inline-block;
  color: #959595;
  margin-left: 10px;
}
.movie_card .info_section .movie_header .locandina {
  position: relative;
  float: left;
  margin-right: 20px;
  height: 120px;
  box-shadow: 0 0 20px -10px rgba(0, 0, 0, 0.5);
}

.movie_card .info_section .movie_desc {
  padding: 25px;
  height: 60%;
  
}
.movie_card .info_section .movie_desc .text {
  color: #545454;
  font-size: 15px;
  line-height:170%;
  transition:1s;
}

.movie_card .info_section .movie_desc .text:hover {
  color: #141414;
}

.movie_card .info_section .movie_social {
  height: 10%;
  padding-left: 15px;
  padding-bottom: 20px;
}
.movie_card .info_section .movie_social ul {
  list-style: none;
  padding: 0;
}
.movie_card .info_section .movie_social ul li {
  display: inline-block;
  color: rgba(0, 0, 0, 0.3);
  transition: color 0.3s;
  transition-delay: 0.15s;
  margin: 0 10px;
}
.movie_card .info_section .movie_social ul li:hover {
  transition: color 0.3s;
  color: rgba(0, 0, 0, 0.7);
}
.movie_card .info_section .movie_social ul li i {
  font-size: 19px;
  cursor: pointer;
}
.movie_card .blur_back {
  position: absolute;
  top: 0;
  z-index: 1;
  height: 100%;
  right: 0;
  background-size: cover;
  border-radius: 11px;
}

@media screen and (min-width: 768px) {
  .movie_header {
    width: 70%;
  }

  .movie_desc {
    width: 50%;
  }

  .info_section {
    background: linear-gradient(to right, #e5e6e6 50%, transparent 100%);
  }

  .blur_back {
    width: 80%;
    background-position: -100% 10% !important;
  }
}
@media screen and (max-width: 768px) {
  .movie_card {
    width: 95%;
    margin: 70px auto;
    min-height: 350px;
    height: auto;
  }

  .blur_back {
    width: 100%;
    background-position: 50% 50% !important;
  }

  .movie_header {
    width: 100%;
    margin-top: 85px;
  }

  .movie_desc {
    width: 100%;
}

  .info_section {
    background: linear-gradient(to top, #e5e6e6 50%, transparent 100%);
    display: inline-grid;
  }
}
.bright_back {
  background: url("https://occ-0-2433-448.1.nflxso.net/art/cd5c9/3e192edf2027c536e25bb5d3b6ac93ced77cd5c9.jpg");
}
</style>