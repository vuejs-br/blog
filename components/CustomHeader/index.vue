<template>
  <div class="w-full h-screen flex flex-col justify-center items-center bg-gray-main relative">
    <navbar class="fixed top-0 mt-12" />
    <div class="w-24">
      <img class="w-full" src="~assets/images/logo.png" alt="logo do vue.js brasil">
    </div>
    <span class="uppercase font-regular text-gray-800 text-md">Bem vindo a comunidade</span>
    <h1 class="uppercase font-black text-gray-800 text-4xl -mt-2">
      Vue.js Brasil
    </h1>
    <p class="max-w-sm text-center text-gray-600 mt-5">
      Acesse nossos canais para tirar dúvidas, saber novidades e interagir com toda a comunidade Vue.js aqui no Brasil
    </p>
    <share-icons />
  </div>
</template>

<script>
import Navbar from '../Navbar'
import ShareIcons from '../ShareIcons'

export default {
  components: { ShareIcons, Navbar }
}
</script>
