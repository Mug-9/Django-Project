<template>
  <div>
    <online-item v-for="item in list" :key="item">
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

      <template v-slot:pubupdate>:{{ item["pubdate"] }} </template>
      <template v-slot:duration>{{ item["duration"] }}</template>
    </online-item>
  </div>
  <div v-if="status['loading']" class="loading"><p>加载中....</p></div>
  <div v-else-if="status['noMore']" class="loading"><p>没有更多了</p></div>
  <div v-else class="loading"></div>
</template>

<script>
import { HotList } from 'network/get_bili.js'
import onlineItem from 'commons/online-list/online-item.vue'
export default {
  components: { onlineItem },
  name: "OnlineList",

  data () {
    return {
      list: [],
      status: {
        loading: false,
        noMore: false
      },
      data: {
        ps: 20,
        pn: 1,
      }
    }
  },
  computed: {
    disabled () {
      return this.status['loading'] || this.status['noMore']
    },
    screenHeight () {
      return document.documentElement.clientHeight
    },
  },
  methods: {
    getHotList () {
      HotList(this.data).then(res => {
        for (let item of res) {
          this.list.push(item)
        }
        this.data['pn']++
        this.status['loading'] = false
      })
    },
    get_url (item) {
      let bv = item['bvid']
      return item['redirect_url'] == undefined ? "https://www.bilibili.com/video/" + bv : item["redirect_url"]
    },
    load () {
      if (this.data['pn'] <= 10) {
        this.status['loading'] = true
        this.getHotList()
      } else {
        this.status['noMore'] = true
      }
    },
    handleScroll () {
      let scrollTop =
        window.pageYOffset || document.documentElement.scrollTop || document.body.scrollTop
      let windowHeight =
        document.documentElement.clientHeight || document.body.clientHeight
      let scrollHeight =
        document.documentElement.scrollHeight || document.body.scrollHeight
      if (scrollTop + windowHeight + 10 >= scrollHeight) {
        this.load()
      } else {
        this.status['noMore'] = false
      }
    },
  },
  mounted () {
    this.getHotList()
    window.addEventListener('scroll', this.handleScroll, true)

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
.online-list {
  margin: 10px auto;
}
.el-textarea.is-disabled :deep() .el-textarea__inner {
  cursor: default;
}
.loading {
  height: 50px;
  display: flex;
  font-size: 1.5em;
  text-align: center;
  vertical-align: middle;
}
.loading p {
  margin: auto auto;
}
</style>