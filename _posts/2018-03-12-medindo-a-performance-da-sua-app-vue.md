---
layout: post
title: 'Medindo a performance da sua App Vue'
main-class: 'dev'
date: 2018-03-12 09:31:17 
color: '#637a91'
tags: vue performance devtools chrome firefox extensao plugin
layout: post
author: daniel-schmitz
---

Neste artigo iremos utilizar uma extensão para o Chrome/Firefox com o objetivo de medir a performance da sua aplicação Vue.

Em termos técnicos, a extensão irá medir estaticamente o desempenho dos componentes Vue baseado na métrica utilizada pela api do `window.performance`.

## Instalação
Para obter a extensão, use os seguintes links:

- [Chrome](https://chrome.google.com/webstore/detail/vue-performance-devtool/koljilikekcjfeecjefimopfffhkjbne)
- [Firefox](https://addons.mozilla.org/en-US/firefox/addon/vue-performance-devtool/)

> **Observação:** Se você utiliza o modo privado para testar as suas apps, certifique-se de habilitar a extensão para este modo também

## Criação do projeto

Se você não possui um projeto Vue para testar, use o comando a seguir para criar um. Vamos aproveitar um template um pouco mais complexo que o normal, baseado por exemplo na ui Vuetify:

```bash
$ npx vue-cli init vuetifyjs/webpack test-perf-app
```

## Configuração

Para ativar o plugin, é necessário abrir o arquivo que instância o Vue. Na maioria dos templates, ele está no arquivo `src/main.js`.

Imediatamente após a instanciação do Vue, adicione estas duas linhas:

```js
Vue.config.devtools = true
Vue.config.performance = true
```
## Uso

Com isso, você estará habilitando a extensão para que ela examine cada componente Vue. Após executar o seu projeto com `npm run dev`, abra o navegador e o modo desenvolvedor (F12), e navegue até o item *Vue Performance*, conforme exibido a seguir:

![](https://i.imgur.com/kt3DsGA.png)

Aqui vemos todos os componentes que foram criados pela app, juntamente com o tempo de cada ciclo, sendo eles:

- **Init**: O tempo entre o evento `beforeCreated` e `created`
- **Render**: O tempo utilizado para criar a instância no Javascript
- **Patch**: O tempo utilizado para o componente renderizar na DOM

Através destes três tempos é possível ter uma ideia de qual componente está no "gargalo", caso a sua aplicação esteja com problemas de performance. 

 
