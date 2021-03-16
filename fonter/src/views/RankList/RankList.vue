<template>
  <div class="main">
    <el-backtop :bottom="70">
      <div
        style="
           {
            height: 100%;
            width: 100%;
            border-radius: 50%;
            background-color: #f2f5f6;
            box-shadow: 0 0 6px rgba(0, 0, 0, 0.12);
            text-align: center;
            line-height: 40px;
            color: #1989fa;
          }
        "
      >
        UP
      </div>
    </el-backtop>
    <div class="content">
      <el-tabs
        tab-position="left"
        class="tabs"
        v-model="activeName"
        @tab-click="handleClick"
      >
        <el-tab-pane name="1" lazy="true">
          <template #label
            ><img src="~@/assets/img/online-icons/online.svg" alt="" />
            <span>在线人数</span>
          </template>
          <div class="tabs-title">
            <img src="~@/assets/img/online-icons/online.svg" alt="" />
            <span style="vertical-align=middle">在线人数</span>
          </div>
          <el-divider> </el-divider>
          <online-list></online-list>
        </el-tab-pane>
        <el-tab-pane name="2" lazy="true">
          <template #label
            ><img src="~@/assets/img/online-icons/hot.svg" alt="" />
            <span>热门视频</span>
          </template>

          <div class="tabs-title">
            <img src="~@/assets/img/online-icons/hot.svg" alt="" />
            <span style="vertical-align=middle">热门视频</span>
          </div>
          <el-divider> </el-divider>
          <hot-list :isIndex="activeIndex"></hot-list>
        </el-tab-pane>
        <el-tab-pane name="3" lazy="true">
          <template #label
            ><img src="~@/assets/img/online-icons/fans_red.svg" alt="" />
            <span>粉丝排行</span>
          </template>

          <div class="tabs-title">
            <img src="~@/assets/img/online-icons/fans_red.svg" alt="" />
            <span style="vertical-align=middle">粉丝排行</span>
          </div>
          <el-divider> </el-divider>
          <fans-list></fans-list>
        </el-tab-pane>
        <el-tab-pane name="4" lazy="true">
          <template #label
            ><img src="~@/assets/img/online-icons/fans_red.svg" alt="" />
            <span>粉丝增长</span>
          </template>

          <div class="tabs-title">
            <img src="~@/assets/img/online-icons/fans_red.svg" alt="" />
            <span style="vertical-align=middle">粉丝增长</span>
          </div>
          <el-divider> </el-divider>
          <fans-incre-list></fans-incre-list>
        </el-tab-pane>
        <el-tab-pane name="5" lazy="true">
          <template #label
            ><img src="~@/assets/img/online-icons/gan.svg" alt="" />
            <span>肝帝排行</span>
          </template>

          <div class="tabs-title">
            <img src="~@/assets/img/online-icons/gan.svg" alt="" />
            <span style="vertical-align=middle">肝帝排行</span>
          </div>
          <el-divider> </el-divider>
          <video-incre-list></video-incre-list>
        </el-tab-pane>
      </el-tabs>
    </div>
  </div>
</template>

<script>
import OnlineList from './OnlineList.vue'
import HotList from './HotList.vue'
import FansList from './FansList.vue'
import FansIncreList from './FansIncreList.vue'
import VideoIncreList from './VideoIncreList.vue'

export default {
  name: "RankList",
  components: {
    OnlineList,
    HotList,
    FansList,
    FansIncreList,
    VideoIncreList
  },
  data () {
    return {
      activeName: '1',
      activeIndex: 1
    }
  },
  methods: {
    handleClick (tab, event) {
      this.activeIndex = tab['index']
    }

  }
}
</script>

<style scoped>
@import "~@/assets/css/views/Ranklist/ranklist.css";
@import "~@/assets/css/component/el-tab/el-tab.css";
</style>