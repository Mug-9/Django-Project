<template>
  <div class="main">
    <div class="content">
      <div class="frame">
        <p class="title2">热点候选详情</p>
        <div class="type">
          <el-button class="button_type">关键字搜索</el-button>
          <el-button class="button_type" type="primary">数据趋势</el-button>
        </div>
        <div>
          <echarts
            class="data"
            echarts_id="abc"
            width="800px"
            height="600px"
            :options="options[0]"
            v-show="false"
          ></echarts>
        </div>
        <div>
          <echarts
            class="data"
            echarts_id="abc1"
            width="800px"
            height="600px"
            :options="options[1]"
          ></echarts>
        </div>
        <div>
          <echarts
            class="data"
            echarts_id="abc2"
            width="800px"
            height="600px"
            :options="options[2]"
          ></echarts>
        </div>
        <div>
          <echarts
            class="data"
            echarts_id="abc3"
            width="800px"
            height="600px"
            :options="options[3]"
          ></echarts>
        </div>
      </div>
    </div>
  </div>
</template>

<script>

import Echarts from '@/components/commons/Echarts/Echarts.vue'
export default {
  name: "HotDetail",
  components: {
    Echarts,
  },
  data () {
    return {
      options: [{
        title: {
          text: '关键词搜索指数'
        },
        tooltip: {
          trigger: 'axis',
          axisPointer: {
            type: 'cross'
          }
        },
        toolbox: {
          feature: {
            dataView: { show: true, readOnly: false },
            restore: { show: true },
            saveAsImage: { show: true }
          }
        },
        legend: {
          data: ['福岛核废水', 'FDA', '圆脸'],
        },
        xAxis: [{
          show: true,
          type: 'category',
          data: ['14:00', "14:30", '15:00', "15:30", "16:00", "16:30", "17:00"],
          axisTick: {
            alignWithLabel: true
          },
          axisLine: {
            lineStyle: {
              width: 2,
              color: '#8a2be2'
            }
          },
        }],
        yAxis: [{
          type: 'value',
          name: '搜索指数',
          nameTextStyle: {//y轴上方单位的颜色
            color: '#151515',
          },
          axisLine: {
            show: true,
            lineStyle: {
              color: '#ff7f50',
              width: 2,
              type: 'solid'
            }
          },
        },
        ],
        series: [
          {
            name: "福岛核废水",
            type: "line",
            color: '#0000ff',
            smooth: 0,
            lineStyle: {
              width: 3
            },
            data: [2000, 3111, 5543, 5354, 6544, 12450, 13000],
          },
          {
            name: 'FDA',
            type: "line",
            color: '#6495ed',
            smooth: 0,
            lineStyle: {
              width: 3
            },
            data: [200, 900, 1500, 1200, 2000, 2600, 3500],
          },
          {
            name: "圆脸",
            type: "line",
            color: '#d14a61',
            smooth: 0,
            lineStyle: {
              width: 3
            },
            data: [1000, 1500, 3000, 3300, 4300, 5500, 5600],
          },
        ]
      }, {
        title: {
          text: '播放量'
        },
        tooltip: {
          trigger: 'axis',
          axisPointer: {
            type: 'cross'
          }
        },
        toolbox: {
          feature: {
            dataView: { show: true, readOnly: false },
            restore: { show: true },
            saveAsImage: { show: true }
          }
        },
        legend: {
          data: ['播放量'],
        },
        xAxis: [{
          show: true,
          type: 'category',
          data: ['14:00', "14:30", '15:00', "15:30", "16:00", "16:30", "17:00"],
          axisTick: {
            alignWithLabel: true
          },
          axisLine: {
            lineStyle: {
              width: 2,
              color: '#8a2be2'
            }
          },
        }],
        yAxis: [{
          type: 'value',
          name: '播放量',
          nameTextStyle: {//y轴上方单位的颜色
            color: '#151515',
          },
          axisLine: {
            show: true,
            lineStyle: {
              color: '#ff7f50',
              width: 2,
              type: 'solid'
            }
          },
        },
        ],
        series: [
          {
            name: "播放量",
            type: "line",
            color: '#d14a61',
            smooth: 0,
            lineStyle: {
              width: 3
            },
            data: [0, 30000, 80000, 160000, 180000, 200000, 234000],
          },
        ]
      }, {
        title: {
          text: '点赞量'
        },
        tooltip: {
          trigger: 'axis',
          axisPointer: {
            type: 'cross'
          }
        },
        toolbox: {
          feature: {
            dataView: { show: true, readOnly: false },
            restore: { show: true },
            saveAsImage: { show: true }
          }
        },
        legend: {
          data: ['点赞量'],
        },
        xAxis: [{
          show: true,
          type: 'category',
          data: ['14:00', "14:30", '15:00', "15:30", "16:00", "16:30", "17:00"],
          axisTick: {
            alignWithLabel: true
          },
          axisLine: {
            lineStyle: {
              width: 2,
              color: '#8a2be2'
            }
          },
        }],
        yAxis: [{
          type: 'value',
          name: '点赞量',
          nameTextStyle: {//y轴上方单位的颜色
            color: '#151515',
          },
          axisLine: {
            show: true,
            lineStyle: {
              color: '#ff7f50',
              width: 2,
              type: 'solid'
            }
          },
        },
        ],
        series: [
          {
            name: "点赞量",
            type: "line",
            color: '#d14a61',
            smooth: 0,
            lineStyle: {
              width: 3
            },
            data: [0, 3000, 8000, 16000, 22000, 26000, 29400],
          },
        ]
      }, {
        title: {
          text: '收藏量'
        },
        tooltip: {
          trigger: 'axis',
          axisPointer: {
            type: 'cross'
          }
        },
        toolbox: {
          feature: {
            dataView: { show: true, readOnly: false },
            restore: { show: true },
            saveAsImage: { show: true }
          }
        },
        legend: {
          data: ['收藏量'],
        },
        xAxis: [{
          show: true,
          type: 'category',
          data: ['14:00', "14:30", '15:00', "15:30", "16:00", "16:30", "17:00"],
          axisTick: {
            alignWithLabel: true
          },
          axisLine: {
            lineStyle: {
              width: 2,
              color: '#8a2be2'
            }
          },
        }],
        yAxis: [{
          type: 'value',
          name: '收藏量',
          nameTextStyle: {//y轴上方单位的颜色
            color: '#151515',
          },
          axisLine: {
            show: true,
            lineStyle: {
              color: '#ff7f50',
              width: 2,
              type: 'solid'
            }
          },
        },
        ],
        series: [
          {
            name: "收藏量",
            type: "line",
            color: '#d14a61',
            smooth: 0,
            lineStyle: {
              width: 3
            },
            data: [0, 300, 800, 1600, 2200, 2600, 2750],
          },
        ]
      },]
    }
  }
}
</script>

<style scoped>
.frame {
  background: white;
  width: 95%;
  margin: 10px auto;
  padding: 5px;
}
.button_type {
  margin: 5px;
}
.data {
  margin-left: 250px;
  margin-top: 30px;
}
.title2 {
  margin: 20px;
  font-size: 1.5em;
  text-align: center;
}
</style>