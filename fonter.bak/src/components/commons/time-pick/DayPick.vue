<template>
  <el-date-picker
    v-model="date"
    align="right"
    type="date"
    placeholder="选择日期"
    :disabled-date="disabledDate"
    :shortcuts="shortcuts"
    size="medium"
    @change="dateChange"
    format="YYYY-MM-DD"
  >
  </el-date-picker>
</template>

<script>
export default {
  name: "DayPick",
  props: {
    dayPick_date: Object
  },
  data () {
    return {
      date: this.dayPick_date,
      disabledDate (time) {
        return time.getTime() > Date.now()
      },
      shortcuts: [
        {
          text: 'Today',
          value: new Date(),
        },
        {
          text: 'Yesterday',
          value: (() => {
            const date = new Date()
            date.setTime(date.getTime() - 3600 * 1000 * 24)
            return date
          })(),
        },
        {
          text: 'A week ago',
          value: (() => {
            const date = new Date()
            date.setTime(date.getTime() - 3600 * 1000 * 24 * 7)
            return date
          })(),
        }],
    }
  },
  mounted () {
  },
  methods: {
    dateChange (val) {
      this.$emit('dateChange', val)
    }
  }
}
</script>

<style scoped>
</style>