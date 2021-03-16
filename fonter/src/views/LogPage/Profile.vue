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
        @tab-click="tabClick"
        v-model="activeName"
      >
        <el-tab-pane name="profile">
          <template #label
            ><img src="~@/assets/img/online-icons/profile.svg" alt="" />
            <span> 信 息</span>
          </template>
          <div class="tabs-title">
            <img src="~@/assets/img/online-icons/profile.svg" alt="" />
            <span style="vertical-align=middle"> 信 息</span>
          </div>
          <el-divider> </el-divider>
        </el-tab-pane>
        <el-tab-pane name="store">
          <template #label
            ><img src="~@/assets/img/online-icons/favorite.svg" alt="" />
            <span> 收 藏 </span>
          </template>
          <div class="tabs-title">
            <img src="~@/assets/img/online-icons/favorite.svg" alt="" />
            <span style="vertical-align=middle"> 收 藏 </span>
          </div>
          <el-divider> </el-divider>
        </el-tab-pane>
        <el-tab-pane name="log">
          <template #label
            ><img src="~@/assets/img/online-icons/log.svg" alt="" />
            <span> 记 录 </span>
            <el-divider> </el-divider>
          </template>
          <div class="tabs-title">
            <img src="~@/assets/img/online-icons/log.svg" alt="" />
            <span style="vertical-align=middle"> 记 录 </span>
          </div>
          <el-divider> </el-divider>
          <log-list></log-list>
        </el-tab-pane>
      </el-tabs>
    </div>
  </div>
</template>

<script>
import * as func from '@/store/mutations-type.ts'
import LogList from './LogList.vue'
export default {
  name: "Profile",
  components: {
    LogList,
  },
  data () {
    return {
      activeName: 'log'
    }
  },
  methods: {
    tabClick (tab) {
      if (tab['index'] == '2') {
        this.$router.push('/log')
      } else if (tab['index'] == '1') {
        this.$router.push('/store')
      } else if (tab['index'] == '0') {
        this.$router.push('/profile')
      }
    }
  },
  mounted () {
  },

}
</script>

<style scoped>
@import "~@/assets/css/views/Ranklist/ranklist.css";
@import "~@/assets/css/views/Profile/profile.css";
@import "~@/assets/css/component/el-tab/el-tab.css";
</style>