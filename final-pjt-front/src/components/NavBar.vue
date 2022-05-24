<template>
  <nav class=" d-flex navbar navbar-expand-lg navbar-dark bg-primary">
    
    <div class="container-fluid mx-5">
      
      <i class="bi bi-list toggle-sidebar-btn"></i>
      <a class="navbar-brand" href="#">MOBEE</a>

      <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
        <span class="navbar-toggler-icon"></span>
      </button>

      <div class="collapse navbar-collapse" id="navbarColor01">
        <ul class="navbar-nav me-auto">
          <li class="nav-item">
            <button class="btn btn-primary" type="button" data-bs-toggle="collapse" data-bs-target="#collapseWidthExample" aria-expanded="false" aria-controls="collapseWidthExample">
              <span class="navbar-toggler-icon"></span>
            </button>
          </li>
          <li class="nav-item">
            <i class="bi bi-list toggle-sidebar-btn"></i>
          </li>
          <li class="nav-item">
            <router-link :to="{ name: 'movie'}"  class="nav-link active" href="#">Home
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
              <a v-if="isLoggedIn" class="dropdown-item text-decoration-none" href="#" @click.prevent="logout">logout</a>
              <router-link class="dropdown-item" :to="{ name: 'profile' }">Profile</router-link>
              <router-link class="dropdown-item" :to="{ name: 'mileageShop' }">Mileage</router-link>
              <!--관리자계정페이지-->
              <div v-if="isStaff" class="dropdown-divider"></div>
              <a v-if="isStaff" class="dropdown-item" href="http://localhost:8000/admin/">Admin Page</a>
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

<style>
    
/*--------------------------------------------------------------
# Header Nav
--------------------------------------------------------------*/
.header-nav ul {
  list-style: none;
}
.header-nav > ul {
  margin: 0;
  padding: 0;
}
.header-nav .nav-icon {
  font-size: 20px;
  color: #b4b4b4; /* 상단바 아이콘 */
}

.header-nav .nav-icon:hover {
  font-size: 20px;
  color: #ffffff; /* 상단바 아이콘 */
}

.header-nav .nav-profile {
  color: #bcbcbc; /* 상단바 사람 이름 */
}
.header-nav .nav-profile img {
  max-height: 36px;
}
.header-nav .nav-profile span {
  font-size: 14px;
  font-weight: 600;
}
.header-nav .badge-number {
  position: absolute;
  inset: 4px 6px auto auto;
  font-weight: normal;
  font-size: 11px;
  padding: 3px 6px;
}
.header-nav .notifications .notification-item {
  display: flex;
  align-items: center;
  padding: 15px 10px;
  transition: 0.3s;
}
.header-nav .notifications .notification-item i {
  margin: 0 20px 0 10px;
  font-size: 24px;
}
.header-nav .notifications .notification-item h4 {
  font-size: 16px;
  font-weight: 600;
  margin-bottom: 5px;
}
.header-nav .notifications .notification-item p {
  font-size: 13px;
  margin-bottom: 3px;
  color: #303030; /* 상단바 알림 content */
}
.header-nav .notifications .notification-item:hover {
  background-color: #f6f9ff;
}
.header-nav .messages .message-item {
  padding: 15px 10px;
  transition: 0.3s;
}
.header-nav .messages .message-item a {
  display: flex;
}
.header-nav .messages .message-item img {
  margin: 0 20px 0 10px;
  max-height: 40px;
}
.header-nav .messages .message-item h4 {
  font-size: 16px;
  font-weight: 600;
  margin-bottom: 5px;
  color: #444444; /* 상단바 메시지 title */
  
}
.header-nav .messages .message-item p {
  font-size: 13px;
  margin-bottom: 3px;
  color: #919191;
}
.header-nav .messages .message-item:hover {
  background-color: #f6f9ff;
}
.header-nav .profile {
  min-width: 240px;
  padding-bottom: 0;
}
.header-nav .profile .dropdown-header h6 {
  font-size: 18px;
  margin-bottom: 0;
  font-weight: 600;
  color: #444444;
}
.header-nav .profile .dropdown-header span {
  font-size: 14px;
}
.header-nav .profile .dropdown-item {
  font-size: 14px;
  padding: 10px 15px;
  transition: 0.3s;
}
.header-nav .profile .dropdown-item i {
  margin-right: 10px;
  font-size: 18px;
  line-height: 0;
}
.header-nav .profile .dropdown-item:hover {
  background-color: #f6f9ff;
}

</style>