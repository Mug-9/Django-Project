<template>
  <div class="main">
    <div class="login-div">
      <div class="welcome-div">Welcome!</div>
      <div class="form-div">
        <el-form
          :model="rulerForm"
          label-width="4em"
          class="form-el"
          :rules="rules"
          status-icon
          ref="rulerForm"
        >
          <el-form-item label="账号" prop="email">
            <el-input v-model="rulerForm.email" autocomplete="off"></el-input>
          </el-form-item>
          <el-form-item label="密码" prop="password">
            <el-input
              type="password"
              v-model="rulerForm.password"
              autocomplete="off"
            ></el-input>
          </el-form-item>
          <el-form-item>
            <el-button type="primary" @click="formLogin">登录</el-button>
            <el-button @click="cancelLogin('rulerForm')">取消</el-button>
          </el-form-item>
        </el-form>
      </div>
    </div>
  </div>
</template>

<script>
import { ElMessage } from 'element-plus'
import { formLogin } from 'network/login.js'
export default {
  name: "Login",
  data () {
    var validataEmail = (rule, value, callback) => {
      console.log(this.rulerForm)
      if (value === '') {
        callback(new Error("账号不能为空"))
      } else if (this.formCheck.emailNotExist) {
        callback(new Error("账号不存在"))
        this.formCheck.emailNotExist = false
      } else {
        callback()
      }
    }
    var validataPassword = (rule, value, callback) => {
      if (value === '') {
        callback(new Error('密码不能为空'))
      } else if (this.formCheck.passwordWrong) {
        callback(new Error("密码错误"))
        this.formCheck.passwordWrong = false
      } else {
        callback()
      }
    }
    return {
      rulerForm: {
        email: this.$store.state.email,
        password: this.$store.state.password,

      },
      formCheck: {
        emailNotExist: false,
        passwordWrong: false,
      },
      rules: {
        email: [
          { validator: validataEmail, trigger: 'change' },
          { required: true, whitespace: true }
        ],
        password: [
          { validator: validataPassword, trigger: 'change' },
          { required: true, whitespace: true }
        ]
      }
    }
  },
  methods: {
    formLogin () {
      let formData = new FormData()
      let email_tmp = this.rulerForm.email
      let password_tmp = this.rulerForm.password
      for (let key in this.rulerForm) {
        formData.append(key, this.rulerForm[key])
      }
      console.log(formData)
      this.rulerForm.email = email_tmp + ' '
      this.rulerForm.password = password_tmp.slice(1) + ' '
      formLogin(formData).then(res => {
        console.log(res)
        this.rulerForm.email = email_tmp
        this.rulerForm.password = password_tmp
        if (res == "账户不存在") {
          ElMessage.error(res)
          this.formCheck.emailNotExist = true
          this.rulerForm.email = email_tmp
        } else if (res == "密码错误") {
          ElMessage.error(res)
          this.formCheck.passwordWrong = true
          this.rulerForm.password = password_tmp
        } else {
          ElMessage.success({
            message: res,
            type: 'success'
          })
          this.$store.state.isLogin = true
          this.$router.replace('/home')
        }
      })
    },
    cancelLogin (formName) {
      this.$refs[formName].resetFields()
      this.$router.push('/home')
    }
  }
}
</script>

<style scoped>
@import "~@/assets/css/login.css";
</style>