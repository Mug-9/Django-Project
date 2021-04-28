<template>
  <div class="main">
    <div class="content">
      <div class="frame">
        <div class="type">
          <p class="title2">2021年4月第1周热榜分析</p>
          <el-button class="button_type" type="primary"
            >bilibili全站榜单</el-button
          >
          <el-button class="button_type">bilibili原创榜单</el-button>
          <el-button class="button_type">bilibili新人榜单</el-button>
        </div>
        <div class="zup">
          <p class="title">作品高频词</p>
          <el-divider></el-divider>
          <img class="zup_img" src="~@/assets/img/高频词.png" alt="" />
          <p>
            如高频词图所示，上周的热榜视频大多为美食视频，说明当下B站美食类作品登上热榜概率更高。用户可以适当选择美食类作品作为个人风格的突破
          </p>
        </div>
        <div class="zup">
          <p class="title">作品发布时间分布</p>
          <el-divider></el-divider>
          <img class="zup_img" src="~@/assets/img/发布时间.png" alt="" />
        </div>
        <div class="zup">
          <p class="title">作品时间分布</p>
          <el-divider></el-divider>
          <img class="zup_img" src="~@/assets/img/时间区间.png" alt="" />
        </div>
        <div class="zup">
          <p class="title">作品播放量分布</p>
          <el-divider></el-divider>
          <img class="zup_img" src="~@/assets/img/播放量分布.png" alt="" />
        </div>
      </div>
      <div class="frame" v-show="false">
        <p class="title">每周热榜分析</p>
        <div class="item">
          <a href="www.bilibili.com"> 2021年4月第1周热榜分析</a>
        </div>
        <div class="item">
          <a href="www.bilibili.com">2021年3月第4周热榜分析</a>
        </div>
        <div class="item">
          <a href="www.bilibili.com">2021年3月第3周热榜分析</a>
        </div>
        <div class="item">
          <a href="www.bilibili.com">2021年3月第2周热榜分析</a>
        </div>
        <div class="item">
          <a href="www.bilibili.com">2021年3月第1周热榜分析</a>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "HotAnay"
}
</script>

<style scoped>
.frame {
  background: white;
  width: 95%;
  margin: 10px auto;
  padding: 5px;
}
.title {
  font-size: 1.2em;
  margin: 10px;
}
.zup {
  padding: 5px;
}
.button_type {
  margin: 5px;
}
.zup_img {
  height: 50%;
  width: 50%;
  margin-left: 300px;
}
.item {
  height: 100px;
  margin: 10px;
}
.title2 {
  margin: 20px;
  font-size: 1.5em;
  text-align: center;
}
</style>