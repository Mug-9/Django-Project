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
      <div>测试111</div>
      <div>测试111</div>
      <div>测试111</div>
      <div>测试111</div>
      <div>测试111</div>
      <div>测试111</div>
      <div>测试111</div>
      <div>测试111</div>
    </div>
  </div>
</template>

<script>
export default {
  name: "Coments",
  data () {
    return {
      touch: {
        favorite: false,
        reply: false,
      },
      number: {
        favorite: 0,
        reply: 0,
      },
      liConHeight: 0, // 折叠面板内容初始高度
      proLists: [
        {
          name: '测试1',
        },
        {
          name: '测试2',
        },
      ],
    }
  },
  methods: {
    favorite_click () {
      this.touch['favorite'] = true
      this.touch['reply'] = false
    },
    like_click () {
      this.touch['favorite'] = false
      this.touch['reply'] = true
      const liCon = this.$refs.liCon
      console.log(liCon)
      let height = liCon.offsetHeight
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
    },


  },
  mounted () {
  }
}
</script>

<style scoped>
@import "~@/assets/css/component/comments/comments.css";
</style>