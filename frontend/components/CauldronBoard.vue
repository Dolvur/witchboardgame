<template>
  <div class="cauldron-board">
    <div class="track">
      <Tile
        v-for="(tile, index) in tiles"
        :key="index"
        :index="index"
        :total-tiles="tiles.length"
        :content="tile.content"
        :occupied="tile.occupied"
        @tile-click="toggleTile"
      />
    </div>
  </div>
</template>

<script setup lang="ts">
interface Tile {
  content: number;
  occupied: boolean;
}

const tiles = ref<Tile[]>(
  Array.from({ length: 33 }, (_, i) => ({
    content: i + 1,
    occupied: false,
  })),
);

function toggleTile(index: number) {
  tiles.value[index].occupied = !tiles.value[index].occupied;
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
