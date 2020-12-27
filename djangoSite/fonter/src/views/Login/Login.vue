<template>
  <div>
    <el-form :model="form" label-width="80px">
      <el-form-item label="账号">
        <el-input v-model="form.account"></el-input>
      </el-form-item>
      <el-form-item label="密码">
        <el-input v-model="form.password"></el-input>
      </el-form-item>
      <el-form-item>
        <el-button type="primary" @click="formLogin">登录</el-button>
        <el-button>取消</el-button>
      </el-form-item>
    </el-form>
  </div>
</template>

<script>
import { formLogin } from 'network/login.js'
export default {
  name: "Login",
  data () {
    return {
      form: {
        account: '',
        password: '',
      }
    }
  },
  methods: {
    formLogin () {
      let formData = new FormData()
      for (let key in this.form) {
        formData.append(key, this.form[key])
      }
      formLogin(formData).then(res => {
        console.log(res)
      })
    }
  }
}
</script>

<style scoped>
</style>