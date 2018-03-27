---
layout: post
title: 'CRUD básico com Vue.js e json-server #3'
main-class: 'dev'
date: 2016-07-25 19:10:27 
color: '#637a91'
tags: vue-js components
layout: post
author: daniel-schmitz
---

Seguindo o [artigo anterior](http://www.vuejs-brasil.com.br/crud-basico-com-vue-js-e-json-server-2/), já estamos exibindo os primeiros registros de cervejarias na tela. Mas como ainda não existe a paginação, precisamos criar este componente.

Um componente de paginação precisa conhecer 3 variáveis:

- A quantidade total de itens
- A quantidade de itens por página a ser exibido
- A página atual que está selecionada

Crie o componente `Pagination.vue` e adicione o seguinte código:

```
<template>
    <nav class="pagination">
          <a class="button" v-show="showPreviousButton" @click="goPreviousPage()">Anterior</a>
          <a class="button" v-show="showNextButton" @click="goNextPage()">Próximo</a>
          <ul>
            <li>
              <a class="button" v-show="showPreviousButton" @click="goFirstPage()">1</a>
            </li>
            <li>
              <span v-show="showPreviousButton">...</span>
            </li>
            <li>
              <a class="button" v-show="showPreviousButton" @click="goPage(page-1)">{{page-1}}</a>
            </li>
            <li>
              <span class="button is-primary">{{page}}</span>
            </li>
            <li>
              <a class="button" v-show="showNextButton" @click="goPage(page+1)">{{page+1}}</a>
            </li>
            <li>
              <span v-show="showNextButton">...</span>
            </li>
            <li>
              <a class="button" v-show="showNextButton" @click="goLastPage()" >{{totalPages}}</a>
            </li>
          </ul>
        </nav>
</template>
<script>
  export default{
    props: ["total","page","itensPerPage"],
    computed: {
      totalPages: function(){
        return Math.ceil(this.total/this.itensPerPage)||1
      },
      showNextButton: function(){
       return  this.page!=this.totalPages
      },
      showPreviousButton: function(){
       return this.page!=1
      }
    },
    methods: {
      goNextPage: function(){
        this.$emit('change-page',this.page+1)
      },
      goPreviousPage: function(){
        this.$emit('change-page',this.page-1)
      },
      goFirstPage: function(){
        this.$emit('change-page',1)
      },
      goLastPage: function(){
        this.$emit('change-page',this.totalPages)
      },
      goPage: function(page){
        this.$emit('change-page',page)
      }
    }
  }
</script>
```

Neste código, usamos como base o componente de paginação do [bulma](http://bulma.io/documentation/components/pagination/) (somente a parte html). No código vue, criamos algumas variáveis que definem a quantidade de páginas, se é necessário exibir o botão "próximo" e se é necessário exibir o botão "anterior".

Perceba que estamos usando a reatividade do vue para exibir/ocultar os botões da paginação, bem como alterar o número das páginas.

Já os métodos contém as ações da paginação, como ir para a próxima página, ir para a última ou para a primeira. Estes métodos usam `this.$emit` que disparam um evento, que poderá ser capturado e tratado no componente pai:

![](https://i.imgur.com/MPH8czX.png)

Com o componente pronto, podemos adicioná-lo no componente Cervejarias.vue. Ele será inserido onde estava  "...paginação..." . A imagem acima mostra o lugar exato.

```
  <Pagination :total="total" :page="page" :itens-per-page="itensPerPage" @change-page="onChangePage"></Pagination>
```

Acima temos o uso das três `props` criadas, que devem possuir o ":" para que o databind do vue seja realizado, ou seja, quando `page` for alterado no componente cervejarias (pai), esta ação será replicada no componente Pagination (filho).

Quando for adicionar o componente Pagination no componente Cervejarias, não esqueça de adicionar a importação do mesmo:

```
  import Pagination from './Pagination.vue'
```

Além de, também,  adicionar a referência na propriedade `components`:

```
export default {
    data () {
      return {
        ...
      }
    },
    components: {
      Pagination
    },
    methods: {
      ...
```

Desta forma, temos o nosso componente de paginação pronto para uso! Até o próximo artigo, onde iremos implementar a busca.

> Pessoal, me desculpem pois usei um componente em português (Cervejarias) e outro em inglês (Pagination) :/ Não vou consertar esse problema agora porque já existem artigos publicados, mas tome nota que ou você usa tudo em inglês ou tudo português.





