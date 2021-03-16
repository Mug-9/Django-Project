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
          <el-form-item label="账号" prop="account">
            <el-input v-model="rulerForm.account" autocomplete="off"></el-input>
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
import { formLogin, getToken } from 'network/login.js'
import * as func from '@/store/mutations-type.ts'
export default {
  name: "Login",
  inject: ['Cookies'],
  data () {
    var validataAccount = (rule, value, callback) => {
      if (value === '') {
        callback(new Error("账号不能为空"))
      } else if (this.formCheck.accountNotExist) {
        callback(new Error("账号不存在"))
        this.formCheck.accountNotExist = false
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
        account: this.$store.state.account,
        password: this.$store.state.password,
      },
      formCheck: {
        accountNotExist: false,
        passwordWrong: false,
      },
      rules: {
        account: [
          { validator: validataAccount, trigger: 'change' },
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
      let account_tmp = this.rulerForm.account
      let password_tmp = this.rulerForm.password
      let data = {
        account: account_tmp,
        password: password_tmp
      }
      console.log(data);
      this.rulerForm.account = account_tmp + ' '
      this.rulerForm.password = password_tmp.slice(1) + ' '
      formLogin(data).then(res => {
        console.log(res)
        this.rulerForm.account = account_tmp
        this.rulerForm.password = password_tmp

        if (res.message == "账户不存在") {
          ElMessage.error(res.message)
          this.formCheck.emailNotExist = true
          this.rulerForm.account = account_tmp
        } else if (res.message == "密码错误") {
          ElMessage.error(res.message)
          this.formCheck.passwordWrong = true
          this.rulerForm.password = password_tmp
        } else {
          localStorage.setItem('token', res.token)
          let date = new Date()
          date.setDate(date.getDate() + 14)
          localStorage.setItem('expires', JSON.stringify(date))
          this.$store.commit(func.SETTOKEN, res.token)
          this.$store.commit(func.SETACCOUNT, res.data['account'])
          this.$store.commit(func.SETEMAIL, res.data['email'])
          this.$store.commit(func.SETNAME, res.data['name'])
          this.$store.commit(func.SETPASSWORD, this.rulerForm.password)
          ElMessage.success({
            message: res.message,
            type: 'success'
          })
          this.$router.replace('/home')
        }
      })
    },
    cancelLogin (formName) {
      this.$refs[formName].resetFields()
      this.$router.push('/home')
    },
  },
}
</script>

<style scoped>
@import "~@/assets/css/login.css";
</style>