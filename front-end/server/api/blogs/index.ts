export default defineEventHandler(async (event) => {
  const config = useRuntimeConfig()
  const query = getQuery(event)
  const page = Number(query.page) || 1

  return await $fetch(`${config.backendUrl}/blogs`, { query: { page } })
})
