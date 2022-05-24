<template>
  <div >
    <!-- ======= Sidebar ======= -->
      <ul class="sidebar-nav" id="sidebar-nav">
        <li class="nav-heading">Pages</li>
        <li class="nav-item">
          <router-link :to="{ name: 'intro' }" class="nav-link collapsed" href="index.html">
            <i class="bi bi-grid"></i>
            <span>Intro</span>
          </router-link>
        </li><!-- End Dashboard Nav -->

        <li class="nav-item">
          <a class="nav-link collapsed" data-bs-target="#movies-nav" data-bs-toggle="collapse" href="#">
            <i class="bi bi-menu-button-wide"></i><span>movies</span><i class="bi bi-chevron-down ms-auto"></i>
          </a>
          <ul id="movies-nav" class="nav-content collapse " data-bs-parent="#sidebar-nav">
            <li>
              <router-link class="text-decoration-none" :to="{ name: 'movie' }">
                <span>최신 영화</span>
              </router-link>
            </li>
            <li>
              <router-link class="text-decoration-none" :to="{ name: 'movie' }">
                <span>인기 영화</span>
              </router-link>
            </li>
            <li>
              <router-link class="text-decoration-none" :to="{ name: 'movie' }">
                <span>내 꿀단지 영화</span>
              </router-link>
            </li>
          </ul>
        </li><!-- End movies Nav -->

        <li class="nav-item">
          <a class="nav-link collapsed" data-bs-target="#Community-nav" data-bs-toggle="collapse" href="#">
            <i class="bi bi-journal-text"></i><span>Community</span><i class="bi bi-chevron-down ms-auto"></i>
          </a>
          <ul id="Community-nav" class="nav-content collapse " data-bs-parent="#sidebar-nav">
            <li>
              <router-link class="text-decoration-none" :to="{ name: 'article' }">
                <span>커뮤니티</span>
              </router-link>
            </li>
            <!-- <li>
              <routers href="Community-layouts.html">
                <span>글 작성</span>
              </routers>
            </li> -->
          </ul>
        </li><!-- End Community Nav -->
        <li class="nav-heading">MY</li>
        <li class="nav-item">
          <a class="nav-link collapsed" data-bs-target="#tables-nav" data-bs-toggle="collapse" href="#">
            <i class="bi bi-layout-text-window-reverse"></i><span>PyPages</span><i class="bi bi-chevron-down ms-auto"></i>
          </a>
          </li>
          <ul id="tables-nav" class="nav-content collapse " data-bs-parent="#sidebar-nav">
            <li v-if="isLoggedIn">
              <router-link v-if="isLoggedIn" class="dropdown-item" :to="{ name: 'profile' }">
                <span>Profile</span>
              </router-link>
            </li><!-- End Profile Page Nav -->

            <li>
              <router-link v-if="isLoggedIn" class="dropdown-item" :to="{ name: 'mileageShop' }">
                <span>Mileage</span>
              </router-link>
            </li><!-- End Mileage Page Nav -->
                          
            <li>
              <a v-if="isLoggedIn" class="dropdown-item text-decoration-none" href="#" @click.prevent="logout">Logout</a>
            </li><!-- End Logout Page Nav -->

            <li v-if="!isLoggedIn" class="dropdown-item">
              <router-link :to="{ name: 'login'}" class="text-decoration-none collapsed" >
                <i class="bi bi-box-arrow-in-right"></i>
                <span>Login</span>
              </router-link>
            </li><!-- End Login Page Nav -->

            <li v-if="!isLoggedIn" class="dropdown-item">
              <router-link class="text-decoration-none collapsed" :to="{ name: 'signup' }">
                <i class="bi bi-card-list"></i>
                <span>Signup</span>
              </router-link>
            </li><!-- End Signup Page Nav -->

            <li v-if="isStaff" class="dropdown-item">
              <a class="text-decoration-none collapsed" href="http://localhost:8080/admin/">
                <i class="bi bi-card-list"></i>
                <span>Admin Page</span>
              </a>
            </li>

            
          </ul>
        
        

        <!-- End Signup Page Nav -->
      </ul>
  </div>
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

<style>


</style>