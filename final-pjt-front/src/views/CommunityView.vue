<template>
  <div>
    <h3>CommunityView</h3>
    <CommunityArticleList/>
    <CommunitySearch/>
  </div>
</template>

<script>
import CommunityArticleList from '@/components/CommunityArticleList.vue'
import CommunitySearch from '@/components/CommunitySearch.vue'


export default {
  name: 'CommunityView',  
  components: { CommunityArticleList, CommunitySearch,  },
}
</script>

<style>
  
</style>