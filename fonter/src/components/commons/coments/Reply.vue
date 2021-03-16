<template>
  <div class="reply-item">
    <img :src="reply['img']" alt="" />
    <div class="reply_content">
      <div class="user_name">
        {{ reply["name"] }}
      </div>
      <div class="text">
        {{ reply["msg"] }}
      </div>
      <div class="time_like">
        <div class="like_unlike" @click="likeClick">
          <img
            v-if="like"
            src="~assets/img/online-icons/like2_touch.svg"
            alt=""
          />
          <img v-else src="~assets/img/online-icons/like2_untouch.svg" alt="" />
          {{ like_count }}
        </div>
        <div class="like_unlike" @click="unlikeClick">
          <img
            v-if="unlike"
            src="~assets/img/online-icons/unlike_touch.svg"
            alt=""
          />
          <img
            v-else
            src="~assets/img/online-icons/unlike_untouch.svg"
            alt=""
          />
          {{ dislike_count }}
        </div>
        <div @click="deleteReply" class="like_unlike" v-if="isUser">删除</div>
      </div>
      <div class="reply_time">
        {{ reply["reply_time"] }}
      </div>
    </div>
  </div>
</template>

<script>
import { ElMessage } from 'element-plus'
import { PostComment } from '@/network/get_bili.js'
export default {
  name: "Reply",
  data () {
    return {
      like_count: this.reply['like'],
      dislike_count: this.reply['dislike'],
      like: this.reply['is_like'],
      unlike: this.reply['is_dislike'],
    }
  },
  props: {
    reply: {
      type: Object,
    },
    comment_id: String
  },
  computed: {
    isUser () {
      return this.$store.state.account == this.reply['user_account']
    }
  },
  methods: {
    likeClick () {
      if (this.$store.state.token == '') {
        ElMessage.error('请先登录')
        return
      }
      if (this.like) {
        this.like = false
        this.like_count--
        this.update('unlike')
      } else {
        if (this.unlike) {
          this.unlike = false
          this.dislike_count--
        }
        this.like = true
        this.like_count++
        this.update('like')
      }
    },
    unlikeClick () {
      if (this.$store.state.token == '') {
        ElMessage.error('请先登录')
        return
      }
      if (this.unlike) {
        this.unlike = false
        this.dislike_count--
        this.update('undislike')
      } else {
        if (this.like) {
          this.like = false
          this.like_count--
        }
        this.unlike = true
        this.dislike_count++
        this.update('dislike')
      }
    },
    update (type) {
      let data = {
        is_like: this.like == true ? 1 : 0,
        is_dislike: this.unlike == true ? 1 : 0,
        like_count: this.like_count,
        dislike_count: this.dislike_count,
        reply_id: this.reply['reply_id'],
        token: this.$store.state.token,
        comment_id: this.comment_id,
        type: type
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
        } else {
          ElMessage.error(res['msg'])
        }
      })
    },
    deleteReply () {
      let data = {
        reply_id: this.reply['reply_id'],
        token: this.$store.state.token,
        comment_id: this.comment_id,
        type: 'delete'
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
          this.$emit('deleteReply', this.reply['reply_id'])
        } else {
          ElMessage.error(res['msg'])
        }
      })
    }
  },
  mounted () {
  }
}
</script>

<style scoped>
@import "~@/assets/css/component/comments/reply.css";
</style>