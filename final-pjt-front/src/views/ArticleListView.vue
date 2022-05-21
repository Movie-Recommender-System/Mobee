<template>
  <div>
    <h3>ArticleListView</h3>
    <ArticleListItem/>
    <ArticleCreateModal/>
  </div>
</template>

<script>
import ArticleListItem from '@/components/ArticleListItem.vue'
import ArticleCreateModal from '@/components/ArticleCreateModal.vue'

export default {
  name: 'ArticleListView',  
  components: { ArticleListItem, ArticleCreateModal },
}
</script>

<style>
  
</style>