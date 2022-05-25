<template>
  <div id="app">

    <header class="header fixed-top align-items-center" id="header">
      <NavBar/>
    </header>
    <br>
    <br>
    <br>
    <br>
    <main>
      <div class="card min-vh-100">
        <div class="card-body">
          <router-view></router-view>
        </div>
        <div class="card-footer text-muted text-center">
          <FooterPage ></FooterPage>
        </div>
      </div>
    </main>
  </div>
</template>

<script>
  import FooterPage from '@/components/FooterPage.vue'
  import NavBar from '@/components/NavBar.vue'
  import { mapActions } from 'vuex'
  export default {
    name: "App",
    components: {
      NavBar, FooterPage, 
    },
    methods: {
      ...mapActions(['fetchCurrentUser', 'fetchGenres'])
    },
    created() {
      this.fetchCurrentUser(),
      this.fetchGenres()
    },
  }
</script>

<style>

@import url("../public/bootstrap.css");
@import url("../public/bootstrap.min.css");

:root {
  scroll-behavior: smooth;

}
input::placeholder {
  font-family: 'Stylish', sans-serif;
}


textarea::placeholder {
  font-family: 'Stylish', sans-serif;
}

/* 커서이미지 */
html, body{
  cursor: url(./assets/bee_cursor.png), auto;
}
a, a:link {
  cursor: url(./assets/bee_hover.png),auto;
}
a:hover, a:focus { 
  cursor: url(./assets/bee_hover.png),auto;
  color:#665f5f;
  } 
a:active {cursor: url(./assets/bee_hover.png),auto;} 
input {cursor: url(./assets/bee_hover.png),auto;} 

#app {
  height: 100vh;
  /* cursor: url("./assets/bee.png"), auto; */
}

/* 글씨체 부분  자유롭게*/
h1, h2, h3, h4, h5, h6 {
  font-family: 'Noto Sans KR' , sans-serif;
  font-weight: 900;
}
p {
  font-family: 'Noto Sans KR', sans-serif;
}
</style>

