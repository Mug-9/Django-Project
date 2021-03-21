<template>
  <div id="nav-bar">
    <el-menu
      mode="horizontal"
      class="el-menu-demo"
      text-color="#E6A23C"
      background-color="#324157"
      router="true"
      @select="handleSelect"
      active-text-color="#F56C6C"
      menu-trigger="hover"
    >
      <el-menu-item index="/home">
        <img src="@/assets/img/logo.png" alt="" />
      </el-menu-item>
      <el-menu-item></el-menu-item>
      <el-menu-item index="/home">首页</el-menu-item>
      <el-menu-item index="/ranklist">排行榜</el-menu-item>
      <el-menu-item index="/search">UP搜索</el-menu-item>
      <el-menu-item index="/searchV">视频搜索</el-menu-item>
    </el-menu>
    <div class="nav-user">
      <div v-if="$store.getters.isLogin">
        <login-nav-bar></login-nav-bar>
      </div>
      <div v-else>
        <un-login-nav-bar></un-login-nav-bar>
      </div>
    </div>
  </div>
</template>

<script>
import LoginNavBar from 'commons/nav-bar/LoginNavBar.vue'
import UnLoginNavBar from 'commons/nav-bar/UnLoginNavBar.vue'

export default {
  components: { LoginNavBar, UnLoginNavBar },
  name: "NavBar",
  methods: {
  },
  data () {
    return {
    }
  },
  computed: {
    isLogin () {
      return this.$store.state.isLogin
    }
  }
}
</script>

<style scoped>
@import "~@/assets/css/navbar.css";
.el-menu--horizontal > .el-menu-item.is-active {
  border-bottom: none;
}
.el-menu-item {
  transition: none;
  font-size: 1.1em;
}
.nav-user {
  height: 61px;
  background-color: #324157;
  border-bottom: solid 1px #e6e6e6;
  display: flex;
  align-content: center;
}
</style>
