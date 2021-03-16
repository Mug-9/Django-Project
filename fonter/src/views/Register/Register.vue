<template>
  <div class="main">
    <div class="login-div">
      <div class="welcome-div">Welcome!</div>
      <div class="form-div">
        <el-form
          :model="form"
          ref="form"
          status-icon
          :rules="rules"
          label-width="8em"
          class="form-el"
        >
          <el-form-item label="邮箱" prop="account">
            <el-input
              type="email"
              v-model="form.account"
              autocomplete="off"
            ></el-input>
          </el-form-item>
          <el-form-item label="密码" prop="password">
            <el-input
              type="password"
              v-model="form.password"
              autocomplete="off"
            ></el-input>
          </el-form-item>
          <el-form-item label="重复密码" prop="passwordAgain">
            <el-input
              type="password"
              v-model="form.passwordAgain"
              autocomplete="off"
            ></el-input>
          </el-form-item>
          <el-form-item>
            <el-button type="primary" @click="submitForm('form')"
              >注册</el-button
            >
            <el-button @click="cancelForm('form')">取消</el-button>
          </el-form-item>
        </el-form>
      </div>
    </div>
  </div>
</template>

<script>  
import { ElMessage } from 'element-plus'
import { formRegister } from 'network/register.js'
import * as func from '@/store/mutations-type.ts'

export default {
  name: "Register",
  data () {
    var validataAccount = (rule, value, callback) => {
      console.log(this.form)
      if (value == '') {
        callback(new Error("账号不能为空"))
      } else if (this.formCheck.emailExits) {
        callback(new Error('账号已存在'))
        this.formCheck.emailExits = false
      } else {
        callback()
      }
    }
    var validataPassword = (rule, value, callback) => {
      if (value == '') {
        callback(new Error("请输入密码"))
      } else if (value.length <= 6) {
        callback(new Error('密码长度应该不短于6'))
      } else if (value.length >= 20) {
        callback(new Error('密码长度应该不长于20'))
      } else {
        if (this.form.passwordAgain != '') {
          this.$refs.form.validateField('check pass')
        }
        callback()
      }
    }
    var validataPasswordAgain = (rule, value, callback) => {
      if (value == '') {
        callback(new Error("请再次输入密码"))
      } else if (value != this.form.password) {
        callback(new Error("两次密码不一致"))
      } else {
        callback()
      }
    }
    return {
      form: {
        account: '',
        password: '',
        passwordAgain: '',
      },
      formCheck: {
        accountExits: false
      },
      rules: {
        account: [
          { validator: validataAccount, trigger: 'change' },
          { required: true, whitespace: true }
        ],
        password: [
          { validator: validataPassword, trigger: 'change' },
          { required: true, whitespace: true }
        ],
        passwordAgain: [
          { validator: validataPasswordAgain, trigger: 'change' },
          { required: true, whitespace: true }
        ]
      }
    }
  },
  methods: {
    submitForm (formName) {
      this.$refs[formName].validate((valid) => {
        if (valid) {
          let formData = new FormData()
          let account_tmp = this.form.account
          let data = {
            account: this.form.account,
            password: this.form.password
          }
          this.form.account = account_tmp + ' '
          formRegister(data).then(res => {
            this.form.account = account_tmp
            if (res == "账号已存在!") {
              ElMessage.error(res)
              this.formCheck.accountExits = true
            } else if (res == "注册成功!") {
              ElMessage.success({
                message: res,
                type: 'success'
              })
              this.$store.commit(func.SETEMAIL, this.form.account)
              this.$store.commit(func.SETPASSWORD, this.form.password)
              this.$store.commit(func.SETACCOUNT, this.form.account)
              this.$router.replace('/login')
            }
          })
        } else {
          console.log('error submit!')
          return false
        }
      })
    },
    cancelForm (formName) {
      this.$refs[formName].resetFields()
    }
  }

}
</script>

<style scoped>
@import "~@/assets/css/register.css";
</style>
