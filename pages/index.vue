<template>
  <div class="w-full h-full">
    <custom-header />
    <!--
    <nuxt-content :document="article" />
    -->
  </div>
</template>

<script>
import CustomHeader from '../components/CustomHeader'

export default {
  components: { CustomHeader },
  async asyncData ({ $content }) {
    const article = await $content('articles', '2016-06-27-vuex').fetch()
    return { article }
  },
  mounted () {
    console.log('article', this.article)
  }
}
</script>
