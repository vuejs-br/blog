---
layout: post
title: 'Comunicação entre componentes com Vue.js 2'
main-class: 'dev'
date: 2016-10-28 14:32:13 
color: '#637a91'
tags: 
layout: post
author: 9
---

Durante a [VanHackathon](https://www.vanhack.com/hackathon) eu tive alguns probleminhas pra entender como o Vue.js 2 tratava os eventos, visto que o meu tão querido *$dispatch* tornou-se obsoleto.

O motivo do *$dispatch* tornar-se obsoleto faz total sentido. Não há razão para mantê-lo, visto que o Vue.js 2 provê um [barramento de eventos](http://www.vuejs-brasil.com.br/usando-eventos-no-vue-js-2/) para a aplicação e uma nova forma de fazer comunicação entre componentes pai e filho. Com isso, temos no nosso template explicitamente quais eventos um determinado componente emite informação. 

### Esqueça *dispatch* e *events*. Vida longa ao *emit* e *v-on*!

O novo fluxo é o seguinte: Um componente filho emite um evento usando o *$emit*. No Vue.js 1 usando *$dispatch* ficaria assim:

```
this.$dispatch('chamou');
```

Agora você escreverá assim:
```
this.$emit('chamou');
```

No componente pai, deveríamos implementar um objeto `events`. Algo assim:
```
<!-- Pai.vue -->
<template>
    <filho></filho>
</template>
<script type="text/babel">
    // ...
    data() {
        frase: '',
    },
    events: {
        chamou() {
            this.respondeu();
        },
    },
    methods: {
        respondeu() {
            this.frase = 'Daqui a pouco eu vou! Me traga uma cerveja.';
        },
    },
    // ...
</script>
```

Agora **não** precisamos mais deste objeto. Tudo que precisamos fazer é usar o `v-on`, apontando qual evento o Pai.vue deve ouvir e qual método deve responder a aquele evento. Um exemplo:

```javascript
<!-- Pai.vue -->
<template>
    <filho v-on:chamou="respondeu"></filho>
</template>
<script type="text/babel">
    // ...
    data() {
        frase: '',
    },
    methods: {
        respondeu() {
            this.frase = 'Daqui a pouco eu vou! Me traga uma cerveja.';
        },
    },
    // ...
</script>
```

#### Vamos por partes.

Foque na linha 3. Nós temos o `v-on` sendo usado. Nós informamos qual evento ele deve ouvir do componente Filho.vue que, neste caso, é o evento `chamou`. Quando o `v-on` ouvir um evento `chamou`, o método `respondeu` será executado. Para não ficar super abstrato, o componente Filho.vue poderia ser implementado desta forma:

```javascript
<!-- Filho.vue -->
<template>
    <button v-on:click.stop="chamarPai">Chamar papai</button>
</template>
<script type="text/babel">
    // ...
    data() {
        frase: '',
    },
    methods: {
        chamarPai() {
            this.$emit('chamou');
        },
    },
    // ...
</script>
```

> Para o exemplo ficar mais fácil: 'Quando o Filho.vue chama o pai - `chamarPai()` - o Pai.vue ouve que alguém o `chamou` e responde - `respondeu()` - que: "Daqui a pouco eu vou! Me traga uma cerveja."'.

### Dica importante!

O Vue.js 2 não possui two-way databind com elementos e suas `props`! Ou seja, usar o `.sync` não funciona mais. Uma forma, ao meu ver, elegante de fazer essas modificações é usar este artigo para resolver o problema. Se uma propriedade precisa ser modificada pelo Filho.vue, faça-o enviar um evento com a mudança para o pai e trate a modificação no Pai.vue.


#### Leituras complementares

* Barramento de eventos: [Usando eventos no Vue.js 2.0](http://www.vuejs-brasil.com.br/usando-eventos-no-vue-js-2/), por Fabio Vedovelli
* Para saber mais sobre `v-on`: "[Comunicação entre componentes (V-ON) VueJs](http://www.vuejs-brasil.com.br/comunicacao-entre-componentes-via-eventos-vuejs-1-0/)", por Jorge Gonçalves Junior
* "[Custom events](http://vuejs.org/guide/components.html#Custom-Events)", vuejs.org
