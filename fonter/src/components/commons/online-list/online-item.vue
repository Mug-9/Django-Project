<template>
  <div class="online-item">
    <div class="slot-img">
      <slot name="slot-img">
        <img src="~@/assets/img/online/default.png" alt="" />
      </slot>
      <div class="div-duration">
        <slot name="duration"></slot>
      </div>
    </div>
    <div class="slot-items">
      <div class="div-title">
        <slot name="item-title"></slot>
      </div>
      <div class="tname_bv">
        <div class="div-bv">
          <slot name="item-bv"></slot>
        </div>
        <div class="div-tname">
          <slot name="item-tname"></slot>
        </div>
      </div>
      <div class="author-time">
        <div class="div-author">
          <slot name="item-author"> </slot>
        </div>
        <div class="pubupdate">
          <img src="~@/assets/img/online-icons/time.svg" alt="" />
          <slot name="pubupdate"></slot>
        </div>
      </div>
      <slot name="item-desc"></slot>

      <div class="div-view">
        <img src="~@/assets/img/online-icons/view.svg" alt="" />
        <slot name="item-view"></slot>
      </div>
      <div class="like_coin_favorite">
        <div class="div-like">
          <img src="~@/assets/img/online-icons/like.svg" alt="" />
          <slot name="item-like"></slot>
        </div>
        <div class="div-coin">
          <img src="~@/assets/img/online-icons/coin.svg" alt="" />
          <slot name="item-coin"></slot>
        </div>
        <div class="div-favorite">
          <img src="~@/assets/img/online-icons/favorite.svg" alt="" />
          <slot name="item-favorite"></slot>
        </div>
      </div>
      <div class="reply-danmu_share">
        <div class="div-reply">
          <img src="~@/assets/img/online-icons/reply.svg" alt="" />
          <slot name="item-reply"></slot>
        </div>
        <div class="div-danmu">
          <img src="~@/assets/img/online-icons/danmu.svg" alt="" />

          <slot name="item-danmu"></slot>
        </div>
        <div class="div-share">
          <img src="~@/assets/img/online-icons/share.svg" alt="" />
          <slot name="item-share"></slot>
        </div>
      </div>
      <slot name="item-online"></slot>
    </div>
  </div>
  <div>
    <comments
      :isShowTrend="true"
      :videoID="videoBV"
      :comment_echarts_data="videoData"
      :comment_data="commentData"
    ></comments>
  </div>
</template>

<script>

import Comments from '@/components/commons/coments/Coment.vue'
export default {
  name: "online-item",
  data () {
    return {
    }
  },
  props: {
    videoBV: String,
    videoData: {
      type: Object
    },
    commentData: {
      type: Object
    }
  },
  components: {
    Comments,
  },
  methods: {
  },
  computed: {
  },
  mounted () {
  }
}
</script>

<style scoped>
@import "~@/assets/css/component/online_item/online_item.css";
</style>