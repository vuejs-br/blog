---
layout: post
title: 'Distribuição de conteúdo com Slots'
main-class: 'dev'
date: 2016-10-08 14:01:12 
color: '#637a91'
tags: slots vue-js
author: pablohpsilva
---

Em todos os meus artigos tento trazer algumas curiosidades ou soluções de problemas que tenho nas aplicações que desenvolvo diariamente. O problema resolvido a algumas semanas atrás era o seguinte: 

> Temos várias modais no sistema. Todas podem possuir um cabeçalho, um corpo e um rodapé. Gostaríamos de criar uma modal única que representasse todas as outras modais do sistema. Obviamente, o conteúdo da mesma seria modificado, de acordo com o contexto em que ela estivesse.

Pensamos em várias soluções, porém, um amigo de trabalho disse que tinha visto algo na documentação do Vue.js que solucionaria o problema. 

### Slots

A grosso modo, [Slots](http://vuejs.org/guide/components.html#Content-Distribution-with-Slots) são blocos no seu componente onde espera-se que conteúdo seja injetado. Sim, eu sei que isso é simples demais, mas aqui está um exemplo:
```html
<!-- Componente Modal -->
<template>
    <div class="modal">
        <div class="modal-header">
            <slot name="header"></slot>
        </div>
        <div class="modal-body">
            <slot name="body"></slot>
        </div>
        <div class="modal-footer">
            <slot name="footer"></slot>
            <slot>Olá, eu funciono como um "catch"!</slot>
        </div>
    </div>
</template>
```

Se a pergunta que você está se fazendo agora é "como de fato usar esse slot", olha só que legal:

```html
<modal>
    <span slot="header">Eu sou um header!</span>
    <span slot="body">Eu sou um body!</span>
    <span slot="footer">Eu sou um footer!</span>
</modal>
```

O resultado, após a modal ser renderizada, será este:

```html
<div class="modal">
    <div class="modal-header">
        <span slot="header">Eu sou um header!</span>
    </div>
    <div class="modal-body">
        <span slot="body">Eu sou um body!</span>
    </div>
    <div class="modal-footer">
        <span slot="footer">Eu sou um footer!</span>
    </div>
</div>
```

Perceba que no componente Modal eu tenho quatro slots: três nomeados e um anônimo. Perceba também que na renderização final o slot anônimo não apareceu. Como ele próprio já denota, ele é um slot tipo "catch", ou seja, se houvesse qualquer slot não nomeado ou com um nome não presente na modal, o conteúdo deste seria substituído no catch. Ou seja:

```html
<modal>
    <span slot="header">Eu sou um header!</span>
    <span slot="body">Eu sou um body!</span>
</modal>
```

removendo o slot "footer", a renderização final do componente Modal seria:
```html
<div class="modal">
    <div class="modal-header">
        <span slot="header">Eu sou um header!</span>
    </div>
    <div class="modal-body">
        <span slot="body">Eu sou um body!</span>
    </div>
    <div class="modal-footer">
        Olá, eu funciono como um "catch"!
    </div>
</div>
```

Abaixo temos um exemplo funcional de slots. Caso o conteúdo não apareça, [clique neste link](https://jsfiddle.net/pablohpsilva/ws2vohpu/2/).

<iframe width="100%" height="300" src="//jsfiddle.net/pablohpsilva/ws2vohpu/2/embedded/js,html,css,result/dark/" allowfullscreen="allowfullscreen" frameborder="0"></iframe>
