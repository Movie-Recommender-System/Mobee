<template>
  <nav class=" d-flex navbar navbar-expand-lg navbar-dark bg-primary sticky-top py-4">
    
    <div class="container-fluid mx-5">
      
      <p class="navbar-brand" >MOBEE</p>

      <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
        <span class="navbar-toggler-icon"></span>
      </button>

      <div class="collapse navbar-collapse" id="navbarColor01">
        <ul class="navbar-nav me-auto">
          <li class="nav-item">
            <i class="bi bi-list toggle-sidebar-btn"></i>
          </li>
          <li class="nav-item">
            <router-link :to="{ name: 'movie'}"  class="nav-link active" href="#">Movie
              <span class="visually-hidden">(current)</span>
            </router-link>
          </li>
          <li class="nav-item">
            <router-link class="nav-link" :to="{ name: 'article' }" >Community</router-link>
          </li>
          <!-- <li v-if="isLoggedIn" class="nav-item">
            <router-link class="nav-link" :to="{ name: 'profile', params: { username } }">
              {{ currentUser.username }}'s page
            </router-link>
          </li> -->
          <li v-if="!isLoggedIn" class="nav-item">
            <router-link class="nav-link" :to="{ name: 'login' }">Login</router-link>
          </li>
          <li v-if="!isLoggedIn" class="nav-item">
            <router-link class="nav-link" :to="{ name: 'signup' }">Signup</router-link>
          </li>
          <li v-if="isLoggedIn" class="nav-item dropdown">
            <a class="nav-link dropdown-toggle" data-bs-toggle="dropdown" href="#" role="button" aria-haspopup="true" aria-expanded="false">My Page</a>
            <div class="dropdown-menu">
              <router-link class="dropdown-item" :to="{ name: 'profile' }">Profile</router-link>
              <a v-if="isStaff" class="dropdown-item" href="http://localhost:8000/admin/">Admin Page</a>
              <!--관리자계정페이지-->
              <div v-if="isStaff" class="dropdown-divider"></div>
              <a v-if="isLoggedIn" class="dropdown-item text-decoration-none" href="#" @click.prevent="logout">logout</a>
            </div>
          </li>
        </ul>
        <form class="d-flex">
          <input class="form-control me-sm-2" type="text" placeholder="Search">
          <button class="btn btn-secondary my-2 my-sm-0" type="submit">Search</button>
        </form>
      </div>
    </div>
  </nav>
</template>

<script>
  import { mapGetters, mapActions } from 'vuex'

  export default {
    name: 'NavBar',
    computed: {
      ...mapGetters(['isLoggedIn', 'currentUser']),
      username() {
        return this.currentUser.username ? this.currentUser.username : 'guest'
      },
      isStaff () {
        return !!this.currentUser.is_staff
      }
    },
    methods: {
      ...mapActions(['logout']),
    }
  }
</script>

<style scoped>
    
/*--------------------------------------------------------------
# Header Nav
--------------------------------------------------------------*/
.nav {
  font-size: 20px;
}

a .router-link:hover {
  color:aqua;
}

</style>