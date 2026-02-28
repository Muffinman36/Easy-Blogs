import { escapeHtml } from '@/utils/escapeHtml'

export function useFormatBlog() {
  function formatContent(content: string): string {
    const paragraphs = content.split(/\n\n+/)
    return paragraphs
      .map((p) => `<p>${escapeHtml(p.trim())}</p>`)
      .join('')
  }

  function generateExcerpt(content: string, maxLength: number = 150): string {
    const plainText = content.replace(/\n+/g, ' ').trim()
    if (plainText.length <= maxLength) {
      return plainText
    }
    return plainText.slice(0, maxLength).trim() + '...'
  }

  return {
    formatContent,
    generateExcerpt
  }
}
