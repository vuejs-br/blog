---
layout: post
title: 'Vue.js para desenvolvedores AngularJS – Parte 3 (Comunicação de componentes)'
main-class: 'dev'
date: 2016-07-21 19:14:00 
description: derscricao
color: '#637a91'
tags: 
layout: post
introduction: introducao
---

Comunicação de componentes (Parte 3)
Várias formas de se passar dados para outros componentes.
- One-way data binding  
- String literal prop  
- Two-way binding (native)  
- Two-way binding (components)  
- One-time binding  

- Citar o conceito de Vuex  
- Linkar com o artigo do Vedovelli

> Atenção: Quando passado um objeto ou array para um componente, ele é passado por referência. Neste caso se for modificado no componente filho, refletirá também no componente pai, então tenha em mente que se for qualquer outro tipo, a ligação de uma via (oneWay) funcionará como esperado. Isso vale tanto para o AngularJS, quanto para o Vue.js.

