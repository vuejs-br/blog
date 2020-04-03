<template>
  <div
    class="relative flex flex-col items-center justify-center w-full h-screen"
  >
    <custom-svg-image name="header-banner" class="absolute top-0 left-0 w-full" />
    <navbar class="fixed top-0 mt-12" />
    <div class="w-24">
      <img class="w-full" src="~assets/images/logo.png" alt="logo do vue.js brasil">
    </div>
    <span class="text-gray-800 uppercase font-regular text-md">Bem vindo a comunidade</span>
    <h1 class="-mt-2 text-4xl font-black text-gray-800 uppercase">
      Vue.js Brasil
    </h1>
    <p class="max-w-sm mt-5 font-light text-center text-gray-600">
      Acesse nossos canais para tirar dúvidas, saber novidades e interagir com toda a comunidade Vue.js aqui no Brasil
    </p>
    <share-icons />
  </div>
</template>

<script>
import Navbar from '../Navbar'
import ShareIcons from '../ShareIcons'
import CustomSvgImage from '../CustomSvgImage'

export default {
  components: { ShareIcons, Navbar, CustomSvgImage }
}
</script>
