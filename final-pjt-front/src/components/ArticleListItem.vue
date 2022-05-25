<template>
  <tr>
    <th scope="row">{{ articleNum }}</th>
    <td><a class="text-decoration-none" href="" @click.prevent="open" data-bs-toggle="modal" 
    data-bs-target="#detailModal">
    {{ article.title }}</a></td>
    <td>{{ article.user.username }}</td>
    <td>{{ article.comment_count }} | {{ article.like_count }}</td>

    <!-- Modal -->
    <div class="modal fade" id="detailModal" data-bs-backdrop="static" data-bs-keyboard="false" tabindex="-1" aria-labelledby="staticBackdropLabel" aria-hidden="true">
      <div class="modal-dialog">
        <div class="modal-content">
          <div class="modal-header">
            <h5 class="modal-title" id="staticBackdropLabel">Modal title</h5>
            <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
          </div>
          <div class="modal-body">
            <ArticleDetail/>
          </div>
          <div class="modal-footer">
            <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">Close</button>
            <button type="button" class="btn btn-primary">Understood</button>
          </div>
        </div>
      </div>
    </div>
  </tr>
</template>

<script>
  import { mapActions, mapGetters } from 'vuex'
  import ArticleDetail from './ArticleDetail.vue'

  export default {
    name: 'ArticleListItem',
    components: { ArticleDetail },
    props: {
      index: Number,
      article: Object,
    },
    data () {
      return {
        modalName: this.article.pk + ''    // 게시글 별로 다른 모달 이름을 주기 위함.
      }
    },
    computed: {
      ...mapGetters(['articlePage']),
      articleNum () {
        return (this.articlePage - 1) * 10 + this.index + 1
      }
    },
    methods: {
      ...mapActions(['fetchArticle']),
      open () {
        this.fetchArticle(this.article.pk)
      },
    }
  }
</script>

<style>

</style>