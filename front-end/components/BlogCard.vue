<script setup lang="ts">
interface Blog {
  id: number
  slug: string
  title: string
  excerpt: string
  createdAt: string
}

defineProps<{
  blog: Blog
}>()
</script>

<template>
  <NuxtLink :to="`/blogs/${blog.slug}`" class="blog-card">
    <h2>{{ blog.title }}</h2>
    <time :datetime="blog.createdAt">{{ blog.createdAt }}</time>
    <p>{{ blog.excerpt }}</p>
  </NuxtLink>
</template>

<style scoped>
.blog-card {
  display: block;
  padding: 1.5rem;
  background: rgba(255, 255, 255, 0.05);
  border-radius: 8px;
  border: 1px solid rgba(255, 255, 255, 0.1);
  transition: all 0.2s ease;
}

.blog-card:hover {
  background: rgba(255, 255, 255, 0.08);
  border-color: rgba(100, 181, 246, 0.3);
  transform: translateY(-2px);
}

.blog-card h2 {
  font-size: 1.25rem;
  margin-bottom: 0.5rem;
  color: #e8e8e8;
}

.blog-card time {
  display: block;
  font-size: 0.85rem;
  color: #9e9e9e;
  margin-bottom: 0.75rem;
}

.blog-card p {
  color: #bdbdbd;
  margin-bottom: 0;
  line-height: 1.6;
}
</style>
