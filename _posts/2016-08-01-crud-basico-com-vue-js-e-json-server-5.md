---
layout: post
title: 'CRUD básico com Vue.js e json-server #5'
main-class: 'dev'
date: 2016-08-01 12:21:33 
color: '#637a91'
tags: vue-js
layout: post
author: halfeld
---

Com a parte de [leitura da tela pronta](http://www.vuejs-brasil.com.br/crud-basico-com-vue-js-e-json-server-4/) (ler os dados, paginar e realizar a busca), podemos iniciar a codificação para inserir e editar as cervejarias. Esta codificação irá alterar bastante o código `Cervejarias.vue`, de forma que iremos a princípio mostrar quais são estas modificações, e no final do artigo mostrar o código por completo.

Para inserir ou editar um item, usaremos o recurso de janela modal do bulma. A criação da janela é feita através de uma `div` com a classe `modal`, e a sua visibilidade é controlada através da classe `is-active`:

```html
<div class="modal" :class="{'is-active':showModal}">
  <div class="modal-background"></div>
  <div class="modal-card">
    <header class="modal-card-head">
      <p class="modal-card-title">Cervejaria: {{selected.name}}</p>
      <button class="delete" @click.prevent="showModal=false"></button>
    </header>
    <section class="modal-card-body">

    <div class="columns">
      <div class="column">
        <label class="label">Nome</label>
          <p class="control">
            <input class="input" type="text" placeholder="Text input" v-model="selected.name">
          </p>
      </div>
      <div class="column">
         <label class="label">Código</label>
    <p class="control">
      <input class="input" type="text" placeholder="Código" v-model="selected.code">
    </p>
      </div>
      </div>

      <label class="label">Descrição</label>
      <p class="control">
        <textarea class="textarea" placeholder="Textarea" v-model="selected.descript"></textarea>
      </p>
      
   <label class="label">Website</label>
    <p class="control">
      <input class="input" type="text" placeholder="Text input" v-model="selected.website">
    </p>
  

    </section>
    <footer class="modal-card-foot">
      <a class="button is-primary" @click.prevent="saveBrewery">Salvar</a>
      <a class="button" @click.prevent="showModal=false">Cancelar</a>
    </footer>
  </div>
</div>
```

Veja que, `:class="{'is-active':showModal}"` controla a visibilidade da janela através da variável `showModal`, que deve ser adicionada a lista de variáveis do componente:

```
    data () {
      return {
        isLoading: false,
        title: 'Vue.js Crud',
        search: '',
        breweries: [],
        page: 1,
        total: 0,
        selected: {},
        itensPerPage: 10,
        showModal:false
      }
```

O formulário da cervejaria possui poucos campos, para que esta parte inicial não seja tão complexa. O formulário resulta em algo semelhante à figura a seguir:

![](https://i.imgur.com/uMZEd9v.png)

Neste formulário, temos apenas os campos Nome, Código, Descrição e Website. 

Para que este formulário apareça, é necessário alterar a variável `showModal`. Fazemos isso no botão de edição de cada linha da tabela, da seguinte forma:

```
<a href="#" @click.prevent="editBrewery(brewery)">
  <i class="fa fa-edit"></i>
</a>
```

O método `editBrewery` contém o seguinte código:

```
methods:{
      ...,
       editBrewery(brewery){
        this.selected=brewery
        this.showModal = true;
       },
      ...
```

Veja que alteramos a variável `selected`, repassando o objeto `brewery` que é o mesmo objeto que representa a "linha" da "tabela". 

Agora o objeto selected possui os dados da cervejaria que está sendo editada. Quando o usuário clicar no botão para fechar a janela, ou no botão cancelar, executamos o seguinte código:

```
<a class="button" @click.prevent="showModal=false">Cancelar</a>
```

Ou seja, usamos a reatividade do Vue para "fechar" a janela, na verdade nós apenas a escondemos.

O botão salvar irá realizar a edição ou inclusão da cervejaria, veja:

```
methods:{
  ...,
saveBrewery(){
        if (this.selected.id!=null){  //EDIT
          this.$http.put(`/breweries/${this.selected.id}`,this.selected).then(
            response=>{
              this.$set('selected',{})
              this.$set('showModal',false)
            },
            error=>{
              console.error(error)
            }
            ).finally(
              this.loadBreweries()
            )
          }
          else
          { //NEW
            this.$http.post(`/breweries`,this.selected).then(
            response=>{
              this.$set('selected',{})
              this.$set('showModal',false)
            },
            error=>{
              console.error(error)
            }
            ).finally(
              this.loadBreweries()
            )
          }
       },
 ...
```

Neste código, verificamos a existência do `{selected.id}`, pois é ele que define se estamos incluindo um novo item ou editando. Se for uma edição, ou seja, existe um `selected.id`, usamos o vue resource e fazemos uma chamada PUT a url `/breweries/id` repassando o selected e, quando o servidor responder, pode-se esconder a janela modal novamente. Veja que usamos o método `finally` para chamar novamente o `loadBreweries`, para recarregar a tabela.

Se for um novo registro, realizamos um POST repassando o objeto `selected`.

Para finalizar, basta adicionar um botão "Novo" que irá criar uma instância vazia do `selected` e abrir a janela modal, veja:


```
<a class="button is-info" @click.prevent="newBreweries">Novo</a>
```

e
```
 newBreweries(){
        this.selected={}
        this.showModal = true;
       },
``` 

O código completo do componente é exibido a seguir:

```
<template>
  <a class="fixo button is-large is-danger is-loading" v-show="isLoading">Loading</a>
  <div class="container">
    <h1 class="title">{{title}}</h1>
    <div class="columns">
      <div class="column is-5">
        <p class="control has-addons">
          <input class="input is-expanded" type="text" placeholder="Procure pelo nome" v-model="search">
          <a class="button is-info" @click.prevent="searchBreweries">Search</a>
        </p>
      </div>
      <div class="column is-6">
         
      </div>
      <div class="column is-1">
        <a class="button is-info" @click.prevent="newBreweries">Novo</a>
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

              <a href="#" @click.prevent="editBrewery(brewery)">
                <i class="fa fa-edit"></i>
              </a>
              <a href="#">
                <i class="fa fa-trash"></i>
              </a>
            </td>
          </tr>
        </tbody>
      </table>
      <Pagination :total="total" :page="page" :itens-per-page="itensPerPage" @change-page="onChangePage"></Pagination>
    </div>
  </div>
</div>

<div id="modal_brewery" class="modal" :class="{'is-active':showModal}">
  <div class="modal-background"></div>
  <div class="modal-card">
    <header class="modal-card-head">
      <p class="modal-card-title">Cervejaria: {{selected.name}}</p>
      <button class="delete" @click.prevent="showModal=false"></button>
    </header>
    <section class="modal-card-body">

    <div class="columns">
      <div class="column">
        <label class="label">Nome</label>
          <p class="control">
            <input class="input" type="text" placeholder="Text input" v-model="selected.name">
          </p>
      </div>
      <div class="column">
         <label class="label">Código</label>
    <p class="control">
      <input class="input" type="text" placeholder="Código" v-model="selected.code">
    </p>
      </div>
      </div>

      <label class="label">Descrição</label>
      <p class="control">
        <textarea class="textarea" placeholder="Textarea" v-model="selected.descript"></textarea>
      </p>
      
   <label class="label">Website</label>
    <p class="control">
      <input class="input" type="text" placeholder="Text input" v-model="selected.website">
    </p>

    </section>
    <footer class="modal-card-foot">
      <a class="button is-primary" @click.prevent="saveBrewery">Salvar</a>
      <a class="button" @click.prevent="showModal=false">Cancelar</a>
    </footer>
  </div>
</div>
</template>

<script>
  import Pagination from './Pagination.vue'

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
        itensPerPage: 10,
        showModal:false
      }
    },
    components: {
      Pagination
    },
    methods: {
      onChangePage(page){
        this.page = page
        this.loadBreweries()
      },
      showLoading(){
        this.isLoading=true;
      },
      hideLoading(){
        this.isLoading=false;
      },
      loadBreweries(){

        let t = this
        this.showLoading()

        let start = (this.page * this.itensPerPage) - (this.itensPerPage)
        let end = this.page * this.itensPerPage
        let qString = "";

        if (this.search){
          qString = `&q=${this.search}`
        }

        this.$http.get(`/breweries?_start=${start}&_end=${end}${qString}`).then(
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
        this.loadBreweries()
       },
       newBreweries(){
        this.selected={}
        this.showModal = true;
       },
       editBrewery(brewery){
        this.selected=brewery
        this.showModal = true;
       },
       saveBrewery(){
        if (this.selected.id!=null){  //EDIT
          this.$http.put(`/breweries/${this.selected.id}`,this.selected).then(
            response=>{
              this.$set('selected',{})
              this.$set('showModal',false)
            },
            error=>{
              console.error(error)
            }
            ).finally(
              this.loadBreweries()
            )
          }
          else
          { //NEW
            this.$http.post(`/breweries`,this.selected).then(
            response=>{
              this.$set('selected',{})
              this.$set('showModal',false)
            },
            error=>{
              console.error(error)
            }
            ).finally(
              this.loadBreweries()
            )
          }
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

Caso você deseje ver as alterações desta parte em relação ao artigo anterior, [clique neste link para ver o diff no github](https://github.com/danielschmitz/crud-vuejs/commit/892ae6d9da244245e043bc3a731c447c49d9a249).

O resultado da edição é exibido a seguir:

![](/content/images/2016/07/Animation.gif)


