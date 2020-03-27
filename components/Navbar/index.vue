<template>
  <nav class="w-full flex justify-between items-center px-10">
    <custom-svg-image name="menu" class="w-6" />

    <div class="flex">
      <ul class="list-none flex mr-10">
        <li class="text-sm mx-5 cursor-pointer uppercase text-gray-700 font-light">
          Blog
        </li>
        <li class="text-sm mx-5 cursor-pointer uppercase text-gray-700 font-light">
          Comunidade
        </li>
        <li class="text-sm mx-5 cursor-pointer uppercase text-gray-700 font-light">
          Newsletter
        </li>
      </ul>
      <custom-svg-image name="search" class="cursor-pointer" />
    </div>
  </nav>
</template>

<script>
import CustomSvgImage from '../CustomSvgImage'

export default {
  components: { CustomSvgImage }
}
</script>
