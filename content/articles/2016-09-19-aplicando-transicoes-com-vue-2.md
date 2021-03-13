---
layout: post
title: 'Aplicando transições com Vue 2'
main-class: 'dev'
date: 2016-09-19 18:05:11 
color: '#637a91'
tags: vue2 transicao animacao css
layout: post
author: daniel-schmitz
---

Na versão 2 do Vue teremos um completo suporte às transições de elementos da DOM da aplicação, tanto para inserção, exclusão ou alteração. Nesse artigo veremos alguns passos introdutórios para a sua compreensão.

As transições que o vue pode suportar são:

- Transições aplicadas diretamente à classe CSS
- Integração com bibliotecas CSS, como o Animate.css
- Uso de javascript diretamente para manipular a DOM e aplicar a transição
- Integração com bibliotecas Javascript, como o Velocity.js

Neste artigo estaremos compreendendo um exemplo simples de como o Vue pode aplicar ao elemento uma classe CSS específica para determinar a transição que deve ser realizada naquele instante, quando o elemento é inserido ou removido da DOM (ou quando ele é apenas "escondido").

Primeiro, criamos uma simples instância do Vue com uma propriedade chamada "show":

```js
new Vue({
  el: '#demo',
  data: {
    show: true
  }
})
```

No nosso template html, criamos um botão que irá alternar o valor da propriedade `show`, e usamos o elemento `<transition>` para determinar que o vue observe os elementos que estarão neste elemento:

```
<div id="demo">
  <button v-on:click="show = !show">
    Toggle
  </button>
  <transition name="fade">
    <p v-if="show">hello</p>
  </transition>
</div>
```

Neste html, temos o elemento `<transition>` e nele temos um `<p>` que possui a condificional `v-if`, isto é, o elemento `<p>` será inserido ou removido da DOM dependendo do valor da propriedade `show`.

Com esses dois fatores, o vue passa a observar este elemento, e quando o valor de `show` muda, ele passa a adicionar classes CSS ao elemento, de forma dinâmica.

Estas classes CSS que irão determinar o comportamento do efeito, de acordo com a propriedade `name` do `<transition>`. Como usamos `name="fade"`, significa que podemos criar as classes `fade-enter-active`, `fade-leave-active`, `fade-enter` e `fade-leave-active`, da seguinte forma:

```
.fade-enter-active, .fade-leave-active {
  transition: opacity .5s
}
.fade-enter, .fade-leave-active {
  opacity: 0
}
```

> Se tivéssemos criado um `name=foo`, a classe CSS seria: foo-enter-active

Com isso já podemos testar o efeito, através do JSFiddle:

<iframe width="100%" height="300" src="//jsfiddle.net/danielschmitz/p7ez3zvf/embedded/" allowfullscreen="allowfullscreen" frameborder="0"></iframe>

Perceba que o efeito da transição está no CSS e não no Vue. O Vue se encarrega apenas de adicionar as classes no momento certo, e em conjunto com o CSS a "mágica" acontece! Ainda existem dezenas de funcionalidades extras em relação à transição e animação de elementos com o Vue, que deve ser estudada através da sua documentação, mas o passo inicial desse processo é compreender este exemplo apresentado. Bons estudos e até a próxima.



