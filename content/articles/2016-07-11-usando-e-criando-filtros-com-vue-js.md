---
layout: post
title: 'Usando e criando filtros com Vue.js'
main-class: 'dev'
date: 2016-07-11 11:56:04 
color: '#637a91'
tags: vue-js
author: daniel-schmitz
---

Filtros são usados, na maioria das vezes, para formatar valores de *databind* (aqueles com {{ e }}). O exemplo a seguir irá pegar todo o valor de `msg` e transformar a primeira letra para maiúscula.

```html
 <div>
   {{ msg | capitalize }}
</div>
```

O nome do filtro a ser aplicado deve estar após o caractere *pipe* `|`. *captalize* é somente um dos filtros disponíveis. Existem os seguintes filtros pré configurados, veja:

**uppercase** 
Converte todas as letras para maiúscula

**lowercase** Converte todas as letras para minúscula

**currency** Converte um valor para moeda, incluindo o símbolo '$' que pode ser alterado de acordo com o seguinte exemplo:

```html
  {{ total | currency 'R$' }}
```

**pluralize** Converte um item para o plural de acordo com o valor do filtro. Suponha que tenhamos uma variável chamada `amount` com o valor 1. Ao realizarmos o filtro `{{ amount | pluralize 'item'}}` teremos a resposta "item". Se o valor `amout` for dois ou mais, teremos a resposta "items".

**json** Converte um objeto para o formato JSON, retornando a sua representação em uma string.

**debounce** Limitado para diretivas, adiciona um atraso em milisegundos no evento em questão, como por exemplo `<input @keyup="onKeyup | debounce 500">`

**limitBy** Limitado por diretivas, é usado para limitar os valores de um `v-for`, usado principalmente para prover paginações. O exemplo a seguir irá mostrar somente os 10 primeiros itens:

```html
 <div v-for="item in items | limitBy 10"></div>
```

E este exemplo exibe os itens de 5 a 15:

```html
 <div v-for="item in items | limitBy 10 5"></div>
```

**filterBy** Limitado a diretivas, realiza um filtro em loops, como o `v-for`. Vamos a alguns exemplos para exemplificar melhor este processo. 

```html
 <div v-for="item in items | filterBy 'hello'">
```

   Neste exemplo, somente valores que contém `hello` serão exibidos. Geralmente, o array `items` é um array de objetos (e não de strings), então para que possamos fazer um filtro em uma propriedade de um item do objeto, podemos fazer da seguinte forma:

```html
   <div v-for="user in users | filterBy 'Jack' in 'name'">
```

No caso acima, `users` é um array de objetos em que a propriedade `name` é filtrada pela string Jack.

No próximo exemplo, criamos uma lista de frutas e usamos o recurso de filtro para: 1) capitalizar os itens e 2) filtrar de acordo com o que for digitado em uma caixa de texto, veja:

```html
<div id="app">
  <input v-model="filterValue"/>
  <ul>
    <li v-for="fruit in fruits | filterBy filterValue in 'name'">
      {{fruit.name | capitalize}}
    </li>
  </ul>  
</div>
```

e

```js
new Vue({
	el:'#app',
  data:{
  	fruits:[
    	{name:'apple'},
      {name:'banana'},
      {name:'orange'},
      {name:'lemon'},
      {name:'grape'},
      {name:'rapberry '},
      {name:'coconut '},
      {name:'pear '}
    ],
    filterValue:''
  }
})
```

Este exemplo pode ser acessado pelo jsFiddle clicando [aqui](https://jsfiddle.net/danielschmitz/dy765x76/). nele, temos a criação da lista usando o filtro  `filterBy filterValue in 'name'` onde `filterName` é a caixa de texto ligada pelo `v-model`.

 Se houver necessidade de filtrar por mais campos, pode-se utilizar a seguinte expressão:

```html
 <li v-for="user in users | filterBy searchText in 'name' 'phone'"></li>
```

**orderBy** Limitada a diretivas, principalmente a `v-for`, é usada para ordenar os itens de um array. Os exemplos a seguir ilustram o processo:

```html
 <ul>
  <li v-for="user in users | orderBy 'name'">
    {{ user.name }}
  </li>
</ul>
```

 Para ordenar de forma decrescente, use:

```html
 <ul>
  <li v-for="user in users | orderBy 'name' -1">
    {{ user.name }}
  </li>
</ul>
```

Pode-se ordenar com dois ou mais valores:

```html
<ul>
  <li v-for="user in users | orderBy 'lastName'
            'firstName'">
    {{ user.lastName }}, {{ user.firstName }}
  </li>
</ul>
```

## Filtros personalizados

É possível criar filtros personalizados através do comando `Vue.filter`. O exemplo a seguir cria um filtro que irá inverter os caracteres de posição.

```js
Vue.filter('reverse', function (value) {
  return value.split('').reverse().join('')
})
```

Após a criação do filtro, pode-se usá-lo da seguinte forma:

```html
<span v-text="message | reverse"></span>
```

Um exemplo:

<iframe width="100%" height="340" src="//jsfiddle.net/nxa7zcaa/embedded/js,html,result/" allowfullscreen="allowfullscreen" frameborder="0"></iframe>

### Concatenar filtros

É possível concatenar filtros para que possam ser executados em série. A concatenação deve ser feita sempre utilizando o caracter pipe "|". O exemplo a seguir ilustra este processo:

```html
<li v-for="fruit in fruits | filterBy filterValue in 'name' | limitBy 3">
```

