---
layout: post
title: 'Vue.js em projetos não SPA'
main-class: 'dev'
date: 2016-09-27 03:00:00 
color: '#637a91'
tags: spa single-page-application web-components components php root-component
layout: post
author: vinicius
---

Vue.js é só uma lib, mas em vários [artigos](http://www.vuejs-brasil.com.br/vue-router/) e exemplos já mostramos como ele pode ser usado para criar SPAs complexos.

Por mais incrível que possa parecer, há pessoas que **não sabem ainda como usar Vue.js em projetos não SPA**. Esse post é para dar uma luz a essas pessoas.

##Iniciando uma aplicação.

> Recomendada a leitura de [**Maneiras de 'montar' uma instância de componente**](http://www.vuejs-brasil.com.br/maneiras-de-montar-uma-instancia-de-componente/)

Este é o *Hello world* clássico da documentação e muitos exemplos de Vue.js:

```javascript
// main.js
new Vue({
  el: '#app',
  data: {
    message: 'Hello Vue.js!'
  }
})
```

```html
<!-- Algum arquivo html -->
...
<body>
 <div id="app">
  {{ message }}
 </div>
...
```

Inicialmente e aparentemente essa é a maneira mais simples para se trabalhar com Vue.js: Ter um arquivo com o javascript e outro com seu HTML atuando como template.

Porém e você leu [Maneiras de 'montar' uma instância de componente](http://www.vuejs-brasil.com.br/maneiras-de-montar-uma-instancia-de-componente/), [Aplicações com VueJS: Pensando em componentes](http://www.vuejs-brasil.com.br/aplicacoes-com-vuejs-pensando-em-componentes/) e [Vue.js não é um Angular simplificado](https://blog.codecasts.com.br/vue-js-nao-e-um-angular-simplificado-6394c18cc689) sabe que não é bem assim...

## Componentes

A melhor maneira (e correta) de se trabalhar com Vue.js é com **componentes**, você já sabe que `new Vue({ ... })` cria um componente *root*, se você já esta desenvolvendo a algum tempo sabe que quando usamos o termo **root** em geral ele é **único**, como o nome sugere é a *raiz*, e só podemos ter uma raiz.

Uma confusão comum é criar vários `new Vue({...})` ligando cada um deles a um **id** do HTML, a ideia é que os elementos com esses *ids* atuaem como *templates* para diferentes partes do projeto.
Porém, o próprio Vue.js vai reclamar se não localizar esses *ids*/elementos.

### Body/Root
No lugar de se perder entre vários `new Vue({ ... })` e arquivos HTMLs soltos pela aplicação, crie uma instância **root** do Vue.js e registre os componentes que você criou. 

```javascript
// main.js
import Vue from 'vue'
import UsersTable from './components/Users/Table.vue'
import UsersForm from './components/Users/Form.vue'
import RootHeader from './components/Root/Header.vue' 

Vue.component('UsersTable', UsersTable)
Vue.component('UsersForm', UsersForm)

new Vue({
  // componentes locais que só existem e podem ser usados na raiz
  components: { RootHeader },
  // body ou outro elemento compartilhado em todas as páginas.
  el: 'body'
})
```

Com isso você pode usar facilmente seus componentes em qualquer lugar do seu HTML.

```html
<!-- Algum arquivo html -->
...
<body>
 <root-header></root-header>
 <users-table></users-table>
...
```

#### Props

Você também pode passar dados/parametros via [props](http://vuejs.org/guide/components.html#Props) livremente para seus componentes.

```html
<!-- Algum arquivo html/php -->
...
<body>
 <root-header 
   :is-admin="<?php echo isAdmin() ? 'true' : 'false' ?>">
 </root-header>
 
 <users-form 
    :user="'<?php echo json_encode($user) ?>'"
     base-url="<?php echo baseUrl() ?>">
 </users-table>
...
```

```javascript
// components/Users/Form.vue
// OMITTED
{
  props: {
   user: {
     required: true,
     type: Object,
     // http://vuejs.org/guide/components.html#Prop-Validation
     coerce(val) {
       return JSON.parse(val) // cast the value to Object
     }
   }
  }
}
// OMITTED
```

## Benefícios
Como você pode ver agora você esta trabalhando de verdade com componentes, o que por si só é uma vantagem.
E por usar componentes (principalmente [Single File Components](http://vuejs.org/guide/application.html#Single-File-Components)) você tem todos os benefícios de reuso e *workflow* proporcionados por eles.

Você fica no **melhor dos dois mundos** tendo a parte *"dinâmica"* da sua aplicação controlada pelo Vue.js enquanto outras partes continuam funcionando como antes (estática), ajuda até mesmo com o SEO.

Sistemas de template que usar a notação `{{ }}` passam a não interferir ou atrapalhar seu trabalho, afinal todos os `{{ }}` do Vue.js estarão dentro de arquivos `.vue`.

Esta é também uma boa abordagem para se migrar aplicações, já que você pode reaproveitar os componentes quando for criar uma aplicação *full-SPA*.

### Dica

Sabe o [**vue-cli**](https://github.com/vuejs/vue-cli)? Você pode usar ele para iniciar uma estrutura de projeto para você (recomendo [**browserify**](https://github.com/vuejs-templates/browserify) para esses casos), depois você copia e cola essa estrutura para onde fizer sentido dentro do seu projeto. Você pode remover os comandos de *dev/server*, provavelmente você não conseguirá usar eles na sua estrutura de projeto não SPA. 

Eu aconselho que seja uma estrutura separada e que tenha seu próprio *node_modules*. Deixe essa estrutura o mais isolada possível, afinal só o resultado de `src/main.js` que irá para produção e ter um *node_modules* separado vai facilitar.
Ajuste o local de *build* para sua pasta pública do projeto (aquela visível no navegador).

Pronto, você agora possui um projeto não SPA usando Vue.js da maneira mais simples e eficiente!

---------

Participe da comunidade

- https://telegram.me/vuejsbrasil
- http://slack.vuejs-brasil.com.br
- https://www.facebook.com/groups/vuejsbr/
- https://forum.codecasts.com.br/t/vuejs

---------

Se quiser saber mais sobre meu trabalho visite [codecasts.com.br](https://codecasts.com.br). Lá você vai ver vídeos sobre [Javascript](https://codecasts.com.br/lesson/domine-this-01-scopes), [jQuery](https://codecasts.com.br/lesson/javascript-jquery-vol1-01-resolvendo-o-problema), [Gulp](https://codecasts.com.br/lesson/gulp-level01-compilando-e-minificando-sass), [ES6](https://codecasts.com.br/lesson/ES6-00-o-que-e-es6), [Vue.JS](https://codecasts.com.br/lesson/vue-init-01-hello-world), [Docker](https://codecasts.com.br/lesson/docker-na-pratica-ola-docker) e muito mais.

-------

# That’s all, folks!
