<template>
  <div
    class="echarts-date"
    v-loading="echartsBase_data['loading']"
    element-loading-spinner="el-icon-loading"
    element-loading-background="rgba(0, 0, 0, 0.8)"
    element-loading-text="拼命加载中"
  >
    <div class="echarts-div">
      <echarts
        :echarts_id="echartsBase_id"
        :width="echarts_width"
        :height="echartsBase_height"
        :options="options"
      ></echarts>
      <div class="days-div">
        <el-dropdown @command="region_dateChange">
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
    <div class="div-progress">
      <ul>
        <li
          v-for="(item, index) in echartsBase_data['real']"
          :key="item['name']"
        >
          <div class="progress-item" v-if="index < 10">
            {{ item["name"] }}
            <el-progress
              :percentage="get_percent(item['value'])"
              :format="format"
              :stroke-width="16"
              :color="customColors"
              class="progress"
              :text-inside="true"
            ></el-progress>
          </div>
        </li>
      </ul>
    </div>
  </div>
  <div v-if="!echartsBase_data['loading']">
    <comments :comment_data="commentData"> </comments>
  </div>
</template>

<script>

import Echarts from '@/components/commons/Echarts/Echarts.vue'
import china from '@/components/map/js/china.js'
import { GetRegion } from 'network/get_baidu_index.js'
import Comments from '@/components/commons/coments/Coment.vue'

export default {
  name: "EchartsRegion",
  components: {
    Echarts,
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
      commentData: {},
      customColor: '#409eff',
      customColors: [
        { color: '#f56c6c', percentage: 20 },
        { color: '#e6a23c', percentage: 40 },
        { color: '#5cb87a', percentage: 60 },
        { color: '#1989fa', percentage: 80 },
        { color: '#6f7ad3', percentage: 100 }
      ],
      echarts_width: this.echartsBase_width,
      echartsBase_data: {
        days: 7,
        loading: true
      },
      days: "近7天",
      options: {
        title: {
          text: '地域分布'
        },
        tooltip: {
          trigger: 'item',
          showDelay: 0,
          transitionDuration: 0.2,
          formatter: function (params) {
            var value = (params.value + '').split('.')
            value = value[0].replace(/(\d{1,3})(?=(?:\d{3})+(?!\d))/g, '$1,')
            return params.name + ': ' + value
          }
        },
        visualMap: {
          left: 'left',
          min: 1,
          max: 34,
          inRange: {
            color: ['#a50026', '#d73027', '#f46d43', '#fdae61', '#fee090', '#ffffbf', '#e0f3f8', '#abd9e9', '#74add1', '#4575b4', '#313695',]
          },
          text: ['排名'],           // 文本，默认为数值文本
          calculable: true
        },
        series: [
          {
            type: 'map',
            map: 'china',
            data: null
          }
        ]
      }
    }
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
    format (percentage) {
      return ''
    },
    get_percent (num) {
      return num * 100 / (this.echartsBase_data['real'][0]['value'] + 200)
    },
    region_dateChange (command) {
      if (command == '0') {
        this.days = "实时"
      } else if (command == '180') {
        this.days = '近半年'
      } else {
        this.days = '近' + command + '天'
      }
      this.echartsBase_data['days'] = command
      this.getRegion()
    },
    customColorMethod (percentage) {
      if (percentage < 30) {
        return '#909399'
      } else if (percentage < 70) {
        return '#e6a23c'
      } else {
        return '#67c23a'
      }
    },
    getRegion () {
      let data = {
        days: this.echartsBase_data['days'],
      }
      if (this.$store.state.token) {
        data.token = this.$store.state.token
      }
      GetRegion(data).then(res => {
        let results = JSON.parse(res)
        for (let result of results) {
          if (result['word'] == 'comment') {
            this.commentData = result
          } else {
            this.echartsBase_data[result['word']] = result['data']
          }
        }
        this.options.series[0].data = this.echartsBase_data['index']
        this.echartsBase_data['loading'] = false
      })
    },
    init () {
      this.options.series[0].data = ''
    }
  },
  mounted () {
    this.init()
    this.getRegion()
  }
}
</script>

<style scoped>
@import "~@/assets/css/echarts_time.css";
ul li {
  list-style-type: none;
}
.div-progress {
  display: table;
  flex: 1;
}
.progress-item {
  display: flex;
  margin: 2% auto;
  width: auto;
}
.progress {
  display: flex;
  width: 90%;
  margin-left: 10px;
}
</style>