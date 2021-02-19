<template>
  <div class="echarts-date">
    <div class="echarts-div">
      <echarts
        v-loading="echartsBase_data['loading']"
        v-if="!echartsBase_data['loading']"
        :echarts_id="echartsBase_id"
        :width="echarts_width"
        :height="echartsBase_height"
        :options="options"
      ></echarts>
    </div>
    <div class="days-div">
      <el-dropdown @command="baiduIndex_dateChange">
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
      <city-pick @cityChange="cityChange" class="city-pick"> </city-pick>
    </div>
  </div>

  <div>
    <baidu-index-general
      v-loading="echartsBase_data['loading']"
      v-if="!echartsBase_data['loading']"
      :general_table="echartsBase_data['general']"
    >
    </baidu-index-general>
  </div>
  <div>
    <comments> </comments>
  </div>
</template>

<script>
import Echarts from './Echarts'
import CityPick from '@/components/commons/select-city/city-pick.vue'
import Comments from '@/components/commons/coments/Coment.vue'
import BaiduIndexGeneral from './baiduIndexGeneral.vue'
import { GetBaiduIndex } from 'network/get_baidu_index.js'


export default {
  name: "EchartsBaiduIndex",
  components: {
    Echarts,
    CityPick,
    BaiduIndexGeneral,
    Comments
  },
  props: {
    echartsBase_id: {
      type: String
    },
    echartsBase_width: {
      type: String
    },
    echartsBase_height: {
      type: String
    },
  },
  data () {
    return {
      echartsBase_data: {
        days: 7,
        area: '全国',
        loading: true,
      },
      echarts_width: this.echartsBase_width,
      days: "近7天",
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
          data: ['整体', 'PC端', '移动端'],
        },
        xAxis: [{
          show: true,
          type: 'category',
          data: null,
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
            name: "整体",
            type: "line",
            color: '#0000ff',
            smooth: 0.6,
            lineStyle: {
              width: 5
            },
            data: null,
          },
          {
            name: 'PC端',
            type: "line",
            color: '#6495ed',
            smooth: 0.6,
            lineStyle: {
              width: 5
            },
            data: null,
          },
          {
            name: "移动端",
            type: "line",
            color: '#d14a61',
            smooth: 0.6,
            lineStyle: {
              width: 5
            },
            data: null,
          },
        ]
      }
    }
  },
  computed: {
  },
  watch: {
    echartsBase_width: {
      handler (newV, oldV) {
        this.echarts_width = newV
      },
      deep: true
    }
  },
  methods: {
    getBaiduIndex () {
      let data = {
        type: this.echartsBase_data['days'] == 0 ? 'live' : 'index',
        days: this.echartsBase_data['days'],
        area: this.echartsBase_data['area'],
      }
      if (this.$store.state.token) {
        data.token = this.$store.state.token
      }
      this.echartsBase_data['userIndex'] = {}
      this.echartsBase_data['general'] = {}
      GetBaiduIndex(data).then(res => {
        let results = JSON.parse(res)
        let kinds = ['all', 'pc', 'wise']
        for (let result of results) {
          if (result['word'] == 'index') {
            for (let kind of kinds) {
              this.echartsBase_data['userIndex'][kind] = result[kind]
            }
            this.echartsBase_data['date'] = result['date']
          } else {
            for (let kind of kinds) {
              this.echartsBase_data['general'][kind] = result[kind]
            }
          }
        }
        this.options.series[0].data = this.echartsBase_data['userIndex']['all']
        this.options.series[1].data = this.echartsBase_data['userIndex']['pc']
        this.options.series[2].data = this.echartsBase_data['userIndex']['wise']
        this.options.xAxis[0].data = this.echartsBase_data['date']
        this.echartsBase_data['loading'] = false
      })
    },
    baiduIndex_dateChange (command) {
      if (command == '0') {
        this.days = "实时"
      } else if (command == '180') {
        this.days = '近半年'
      } else {
        this.days = '近' + command + '天'
      }
      this.echartsBase_data['days'] = command
      this.getBaiduIndex()
    },
    cityChange (val) {
      this.echartsBase_data['area'] = val
      this.getBaiduIndex()
    }
  },
  mounted () {
    this.getBaiduIndex()
  }
}
</script>

<style scoped>
@import "~@/assets/css/echarts_time.css";
</style>