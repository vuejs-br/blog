---
layout: post
title: 'Trabalhando com arquivos .env no Vue'
main-class: 'dev'
date: 2018-03-05 12:11:59 
color: '#637a91'
tags: vue webpack env devops configuracao
layout: post
author: 4
---

Uma dúvida interessante que recebi de um leitor foi em como trabalhar de forma correta com configurações distintas entre o servidor de desenvolvimento e o servidor de produção. Por exemplo, quando estamos em desenvolvimento, queremos acessar uma API REST que está também em desenvolvimento, muito possivelmente algo como *http://localhost:8080/api*, e quando estamos no servidor de produção, a url de acesso a api muda para algo como *https://www.seusite.com/api*, então é preciso encontrar uma forma **correta** de manipular estas informações.

> **Eba!** Toda segunda tem artigo sobre Vue no site vuejs-brasil.com. Quer sugerir um tema? Acesse nosso [fórum oficial](https://github.com/vuejs-br/forum/issues/7) e faça sua sugestão

## Objetivo deste artigo
Criar uma forma de manipular variáveis que mudam de acordo com o servidor de desenvolvimento e produção.

## Arquivos .env
No desenvolvimento de sistemas os arquivos ".env" (de environment) são responsáveis em armazenar informações que são sensíveis ao ambiente (desenvolvimento, testes e produção). 

## Utilizando env no Vue
Minha primeira dica para poder usar arquivos .env no vue é através do o **vue-cli**, criando uma app básica pronta. Recomendo usar o template *webpack* com as suas diversas opções de instalação.

Com o Node 8 ou superior instalado, digite no terminal:

```
npx vue-cli init webpack envtest
```

Isso irá criar uma aplicação com diversos arquivos prontos para uso. A dificuldade para quem ainda não está habituado com o webpack é saber o que cada arquivo representa. Neste artigo estamos focados apenas na configuração de ambiente.

Para a configuração do seu *enviroment*, analise o diretório *config*:

![image](https://user-images.githubusercontent.com/1509692/36630705-62054f70-1949-11e8-92c2-e7cadbe2a8c8.png)

Perceba dois arquivos no diretório config: dev.env.js e prod.env.js. Eles são usados no modo desenvolvimento e produção, ou seja, quando você está está executando a aplicação através do comando `npm run dev` o arquivo dev.env.js é utilizado, e quando você compila o projeto para produção através do comando `npm run build` o arquivo prod.env.js é utilizado. 

Vamos alterar cada arquivo da seguinte forma:

```js
'use strict'
const merge = require('webpack-merge')
const prodEnv = require('./prod.env')

module.exports = merge(prodEnv, {
  NODE_ENV: '"development"',
  ROOT_API: '"http://localhost/api"'
})
```

Este é o `dev.env.js`, com uma informação adicional chamada **ROOT_API**. Perceba ali um "merge(prodEnv" significando que as variáveis que estão no `prod.env.js` mas não estão no `dev.env.js` poderão ser utilizadas.

Vamos agora dar uma olhada no arquivo `prod.env.js`:

```js
'use strict'
module.exports = {
  NODE_ENV: '"production"',
  ROOT_API: '"http://www.site.com.br/api"'
}
```

Aqui temos a mesma ROOT_API, mas com o valor apontando para o site real, que deverá ser usada somente em modo de produção.

## Acessando as variáveis ENV no seu código

Após criar a variável ROOT_API, podemos usá-la em qualquer lugar do vue através do seguinte caminho:

```
process.env.ROOT_API
```

Vamos a um exemplo! Abra o arquivo `src/componentes/HelloWorld.vue` e no script adicione:

```
 mounted() {
      console.log(process.env.ROOT_API)
    }
```

Após executar `npm run dev` e o navegador abrir, você verá a informação no console do dev tools:

![image](https://user-images.githubusercontent.com/1509692/36630809-4d064ce4-194b-11e8-8653-8d95f7b9808c.png)

Se você executar o comando "npm run build", o diretório `dist` será criado com a aplicação pronta para ser enviada ao ambiente de produção, e a variável ROOT_API irá mostrar o valor `http://www.site.com.br/api`, conforme foi especificado em `prod.env.js`.

Dessa forma, podemos trabalhar com variáveis diferenciadas pelo ambiente, utilizando a configuração pronta que o template webpack nos fornece. Se você utilizar um outro template, certifique-se de encontrar esta funcionalidade.






