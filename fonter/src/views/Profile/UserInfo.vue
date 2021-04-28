<template>
  <div class="user_info">
    <div class="user_img">
      <img src="~@/assets/img/online/default.png" />
      <div class="upload-demo" v-if="changeImg">
        <el-upload
          drag
          action="https://jsonplaceholder.typicode.com/posts/"
          multiple
        >
          <i class="el-icon-upload"></i>
          <div class="el-upload__text">将文件拖到此处，或<em>点击上传</em></div>
          <template #tip>
            <div class="el-upload__tip">
              只能上传 jpg/png 文件，且不超过 500kb
            </div>
          </template>
        </el-upload>
        <el-button type="primary">确定</el-button>
        <el-button type="primary" @click="showChange">取消</el-button>
      </div>

      <el-button
        v-if="!changeImg"
        @click="showChange"
        type="primary"
        class="changeImgButton"
        >更改头像</el-button
      >
    </div>
    <div class="info">
      <div class="nickName">
        昵称：
        <el-input
          class="nameInput"
          v-model="userName"
          placeholder="请输入内容"
          maxlength="10"
        ></el-input>
      </div>
      <div class="account">账号：{{ account }}</div>
      <div class="account">
        性别：
        <el-radio v-model="sex" label="male">男</el-radio>
        <el-radio v-model="sex" label="female">女</el-radio>
      </div>
      <div class="password">
        密码：
        <el-input
          class="nameInput"
          v-model="password"
          placeholder="请输入内容"
          maxlength="20"
          show-password
        ></el-input>
      </div>
      <div class="email">
        邮箱：
        <el-input
          class="nameInput"
          v-model="email"
          placeholder="请输入内容"
          maxlength="20"
        ></el-input>
      </div>
    </div>
    <el-button class="saveButton" type="primary" @click="saveChange"
      >保存</el-button
    >
  </div>
</template>

<script>
import { ElMessage } from 'element-plus'
import { updateStore } from 'network/login.js'
export default {
  name: "UserInfo",
  data () {
    return {
      sex: 'male',
      userName: this.$store.state.name,
      account: this.$store.state.account,
      password: this.$store.state.password,
      email: this.$store.state.email,
      changeImg: false
    }
  },
  methods: {
    showChange () {
      this.changeImg = !this.changeImg
    },
    saveChange () {
      let data = {
        'token': this.$store.state.token,
        'data': {
          'nickName': this.userName,
          'account': this.account,
          'password': this.password,
          'email': this.email
        }
      }
      updateStore(data).then(res => {
        if (res['code'] == 200) {
          ElMessage.success({
            message: res.message,
            type: 'success'
          })
        } else {
          ElMessage.error(res.message)
        }
      })
    }
  },
  mounted () {
  }

}
</script>

<style scoped>
.changeImgButton {
  height: 50px;
  margin: auto 20px;
}
.saveButton {
  width: 120px;
  height: 40px;
  margin: 20px 30%;
}

.user_img {
  display: flex;
  margin: 50px 20%;
  text-align: center;
}
.nickName {
  display: flex;
  font-size: 1.3em;
  line-height: 2em;
  width: 25em;
  margin: 10px 20%;
}

.password {
  display: flex;
  font-size: 1.3em;
  line-height: 2em;
  width: 25em;
  margin: 10px 20%;
}

.account {
  margin: 10px 20%;
  font-size: 1.3em;
  line-height: 2em;
}

.email {
  display: flex;
  font-size: 1.3em;
  line-height: 2em;
  width: 25em;
  margin: 10px 20%;
}

.nameInput {
  width: 20em;
}

.user_img img {
  width: 300px;
  height: 300px;
  border-radius: 50%;
}
.upload-demo {
  margin: auto 30px;
}
</style>