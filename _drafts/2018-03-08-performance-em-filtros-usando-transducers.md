---
layout: post
title: 'Performance em filtros usando transducers'
main-class: 'dev'
date: 2018-03-08 00:00:00 
description: derscricao
color: '#637a91'
tags: 
layout: post
introduction: introducao
---

A algumas semanas atrás escrevi um artigo sobre filtros dinâmicos em Vuejs. Este artigo é uma melhoria que encontrei e implementei. Os resultados foram incríveis e, mesmo que você não encontre este problema eu o encorajo a ler e entender como usar transducers.

Antes de continuar, gostaria de fazer um *disclaimer*:

> This article was based on some articles found on [medium](https://medium.com) specially the ones written by [Roman Liutikov](https://medium.com/@roman01la) (thank you Liutikov! You're awesome!).

Transducers (em português *Transdutores*) são funções compostas (*composable*) e eficientes que transformam dados **não** criando coleções intermediárias.

Veja as duas animacoes abaixo para compreender melhor o conceito:
<center>
![](/content/images/2016/07/chained.gif)
*Tres metodos chamados de forma encadeada, gerando uma colecao para cada chamada feita*
</center>
<center>
![](/content/images/2016/07/transduced.gif)
*Transducer usando tres metodos diferentes sem gerar colecoes intermediarias.*
</center>


