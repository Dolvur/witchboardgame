<template>
  <div class="cauldron-board">
    <div class="track">
      <Tile
        v-for="(tile, index) in tiles"
        :key="index"
        :index="index"
        :money="tile.money"
        :victorypoints="3"
        :ruby="true"
        :occupied="tile.occupied"
        :theta="thetaValues[index]"
        :a="a"
        @tile-click="toggleTile"
      />
    </div>
  </div>
</template>

<script setup lang="ts">
interface Tile {
  money: number;
  victorypoints: number;
  ruby: boolean;
  occupied: boolean;
}

const tiles = ref<Tile[]>(
  Array.from({ length: 54 }, (_, i) => ({
    money: i + 1,
    victorypoints: i + 1,
    ruby: true,
    occupied: false,
  })),
);

function toggleTile(index: number) {
  tiles.value[index].occupied = !tiles.value[index].occupied;
}

const numPoints = 54;
const numTurns = 4;
const thetaMax = 2 * Math.PI * numTurns; // 4 turns = 8π
const maxRadius = 360; // Max radius in pixels
const a = maxRadius / thetaMax; // Spiral constant ≈ 360 / (8π)
const targetArcLength = 80; // Desired arc length between points;

const thetaValues = [0];
let currentTheta = 0;
for (let i = 1; i < numPoints; i++) {
  const r = a * currentTheta;
  const deltaTheta = targetArcLength / Math.sqrt(a * a + r * r);
  currentTheta += deltaTheta;
  if (currentTheta > thetaMax) {
    console.warn(`Reached θ_max at point ${i}. Stopping early.`);
    break;
  }
  thetaValues.push(currentTheta);
}
</script>

<style scoped>
.cauldron-board {
  display: flex;
  justify-content: center;
  align-items: center;
  min-width: 800px;
  width: 100%;
  height: 80vh;
}

.track {
  position: relative;
  width: 800px;
  height: 800px;
  border: 4px solid #000;
  border-radius: 50%;
  background-color: darkgreen;
}
</style>
