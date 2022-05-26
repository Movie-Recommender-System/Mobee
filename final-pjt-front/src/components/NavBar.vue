<template>
  <nav class="navbar navbar-expand-lg navbar-light bg-light sticky-top py-2 d-flex">
    <div class="container mx-5">
      <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNavDropdown" aria-controls="navbarNavDropdown" aria-expanded="false" aria-label="Toggle navigation">
      <span class="navbar-toggler-icon"></span>
    </button>

      <div class="collapse navbar-collapse" id="navbarNavDropdown">
        <ul class="navbar-nav">
          <li class="nav-item me-5">
            <router-link :to="{ name: 'bee' }" class="nav-link" >bee</router-link>
          </li>
          <li class="nav-item me-5">
            <router-link :to="{ name: 'intro' }" class="nav-link" >MOBEE</router-link>
          </li>
          <li class="nav-item me-5">
            <router-link :to="{ name: 'first' }" class="nav-link" >first</router-link>
          </li>
          <li class="nav-item">
            <router-link :to="{ name: 'movie'}"  class="nav-link">Movie</router-link>
          </li>
          <li class="nav-item">
            <router-link class="nav-link" :to="{ name: 'article' }" >Community</router-link>
          </li>
          <li v-if="!isLoggedIn" class="nav-item">
            <router-link class="nav-link" :to="{ name: 'login' }">Login</router-link>
          </li>
          <li v-if="!isLoggedIn" class="nav-item">
            <router-link class="nav-link" :to="{ name: 'signup' }">Signup</router-link>
          </li>
          <li v-if="isLoggedIn" class="nav-item dropdown">
            <a class="nav-link dropdown-toggle" href="#" id="navbarDropdownMenuLink" role="button" data-bs-toggle="dropdown" aria-expanded="false">My Page</a>
            <div class="dropdown-menu">
              <router-link class="dropdown-item" :to="{ name: 'profile' }">Profile</router-link>
              <a v-if="isStaff" class="dropdown-item" href="http://localhost:8000/admin/">Admin Page</a>
              <!--관리자계정페이지-->
              <div v-if="isStaff" class="dropdown-divider"></div>
              <a v-if="isLoggedIn" class="dropdown-item text-decoration-none" href="#" @click.prevent="logout">logout</a>
            </div>
          </li>
        </ul>
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