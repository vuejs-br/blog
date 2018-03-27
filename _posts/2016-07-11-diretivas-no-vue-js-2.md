---
layout: post
title: 'Diretivas no Vue.js #2'
main-class: 'dev'
date: 2016-07-11 20:23:44 
color: '#637a91'
tags: vue-js diretivas
layout: post
author: 6
---

Continuando o assunto de como criar diretivas no Vue, vamos ver agora como fazer usando técnicas e propriedades mais avançadas. Caso você não leu a [parte 1](http://www.vuejs-brasil.com.br/diretivas-no-vue-js-1-2/) deste artigo, recomendo fortemente você dar um olhada para entender tranquilamente o que vou falar aqui.

> Tá esperando o que? começa logo :D

### Deep

Se sua diretiva precisa que um objeto seja passado, para que além de acessar suas propriedades faça determinada tarefa quando a mesma é mudada, é possível habilitar o `deep` como `true` e receber o objeto e as mudanças na Hook Function `update`, dessa forma:

```html
<div v-my-directive="obj"></div>
```

```javascript
Vue.directive('my-directive', {
  deep: true,
  update: function (obj) { }
})
```

A Hook Function `update` vai ser chamada sempre que houver mudanças em `obj`.

### Two Way

Com isso você pode "escrever um valor" de volta para a instância do Vue, permitindo você usar o `this.set(value)`.
Bastando apenas você settar o `twoWay` como `true`, olha só esse cara em ação:

<p data-height="366" data-theme-id="light" data-slug-hash="PzOwGN" data-default-tab="result" data-user="Halfeld" data-embed-version="2" class="codepen">See the Pen <a href="http://codepen.io/Halfeld/pen/PzOwGN/">TwoAway property on VueJS directive</a> by Igor Luíz (<a href="http://codepen.io/Halfeld">@Halfeld</a>) on <a href="http://codepen.io">CodePen</a>.</p>
<script async src="//assets.codepen.io/assets/embed/ei.js"></script>


### Accept Statement

Ele sendo passado como `true`, é possível escrever declarações inline.
Assim:

```html
<div v-my-directive="a++"></div>
```

```javascript
Vue.directive('my-directive', {
  acceptStatement: true,
  update: function (fn) {}
})
```

### Priority

Você pode colocar uma ordem de prioridade em suas diretivas que caso não informado é definido como valor padrão. `1000` para diretivas comuns e `2000` para diretivas terminais, as diretivas com maior número no atributo `priority` vão ser renderizadas mais cedo no elemento,  as  que tem o mesmo valor vão ser renderizadas na ordem que foram declaradas, embora essa ordem como diz na documentação não é garantida nos diferentes tipos browsers.
Um coisa que é preciso ter em mente é que as diretivas `v-if` e `v-for` tem sempre maior prioridade na compilação.

### Terminal

> 1.0.19+

O Vue compila o template andando recursivamente pela árvore do [Document Object Model (DOM)](https://www.w3.org/DOM/), entretanto quando encontra uma diretiva terminal, ele para de andar sobre seus elementos filhos tirando muito do trabalho na etapa de compilação. Tomando como exemplo, as diretivas `v-if` e `v-for` são terminais.
Escrever uma diretiva terminal é assunto bem avançado e você precisa ter um conhecimento legal do ciclo de compilação do Vue, mas no geral é especificar `terminal` como `true`.
Caso tenha alguma dúvida em como ciclo do Vue funciona é só dar uma olha aqui:

![ciclo de como o Vuejs funciona](http://vuejs.org/images/lifecycle.png)

bem... tendo muuitas dúvidas nessa imagem, faço um post explicando o ciclo de funcionamento do Vue, mas por hora é só na olhadinha mesmo xD

É isso aí pessoal, agora a imaginação é o limite.
Soltem a criatividade nas possibilidades de manuseio do DOM que vocês tem...


