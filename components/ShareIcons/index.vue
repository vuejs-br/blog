<template>
  <div class="flex">
    <a
      v-for="(item, index) in items"
      :key="index"
      target="_blank"
      class="mx-5 mt-8"
      :href="item.url"
    >
      <custom-svg-image
        :name="item.icon"
      />
    </a>
  </div>
</template>

<script>
import CustomSvgImage from '../CustomSvgImage'

const items = [
  {
    icon: 'telegram',
    url: ''
  },
  {
    icon: 'facebook',
    url: ''
  },
  {
    icon: 'youtube',
    url: 'https://www.youtube.com/channel/UC9DvZyV1QU3Y0-Tpv97oAxw'
  },
  {
    icon: 'slack',
    url: ''
  }
]

export default {
  components: { CustomSvgImage },
  data: () => ({
    items
  })
}
</script>
