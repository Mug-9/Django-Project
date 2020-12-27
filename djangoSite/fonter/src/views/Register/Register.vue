<template>
  <div class="form-div">
    <el-form
      :model="form"
      ref="form"
      status-icon
      :rules="rules"
      label-width="80px"
      class="form-el"
    >
      <el-form-item label="账号" prop="account">
        <el-input v-model="form.account" autocomplete="off"></el-input>
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
        <el-button type="primary" @click="submitForm('form')">注册</el-button>
        <el-button>取消</el-button>
      </el-form-item>
    </el-form>
  </div>
</template>

<script>
import { formRegister } from 'network/register.js'
export default {
  name: "Register",
  data () {
    var validataAccount = (rule, value, callback) => {
      if (value == '') {
        callback(new Error("账号不能为空"))
      } else {
        callback()
      }
    }
    var validataPassword = (rule, value, callback) => {
      if (value == '') {
        callback(new Error("请输入密码"))
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
      rules: {
        account: [
          { validator: validataAccount, trigger: 'blur' }
        ],
        password: [
          { validator: validataPassword, trigger: 'blur' }
        ],
        passwordAgain: [
          { validator: validataPasswordAgain, trigger: 'blur' }
        ]
      }
    }
  },
  methods: {
    submitForm (formName) {
      this.$refs[formName].validate((valid) => {
        if (valid) {
          alert('submit!')
          let formData = new FormData()
          for (let key in this.form) {
            formData.append(key, this.form[key])
          }
          formRegister(formData).then(res => {
            console.log(res)
          })
        } else {
          console.log('error submit!')
          return false
        }
      })

    }
  }

}
</script>

<style scoped>
.form-div {
  display: flex;
  justify-content: center; /* 水平居中 */
  align-items: center; /* 垂直居中 */
}
.form-el {
  padding-top: 100px;
  width: 500px;
}
</style>