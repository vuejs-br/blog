---
layout: post
title: 'Migração Vue 1 para Vue 2 com vue-migration-helper'
main-class: 'dev'
date: 2016-10-03 17:31:17 
color: '#637a91'
tags: vue vue2 migracao ferramentas
layout: post
author: 4
---

Com o release oficial do Vue 2 já podemos iniciar a migração de nossas aplicações do Vue 1 para o Vue 2. Minha primeira dica é realizar esta migração do seu projeto em um branch separado no seu repositório. 

A segunda dica é usar o **Vue Migration Helper**. Ele irá realizar uma busca pelos códigos Vue e apontar alterações que devem ser realizadas para que o Vue 2 possa funcionar.

**Instalação**

Para instalar o *Vue Migration Helper*, execute o seguindo comando no cnosole:

```
$ npm install --global git://github.com/vuejs/vue-migration-helper.git
```

Para usá-lo, execute o seguinte comando no diretório onde a sua aplicação está:

```
$ vue-migration-helper
```

Você obterá uma resposta semelhante à figura a seguir:

![](/content/images/2016/10/2016-10-03-14_19_44-npm.png)

Após realizar todas as alterações, você deverá abrir o arquivo `package.json` do seu projeto e alterar a versão do vue (e de outras bibliotecas também, como o vue-router). Deve-se alterar para algo do tipo:

```
"dependencies": {
    "vue": "^2.0.1",
    "vue-router": "^2.0.0",
    "vuex": "^2.0.0"
  }
```

Após alterar, execute novamente o comando `npm install` para atualizar todas as bibliotecas.
