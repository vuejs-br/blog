---
layout: post
title: 'CRUD básico com Vue.js e json-server #1'
main-class: 'dev'
date: 2016-07-15 11:26:55 
color: '#637a91'
tags: vue-js
layout: post
author: daniel-schmitz
---

Nesta sequência de artigos veremos como criar um CRUD completo utilizando Vue, Vue Resource e json-sevrer.

Neste primeiro artigo, será abordado o [json server](https://github.com/typicode/json-server), que é um servidor RESTfull que expõe uma API completa baseada apenas com um simples arquivo json.

Para instalar o json-server, recorremos ao npm, da seguinte forma:

```
npm install -g json-server 
```

> Use o `sudo` se estiver no linux

Instale o [vue-cli](https://github.com/vuejs/vue-cli) também, caso ainda não tenha instalado.

```
npm install -g vue-cli
```

Com o parâmetro -g,  instalamos o json-server globalmente. Após a instalação, usamos o vue-cli para criar o projeto Vue. Neste artigo, tanto cliente como servidor estarão em um mesmo projeto/diretório.

```
$ vue init browserify-simple#1.0 crud-vue
$ cd crud-vue
$ npm install
```

###### Vamos falar um pouco sobre o json-server

O  `json-server` é uma aplicação em node que simula uma API RESTfull com uma base de dados formada através de um arquivo simples, no formato JSON. O processo é muito simples, primeiro criamos um arquivo `json`, como por exemplo:


***db.json***
```
{
  "posts": [
    { "id": 1, "title": "json-server", "author": "typicode" }
  ],
  "comments": [
    { "id": 1, "body": "some comment", "postId": 1 }
  ]
}
```

Depois, iniciamos o servidor da seguinte forma:

```
$ json-server --watch db.json
```

Como temos duas "coleções" no arquivo json, que são *posts* e *comments*, após o servidor iniciar, temos já a disposição a seguinte API:

- `GET /posts` Obtém todos os posts
- `GET /posts/1` Obtém o post cujo id é 1
- `POST /posts` Adiciona um post à coleção
- `PUT /posts/1` Edita o post cujo id é 1
- `DELETE /posts/1` Deleta o post cujo id é 1

É possível, por exemplo, lidar com relacionamentos diretamente pela API. Por exemplo, `GET /posts?_embed=comments` irá trazer todos os posts e seus referidos cometários (perceba o "postId" na coleção comments).

###### Nosso banco
O "banco de dados" que iremos utilizar é o famoso *cervejarias*, no qual você deve obtê-lo neste link: 

https://raw.githubusercontent.com/danielschmitz/crud-vuejs/master/cervejarias.json

Salve este arquivo no diretório `crud-vue` onde o nosso projeto reside, e altere o arquivo `package.json` para que o servidor seja o *json-server* e não mais o *live-server*:

```
 "scripts": {
    "watchify": "...",
    "serve": "json-server --watch cervejarias.json --static ./",
    "dev": "...",
    "build": "..."
  },
``` 

Troque somente o item "serve". Se estiver confuso quanto ao arquivo de configuração leia este artigo: [Crie rapidamente um projeto Vue com vue-cli e browserify](http://www.vuejs-brasil.com.br/crie-rapidamente-um-projeto-vue-com-vue-cli-e-browserify/).

Depois da modificação do `package.json` e com o arquivo `cervejarias.json` no diretório vue, execute o projeto com `npm run dev`:

![](/content/images/2016/07/2016-07-15-08_13_27-npm-1.png)

Perceba que o servidor foi criado na porta 3000, então ao acessar `http://localhost:3000/breweries` teremos a resposta, em JSON, com as cervejarias. 

Temos, só com o arquivo json e o json-server, as seguintes ações já prontas:

**cerejarias**
```
GET    /breweries   #Obter todas as cervejarias 
GET    /breweries/1 #Obter cervejaria cujo o id é 1
POST   /breweries #Adiciona uma cervejaria na lista 
PUT    /breweries/1 #Edita a cervejaria cujo id é 1
DELETE /breweries/1 #Deleta a cervejaria cujo id é 1
```

**cervejas**
```
GET    /beers   #Obter todas as cervejas 
GET    /beers/1 #Obter cerveja cujo o id é 1
POST   /beers #Adiciona uma cerveja na lista 
PUT    /beers/1 #Edita a cerveja cujo id é 1
DELETE /beers/1 #Deleta a cerveja cujo id é 1
```

Isso significa que o servidor está pronto, e que já podemos focar no código vue para criar o nosso crud! Veremos isso no próximo artigo, até lá.


