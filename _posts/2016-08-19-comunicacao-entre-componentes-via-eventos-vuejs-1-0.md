---
layout: post
title: 'Comunicação entre componentes (V-ON) VueJs'
main-class: 'dev'
date: 2016-08-19 12:00:00 
description: derscricao
color: '#637a91'
tags: vuejs
 -vue
 -events
 -v-on
 -components
layout: post
introduction: introducao
---

>Apesar que conter inúmeros artigos por aí a fora, poucos ou quase nenhum exemplifica uma maneira de comunicação entre componentes no Vue via `v-on`. 

>E neste artigo você verá de forma simples e objetiva como fazer isso! *Bora lá!*

### Cenário:

Digamos que você criou aqueles 2 (*dois*) componentes maneiros e colocou eles num modal show de bola! Há um botão de confirmação para algo que só você sabe... mas que está aí se matando ao lidar com ***event-hell***, ou tendo que capturar *quem foi o cara que disparou aquilo*.

Bem, eu tenho trabalhado com o Vue durante este último ano bem intensamente, e muitas coisas que fiz para atingir o objetivo acima eram nestes moldes:

```
events: {
  'algum-evento'(sender, data) {
    if(sender == 'esse cara sou eu!') {
      //é quem eu quero? 
      //entao bora! =D
    }
}
```

O **Vue** nos proporciona uma maneira fácil de "agrupar" os eventos que queremos observar, e isso fica óbvio com o bloco acima, não acha? Porém, imagina listar dezenas de métodos neste bloco... difícil né? Pode ser que não... mas a maneira que quero mostrar aqui é justamente uma maneira que encontrei de ***dar nomes aos bois*** sem que eu precise ficar avaliando quem foi que disparou tal evento.

Bom mas voltando ao seus componentes!

### Escovando bits:

Vou exemplificar os dois componentes: o primeiro, **foo**, é apenas aquele que exibe o tal modal, o segundo, **bar** é aquele que vai notificar o **foo** que ele confirmou algo, bem simples.

>O componente foo:
```
<script>
export default {
  data() {
    return {
      foo: {},
      showModal: false
    }
  },
  
  methods: {
    saveBar(bar) {
      //save bar
    },
}
</script>
<template>
  <div>
    <!-- AQUI IRÁ O COMP BAR -->
    <button @click="showModal = true">Open Bar</button>
  </div>
</template>
```

>O componente bar:

*Só uma pequena observação: não vou entrar no mérito de como montar o modal, há diversos artigos/screencasts que mostram como fazer, e há também o [Bootstrap](http://getbootstrap.com). O exemplo aqui é apenas "simular" =D.*

```
<script>
export default {
  data() {
    return {
      bar: {
        msg: 'Eu sou o Bar!'
      }
    }
  },

  methods: {
    confirm() {
      this.$emit('confirmed', this.bar)
    }
  }
</script>
<template>
  <div>
    <button @click="confirm">Confirmar</button>
  </div>
</template>
```

Observe o código acima: ao clicar no botão **Confirmar**, o componente **bar** irá disparar um evento via `emit` chamado **confirmed**.

Mas... como eu "capturo" este evento? 

Bem, eu mostrei como eu "fazia"... agora repare neste trecho do código do componente **foo**.

```
  <div>
    <!-- AQUI IRÁ O COMP BAR -->
    <button @click="showModal = true">Open Bar</button>
  </div>
```

Repare que não coloquei o componente **bar** ali propositalmente, e vamos fazer isso agora!

```
   <div>
    <bar v-on:confirmed="saveBar"></bar>
    <button @click="showModal = true">Open Modal</button>
  </div>
```

Agora observe a diferença: antes eu observava os eventos no bloco `events`, agora eu observo os eventos **diretamente** no componente filho via `v-on` ou `@` se preferir. O que eu estou dizendo ali é: "*quando o componente **bar** disparar o evento **'confirmed'** chame o método **'saveBar'** aqui no **foo***". 

***É isso!***


Até a próxima! Cya!
