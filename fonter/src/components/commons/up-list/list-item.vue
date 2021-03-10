<template>
  <div class="list-item">
    <div class="slot-img">
      <slot name="slot-header"></slot>
    </div>
    <div class="user_detail">
      <div class="slot-name">
        <slot name="slot-name"></slot>
      </div>
      <div class="slot-fans">
        <img src="~@/assets/img/online-icons/fans.svg" />
        <slot name="slot-fans"></slot>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "list-item"
}
</script>

<style scoped>
.list-item {
  margin: 15px auto;
  display: flex;
  background: linear-gradient(
    to right bottom,
    rgba(255, 255, 255, 0.7),
    rgba(255, 255, 255, 0.3)
  );
  border-radius: 1rem;
}

.slot-name {
  font-size: 1.5em;
  color: black;
}

.user_detail {
  margin: 10px;
}
.slot-fans {
  line-height: 20px;
  align-content: center;
  margin-top: 30px;
}

.slot-fans img {
  width: 18px;
  height: 18px;
}
</style>