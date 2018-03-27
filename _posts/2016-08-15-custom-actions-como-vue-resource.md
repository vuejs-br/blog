---
layout: post
title: 'Custom Actions com vue-resource'
main-class: 'dev'
date: 2016-08-15 12:01:52 
color: '#637a91'
tags: vue-js vue-resource
layout: post
author: leonardovilarinho
---

#### O que é?
O [vue-resource](https://github.com/vuejs/vue-resource) é um plugin do Vue.js para fazer requisições web e gerenciar respostas usando XMLHttpRequest ou JSONP. Este plugin é compacto, dá suporte a Promises, URI Templates, interceptors para request e response e funciona em todos os browsers modernos (sim, dá suporte ao IE9).

#### Problema
Durante o desenvolvimento de uma aplicação freelance, deparei-me com a mudança constante de URIs da API da empresa em questão. Como eu tinha vários códigos como este
```javascript
this.$http.get(`/api/url/que/nao/para/de/mudar/${user.id}`);
```
dentro de alguns componentes, eu lembrei que havia lido na documentação do próprio plugin que pode-se criar [Custom Actions](https://github.com/vuejs/vue-resource/blob/master/docs/resource.md) (*valeu* @danielschmitz) e "encapsular" recursos para serem usados depois.

Uma *Custom Action*, em suma, é criar uma extenção de ação padrão do HTTP e dar um novo sentido a ela, assim como determinar onde esta Custom Action acessará um recurso específico.

Para organizar o código, criei um arquivo contendo todos essas *Custom Action* e expus cada uma dessas para que a minha aplicação pudesse chamá-la quando fosse necessário. Desta forma, quando houver mudanças na API, o meu trabalho será modificar apenas um arquivo e, automaticamente, toda a minha aplicação entenderia a mudança e continuaria funcionando perfeitamente.

#### Exemplo

Abaixo encontra-se um exemplo do que eu fazia **antes**. Perceba que a URI do recurso está ligada a uma requisição. Imagine uma linha dessa para cada recurso espalhado numa aplicação. Ruim, né?
<iframe width="100%" height="300" src="//jsfiddle.net/t40Lcgqk/13/embedded/js,html,css,result/dark/" allowfullscreen="allowfullscreen" frameborder="0"></iframe>

Como comentei antes, o meu trabalho foi modularizar esses recursos em um arquivo como este:

```javascript
/**
 * Arquivo /resources/github.js
 */

const githubActions = {
    listCommits: { method: 'GET', url: 'https://api.github.com/repositories/:id/commits?per_page=5&sha=' }
};
export const githubResource = (resource) => resource('https://api.github.com/repositories/:id/commits?per_page=5&sha=', {}, githubActions);
```

Agora eu posso usar este recurso na aplicação da seguinte forma:
```javascript
import { githubResource } form './resources/github';

// ...

const gitResource = githubResource(this.$resource);

gitResource.listCommits({ id: '11730342' });

// ...
```

Para demonstrar que realmente funciona, aqui está um exemplo no JSFiddle:
<iframe width="100%" height="300" src="//jsfiddle.net/t40Lcgqk/14/embedded/js,html,css,result/dark/" allowfullscreen="allowfullscreen" frameborder="0"></iframe>
