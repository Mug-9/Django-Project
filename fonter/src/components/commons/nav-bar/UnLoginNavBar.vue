<template>
  <div class="nav-bar-item">
    <div class="nav-avatar">
      <el-avatar @click="itemClick" :size="52" src=""></el-avatar>
    </div>
    <div class="login_register">
      <el-button type="primary" round @click="loginClick">登录</el-button>
      <el-button type="warning" round @click="registerClick">注册</el-button>
    </div>
  </div>
</template>

<script>
import { ElMessage } from 'element-plus'

export default {
  name: "nav-user",
  props: {
    width: {
      type: String,
      defalut: "240px"
    }
  },
  data () {
    return {
      path: '/profile'
    }
  },
  computed: {
  },
  methods: {
    itemClick () {
      console.log('item click')
      if (this.$store.isLogin) {

      } else {
        ElMessage.error('请先登录')
      }
    },
    loginClick () {
      this.$router.push('/login')
    },
    registerClick () {
      this.$router.push('/register')
    }
  }

}
</script>

<style scoped>
.login_register {
  display: inline-flex;
  justify-content: center;
  align-items: center;
}
.login_register button {
  height: 2.5em;
  margin: auto 7px;
  font-size: 1em;
}
.nav-bar-item {
  margin-top: 4px;
  display: flex;
  align-content: center;
}
.nav-avatar {
  display: inline-flex;
  height: 100%;
}
</style>
