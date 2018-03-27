---
layout: post
title: 'Como usar o JSFiddle com Vue e Vue Resource'
main-class: 'dev'
date: 2016-07-08 11:40:01 
color: '#637a91'
tags: ferramentas
layout: post
author: daniel-schmitz
---

Existem vários "editores" html/javascript no mercado. Temos o codepen, jsfiddle, jsbin, Codenvy...

Neste artigo iremos usar o **JSFiddle**, não porque é o melhor ou pior, é apenas uma escolha. 

O JSFiddle divide-se em 3 partes: Html, Javascript e Css, onde pode-se escrever em cada uma delas, de acordo com a linguagem:

![](https://i.imgur.com/BN1yxxT.png)

A quarta parte é o resultado, ou seja, o código html+javascript+css juntos. Pode-se ver o resultado clicando no botão RUN, na barra superior:

![](https://i.imgur.com/qMbFDIa.png)

## Adicionando o Vue

Para a adicionar a biblioteca Vue ao JSFiddle, clique na engrenagem do código Javscript e escolha Vue 1.0.XX (ou a última versão), veja:

![](https://i.imgur.com/WfD2PKJ.png)

A partir deste momento, pode-se escrever código javascript usando oVue! Veja:

![](https://i.imgur.com/wsJHBzw.png)

Você pode inclusive misturar a classe Vue com outros códigos javascript:

![](https://i.imgur.com/jBO1aBb.png)

E até mesmo usar as novas funcionalidades do ES6:

![](https://i.imgur.com/ZguU1Pq.png)

## Adicionando outras libs

Além do vue podemos adicionar outras libs, como o vue-resource e o bootstrap. Primeiro, é preciso saber o endereço CDN de cada uma delas. Copie estes endereços e adicione, uma a uma, na aba **External Resources**:

![](https://i.imgur.com/YgtEMKz.png)

Por exemplo, o CDN do bootstrap é: https://maxcdn.bootstrapcdn.com/bootstrap/3.3.6/css/bootstrap.min.css

O CDN do Vue Resource é:
https://cdnjs.cloudflare.com/ajax/libs/vue-resource/0.9.3/vue-resource.min.js

Adicione estas 2 urls no External Resource, ficando semelhante a figura a seguir:

![](https://i.imgur.com/QbuvG4r.png)

Assim pode-se usar o bootstrap sem alterar muito o código html, veja:

![](https://i.imgur.com/ykY3GSu.png)

## Vue+Vue Resource

Assim que colocamos o cdn do Vue Resource no External Resources, podemos usar o `this.$http` para realizar chamadas ajax ao servidor, conforme o exemplo a seguir:


<iframe width="100%" height="300" src="//jsfiddle.net/c5d7few9/embedded/" allowfullscreen="allowfullscreen" frameborder="0"></iframe>

## Divulgando o seu código:

Após criar um código, basta clicar no botão Save, ou Update, e copiar a URL ! 



