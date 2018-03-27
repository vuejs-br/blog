---
layout: post
title: 'Conheça a tag <template>'
main-class: 'dev'
date: 2016-07-13 13:28:32 
color: '#637a91'
tags: vue-js
layout: post
author: halfeld
---

Você sabia que o vue.js possui a tag `<template>` ? Ela é muito útil em coleções na qual não existe você não possui uma tag html associada. 

Por exemplo, fazer uma lista qualquer com o `<li>` é relativamente simples:

```
<li v-for="fruta in frutas">
...
</li>
```

Mas e se você deseja fazer uma lista um pouco mais complexa, que envolve um elemento `<h2>` e outro elemento `<p>`. O que fazer? Uma solução rápida e "suja" seria:

```
<div v-for="fruta in frutas">
 <h2>{{fruta.titulo}}</h2>
 <p>{{fruta.descricao}}</p>
</div>
```

Mas esta solução traz um problema filosófico: porque usar um elemento div "atoa" ? E se no css desse projeto toda div possui um fundo rosa? E se o google search bot não conseguir entender que o h2 que está logo ali dentro do div... 

Para este problema, o `<template>` é a solução, pois ele se encarregará de realizar corretamente o laço, sem a necessidade de um elemento html. Assim, temos:

```
<template v-for="fruta in frutas">
 <h2>{{fruta.titulo}}</h2>
 <p>{{fruta.descricao}}</p>
</template>
```

o que reproduzirá:

```
<h2>Fruta 1</h2>
<p>Descrição da fruta 1</p>
<h2>Fruta 2</h2>
<p>Descrição da fruta 2</p>
<h2>Fruta 3</h2>
<p>Descrição da fruta 3</p>
```
