<template>
  <el-table :data="generals" class="table">
    <el-table-column prop="title" label="title"> </el-table-column>
    <el-table-column prop="avg" label="日均值"> </el-table-column>
    <el-table-column prop="yoy" label="同比">
      <template #default="scope">
        <span :class="computed_class(scope.row.yoy)">{{ scope.row.yoy }}</span>
        <img v-if="isPosition(scope.row.yoy)" src="~assets/img/up.svg" alt="" />
        <img
          v-else-if="isReal(scope.row.yoy)"
          src="~assets/img/dicline.svg"
          alt=""
        />
      </template>
    </el-table-column>
    <el-table-column prop="qoq" label="环比">
      <template #default="scope">
        <span :class="computed_class(scope.row.qoq)">{{ scope.row.qoq }}</span>
        <img v-if="isPosition(scope.row.qoq)" src="~assets/img/up.svg" alt="" />
        <img
          v-else-if="isReal(scope.row.qoq)"
          src="~assets/img/dicline.svg"
          alt=""
        />
      </template>
    </el-table-column>
  </el-table>
</template>

<script>
export default {
  name: "feedIndexGeneral",
  props: {
    general_table: {
    }
  },
  computed: {
    generals () {
      return this.general_table == undefined ? "" : [{
        avg: this.general_table['avg'],
        qoq: this.general_table['qoq'] + '%',
        yoy: this.general_table['yoy'] + '%',
        title: this.general_table['title']
      }]
    },
  },
  methods: {

    isPosition (value) {
      if (value[0] == '-') false
      else return true
    },
    isReal (value) {
      if (this.isPosition(value)) return true
      if (value[1] == '%') return false
      return true
    },
    computed_class (value) {
      if (this.isPosition(value)) return "span_red"
      else if (this.isReal(value)) return "span_green"
      else return "span_burlywood"
    }

  }
}
</script>

<style scoped>
.table {
  background: rgb(220, 220, 220);
  margin: 10px auto;
  flex: 1;
  padding: 10px;
  border: none;
}

.table img {
  width: 13px;
  height: 13px;
  margin-left: 5px;
}

.span_red {
  color: red;
}

.span_green {
  color: rgb(25, 190, 107);
}

.span_burlywood {
  color: rgb(222, 184, 135);
}
</style>