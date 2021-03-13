---
layout: post
title: 'Vue.js 2.0 com duas builds?'
main-class: 'dev'
date: 2016-10-04 13:54:33 
color: '#637a91'
tags: vue2 vuejs
author: halfeld
---

Se você já começou a brincar com a nova versão do Vue, provavelmente ouviu falar de duas builds que estão sendo liberadas.

Esta foi uma medida inteligente já que se continuasse em uma build, haveria código desnecessário, tendo agora a **Standalone** e a **Runtime-only**.

As considerações sobre elas são as seguintes: 

+ **Standalone** - Suportando a opção de `template` , ela inclui tanto o **compiler** quanto o **runtime**, é usada quando você baixa o arquivo minificado do site ou puxa de um CDN por exemplo,
esta build funciona exatamente como na versão 1.0 do Vue.

> Além de também ter que confiar nas APIs dos browsers e não conseguir dar suporte ao Server Side Rendering

+ **Runtime-only** - Esta build não vem com o **compiler**, como o próprio nome diz, é só o **runtime**. Não suportando a opção de `template`, a única forma de renderização é através das [Render Functions](http://www.vuejs-brasil.com.br/render-functions-no-vue-js-2-0/) que por sua vez suportam a genial ideia dos Single File Components que são pré-compilados por um `vue-loader` quando usado com `webpack` ou por um `vuerify` quando usado com `browserify`, tendo assim a eliminação da necessidade de um compilador, fazendo com que essa build tenha incríveis 16kb min+gzip sendo cerca de 30% mais leve que a **Standalone.** É usada quando usamos o `vue-cli` por exemplo.

Então é isso galera! Isso é uma coisa que precisamos saber, mesmo que seja um pouco mais difícil usarmos a versão **Standalone**(meu caso :P) 
