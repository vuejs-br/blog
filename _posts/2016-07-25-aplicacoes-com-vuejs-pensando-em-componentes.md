---
layout: post
title: 'Aplicações com VueJS: Pensando em componentes'
main-class: 'dev'
date: 2016-07-25 12:18:08 
description: derscricao
color: '#637a91'
tags: web-components
 - components
 - vuex
 - flux
 - events
 - vue-js
 - single-page-application
layout: post
introduction: introducao
---

## O futuro é Lego!

Se você trabalha com desenvolvimento a algum tempo já sentiu a necessidade de reuso. Reuso de funções, classes, comportamentos, lógicas, regras de negócio e até *sistemas inteiros*.  
É de conhecimento comum que um bom programador é *preguiçoso*, pois entre muitas coisas ele odeia fazer a mesma coisa duas vezes.  
Seja isso verdade ou não, nós precisamos de reuso todos os dias em todos os projetos.

> Todo desenvolvedor tem o desejo de fazer um projeto com o máximo de reuso, onde se possa ir criando a aplicação como se estivesse usando legos, "encaixando" coisas umas nas outras.

Há diversas técnicas de reuso. Cada uma com sua vantagem e desvantagem, porém acredito que o maior problema estar em dar nome à essas técnicas. Afinal um componente ou módulo pode ser e, significar muitas coisas para muitos projetos e  desenvolvedores. Então precisamos começar definindo o que é um componente dentro do contexto do **VueJS** e consequentemente para projetos web criados com ele.

### Componentes

![componente](/content/images/2016/07/componente.png)

VueJS é uma biblioteca para se criar componentes, então ao criar uma aplicação com "VueJS" você estará criando uma aplicação com componentes. Isso é o mais próximo que se tem da "visão lego" de desenvolvimento web.  

> A principal diferença entre os componentes "VueJS" e o Lego é que você que esta criando as peças :)

Os componentes do VueJS são utilizados como **custom-tags do HTML**, permitindo criar uma composição de páginas/interfaces bem intuitiva e reutilizável.

#### Compondo componentes

Composição é a palavra chave para os componentes VueJS.
Inicialmente se assume que ao criar um componente você está criando ele para reuso, mas nem todo componente é para reuso. Um componente pode existir apenas para compor uma parte de outro componente por exemplo, ou até mesmo para ser usado só uma vez em todo o projeto.

> Ao criar componentes você está facilitando a organização e manutenção do projeto, não apenas o reuso.

Geralmente em projetos criados com componentes, você tem o componente **root/raiz**, que é comumente chamado de `App`. Depois disso você vai compondo **níveis** com outros componentes.

![componentes em uma aplicação](/content/images/2016/07/components.jpg)

VueJS possui **componentes globais**, que *existem* e podem ser usados por qualquer componente em qualquer lugar e momento. Ele permite também que você tenha **componentes locais**, que só existem dentro de um único local e/ou componente.

### Um por todos todos por um!

**Tudo** que você leu até agora se aplica à qualquer projeto baseado em componentes, seja ele *ReactJS* ou *Angular2*.  
Então o que de **especial** VueJS tem com relação aos componentes que essas outras ferramentas não tem?

Uma das premissas dos *web-components* é ele carregar tudo que precisa. Um componente carrega seu html, css e javascript (estrutura, estilo e comportamento). 
Os componentes do VueJS são feitos com **javascript puro**. Isso mesmo, você cria seus componentes como objetos javascript, isso inclui colocar a template e (se necessário) o css como propriedades de um objeto.

```javascript
// define
var WinterMessage = Vue.extend({
  template: '<div>The winter is comming!</div>'
})

// register (global)
Vue.component('winter-message', WinterMessage)

// root instance
new Vue({
  el: '#example'
})
```

```html
<div id="example">
  <winter-message></winter-message>
</div>
```

Uma template mais complexa não seria nada agradável de manter, e usar técnicas de carregamento externo de html [não são incentivadas pela comunidade](http://vuejs.org/2015/10/28/why-no-template-url/ "Why Vue.js doesn't support templateURL").

Para essa situação nós usamos os **[Single File Components](http://vuejs.org/guide/application.html#Single-File-Components)**. Uma solução extremamente elegante e simples para se criar componentes com VueJS.  
Trata-se de um arquivo com a extensão **.vue**, composto em até 3 partes: `script`,  `template`  e `style`.

![Single File Component](/content/images/2016/07/vue-component.png)

Pessoalmente, considero essa uma das melhores abordagens já criadas para se trabalhar com componentes. Outras bibliotecas como React e Angular2 *"misturam"* a sintaxe de html e css em arquivos **.js** deixando as coisas um pouco confusas, e ter mais 2 arquivos separados para encapsular esse conteúdo não é tão produtivo. Quando estamos trabalhando com **dezenas ou centenas de componentes**.  
Esse tipo de organização faz toda a diferença no dia-a-dia do projeto, incentivando a criação de cada vez mais componentes, deixando eles o mais *especializados* possível. 

Essa abordagem abre outras possibilidades, como usar *pré-processadores* de css, html e js, deixando você mais a vontade ainda com seus componentes, escrevendo na sintaxe que mais te agrada.

![pré-processadores](/content/images/2016/07/vue-component-with-pre-processors.png)

As possibilidades são inúmeras.

### Quem não comunica se *trumbica*

![sadness](http://i.giphy.com/33iqmp5ATXT5m.gif)

Nem tudo é tão simples como parece. Há um problema **muito** sério em projetos baseados em componentes: **a comunicação entre os componentes**.
Quem veio de angular pode não estar acostumado, mas sabe muito bem quando se depara com o **event-hell**, esse não é um problema exclusivo de componentes, a grande maioria dos projetos *SPA* passa por isso.

A comunicação primária entre os componentes se dá através de eventos, um componente *"pai"* envia e recebe eventos com dados dos componentes *"filhos"*. Isso é algo corriqueiro e simples. Você vai fazer muito uso de eventos durante o projeto.

O problema começa quando uma ação que ocorreu em um componente de nível *"baixo"* e precisa ser refletida em um componente de nível superior ou de *"topo"*. Nessa situação você facilmente e provavelmente vai cair no "event-hell", situação onde são tantos os eventos, *"disparadores"* e *"ouvintes"* que você fica perdido.

Para essa situação que a arquitetura **Flux** foi desenvolvida, no VueJS nós temos o **[Vuex](https://github.com/vuejs/vuex)** que é uma implementação do Flux.  
[Você pode saber mais sobre Vuex aqui](http://www.vuejs-brasil.com.br/vuex/).

Não é toda a aplicação que precisa do Vuex, porém a maioria acaba precisando dele. Pode parecer difícil ou estranho inicialmente, com o tempo você se adapta e vê o valor de usá-lo no seu projeto. 

-------------------------------

## Reforçando [TL;DR]

- Componentes encapsulam html, css e javascrip (estrutura, estilo e comportamento).
- Você usa componentes para compor interfaces/sistemas.
- Um componente não precisa ser de reuso (ser usado mais de uma vez em mais de um local).
- Componentes podem possuir componentes internos.
- Um dos principais objetivos dos componentes é a organização e manutenção.
- Use **.vue** para criar seus componentes ([Single File Components](http://vuejs.org/guide/application.html#Single-File-Components)).
- Cuidado com o *event-hell*, procure usar [Vuex](https://github.com/vuejs/vuex).

-------------------------------

#### That’s all, folks!
