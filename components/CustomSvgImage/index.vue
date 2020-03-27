<template>
  <img
    :src="source"
    :alt="alt"
  >
</template>

<script>
export default {
  props: {
    name: { type: String, required: true },
    alt: { type: String, default: 'Imagem' }
  },
  computed: {
    source () {
      return require(`../../assets/images/${this.name}.svg`)
    }
  }
}
</script>
