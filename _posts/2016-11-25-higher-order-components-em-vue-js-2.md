---
layout: post
title: 'Higher-Order Components em Vue.js 2'
main-class: 'dev'
date: 2016-11-25 19:51:52 
color: '#637a91'
tags: 
layout: post
author: pablohpsilva
---

Para resolver um problema do meu trabalho (como sempre), queria criar um componente que era muito parecido com outro que já havia feito. Pensei bastante e resolvi dar uma lida em alguns artigos do Medium. Durante a leitura de um artigo que era contra o uso de mixins, encontrei um artigo sobre Higher-Order Components. O título me chamou atenção e acabou resolvendo o meu problema.

#### O que é Higher-Order Component?
> Higher-Order Components é o conceito de Higher-Order Functions aplicado a componentes.

> Uma Higher-Order Function é uma função que opera sobre outras funções. Ou seja, ela recebe uma função como input e retorna outra função.

> Sendo assim, Higher-Order Component é um componente que opera sobre outros componentes.

O meu objetivo inicial era aproveitar métodos e variáveis de um componente e mudar completamente o *template* e *style* de um novo componente. Mas como fazer isso sem ficar duplicando código?

#### Vamos direto ao ponto? Cadê o exemplo?

Aqui está o componente que eu quero usar para compor um novo componente:

```html
<template lang="html">
  <div class="ProductItem__wrapper"
    v-if="product">
    <!-- ... -->
  </div>
</template>

<script type="text/babel">
  export default {
    props: {
      product: {
        type: Object,
        default() { return null; },
      },
    },
    data() {
      return {
        openDetails: false,
      };
    },
    components: {},
    computed: {},
    methods: {
      openProductPage() {
        this.$router.push({ path: '/products/1' });
      },
    },
    mounted() {},
  };
</script>

<style lang="stylus">
  +prefix-classes('ProductItem__')
    .wrapper
      background #FFF
      min-height 420px
      max-height 420px
      height 100%
      min-width 280px
      max-width 280px
      width 100%
      margin 20px
      position relative
      font 200 10px/1em Montserrat
      box-shadow 0px 2px 10px -4px rgba(0,0,0,0.3)
      transition all .3s ease
      &:hover
        box-shadow 0px 10px 25px -5px rgba(0,0,0,0.3)
  /* ... */
</style>
```
Deste componente, como falei antes, gostaria de aproveitar os *methods*, *data* e mudar o restante dos conteúdos das tags *template* e *style* e acrescentar mais *methods*, *data*, etc. Com isso em mente, construí este componente:

```html
<template lang="html">
  <div @click="clicked()">oi</div>
</template>

<script type="text/babel">
  import ProductItem from '../../shared-components/Item';
  export default {
    extends: { // The Magic is happening right here
      props: {
        ...ProductItem.props,
      },
      data() {
        return {
          ...ProductItem.data(),
        };
      },
      methods: {
        ...ProductItem.methods,
      },
    },
    data() {
      return {
        teste: 1,
      };
    },
    methods: {
      clicked() {
        console.log('clicked');
      },
    },
    mounted() {
    },
  };
</script>

<style lang="css">
</style>
```

Repare na propriedade `extends` do componente acima. É lá onde a mágica acontece! Perceba que eu importei para o novo componente somente aquilo que eu precisava do componente base. Interessante, não?

Podemos importar um componente base **inteiro** fazendo isso:
```html
<template lang="html">
  <div @click="clicked()">oi</div>
</template>

<script type="text/babel">
  import ProductItem from '../../shared-components/Item';
  export default {
    extends: { // The Magic is happening right here
      ...ProductItem,
    },
    data() {
      return {
        teste: 1,
      };
    },
    methods: {
      clicked() {
        console.log('clicked');
      },
    },
    mounted() {
    },
  };
</script>

<style lang="css">
</style>
```
#### Porque não importar o componente inteiro sempre?
Porque, pelo menos neste exemplo, não faz sentido.

#### Porque não usar Slots?
Porque, neste caso, a solução que os Slots propõe não é boa o suficiente. Injetar conteúdo em um componente Slot mantém a lógica do que foi injetado dentro do componente pai e não no Slot. O que eu busco é mais uma composição do que uma forma de injetar dados em componentes.

#### Mixins não resolvem este problema?
De acordo com [Sebastian Markbåge](https://twitter.com/sebmarkbage) do React Team:
> [To be clear, mixins is an escape hatch to work around reusability limitations in the system. It’s not idiomatic React. Making composition easier is a higher priority than making arbitrary mixins work. I’ll focus on making composition easier so we can **get rid of mixins**](https://github.com/facebook/react/issues/1380#issue-31121026).

Para deixar claro: Eu uso mixins! Após ler o que esse cara tinha a dizer, resolvi procurar uma outra forma de compor esse novo componente sem usar mixins. Mixins, dependendo da forma que forem criados, podem fazer com que haja perda de contexto de onde usar aquele método ou estrutura. O fato de pensar em criar estruturas que contenham lógica de um componente em um arquivo de mixins não me agrada, então, Higher-Order Components é uma ótima solução.

#### Fontes
* [Meu artigo original em inglês no Medium](https://medium.com/tldr-tech/higher-order-components-in-vue-js-38b500c6d49f#.bga8w8o1a);
* [Mixins Are Dead. Long Live Composition](https://medium.com/@dan_abramov/mixins-are-dead-long-live-higher-order-components-94a0d2f9e750#.xjhx30toe) by [Dan Abramov](http://twitter.com/dan_abramov);
* [Presentational and Container Components](https://medium.com/@dan_abramov/smart-and-dumb-components-7ca2f9a7c7d0#.2zvg0wqtr) by [Dan Abramov](http://twitter.com/dan_abramov);
* [Vue.js #extends](http://vuejs.org/v2/api/#extends).

#### Agradecimentos:
* [Fabio Vedovelli](http://www.vuejs-brasil.com.br/author/vedovelli/) por levantar o questionamento sobre mixins;
* [Vinícius Reis](http://www.vuejs-brasil.com.br/author/vinicius/) por ajudar a melhorar o código original.
