<template>
  <div id="app">

    <header class="header navbar0 fixed-top align-items-center" id="header">
      <NavBar/>
    </header>
    

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
    // mounted() {
    //       /**
    //    * Easy on scroll event listener 
    //    */
    //   const onscroll = (el, listener) => {
    //     el.addEventListener('scroll', listener)
    //   }
    //   /**
    //    * Sidebar toggle
    //    */
    //     if (select('.toggle-sidebar-btn')) {
    //       on('click', '.toggle-sidebar-btn', function(e) { select('body').classList.toggle('toggle-sidebar')})
    //   }
    // }
  }
</script>

<style>

@import url("../public/bootstrap.css");

:root {
  scroll-behavior: smooth;

}

/* 커서이미지 */
html, body{
  cursor: url(./assets/bee_cursor.png), auto;
}
a, a:link {
  cursor: url(./assets/bee_hover.png),auto;
}
a:hover, a:focus { cursor: url(./assets/bee_hover.png),auto;} 
a:active {cursor: url(./assets/bee_hover.png),auto;} 
input {cursor: url(./assets/bee_hover.png),auto;} 

#app {
  height: 100vh;
  /* cursor: url("./assets/bee.png"), auto; */
}

h1, h2, h3, h4, h5, h6 {
  font-family: "Nunito", sans-serif; /*재설정하기!*/
}

/*--------------------------------------------------------------
# Main
--------------------------------------------------------------*/
#main {
  margin-top: 90px;
  padding: 10px 10px;
  transition: all 0.3s;  
}
@media (max-width: 1200px) {
  #main {
    margin-left: 10px;
    padding: 20px;
  }
}

/*--------------------------------------------------------------
# Page Title
--------------------------------------------------------------*/
.pagetitle {
  margin-bottom: 10px;
}
.pagetitle h1 {
  font-size: 24px;
  margin-bottom: 0;
  font-weight: 600;
  color: #1a1a1a;
}

/* 
.contents {
  min-height: 200vh;

} */

.header {
  transition: all 0.5s;
  z-index: 997;
  height: 90px;
  box-shadow: 0px 2px 20px rgba(117, 117, 117, 0.1); /* 상단바 밑 그림자색 */
  background-color: rgb(255, 255, 255);
  padding-left: 20px;
  padding: 1rem;
  /* padding-bottom: 1rem; */
  /* Toggle Sidebar Button */
  /* Search Bar */
}
.header .toggle-sidebar-btn {
  font-size: 32px;
  padding-left: 10px;
  cursor: pointer;
  color: #ffffff;
}
.header .search-bar {
  min-width: 360px;
  padding: 0 20px;
}
@media (max-width: 1199px) {
  .header .search-bar {
    position: fixed;
    top: 50px;
    left: 0;
    right: 0;
    padding: 20px;
    box-shadow: 0px 0px 15px 0px rgba(112, 1, 1, 0.1);
    background: white; /*  */
    z-index: 9999;
    transition: 0.3s;
    visibility: hidden;
    opacity: 0;
  }
  .header .search-bar-show {
    top: 60px;
    visibility: visible;
    opacity: 1;
  }
}
.header .search-form {
  width: 100%;
}
.header .search-form input {
  border: 0;
  font-size: 14px;
  color: #000000; /* 상단바 검색창 글자색 */
  border: 1px solid rgba(1, 41, 112, 0.2); /* 상단바 검색창 기본 테두리 색 */
  padding: 7px 38px 7px 8px;
  border-radius: 3px;
  transition: 0.3s;
  width: 100%;
}
.header .search-form input:focus, .header .search-form input:hover {
  outline: none;
  box-shadow: 0 0 10px 0 rgba(255, 221, 0, 0.15); /* 상단바 검색창 누르면 테두리 그림자색 */
  border: 1px solid rgba(238, 255, 0, 0.3); /* 상단바 검색창 누르면 테두리 색 */
}
.header .search-form button {
  border: 0;
  padding: 0;
  margin-left: -30px;
  background: none;
}
.header .search-form button i {
  color: #323232; /* 상단바 검색창 아이콘 */
}
</style>

