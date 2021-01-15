<template>
  <div class="user-avatar">
    <el-dropdown>
      <el-avatar
        @click="itemClick"
        :size="52"
        src="https://cube.elemecdn.com/3/7c/3ea6beec64369c2642b92c6726f1epng.png"
        class="el-avatar"
      ></el-avatar>
      <template #dropdown>
        <el-dropdown-menu>
          <el-dropdown-item @click="profileClick">个人信息</el-dropdown-item>
          <el-dropdown-item @click="storeClick">收藏</el-dropdown-item>
          <el-dropdown-item @click="logClick">记录</el-dropdown-item>
          <el-dropdown-item @click="logoutClick">退出</el-dropdown-item>
        </el-dropdown-menu>
      </template>
    </el-dropdown>
    <i @click="messageClick">
      <img src="~assets/img/message.svg" alt="" />
    </i>
  </div>
</template>

<script>

import * as func from '@/store/mutations-type.ts'
export default {
  name: "login-nav-bar",
  methods: {
    profileClick () {
      this.$router.push('/profile')
    },
    storeClick () {
      this.$router.push('/sotre')
    },
    logClick () {
      this.$router.push('/log')
    },
    logoutClick () {
      window.localStorage.clear()
      this.$store.commit(func.CLEARTOKEN)
      this.$router.push('/home')
    },
    messageClick () {
      this.$router.push('/message')
    }
  }
}
</script>

<style scoped>
.user-avatar {
  margin-right: 2em;
  margin-top: 8px;
  display: flex;
  align-content: center;
}
.user-avatar img {
  width: 27px;
  height: 27px;
  margin-top: 20px;
}
.el-avatar {
  margin-right: 2em;
}
</style>
