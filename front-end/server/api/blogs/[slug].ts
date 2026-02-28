export default defineEventHandler(async (event) => {
  const config = useRuntimeConfig()
  const slug = getRouterParam(event, 'slug')

  return await $fetch(`${config.backendUrl}/blogs/${slug}`)
})
