<script setup lang="ts">
useHead({
  title: 'Hack USU'
})

const route = useRoute()
const router = useRouter()

const currentPage = computed(() => Number(route.query.page) || 1)

const { data, error } = await useAsyncData(
  `blogs-page-${currentPage.value}`,
  () => $fetch('/api/blogs', { query: { page: currentPage.value } }),
  {
    watch: [currentPage],
    getCachedData: (key, nuxtApp) =>
      nuxtApp.isHydrating ? (nuxtApp.payload.data as Record<string, unknown>)[key] : undefined,
  }
)

function goToPage(page: number) {
  router.push({ query: { page } })
}
</script>

<template>
  <div class="container">
    <h1>Hack USU</h1>

    <div v-if="error" class="error">
      Failed to load blogs. Please try again later.
    </div>

    <div v-else-if="data" class="blogs-list">
      <BlogCard
        v-for="blog in data.results"
        :key="blog.id"
        :blog="blog"
      />

      <Pagination
        v-if="data.total_pages > 1"
        :current-page="data.page"
        :total-pages="data.total_pages"
        @page-change="goToPage"
      />
    </div>
  </div>
</template>

<style scoped>
h1 {
  margin-bottom: 2rem;
  text-align: center;
}

.blogs-list {
  display: flex;
  flex-direction: column;
  gap: 1.5rem;
}

.error {
  text-align: center;
  color: #ef5350;
  padding: 2rem;
}
</style>
