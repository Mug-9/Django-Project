<template>
  <div class="echarts-date">
    <div class="echarts-div">
      <echarts
        :echarts_id="echartsBaiduIndex_id"
        :width="echarts_width"
        :height="echartsBaiduIndex_height"
        :options="options"
      ></echarts>
    </div>
    <div class="days-div">
      <el-dropdown @command="dateChange">
        <el-button type="primary">
          {{ days + "   " }}<i class="el-icon-arrow-down el-icon--right"></i>
        </el-button>

        <template #dropdown>
          <el-dropdown-menu>
            <el-dropdown-item command="0">实时</el-dropdown-item>
            <el-dropdown-item command="7">近7天</el-dropdown-item>
            <el-dropdown-item command="30">近30天</el-dropdown-item>
            <el-dropdown-item command="60">近60天</el-dropdown-item>
            <el-dropdown-item command="90">近90天</el-dropdown-item>
            <el-dropdown-item command="180">近半年</el-dropdown-item>
          </el-dropdown-menu>
        </template>
      </el-dropdown>
    </div>
  </div>
</template>

<script>
import Echarts from './Echarts'
import DayPick from 'commons/time-pick/DayPick.vue'

export default {
  name: "EchartsBaiduIndex",
  components: {
    Echarts,
    DayPick
  },
  props: {
    echartsBaiduIndex_id: {
      type: String
    },
    echartsBaiduIndex_width: {
      type: String
    },
    echartsBaiduIndex_height: {
      type: String
    },
    echartsBaiduIndex_data: {
      type: Object
    },
    echartsBaiduIndex_date: {
      type: Object,
    },
  },
  data () {
    return {
      echarts_width: this.echartsBaiduIndex_width,
      days: "近7天",
      now_date: this.echartsBaiduIndex_date,
      options: {

        title: {
          text: '百度搜索指数'
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
          data: ['all', 'pc', 'wise'],
        },
        xAxis: [{
          show: true,
          type: 'category',
          // min: this.echartsBaiduIndex_data.date[0],
          // max: this.echartsBaiduIndex_data.date[6],
          //data: this.echartsBaiduIndex_data.date,
          data: this.echartsBaiduIndex_data.date,
          axisTick: {
            alignWithLabel: true
          },
          axisLine: {
            lineStyle: {
              width: 2,
              color: '#ff7f50'
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
            name: "all",
            type: "line",
            color: '#0000ff',
            smooth: 0.6,
            lineStyle: {
              width: 5
            },
            data: this.echartsBaiduIndex_data.userIndexes['all'],
          },
          {
            name: "pc",
            type: "line",
            color: '#6495ed',
            smooth: 0.6,
            lineStyle: {
              width: 5
            },
            data: this.echartsBaiduIndex_data.userIndexes['pc'],
          },
          {
            name: "wise",
            type: "line",
            color: '#d14a61',
            smooth: 0.6,
            lineStyle: {
              width: 5
            },
            data: this.echartsBaiduIndex_data.userIndexes['wise'],
          },
        ]
      }
    }
  },
  watch: {
    'echartsBaiduIndex_data.userIndexes': {
      handler (newV, oldV) {
        this.options.series[0].data = newV['all']
        this.options.series[1].data = newV['pc']
        this.options.series[2].data = newV['wise']
        this.echartsBaiduIndex_data.userIndexes = newV
      },
      deep: true
    },
    'echartsBaiduIndex_data.date': {
      handler (newV, oldV) {
        this.echartsBaiduIndex_data.date = newV
        this.options.xAxis[0].data = newV
      },
      deep: true
    },
    echartsBaiduIndex_width: {
      handler(newV, oldV) {
        this.echarts_width = newV
      },
      deep: true
    }
  },
  methods: {
    dateChange (command) {
      if (command == '0') {
        this.days = "实时"
      } else if (command == '180') {
        this.days = '近半年'
      } else {
        this.days = '近' + command + '天'
      }
      this.$emit('dateChange', command)
    }
  },
}
</script>

<style scoped>
@import "~@/assets/css/echarts_time.css";
</style>