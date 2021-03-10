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
          :value="userReply"
          type="textarea"
          rows="4"
          resize="none"
          placeholder="请输入您的评论"
          class="reply_input"
        >
        </el-input>
        <el-button type="primary" class="reply_button">发表评论</el-button>
      </div>
      <div>
        <reply :reply="reply_data"></reply>
        <reply :reply="reply_data"></reply>
        <reply :reply="reply_data"></reply>
        <reply :reply="reply_data"></reply>
      </div>
    </div>
    <div class="hidden_content" ref="showTrend"></div>
  </div>
</template>

<script>
import Reply from './Reply.vue'
export default {
  name: "Coments",
  components: {
    Reply,
  },
  props: {
    isShowTrend: false
  },
  data () {
    return {

      screenWidth: document.body.clientWidth * 0.7,
      touch: {
        favorite: false,
        reply: false,
        trend: false,
      },
      number: {
        favorite: 0,
        reply: 0,
      },
      reply_data: {
        img: 'https://t7.baidu.com/it/u=1595072465,3644073269&fm=193&f=GIF',
        name: 'abcd',
        msg: 'adgasdfasdfas',
        time: '4分钟',
        like: 4,
        dislike: 5,
      },
      userReply: '',
      liConHeight: 0, // 折叠面板内容初始高度
    }
  },
  computed: {
    baiduIndexWidth () {
      return Math.max(700, this.screenWidth) + 'px'
    }
  },
  methods: {
    favorite_click () {
      this.touch['favorite'] = !this.touch['favorite']
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
        liCon.style.height = this.liConHeight + 'px'
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