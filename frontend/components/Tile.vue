<template>
  <div
    class="tile"
    :class="{ occupied: occupied }"
    :style="tileStyle"
    @click="$emit('tile-click', index)"
  >
    {{ content }}
  </div>
</template>

<script setup lang="ts">
import type { CSSProperties } from "vue";
const { content, index, occupied, theta, a } = defineProps({
  content: { type: Number, required: true },
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
