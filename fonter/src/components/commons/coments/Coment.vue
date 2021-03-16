<template>
  <div>
    <div class="touch_icon">
      <div class="like" @click="favorite_click">
        <img
          v-if="touch['favorite']"
          src="~assets/img/online-icons/favorite_touch.svg"
          alt=""
        />
        <img v-else src="~assets/img/online-icons/favorite_untouch.svg" />
        {{ number["favorite"] }}
      </div>
      <div class="like" @click="trend_click" v-if="isShowTrend">
        <img
          v-if="touch['trend']"
          src="~assets/img/online-icons/trend_red.svg"
          alt=""
        />
        <img v-else src="~assets/img/online-icons/trend.svg" />
      </div>
      <div class="like" @click="like_click">
        <img
          v-if="touch['reply']"
          src="~assets/img/online-icons/reply_touch.svg"
          alt=""
        />
        <img v-else src="~assets/img/online-icons/reply_untouch.svg" />
        {{ number["reply"] }}
      </div>
    </div>
    <div class="hidden_content" ref="liCon">
      <div class="userReply">
        <img src="~assets/img/online/default.png" alt="" />
        <el-input
          v-model="myReply"
          type="textarea"
          rows="4"
          resize="none"
          placeholder="请输入您的评论"
          class="reply_input"
        >
        </el-input>
        <el-button type="primary" class="reply_button" @click="subReply"
          >发表评论</el-button
        >
      </div>
      <div :key="key">
        <div v-for="item in replys" :key="item">
          <reply
            :reply="item"
            :comment_id="comment_data['comment_id']"
            @deleteReply="updatePage"
          ></reply>
        </div>
      </div>
    </div>
    <div class="hidden_content" ref="showTrend" v-if="isShowTrend">
      <video-trend
        :echartsBase_id="videoID"
        echartsBase_height="600px"
        echartsBase_width="1000px"
        :echartsBase_data="data"
      ></video-trend>
    </div>
  </div>
</template>

<script>
import { ElMessage } from 'element-plus'
import { ref } from 'vue'
import VideoTrend from '@/components/content/VideoTrend/VideoTrend.vue'
import Reply from './Reply.vue'
import { PostComment} from '@/network/get_bili.js'

export default {
  name: "Coments",
  components: {
    Reply,
    VideoTrend
  },
  props: {
    isShowTrend: false,
    videoID: String,
    comment_echarts_data: {
      type: Object
    },
    comment_data: {
      type: Object
    }
  },
  data () {
    return {
      key: 0,
      data: this.comment_echarts_data,
      screenWidth: document.body.clientWidth * 0.7,
      touch: {
        favorite: this.comment_data['is_like'],
        reply: 0,
        trend: false,
      },
      number: {
        favorite: this.comment_data['web_like'],
        reply: this.comment_data['web_reply'],
      },
      replys: this.comment_data['replys'],
      myReply: ref(''),
      liConHeight: 0, // 折叠面板内容初始高度
    }
  },
  computed: {
    VideoWidth () {
      return Math.max(700, this.screenWidth) + 'px'
    }
  },
  methods: {
    favorite_click () {
        if (this.$store.state.token == '') {
          ElMessage.error('请先登录')
          return
        }
      this.touch['favorite'] = !this.touch['favorite']
      if (this.touch['favorite']) {
        this.number['favorite']++

        let data = {
          favorite: this.number['favorite'],
          reply: this.number['reply'],
          token: this.$store.state.token,
          comment_id: this.comment_data['comment_id'],
          is_like: 1,
          type: 'comment'
        }
        PostComment(data).then(res => {
          if (res['code'] == 200) {
            ElMessage.success({
              message: res['msg'],
              type: 'success'
            })
          } else {
            ElMessage.error(res['msg'])
          }
        })
      } else {
        if (this.$store.state.token == '') {
          ElMessage.error('请先登录')
          return
        }
        this.number['favorite']--
        let data = {
          favorite: this.number['favorite'],
          reply: this.number['reply'],
          token: this.$store.state.token,
          comment_id: this.comment_data['comment_id'],
          is_like: 0,
          type: 'comment'
        }
        PostComment(data).then(res => {
          if (res['code'] == 200) {
            ElMessage.success({
              message: res['msg'],
              type: 'success'
            })
          } else {
            ElMessage.error(res['msg'])
          }
        })
      }
    },
    like_click () {
      this.touch['reply'] = !this.touch['reply']
      const liCon = this.$refs.liCon
      let height = liCon.offsetHeight
      if (this.touch['reply']) {
        if (this.touch['trend']) {
          this.trend_click()
        }
        if (height === this.liConHeight) { // 展开
          liCon.style.height = 'auto'
          height = liCon.offsetHeight
          liCon.style.height = this.liConHeight + 'px'
          // eslint-disable-next-line no-unused-vars
          let f = document.body.offsetHeight // 必加
          liCon.style.height = height + 'px'
        } else { // 收缩
          liCon.style.height = this.liConHeight + 'px'
        }
      } else {
        if (height === this.liConHeight) { // 展开
          liCon.style.height = 'auto'
          height = liCon.offsetHeight
          liCon.style.height = this.liConHeight + 'px'
          // eslint-disable-next-line no-unused-vars
          let f = document.body.offsetHeight // 必加
          liCon.style.height = height + 'px'
        } else { // 收缩
          liCon.style.height = this.liConHeight + 'px'
        }
      }
    },
    trend_click () {
      this.touch['trend'] = !this.touch['trend']
      const liCon = this.$refs.showTrend
      let height = liCon.offsetHeight
      if (this.touch['trend']) {
        if (this.touch['reply']) {
          this.like_click()
        }
        if (height === this.liConHeight) { // 展开
          liCon.style.height = 'auto'
          height = liCon.offsetHeight
          liCon.style.height = this.liConHeight + 'px'
          // eslint-disable-next-line no-unused-vars
          let f = document.body.offsetHeight // 必加
          liCon.style.height = height + 'px'
        } else { // 收缩
          liCon.style.height = this.liConHeight + 'px'
        }
      } else {
        if (height === this.liConHeight) { // 展开
          liCon.style.height = 'auto'
          height = liCon.offsetHeight
          liCon.style.height = this.liConHeight + 'px'
          // eslint-disable-next-line no-unused-vars
          let f = document.body.offsetHeight // 必加
          liCon.style.height = height + 'px'
        } else { // 收缩
          liCon.style.height = this.liConHeight + 'px'
        }
      }

    },
    subReply () {
      this.number['reply']++
      let reply_id = this.getRandId()
      let data = {
        reply_content: this.myReply,
        token: this.$store.state.token,
        comment_id: this.comment_data['comment_id'],
        type: 'reply',
        reply_id: reply_id
      }
      if (this.$store.state.token == '') {
        ElMessage.error('请先登录')
        return
      }
      PostComment(data).then(res => {
        console.log(res)
        if (res['code'] == 200) {
          ElMessage.success({
            message: res['msg'],
            type: 'success'
          })
          let time = new Date()
          Date.prototype.toLocaleString = function () {   // 重写日期函数格式化日期
              return `${this.getFullYear()}-${this.getMonth() + 1 >= 10 ? (this.getMonth() + 1) : '0' + (this.getMonth() + 1)}-${this.getDate() >= 10 ? this.getDate() : '0' + this.getDate()} ${this.getHours() >= 10 ? this.getHours() : '0' + this.getHours()}:${this.getMinutes() >= 10 ? this.getMinutes() : '0' + this.getMinutes()}:${this.getSeconds() >= 10 ? this.getSeconds() : '0' + this.getSeconds()}`;
          };
          this.replys.unshift({
            img: 'https://t7.baidu.com/it/u=1595072465,3644073269&fm=193&f=GIF',
            name: this.$store.state.name,
            msg: this.myReply,
            like: 0,
            dislike: 0,
            reply_id: reply_id,
            reply_time: time.toLocaleString()
          })
          this.myReply = ref('')
          this.key += 1
          this.like_click()
          setTimeout(() => {
            this.like_click()
          }, 500)
        } else {
          ElMessage.error(res['msg'])
        }
      })
      data = {
        favorite: this.number['favorite'],
        reply: this.number['reply'],
        token: this.$store.state.token,
        comment_id: this.comment_data['comment_id'],
        is_like: this.touch['favorite'] == true ? 1 : 0,
        type: 'comment'
      }
      PostComment(data).then(res => {
      })

    },
    getRandId () {
      return 'xxxxxxxx-xxxx-4xxx-yxxx-xxxxxxxxxxxx'.replace(/[xy]/g, function (c) {
        var r = Math.random() * 16 | 0,
          v = c == 'x' ? r : (r & 0x3 | 0x8)
        return v.toString(16)
      })
    },
    updatePage (id) {
      for (let idx in this.replys) {
        if (this.replys[idx]['reply_id'] == id) {
          this.replys.splice(idx, 1)
          break
        }
      }
      this.number['reply']--
    }
  },
  mounted () {
    window.onresize = () => {
      return (() => {
        this.screenWidth = document.body.clientWidth * 0.7
      })()
    }
  }
}
</script>

<style scoped>
@import "~@/assets/css/component/comments/comments.css";
</style>