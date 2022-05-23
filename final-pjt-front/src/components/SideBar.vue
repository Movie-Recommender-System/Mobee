<template>
  <div>
    <!-- ======= Sidebar ======= -->
      <ul class="sidebar-nav" id="sidebar-nav">

        <li class="nav-item">
          <a class="nav-link collapsed" href="index.html">
            <i class="bi bi-grid"></i>
            <span>Dashboard</span>
          </a>
        </li><!-- End Dashboard Nav -->

        <li class="nav-item">
          <a class="nav-link collapsed" data-bs-target="#movies-nav" data-bs-toggle="collapse" href="#">
            <i class="bi bi-menu-button-wide"></i><span>movies</span><i class="bi bi-chevron-down ms-auto"></i>
          </a>
          <ul id="movies-nav" class="nav-content collapse " data-bs-parent="#sidebar-nav">
            <li>
              <router-link class="text-decoration-none nav-link" :to="{ name: 'movie' }">
                <i class="bi bi-circle"></i><span>최신 영화</span>
              </router-link>
            </li>
            <li>
              <router-link class="text-decoration-none nav-link" :to="{ name: 'movie' }">
                <i class="bi bi-circle"></i><span>인기 영화</span>
              </router-link>
            </li>
            <li>
              <router-link class="text-decoration-none nav-link" :to="{ name: 'movie' }">
                <i class="bi bi-circle"></i><span>내 꿀단지 영화</span>
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
              <router-link :to="{ name: 'article' }">
                <i class="bi bi-circle"></i><span>커뮤니티</span>
              </router-link>
            </li>
            <!-- <li>
              <routers href="Community-layouts.html">
                <i class="bi bi-circle"></i><span>글 작성</span>
              </routers>
            </li> -->
          </ul>
        </li><!-- End Community Nav -->

        <li class="nav-item">
          <a class="nav-link collapsed" data-bs-target="#tables-nav" data-bs-toggle="collapse" href="#">
            <i class="bi bi-layout-text-window-reverse"></i><span>Tables</span><i class="bi bi-chevron-down ms-auto"></i>
          </a>
          <ul id="tables-nav" class="nav-content collapse " data-bs-parent="#sidebar-nav">
            <li>
              <router-link class="dropdown-item" :to="{ name: 'profile' }">
                <i class="bi bi-circle"></i><span>Profile</span>
              </router-link>
            </li>
            <li>
              <router-link class="dropdown-item" :to="{ name: 'mileageShop' }">
                <i class="bi bi-circle"></i><span>Mileage</span>
              </router-link>
            </li>
            <div v-if="isStaff" class="dropdown-divider"></div>
            <li>
              <a v-if="isStaff" class="dropdown-item" href="#">
                <i class="bi bi-circle"></i><span>Admin Page</span>
              </a>
            </li>
          </ul>
        

        <li class="nav-heading">Pages</li>

        <li class="nav-item">
          <a class="nav-link collapsed" href="users-profile.html">
            <i class="bi bi-person"></i>
            <span>Profile</span>
          </a>
        </li><!-- End Profile Page Nav -->


        <li class="nav-item">
          <a class="nav-link collapsed" href="pages-contact.html">
            <i class="bi bi-envelope"></i>
            <span>Contact</span>
          </a>
        </li><!-- End Contact Page Nav -->

        <li class="nav-item">
          <a class="nav-link collapsed" href="pages-register.html">
            <i class="bi bi-card-list"></i>
            <span>Register</span>
          </a>
        </li><!-- End Register Page Nav -->

        <li class="nav-item">
          <a class="nav-link collapsed" href="pages-login.html">
            <i class="bi bi-box-arrow-in-right"></i>
            <span>Login</span>
          </a>
        </li><!-- End Login Page Nav -->
      </ul>
  </div>
</template>
<script>
export default {
  name: 'SideBar',
}
</script>
<style>


</style>