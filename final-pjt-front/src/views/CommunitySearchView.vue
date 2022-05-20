<template>
  <div>
    <h3>CommunitySearch</h3>
    <CommunitySearchList/>
    <CommunitySearchForm/>
  </div>
</template>

<script>
import CommunitySearchList from '@/components/CommunitySearchList.vue'
import CommunitySearchForm from '@/components/CommunitySearchForm.vue'


export default {
  name: 'CommunitySearch',  
  components: { CommunitySearchList, CommunitySearchForm },
}
</script>

<style>
  
</style>