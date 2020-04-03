<template>
  <div class="w-full h-full">
    <custom-header />
  </div>
</template>

<script>
import { mapState } from 'vuex'
import CustomHeader from '../components/CustomHeader'

export default {
  components: { CustomHeader },
  computed: {
    ...mapState({
      posts: state => state.posts
    })
  },
  mounted () {
    console.log('posts', this.posts)
  }
}
</script>
