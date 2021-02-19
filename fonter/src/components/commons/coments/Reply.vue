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
        <span>{{ reply["time"] }}</span>
        <div class="like_unlike" @click="likeClick">
          <img
            v-if="like"
            src="~assets/img/online-icons/like2_touch.svg"
            alt=""
          />
          <img v-else src="~assets/img/online-icons/like2_untouch.svg" alt="" />
          {{ reply["like"] }}
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
          {{ reply["dislike"] }}
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "Reply",
  data () {
    return {
      like: false,
      unlike: false,
    }
  },
  props: {
    reply: {
      type: Object,
    }
  },
  methods: {
    likeClick () {
      this.like = true
      this.unlike = false
    },
    unlikeClick () {
      this.like = false
      this.unlike = true
    }
  },
  mounted () {
  }
}
</script>

<style scoped>
@import "~@/assets/css/component/comments/reply.css";
</style>