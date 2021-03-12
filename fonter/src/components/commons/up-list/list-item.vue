<template>
  <div class="list-item">
    <div class="slot-img">
      <slot name="slot-header"></slot>
    </div>
    <div class="user_detail">
      <div class="slot-name">
        <slot name="slot-name"></slot>
      </div>
      <div class="fans_videos">
        <div class="slot-fans">
          <img src="~@/assets/img/online-icons/fans.svg" />
          <slot name="slot-fans"></slot>
        </div>
        <div class="slot-videos">
          <slot name="slot-videos"></slot>
        </div>
      </div>

      <div class="like_view">
        <div class="slot-archive-like">
          <slot name="slot-archive-like"></slot>
        </div>
        <div class="slot-archive-view">
          <slot name="slot-archive-view"></slot>
        </div>
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
  margin: 5px 20px;
  width: 100%;
}
.fans_videos {
  display: flex;
  margin: 2px auto;
}
.like_view {
  display: flex;
  margin: 2px auto;
}
.slot-fans {
  flex: 1;
  line-height: 20px;
  align-content: center;
  margin: 2px;
}
.slot-videos {
  flex: 1;
  line-height: 20px;
  align-content: center;
  margin: 2px;
}

.slot-archive-like {
  flex: 1;
  line-height: 20px;
  align-content: center;
  margin: 2px;
}

.slot-archive-view {
  flex: 1;
  line-height: 20px;
  align-content: center;
  margin: 2px;
}

.user_detail img {
  width: 18px;
  height: 18px;
}
</style>