---
layout: post
title: 'Criando um template com o vue-cli'
main-class: 'dev'
date: 2017-01-03 02:36:25 
description: derscricao
color: '#637a91'
tags: 
layout: post
introduction: introducao
---

O [vue-cli](https://github.com/vuejs/vue-cli) é uma ferramenta poderosa para a criação de templates para a iniciação de projetos.

Tive como objetivo criar um template usando o `vue-cli` que tivesse as seguintes especificações:

1. vue 2.0;
* vuex;
* vue-router;
* validações;
* componentes básicos;
* configuração básica do vuex;
* configuração básica do vue-router;
* arquitetura sustentável e escalável;
* uso do webpack.

Para que você possa criar um template `vue-cli`, basta clonar [este repositório git](https://github.com/vuejs-templates/webpack) e fazer as alterações dentro da pasta `template` que está neste repositório.

Para que eu pudesse fazer as alterações mencionadas acima, eu precisei:

1. Modificar o arquivo `package.json`;
* Modifiquei o arquivo `App.vue`;
* Alterei o arquivo `main.js` para que usasse todas os plugins mencionados;
* Criei um arquivo de configuração de rotas chamado `router-config.js`;
* Criei a estrutura necessária para que o projeto pudesse ser usado.

A arquitetura que montei para este template é essa:

```bash
├── src
│   ├── App.vue
│   ├── assets
│   │   └── logo.png
│   ├── common
│   │   ├── directives
│   │   │   └── masks.js
│   │   ├── functions
│   │   │   └── helpers.js
│   │   ├── resources
│   │   │   └── resources.js
│   │   └── validations
│   │       ├── email.js
│   │       └── social.js
│   ├── spa
│   │   ├── Hello.vue
│   │   └── Home.vue
│   └── vuex
│   │   ├── actions.js
│   │   ├── getters.js
│   │   ├── modules
│   │   │   └── example.js
│   │   ├── mutation-types.js
│   │   └── store.js
│   ├── main.js
│   └── router-config.js
├── index.html
└── package.json
```

Com essa arquitetura, temos:

* **common**. Diretório onde arquivos que são compartilhados por toda aplicação;
* **common/directives**. Diretivas Vue que podem ser usadas na aplicação;
* **common/functions**. Funções usadas na aplicação;
* **common/resources**. Resources para consumo de API Rest;
* **common/validations**. Validações customizadas que atendam às necessidades da aplicação;
* **spa**. Onde cada uma das páginas da SPA serão criadas;
* **vuex**. Todos os arquivos necessários para que o vuex funcione. Contempla actions, mutations, getters e a store;
* **vuex/modules**. Módulos do vuex que serão usados na aplicação.
* **`router-config.js`**. Arquivo que configura um objeto VueRouter para ser usada na aplicação. Todas as rotas encontram-se aqui. Este arquivo é o arquivo raíz de rotas, sendo assim, arquivos externos poderão ser importados e usados aqui;
* **`App.vue`**. Componente raíz da aplicação já com vue-router inciado, assim como, com transição `slide-fade` adicionada;
* **`main.js`**. Arquivo de confguração raíz da aplicação. Onde tudo inicia.

Se você quer ver o meu template e gostaria de melhorá-lo, por favor, basta acessar [este repositório](https://github.com/pablohpsilva/webpack-vuex-router/tree/master/template), dê um fork e envie - seu Pull Request.

Se você gostou ou está curioso e quer usar este template, basta instalar o [vue-cli](https://github.com/vuejs/vue-cli) e executar o seguinte comando:
```bash
$ vue init pablohpsilva/webpack-vuex-router
```

