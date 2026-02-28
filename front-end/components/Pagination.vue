<script setup lang="ts">
const props = defineProps<{
  currentPage: number
  totalPages: number
}>()

const emit = defineEmits<{
  pageChange: [page: number]
}>()

const hasPrevious = computed(() => props.currentPage > 1)
const hasNext = computed(() => props.currentPage < props.totalPages)

function goToPrevious() {
  if (hasPrevious.value) {
    emit('pageChange', props.currentPage - 1)
  }
}

function goToNext() {
  if (hasNext.value) {
    emit('pageChange', props.currentPage + 1)
  }
}
</script>

<template>
  <nav class="pagination">
    <button
      :disabled="!hasPrevious"
      class="pagination-btn"
      @click="goToPrevious"
    >
      &larr; Previous
    </button>

    <span class="page-info">
      Page {{ currentPage }} of {{ totalPages }}
    </span>

    <button
      :disabled="!hasNext"
      class="pagination-btn"
      @click="goToNext"
    >
      Next &rarr;
    </button>
  </nav>
</template>

<style scoped>
.pagination {
  display: flex;
  justify-content: center;
  align-items: center;
  gap: 1rem;
  margin-top: 2rem;
  padding-top: 1.5rem;
  border-top: 1px solid rgba(255, 255, 255, 0.1);
}

.pagination-btn {
  padding: 0.5rem 1rem;
  background: rgba(100, 181, 246, 0.2);
  border: 1px solid rgba(100, 181, 246, 0.3);
  border-radius: 4px;
  color: #90caf9;
  cursor: pointer;
  transition: all 0.2s ease;
}

.pagination-btn:hover:not(:disabled) {
  background: rgba(100, 181, 246, 0.3);
  border-color: rgba(100, 181, 246, 0.5);
}

.pagination-btn:disabled {
  opacity: 0.4;
  cursor: not-allowed;
}

.page-info {
  color: #9e9e9e;
  font-size: 0.9rem;
}
</style>
