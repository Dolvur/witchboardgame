<template>
  <div
    class="tile"
    :class="{ occupied: occupied }"
    :style="tileStyle"
    @click="$emit('tile-click', index)"
  >
    <p class="no-margin money">{{ money }}</p>
    <div class="second-row">
      <p class="no-margin victorypoints">{{ victorypoints }}</p>
      <!-- <p v-if="ruby" class="no-margin">5</p> -->
      <NuxtImg src="/images/ruby.png" width="20" height="20" />
    </div>
  </div>
</template>

<script setup lang="ts">
import type { CSSProperties } from "vue";
const { money, victorypoints, ruby, index, occupied, theta, a } = defineProps({
  money: { type: Number, required: true },
  victorypoints: { type: Number, required: true },
  ruby: { type: Boolean, required: true },
  index: { type: Number, required: true },
  occupied: { type: Boolean, required: true },
  theta: { type: Number, required: true },
  a: { type: Number, required: true },
});

defineEmits(["tile-click"]);

const tileStyle = computed<CSSProperties>(() => {
  return {
    transform: `translate(-50%, -50%) rotate(-${theta}rad) translate(${a * theta}px) rotate(${theta}rad) translateY(-20px)`,
    position: "absolute",
    top: "50%",
    left: "50%",
    transformOrigin: "center center",
  };
});
</script>

<style scoped>
.second-row {
  display: flex;
  flex-direction: row;
  gap: 10px;
}

.no-margin {
  margin: 0;
}

.money {
  color: lightgray;
  text-shadow: 1px 1px 1px black;
}

.victorypoints {
  /* color: blue; */
  background-color: #ebdebc;
  border: solid 2px black;
  color: darkorange;
  text-shadow: 1px 1px 1px black;
}

.tile {
  width: 60px;
  height: 60px;
  background-color: #f0f0f0;
  border: 2px solid #333;
  border-radius: 50%; /* Circular tiles */
  display: flex;
  justify-content: center;
  align-items: center;
  font-size: 24px;
  cursor: pointer;
  flex-direction: column;
  justify-content: flex-end;
}

.tile.occupied {
  background-color: #ff6b6b;
}

.tile:hover {
  background-color: #ddd;
}

.tile.occupied:hover {
  background-color: #ff7a7a;
}
</style>
