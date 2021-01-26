<template>
  <el-table :data="generals" class="table">
    <el-table-column prop="all_avg" label="整体日均值"> </el-table-column>
    <el-table-column prop="wise_avg" label="移动日均值"> </el-table-column>
    <el-table-column prop="all_yoy" label="整体同比">
      <template #default="scope">
        <span :class="computed_class(scope.row.all_yoy)">{{
          scope.row.all_yoy
        }}</span>
        <img
          v-if="isPosition(scope.row.all_yoy)"
          src="~assets/img/up.svg"
          alt=""
        />
        <img
          v-else-if="isReal(scope.row.all_yoy)"
          src="~assets/img/dicline.svg"
          alt=""
        />
      </template>
    </el-table-column>
    <el-table-column prop="all_qoq" label="整体环比">
      <template #default="scope">
        <span :class="computed_class(scope.row.all_qoq)">{{
          scope.row.all_qoq
        }}</span>
        <img
          v-if="isPosition(scope.row.all_qoq)"
          src="~assets/img/up.svg"
          alt=""
        />
        <img
          v-else-if="isReal(scope.row.all_qoq)"
          src="~assets/img/dicline.svg"
          alt=""
        />
      </template>
    </el-table-column>

    <el-table-column prop="wise_yoy" label="移动同比">
      <template #default="scope">
        <span :class="computed_class(scope.row.wise_yoy)">{{
          scope.row.wise_yoy
        }}</span>
        <img
          v-if="isPosition(scope.row.wise_yoy)"
          src="~assets/img/up.svg"
          alt=""
        />
        <img
          v-else-if="isReal(scope.row.wise_yoy)"
          src="~assets/img/dicline.svg"
          alt=""
        />
      </template>
    </el-table-column>
    <el-table-column prop="wise_qoq" label="移动环比">
      <template #default="scope">
        <span :class="computed_class(scope.row.wise_qoq)">{{
          scope.row.wise_qoq
        }}</span>
        <img
          v-if="isPosition(scope.row.wise_qoq)"
          src="~assets/img/up.svg"
          alt=""
        />
        <img
          v-else-if="isReal(scope.row.wise_qoq)"
          src="~assets/img/dicline.svg"
          alt=""
        /> </template
    ></el-table-column>
  </el-table>
</template>

<script>
export default {
  name: "general-table",
  props: {
    general_table: {
    }
  },
  computed: {
    generals () {
      return this.general_table['all'] == undefined ? "" : [{
        all_avg: this.general_table['all'].avg,
        wise_avg: this.general_table['wise'].avg,
        all_yoy: this.general_table['all'].yoy + '%',
        all_qoq: this.general_table['all'].qoq + '%',
        wise_yoy: this.general_table['wise'].yoy + '%',
        wise_qoq: this.general_table['wise'].qoq + '%',
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
  width: 95%;
  padding: 10px;
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