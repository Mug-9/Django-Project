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
      <el-tabs tab-position="left" class="tabs">
        <el-tab-pane>
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
        <el-tab-pane>
          <template #label
            ><img src="~@/assets/img/online-icons/hot.svg" alt="" />
            <span>热门视频</span>
          </template>

          <div class="tabs-title">
            <img src="~@/assets/img/online-icons/hot.svg" alt="" />
            <span style="vertical-align=middle">热门视频</span>
          </div>
          <el-divider> </el-divider>
          <online-list></online-list>
        </el-tab-pane>
      </el-tabs>
    </div>
  </div>
</template>

<script>
import OnlineList from './OnlineList.vue'
export default {
  name: "RankList",
  components: {
    OnlineList
  },
}
</script>

<style scoped>
@import "~@/assets/css/views/Ranklist/ranklist.css";
@import "~@/assets/css/component/el-tab/el-tab.css";
</style>