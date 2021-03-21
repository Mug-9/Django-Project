<template>
  <div class="main">
    <div class="content">
      <div class="tab-title">
        <img src="~@/assets/img/online-icons/search.svg" alt="" />
        <span style="vertical-align=middle">视频搜索</span>
      </div>
      <div class="keyInput">
        <el-input
          v-model="input"
          placeholder="搜索你想要的视频"
          maxlength="20"
          class="inputStyle"
        ></el-input>
        <el-button type="primary" @click="SearchVideo"> 搜索</el-button>
      </div>
      <online-item v-if="loading" :isShowComment="true">
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
      <video-trend
        v-if="isData"
        :echartsBase_id="item['bvid']"
        echartsBase_height="800px"
        echartsBase_width="1000px"
        :echartsBase_data="item['echarts_data']"
      >
      </video-trend>
      <div v-else class="noData" v-show="loading">
        视频尚未入库
        <el-button type="primary" @click="putData">入库</el-button>
      </div>
    </div>
  </div>
</template>

<script>
import { ref } from 'vue'
import { Search, rSearch } from '@/network/get_bili'
import VideoTrend from '@/components/content/VideoTrend/VideoTrend.vue'
import OnlineItem from '@/components/commons/online-list/online-item.vue'
export default {
  name: "SearchV",
  components: {
    VideoTrend,
    OnlineItem
  },
  data () {
    return {
      input: ref(''),
      item: {},
      loading: false,
      isData: false
    }
  },
  methods: {
    SearchVideo () {
      let data = {
        type: 'video',
        bv: this.input
      }
      this.loading = false
      this.isData = false
      this.item = {}
      Search(data).then(res => {
        this.item = {}
        this.item = res['result']
        console.log(this.item)
        this.loading = true
        if (res['code'] == 200) {
          this.isData = true
        }
      })
    },
    get_url (item) {
      let bv = item['bvid']
      return item['redirect_url'] == undefined ? "https://www.bilibili.com/video/" + bv : item["redirect_url"]
    },
    putData () {
      let data = {
        type: 'video',
        bv: this.input
      }
      rSearch(data).then(res => {
        console.log(res)
      })
    }
  }
}
</script>

<style scoped>
.keyInput {
  display: flex;
  margin: 5% auto;
}

.inputStyle {
  width: 70%;
  margin-left: 10%;
  margin-right: 30px;
}
.slot-img img {
  width: 400px;
  height: 280px;
  border-radius: 1rem;
}
.tab-title img {
  width: 40px;
  height: 40px;
}
.tab-title {
  line-height: 50px;
  text-align: center;
  font-size: 1.5em;
  margin: auto 10px;
}
.noData {
  text-align: center;
}
</style>