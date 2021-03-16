<template>
  <div
    v-loading="onlineItems['loading']"
    element-loading-spinner="el-icon-loading"
    element-loading-background="rgba(0, 0, 0, 0.8)"
    element-loading-text="拼命加载中"
  >
    <div v-for="item in onlineItems['list']" :key="item">
      <online-item :videoBV="item['bvid']" :videoData="item['echarts_data']" :commentData="item['comment']">
        <template v-slot:slot-img>
          <a :href="get_url(item)"><img :src="item['pic']" alt="" /></a>
        </template>
        <template v-slot:item-title>
          <p>{{ item["title"] }}</p>
        </template>
        <template v-slot:item-bv>
          <el-link type="primary" :href="get_url(item)" :underline="false">
            {{ item["bvid"] }}</el-link
          >
        </template>
        <template v-slot:item-desc>
          <el-input
            type="textarea"
            :autosize="{ minRows: 2, maxRows: 2 }"
            v-model="item['desc']"
            :disabled="true"
          >
          </el-input>
        </template>
        <template v-slot:item-author>
          <a href=""></a><img :src="item['owner']['face']" alt="" />
          {{ item["owner"]["name"] }}
        </template>
        <template v-slot:item-coin>:{{ item["stat"]["coin"] }} </template>
        <template v-slot:item-like>:{{ item["stat"]["like"] }} </template>
        <template v-slot:item-danmu>:{{ item["stat"]["danmaku"] }} </template>
        <template v-slot:item-favorite>
          :{{ item["stat"]["favorite"] }}
        </template>
        <template v-slot:item-reply>:{{ item["stat"]["reply"] }} </template>
        <template v-slot:item-share>:{{ item["stat"]["share"] }} </template>
        <template v-slot:item-view>:{{ item["stat"]["view"] }} </template>
        <template v-slot:item-tname> {{ item["tname"] }} </template>
        <template v-slot:item-online>
          在线人数:{{ item["online_count"] }}</template
        >
        <template v-slot:pubupdate>:{{ item["pubdate"] }} </template>
        <template v-slot:duration>{{ item["duration"] }}</template>
      </online-item>
    </div>
  </div>
</template>

<script>
import { OnlineList } from 'network/get_bili.js'
import onlineItem from 'commons/online-list/online-item.vue'
export default {
  components: { onlineItem },
  name: "OnlineList",

  data () {
    return {
      onlineItems: {
        loading: true
      }
    }
  },
  methods: {
    getOnlineList () {
      let data = {
        token: this.$store.state.token
      }
      OnlineList(data).then(res => {
        this.onlineItems['list'] = res
        this.onlineItems['loading'] = false
      })
    },
    get_url (item) {
      let bv = item['bvid']
      return item['redirect_url'] == undefined ? "https://www.bilibili.com/video/" + bv : item["redirect_url"]
    },
    relieve_num (num) {
      console.log(num)
    },
  },
  mounted () {
    this.getOnlineList()
  }
}
</script>

<style scoped>
.slot-img img {
  width: 400px;
  height: 280px;
  border-radius: 1rem;
}
.slot-items img {
  width: 35px;
  height: 35px;
  border-radius: 50%;
  vertical-align: middle;
}
.el-textarea.is-disabled :deep() .el-textarea__inner {
  cursor: default;
}
</style>