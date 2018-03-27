---
layout: post
title: 'Vue.js 2: O que mudou?'
main-class: 'dev'
date: 2016-08-16 19:42:29 
color: '#637a91'
tags: 
layout: post
author: halfeld
---

Com a chegada do Vue 2 na versão RC (Release Candidate) já podemos dar uma olhada em geral nas mudanças que estão por vir. Primeiro, é preciso saber que houve sim alterações importantes no Vue 2, mas não uma completa reformulação da biblioteca (como aconteceu com Angular 2).

Se desejar testar o Vue.js 2, você deve usar o pacote vue@next na instalação via npm, da seguinte forma:

```
$ npm install vue@next
```

> Use o `vue@next` somente se a atual versão do Vue 2 for a RC. Talvez na data de leitura deste artigo o Vue 2 seja a oficial, então basta usar `npm install vue`.

## O que foi depreciado?

Um item é marcado como depreciado quando se torna obsoleto, ou seja, ele será removido muito em breve da api e não poderá mais ser usado. Então, é de extrema importância que você substitua o item por outro equivalente, geralmente comentado na documentação.

Muitas propriedades e métodos da API não serão mais usadas. A seguir uma lista das mais importantes:

### API Global

- Vue.config.debug (warnings estarão presentes no console por padrão)
- Vue.config.unsafeDelimiters (Use v-html)
- Vue.elementDirective (Use somente componentes)
- Vue.partial

### data

- props.coerce (Use variáveis computadas)

### Ciclo de vida da aplicação

Novos eventos:

- beforeMount
- mounted
- beforeUpdate
- updated
- activated
- deactivated

Eventos depreciados:

- Activate (movido para o vue-router)
- beforeCompile (use created)
- compiled (use mounted)
- atacched
- deatached


## Eventos com dispatch e broadcast 

Tanto `$dispatch` quanto `$broadcast` foram depreciados e não podem mais ser usados. Estes eventos eram usados para se repassar informações através dos componentes, tanto para seus filhos (e filhos dos filhos) quanto para os pais. 

Se você deseja compartilhar informações sobre componentes distintos que não são pai/filho, pode-se usar vuex ou outro sistema de eventos.

Os eventos `$on` e `$emit` continuam a existir, ou seja, é possível e perfeitamente aceitável que um componente filho dispare um evento para o seu componente pai.

## Laços com v-for

Uma das alterações no Vue 2 é que não se usa mais as variáveis `$index` e `$key`, que determinavam o índice e a chave do laço. Agora deve-se declará-las no laço, como por exemplo: `v-for="(value, index) in arr"`

## Diretivas perdem "poder"

O Vue 2 está caminhando para o uso contínuo de componentes, então as diretivas quase nunca são mais usadas. Dê sempre preferência a criação de componentes.

## Filtros

Filtros agora podem somente ser usados em `{{ }}`. Filtros em laços "v-for" ou `v-model` não serão mais suportados, que podem ser substituídos por propriedades computadas, como no exemplo a seguir:

```
<input type="text" v-model="filter">
<ul>
    <li v-for="item in filteredItems">{{ item }}</li>
</ul>
```
e
```
new Vue({
    el: 'body',

    data: {
        items: [],
        filter: ''
    },

    computed: {
        filteredItems() {
            var self = this
            return this.items.filter(function(item) {
                return item.indexOf(self.filter) > -1
            })
        }
    }
})
```

## Model

### lazy

O uso do `lazy` agora deverá estar associado ao model, como um modificador. Por exemplo, `v-model.lazy="foo"`.

### trim

Há um novo modificador para o `v-model`, o trim, que remove espaços em branco no início e final do valor.

### debounce

Debounce está depreciado e nao pode mais ser usado




