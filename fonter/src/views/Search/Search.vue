<template>
  <div class="main">
    <div class="content">
      <div class="tab-title">
        <img src="~@/assets/img/online-icons/search.svg" alt="" />
        <span style="vertical-align=middle">UP搜索</span>
      </div>
      <div class="keyInput">
        <el-input
          v-model="input"
          placeholder="搜索你想要的UP"
          maxlength="20"
          class="inputStyle"
        ></el-input>
        <el-button type="primary" @click="SearchUser"> 搜索</el-button>
      </div>
      <div v-if="loading" v-show="isData">
        <list-item class="each_item">
          <template v-slot:slot-header>
            <a :href="get_url(item)"><img :src="item['face']" /></a>
          </template>
          <template v-slot:slot-name>
            <a :href="get_url(item)"> {{ item["name"] }}</a>
          </template>
          <template v-slot:slot-fans> ：{{ item["fans"] }} </template>
          <template v-slot:slot-videos>
            总视频数：{{ item["video_count"] }}
          </template>
          <template v-slot:slot-archive-like>
            视频总获赞数：{{ item["archive_like"] }}
          </template>
          <template v-slot:slot-archive-view>
            视频总播放数：{{ item["archive_view"] }}
          </template>
        </list-item>
        <fans-in
          v-if="isData"
          :echartsBase_id="item['name']"
          echartsBase_height="600px"
          echartsBase_width="800px"
          :echartsBase_data="item"
        ></fans-in>
      </div>
      <div v-if="loading" class="noData" v-show="!isData">
        UP尚未入库,请输入用户ID入库
        <el-input
          v-model="userID"
          placeholder="输入ID"
          maxlength="20"
          style="width: 30%; margin: 10px 20px"
        ></el-input>
        <el-button type="primary" @click="putData">入库</el-button>
      </div>
    </div>
  </div>
</template>

<script>
import { ElMessage } from 'element-plus'
import { ref } from 'vue'
import { Search, rSearch } from '@/network/get_bili'
import listItem from 'commons/up-list/list-item.vue'
import FansIn from './FansIn.vue'
export default {
  name: "Search",
  components: {
    listItem,
    FansIn
  },
  data () {
    return {
      input: ref(''),
      item: {},
      loading: false,
      isData: false,
      userID: ref('')
    }
  },
  methods: {
    SearchUser () {
      let data = {
        type: 'user',
        name: encodeURI(this.input)
      }
      this.loading = false
      this.isData = false
      this.item = {}
      Search(data).then(res => {
        console.log(res)
        this.item = res['result']
        if (res['code'] == 200) {
          this.isData = true
        }
        this.loading = true
      })
    },
    get_url (item) {
      let bv = item['bvid']
      return item['redirect_url'] == undefined ? "https://www.bilibili.com/video/" + bv : item["redirect_url"]
    },
    putData () {
      let data = {
        type: 'user',
        mid: this.userID
      }
      rSearch(data).then(res => {
        ElMessage.success({
          message: res['msg'],
          type: 'success'
        })
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

.each_item {
  margin-left: 10px;
  flex: 1;
}
.slot-img img {
  width: 100px;
  height: 100px;
  border-radius: 1rem;
}
a {
  text-decoration: none;
  color: black;
}
</style>