<template>
  <div class="tips">
    粉丝排名前100
    <div class="update_time">更新时间:02:00:00</div>
  </div>
  <div
    v-loading="loading"
    element-loading-spinner="el-icon-loading"
    element-loading-background="rgba(0, 0, 0, 0.8)"
    element-loading-text="拼命加载中"
  >
    <div v-for="(item, index) in fanslist" :key="item" class="items">
      <div class="li_index" :style="indexColor(index)">
        {{ (currentPage - 1) * 10 + index + 1 }}
      </div>
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
    </div>
    <div class="pager">
      <el-pagination
        background
        layout="prev, pager, next"
        :total="50"
        @current-change="handleCurrentChange"
      ></el-pagination>
    </div>
  </div>
</template>

<script>
import { getUpRank } from 'network/getUps.js'
import listItem from 'commons/up-list/list-item.vue'
export default {
  name: "FansList",
  components: {
    listItem
  },
  data () {
    return {
      fanslist: [],
      loading: true,
      currentPage: 1
    }
  },
  computed: {

  },
  methods: {
    UpRank (data = { 'ps': 1, 'pn': 20 }) {
      this.fanslist = []
      getUpRank(data).then(res => {
        this.fanslist = res
        this.loading = false
      })
    },
    handleCurrentChange (val) {
      this.loading = true
      this.currentPage = val
      let data = {
        'ps': val,
        'pn': 20,
      }
      this.UpRank(data)
    },
    indexColor (index) {
      let num = (this.currentPage - 1) * 10 + index + 1
      if (num == 1) {
        return {
          background: 'gold'
        }
      } else if (num == 2) {
        return {
          background: '#c0c0c0'
        }
      } else if (num == 3) {
        return {
          background: '#B87333'
        }
      } else {
        return {
          background: '#1296db'
        }
      }
    },
    get_url (item) {
      let mid = item['mid']
      return "https://space.bilibili.com/" + mid + '/'
    },
  },
  mounted () {
    this.UpRank()
  }
}
</script>

<style scoped>
a {
  text-decoration: none;
  color: black;
}
.slot-img img {
  width: 100px;
  height: 100px;
  border-radius: 1rem;
}
.tips {
  padding: 5px;
  color: gray;
  display: flex;
  text-align: center;
  margin: 0 auto;
}
.update_time {
  margin: 0 10px 0 auto;
}
.pager {
  margin: 0 auto;
  width: 50%;
}
.li_index {
  background: #1296db;
  font-size: 1.5em;
  width: 40px;
  height: 40px;
  border-radius: 50%;
  text-align: center;
  padding: 5px;
  margin: auto 5px;
}
.items {
  display: flex;
  align-content: center;
}
.each_item {
  margin-left: 10px;
  flex: 1;
}
</style>