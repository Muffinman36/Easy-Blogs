const blogs = [
  {
    id: 1,
    slug: 'getting-started-with-nuxt',
    title: 'Getting Started with Nuxt 3',
    content: `Nuxt 3 is a powerful framework for building modern web applications with Vue.js. It provides server-side rendering out of the box, making your apps fast and SEO-friendly.

In this guide, we'll explore the basics of setting up a Nuxt 3 project and understanding its core concepts.

The file-based routing system makes it incredibly easy to create new pages. Simply add a Vue file to the pages directory and Nuxt handles the rest.`,
    createdAt: '2026-02-15'
  },
  {
    id: 2,
    slug: 'understanding-ssr',
    title: 'Understanding Server-Side Rendering',
    content: `Server-side rendering (SSR) is a technique where the server generates the full HTML for a page before sending it to the client. This approach offers several benefits.

First, it improves SEO since search engines can easily crawl the fully rendered content. Second, it provides faster initial page loads because users see content immediately.

Nuxt 3 makes SSR seamless with its universal rendering mode. Your Vue components work the same way whether rendered on the server or client.`,
    createdAt: '2026-02-20'
  },
  {
    id: 3,
    slug: 'vue-composables-guide',
    title: 'A Guide to Vue Composables',
    content: `Composables are one of the most powerful features in Vue 3's Composition API. They allow you to extract and reuse stateful logic across components.

A composable is simply a function that uses Vue's reactivity system. By convention, composable function names start with "use", like useCounter or useFetch.

The beauty of composables is their composability - you can combine multiple composables to build complex functionality from simple, reusable pieces.`,
    createdAt: '2026-02-25'
  }
]

const pageSize = 2

export default defineEventHandler((event) => {
  const query = getQuery(event)
  const page = Number(query.page) || 1

  const totalPages = Math.ceil(blogs.length / pageSize)
  const start = (page - 1) * pageSize
  const end = start + pageSize

  const results = blogs.slice(start, end).map((blog) => ({
    id: blog.id,
    slug: blog.slug,
    title: blog.title,
    excerpt: blog.content.split('\n\n')[0],
    createdAt: blog.createdAt
  }))

  return {
    page,
    total_pages: totalPages,
    results
  }
})
