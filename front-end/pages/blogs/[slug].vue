<script setup lang="ts">
const route = useRoute()
const slug = route.params.slug as string

const { data: blog, error } = await useAsyncData(
  `blog-${slug}`,
  () => $fetch(`/api/blogs/${slug}`)
)

useHead({
  title: computed(() => blog.value?.title || 'Blog Post')
})

const { formatContent } = useFormatBlog()

const formattedContent = computed(() => {
  if (!blog.value?.content) return ''
  return formatContent(blog.value.content)
})
</script>

<template>
  <div class="container">
    <NuxtLink to="/blogs" class="back-link">
      &larr; Back to blogs
    </NuxtLink>

    <div v-if="error" class="error">
      Blog post not found.
    </div>

    <article v-else-if="blog" class="blog-detail">
      <header>
        <h1>{{ blog.title }}</h1>
        <time :datetime="blog.createdAt">{{ blog.createdAt }}</time>
      </header>

      <div class="content" v-html="formattedContent" />
    </article>
  </div>
</template>

<style scoped>
.back-link {
  display: inline-block;
  margin-bottom: 2rem;
  color: #90caf9;
}

.back-link:hover {
  color: #64b5f6;
}

.blog-detail header {
  margin-bottom: 2rem;
  padding-bottom: 1rem;
  border-bottom: 1px solid rgba(255, 255, 255, 0.1);
}

.blog-detail h1 {
  margin-bottom: 0.5rem;
}

.blog-detail time {
  color: #9e9e9e;
  font-size: 0.9rem;
}

.content {
  line-height: 1.8;
}

.content :deep(p) {
  margin-bottom: 1.5rem;
}

.error {
  text-align: center;
  color: #ef5350;
  padding: 2rem;
}
</style>
