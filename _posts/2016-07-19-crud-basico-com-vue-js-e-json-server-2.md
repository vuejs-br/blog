---
layout: post
title: 'CRUD básico com Vue.js e json-server #2'
main-class: 'dev'
date: 2016-07-19 13:12:34 
description: derscricao
color: '#637a91'
tags: vue-js
layout: post
introduction: introducao
---

Com o servidor/api prontos ([artigo anterior](http://www.vuejs-brasil.com.br/crud-basico-com-vue-js-e-json-server-parte-1/)) podemos começar a criar a tela com o crud de cervejarias.

Primeiro, é preciso adicionar o Vue Resource para acesso a api, um framework css (neste caso usaremos o bulma), e uma bibliotcea de ícones (font-awesome por exemplo).

```
npm i -S vue-resource bulma font-awesome
```

Após adicionar estas três bibliotecas, altere o arquivo index.html para que o css do bulma e do font-awesome sejam incorporados a sua aplicação:


```
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <title>crud-vuejs</title>
    <link rel="stylesheet" href="node_modules/bulma/css/bulma.css">
    <link rel="stylesheet" href="node_modules/font-awesome/css/font-awesome.min.css">
  </head>
  <body>
    <app></app>
    <script src="dist/build.js"></script>
  </body>
</html>
```

No arquivo `main.js`, precisamos adicionar o Vue Resource, da seguinte forma: 

```
import Vue from 'vue'
import App from './App.vue'
import VueResource from 'vue-resource'

Vue.use(VueResource)

new Vue({
  el: 'body',
  components: { App }
})
```

Para exemplificar o uso de componentes, crie o arquivo `src/Cervejarias.vue` com o seguinte código:

```
<template>Cervejarias</template>
<script>export default {
}
</script>
```

E, no arquivo da aplicação, `App.vue`, adicione este componente da seguinte forma:

```
<template>
  <div id="app">
    <Cervejarias></Cervejarias>
  </div>
</template>

<script>
  import Cervejarias from './cervejarias.vue'
  export default {
    components: {
      Cervejarias
    }
  }
</script>
<style>
  body {
    margin-top: 50px
  }
</style>
```

Agora podemos programar a tela que conterá as Cervejarias. No template, podemos criar um botão que irá indicar o acesso do cliente ao servidor. Você pode usar uma imagem de loading, uma tela modal etc. Com o bulma, podemos simplesmente usar:

```
<a class="fixo button is-large is-danger is-loading" v-show="loading">Loading</a>
```

A classe "fixo" foi criada no `<style></style>` do componente, veja:

```
<style>
  .fixo{float: right; margin-right: 10px; margin-top: 0px; z-index: 1000;}
</style>
```

O botão de "loading" possui a propriedade `isLoading` que controla a visibilidade do mesmo. 

Continuando com o template, após o botão, criamos uma div que conterá um título, uma barra de busca, e a tabela, veja:

```
<div class="container">
  <h1 class="title">{{title}}</h1>
  <div class="columns">
    <div class="column is-5">
      <p class="control has-addons">
        <input class="input is-expanded" type="text" placeholder="Procure pelo nome" v-model="search">
        <a class="button is-info" @click="searchBreweries">Search</a>
      </p>
    </div>
    <div class="column is-5">

    </div>
  </div>
  <div class="columns">
    <div class="column is-12">
      <table class="table is-narrow is-bordered">
        <thead>
          <th>Nome</th>
          <th>Cidade</th>
          <th>Telefone</th>
          <th>Mais</th>
          <th>Ações</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="brewery in breweries">
          <td>{{brewery.name}}</td>
          <td>{{brewery.city}}</td>
          <td>{{brewery.phone}}</td>
          <td class="is-icon">
            <a href="#">
              <i class="fa fa-map-marker"></i>
            </a>
            <a href="#">
              <i class="fa fa-plus-circle"></i>
            </a>
          </td>
          <td class="is-icon">

            <a href="#">
              <i class="fa fa-edit"></i>
            </a>
            <a href="#">
              <i class="fa fa-trash"></i>
            </a>
          </td>
        </tr>
      </tbody>
    </table>
    ...Paginação...
  </div>
 </div>
</div>
```

O título da página é formado pelo `{{title}}` que deverá ser informado no *data* doc omponente. Após o título, usamos um pouco do bulm framwork para criar uma caixa de texto para a busca. A caixa de busca observa a variável `search`, e o botão que executa a busca chama o método `searchBreweries`.

Após a busca incluímos a tabela, e no `<tbody>` usamos o `v-for` para fazer um loop na variável `breweries`, incluindo os dados das cervejarias. A princípio não vamos adicionar as funcionalidades nos links criados, como editar e apagar. Vamos deixar isso para outro artigo.

Agora vamos começar a programar o componente, lembrando que neste artigo iremos fazer da forma mais simples e rápida possível. Primeio, vamos configurar a propriedade *data*:

```
<script>
  export default {
    data () {
      return {
        isLoading: false,
        title: 'Vue.js Crud',
        search: '',
        breweries: [],
        page: 1,
        total: 0,
        selected: {},
        itensPerPage: 10
      }
    },
    ... (continua) ...
``` 

Uma explicação para cada variável:

- **isLoding** Uma flag para mostrar ou esconder o botão de "carregando" indicando uma atividade no servidor. 
- **title** O título do componente
- **search** Um bind para o campo de busca
- **breweries** A lista de cervejarias, lembrando que não carregamos todos os itens de uma vez só, apenas os itens daquela paginação. 
- **page** A página corrente da paginação de dados
- **total** A quantidade total de itens, total mesmo, todos os itens. É usada para calcular a quantidade de páginas
- **selected** Será o registro selecionado para edição/remoção
- **itensPerPage** A quantidade de itens a ser mostrada na página

Após criar os dados, podemos criar os métodos que manipulam esses dados. 


```
 methods: {
      showLoading(){
        this.isLoading=true;
      },
      hideLoading(){
        this.isLoading=false;
      },
      loadBreweries(){

        let t = this
        this.showLoading()

        let start = (this.page * this.itensPerPage) - this.itensPerPage
        let end = this.page * this.itensPerPage

        this.$http.get(`/breweries?_start=${start}&_end=${end}`).then(
         response=>{
           t.breweries = response.json()
           t.total = response.headers['X-Total-Count']
         },
         error=>{
           console.log(error)
         }).finally(function () {
          t.hideLoading();
        })

       },
       searchBreweries(){

       }
     },
```

Inicialmente temos os métodos `showLoading` e  `hideLoading`, que serão usados nos métodos que acessam o servidor. Depois, temos o método `loadBreweries`, que irá usar o Vue Resource para fazer uma requisição `this.$http.get` à url `/breweries`, repassando alguns parâmetros na própria url, que são:

- **_start** o registro inicial da consulta 
- **_end** o conjunto final da consulta

Através do `start` e do `end`, é possível realizar a paginação. tanto start quanto end são calculados previamente:

```
let start = (this.page * this.itensPerPage) - this.itensPerPage
let end = this.page * this.itensPerPage
```

Após a consulta ser realizada, um objeto Promise é retornado e o usamos para preencher a variável `breweries`. Fazemos isso da seguinte forma:

```
response=>{
 t.breweries = response.json()
 t.total = response.headers['X-Total-Count']
}
```

Neste código, a variável `t` foi definida no início do método (`let t = this`) e é usada para evitar problemas de escopo. A variável `t.breweries` recebe o conteúdo do response, devidamente formatado do JSON. A variável `t.total` recebe o valor total de registros da tabela, que o servidor enviar pelo cabeçalho.

Se houver algum erro, o promise `error` será chamado e, a princípio, emitimos apenas um erro no console. 

Finalizando o Promise de acesso ao servidor, temos o método `finally` que é executado independente do estado de retorno do Promise. Neste método, é chamada a função  `hideLoading` para esconder o botão *carregando...*

Até este momento, temos aqui uma tabela mas sem paginação, como na figura a seguir:

![](/content/images/2016/07/2016-07-15-15_33_37-crud-vuejs.png)

Precisamos então fornecer a tela um componente de paginação, que será visto no próximo artigo.

O componente Cervejarias.vue completo é exibido a seguir:


```
<template>
  <a class="fixo button is-large is-danger is-loading" v-show="isLoading">Loading</a>
  <div class="container">
    <h1 class="title">{{title}}</h1>
    <div class="columns">
      <div class="column is-5">
        <p class="control has-addons">
          <input class="input is-expanded" type="text" placeholder="Procure pelo nome" v-model="search">
          <a class="button is-info" @click="searchBreweries">Search</a>
        </p>
      </div>
      <div class="column is-5">

      </div>
    </div>
    <div class="columns">
      <div class="column is-12">
        <table class="table is-narrow is-bordered">
          <thead>
            <th>Nome</th>
            <th>Cidade</th>
            <th>Telefone</th>
            <th>Mais</th>
            <th>Ações</th>
          </tr>
        </thead>
        <tbody>
          <tr v-for="brewery in breweries">
            <td>{{brewery.name}}</td>
            <td>{{brewery.city}}</td>
            <td>{{brewery.phone}}</td>
            <td class="is-icon">
              <a href="#">
                <i class="fa fa-map-marker"></i>
              </a>
              <a href="#">
                <i class="fa fa-plus-circle"></i>
              </a>
            </td>
            <td class="is-icon">

              <a href="#">
                <i class="fa fa-edit"></i>
              </a>
              <a href="#">
                <i class="fa fa-trash"></i>
              </a>
            </td>
          </tr>
        </tbody>
      </table>
      ... Paginação ....
  </div>
</div>
</template>
<script>


  export default {
    data () {
      return {
        isLoading: false,
        title: 'Vue.js Crud',
        search: '',
        breweries: [],
        page: 1,
        total: 0,
        selected: {},
        itensPerPage: 10
      }
    },
    methods: {
      showLoading(){
        this.isLoading=true;
      },
      hideLoading(){
        this.isLoading=false;
      },
      loadBreweries(){

        let t = this
        this.showLoading()

        let start = (this.page * this.itensPerPage) - (this.itensPerPage - 1)
        let end = this.page * this.itensPerPage

        this.$http.get(`/breweries?_start=${start}&_end=${end}`).then(
         response=>{
           t.breweries = response.json()
           t.total = response.headers['X-Total-Count']
         },
         error=>{
           console.log(error)
         }).finally(function () {
          t.hideLoading();
        })

       },
       searchBreweries(){

       }
     },
     created(){
      this.loadBreweries();
    },
  }
</script>
<style>
  .fixo{float: right; margin-right: 10px; margin-top: 0px; z-index: 1000;}
</style>
```


