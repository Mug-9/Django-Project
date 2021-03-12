<template>
  <div class="tips">
    肝帝排名前20
    <div class="update_time">更新时间:02:00:00</div>
  </div>
  <div class="days_select">
    <el-dropdown @command="day_change">
      <el-button type="primary">
        {{ days }} <i class="el-icon-arrow-down el-icon--right"></i>
      </el-button>
      <template #dropdown>
        <el-dropdown-menu>
          <el-dropdown-item command="7">上周</el-dropdown-item>
          <el-dropdown-item command="30">上个月</el-dropdown-item>
        </el-dropdown-menu>
      </template>
    </el-dropdown>
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
          视频增长数：{{ item["video_incre"] }}
        </template>
      </list-item>
    </div>
  </div>
</template>

<script>
import { getVideoIncreRank } from 'network/getUps.js'
import listItem from 'commons/up-list/list-item.vue'
export default {
  name: "VideoIncreList",
  components: {
    listItem
  },
  data () {
    return {
      fanslist: [],
      loading: true,
      currentPage: 1,
      days: '上周',
      data: {}
    }
  },
  computed: {

  },
  methods: {
    UpRank () {
      this.fanslist = []
      getVideoIncreRank().then(res => {
        this.data = res
        this.fanslist = this.data['week']
        this.loading = false
      })
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
    day_change (val) {
      if (val == 7) {
        this.days = "上一周"
        this.fanslist = []
        this.fanslist = this.data['week']
        console.log(this.fanslist)
      } else if (val == 30) {
        this.days = "上个月"
        this.fanslist = []
        this.fanslist = this.data['month']
        console.log(this.fanslist)
      }
    }
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
.days_select {
  margin: 0 auto;
}
</style>