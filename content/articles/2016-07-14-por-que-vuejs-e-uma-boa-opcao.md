---
layout: post
title: 'Por que VueJS é uma boa opção?'
main-class: 'dev'
date: 2016-07-14 14:47:23 
color: '#637a91'
tags: angular conceitos tecnologia web-components reactjs
author: vinicius
---

**Vue.JS** é um nome bem peculiar para uma biblioteca javascript, principalmente para nós brasileiros, o povo do *huehuebr*. Porém esse é o nome da *lib* javascript que tem chamado a atenção das comunidades de desenvolvimento nos últimos meses.

## O que é Vue.JS?
*Vue.JS*, *VueJS* ou simplesmente *Vue* é uma biblioteca (lib) javascript para o desenvolvimento de **componentes reativos para interfaces web modernas** (*Reactive Components for Modern Web Interfaces*).  
Nesse momento você pode ser perguntar: *O que isso significa?* 

### Componentes
Em resumo são "pedaços de código" que contém marcação, estilo e comportamento (*html*, *css* e *javascript*) e que juntos podem compor interfaces extremamente reaproveitáveis.

Uma das características dos *web components* é a possibilidade de usar eles como *tags* html customizadas (custom tags), sendo fácil de usar, ler e entender como uma interface (tela) esta sendo construída.

<script src="https://gist.github.com/anonymous/4397aed356af3a3bf6c1795b9978264b.js"></script>

Atualmente isso é o que há de mais moderno em construção de interfaces com javascript.

### Reativo
Infelizmente essa palavra ficou muito "ligada" ao ReactJS, porém essa técnica/característica não é exclusiva do ReactJS. Há outras bibliotecas e *frameworks* que implementam essa técnica.

![Reactivity in Depth](/content/images/2016/07/vue-reativo.png)
http://vuejs.org/guide/reactivity.html

Basicamente é observar um objeto javascript e refletir suas alterações no DOM do html.  
Quem já tentou isso com javascript puro ou até mesmo *jQuery* sabe que não é algo trivial, porém VueJS torna isso extremamente simples.

### Moderno

Se você não esteve em uma caverna nos últimos anos já ouviu falar do ReactJS.  
Há muitas semelhanças entre VueJS e ReactJS. VueJS compartilha semelhanças com muitas libs e frameworks que permitem criar componentes, isso inclui Angular2, porém pequenos detalhes fazem toda a diferença.

> Vale mencionar que VueJS não tem muitas semelhanças com Angular1, nem sendo considerado um concorrente para ele, já que a filosofia do Angular1 é completamente diferente da filosofia do VueJS e até mesmo Angular2.  

Como dito anteriormente VueJS possui características que fazem toda a diferença frente a seus concorrentes.

![](http://i.giphy.com/Qg1LsECZlMynS.gif)

#### Sintaxe e API claras
Criar componentes com VueJS é muito simples e objetivo. Sua API é intuitiva e simples, seu sistema de template pega o que já estamos acostumados e torna muito simples, previsível e agradável.   
O grande destaque esta em como o código javascript é escrito, tudo possui seu lugar de maneira clara. Mesmo ele sendo extremamente flexível os caminhos que a informação e código percorrem são extremamente previsíveis, sendo muito fácil trabalhar em equipe e usar componentes de terceiros.

![Você não corre o risco de ser esse cara](http://i.giphy.com/YFkpsHWCsNUUo.gif)

#### Flexibilidade
VueJS não é um "ditador". Ele te deixa livre para fazer uso dele da maneira que melhor convir ao seu projeto.   
Isso é uma característica muito importante nos projetos feitos  javascript.

> VueJS é uma lib javascript e não um framework, então você pode usar ele desde projetos pequenos a projetos maiores e mais complexos.

O fato dele não ser um *framework fullstack* pode deixar algumas pessoas com receito de usa-lo, porém ele possui um ecossistema de libs complementares muito bom, com destaque para [vue-router](https://github.com/vuejs/vue-router) (rotas spa), [vue-resource](https://github.com/vuejs/vue-resource) (http) e [vuex](https://github.com/vuejs/vuex) (flux para vuejs).

#### Performance
VueJS possui uma performance excelente, em alguns testes ele se saiu melhor do que o ReactJS ([comparing React.js to Vue.js for dynamic tabular data](https://engineering.footballradar.com/from-a-react-point-of-vue-comparing-reactjs-to-vuejs-for-dynamic-tabular-data/))  
E essa performance foi alcançada mesmo sem o VueJS fazer uso de *Virtual-DOM* como o ReactJS.

![](http://i.giphy.com/5rUNdEUmimikM.gif)

## VueJS para todos
Uma característica do javascript, e por consequência também do VueJS, é a capacidade de ser utilizado em qualquer tipo de projeto e tecnologia.   
Seu projeto pode estar sendo feito em Ruby, PHP, Python, Node, Java, Go ou qualquer outra linguagem, você pode usar VueJS.

Já há projetos usando VueJS com Electron ([cloudradioo-app](https://github.com/devfake/cloudradioo-app)), cordova ([Quasar Framework](http://quasar-framework.org/) e [vue-cordova](https://github.com/didierfranc/vue-cordova)) e muito mais em  [awesome-vue](https://github.com/vuejs/awesome-vue).

A curva de aprendizagem é uma das mais curtas. Para começar a usar VueJS basta importar um script via *cdn*, sem contar com o apoio da comunidade [Telegram](https://telegram.me/vuejsbrasil), [Slack](slack.vuejs-brasil.com.br) e [StackOverflow](http://pt.stackoverflow.com/questions/tagged/vuejs)

![Mesmo com pouco conhecimeto já da para começar](http://i.giphy.com/s0z685OFhWyuk.gif)

### Futuro
[VueJS 2.0 já esta em beta](https://twitter.com/vuejs/status/751173451554095105), mas não se assuste. Muitas pessoas se *traumatizaram* com Angular2, porém VueJS não corre esse risco.   
[Aqui](https://github.com/vuejs/vue/issues/2873) você tem acesso a todos os recursos que mudaram e as novas funcionalidades.

> Se você vem usa angular, leia esta post: [Vue.js para desenvolvedores AngularJS](http://www.vuejs-brasil.com.br/vue-js-para-desenvolvedores-angularjs-parte-1-logica-de-templates/)

A maior mudança será a implementação do VirtualDOM e o SSR (Server Side Render), com isso VueJS v2 será de 2x a 4x mais rápido que VueJS v1, e a migração será suave. Já há [projetos migrando para a versão 2](https://twitter.com/notphanan/status/751302784603918336) 

> VueJS é uma ferramenta feita pensando no desenvolvedor, na **nossa** experiencia de uso.

---------------
#### That’s all, folks!
