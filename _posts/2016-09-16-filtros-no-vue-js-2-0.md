---
layout: post
title: 'Filtros no Vue.js 2.0'
main-class: 'dev'
date: 2016-09-16 13:09:23 
description: derscricao
color: '#637a91'
tags: filters
 -filtros
 -vue2
 -vue-js
 -vue-js2
 -vue-2-0
 -vue-js-2-0
layout: post
introduction: introducao
---

Uma coisa muito útil são filtros, mas não confunda-os com diretivas, já vi uma galera aí tentando modificar o valor de um input com eles xD

Enfim, é muito simples usar eles no Vue e agora na segunda versão ficou mais fácil ainda. Não teve muitas mudanças, mas existem alguns poréns...

Eles são 3 basicamente, o primeiro é:

Você **só** poderá usar eles dentro da interpolação de mustaches(`{{}}`), nada de usar isso em diretivas como o `v-for` ou `v-model`, isso foi devido a complexidade que ficava, agora a responsabilidade foi passada para as **computed properties** que você consegue filtrar algo que necessite de mais tratamentos facilmente, já que é puro javascript.

o segundo é:

**Sem filtros embarcados**, isso quer dizer, nada de `orderBy`, `filterBy`, `uppercase`...
Caso você precise deles basta criar ou recorrer a libs de terceiros(apesar que você não poderia usar o `orderBy` e `filterBy` no `v-for` mesmo), masss a facilidade de criar é incrível!

e o terceiro porém é:

Caso passe parâmetros, **use o filtro como uma função javascript**!
Isso mesmo, o Vue nessa segunda versão tem amostrado uma API mas parecida como o js faz as coisas, não é como uma camada de abstração no meio(apesar que na primeira versão já era muito simples).

em quanto antes você passava parâmetros assim: 

```javascript
<span>{{message | say 'Igor' 'Luíz'}}</span>
```

agora usa assim:

```javascript
<span>{{message | say('Igor','Luíz')}}</span>
```

e esses são os poréns, que acabam melhorando a forma de fazermos nossas aplicações.

O modo como se criam os filtros é o mesmo, como eu disse as grandes mudanças foram esses poréns, mas caso quera saber como criar eles, estou fazendo uma [serie sobre Vue 2.0](https://www.youtube.com/playlist?list=PLFtCenSt_W2Fxgh1fjjwXK20qg2MdC2wp) e já tem o vídeo que fala sobre filtros, então corre lá qué de grátis xD

É isso pessoal, apesar da minha vida estar um pouco conturbada ultimamente, vou trazendo coisas sobre o Vue 2.0 aqui :D
