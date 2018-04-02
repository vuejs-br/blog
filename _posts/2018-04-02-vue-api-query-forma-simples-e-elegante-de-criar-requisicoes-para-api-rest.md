---
layout: post
title: 'VUE API QUERY: Forma simples e elegante de criar requisições para API REST'
date: 2018-04-02 12:00:00 
tags: vue api query rest api nuxt
author: robsontenorio
---

# VUE API QUERY: Forma simples e elegante de criar requisições para API REST

<p align="center">
  <img src="https://raw.githubusercontent.com/robsontenorio/vue-api-query/master/bird.png" />  
</p>

Este pacote ajuda a construir rapidamente requisições para API REST. Mova sua lógica e requisições ao backend para classes dedicadas. Matenha seu código simples e elegante. 

🔥  Se você usa Laravel como backend, este pacote combina perfeitamente com [spatie/laravel-query-builder](https://github.com/spatie/laravel-query-builder).

# Repositório oficial

O conteúdo a seguir foi publicado como um artigo no site VUE JS BRASIL. Você deve acompanhar todas as futuras atualizações desta biblioteca diretamente no repositório oficial. 

🔗 https://github.com/robsontenorio/vue-api-query


# Uso básico

Devolva o resultado para determinados critédios, inclua algumas entidades, acrescente alguns campos extras e ordene-o!
```js
// GET /posts?filter[status]=ACTIVE&include=user,category&append=likes&orderBy=-created_at,category_id

let posts = await Post
  .where('status', 'ACTIVE')
  .include('user', 'category')
  .append('likes')
  .orderBy('-created_at', 'category_id')  
  .get()

```
Agora dê-me apenas a primeira ocorrência do resultado:

```js
// GET /posts?filter[status]=ACTIVE

let post = await Post
  .where('status', 'ACTIVE')
  .first()
```

Legal! Agora eu quero um objeto específico:

```js
// GET /posts/1

let post = await Post.find(1)
```


Edite isso e envie o objeto devolta ao backend:

```js
// PUT /posts/1 

post.title = 'Awsome!'
post.save()
```

Vamos criar um novo objeto e postá-lo:

```js
let post = new Post()

// ou

let post = new Post({title: 'Cool!'})


// POST /post

post.title = 'Another one'
post.save()
```

Nós podemos usar relacionamentos: 

```js

// GET /users/1
let user = await User.find(1)

// GET users/1/posts
let posts = await user
  .posts()
  .get()

```

# Instalação

```js
yarn add vue-api-query
```

## NUXT

Crie um plugin `~/plugins/vue-api-query.js`

```js
// injete a instância global do axios como cliente http do Model

import { Model } from 'vue-api-query'

export default function (ctx, injext) {  
  Model.$http = ctx.$axios
}
```

E registre-o em `nuxt.config.js`

```js
plugins: [
  '~plugins/vue-api-query'
]
```


## VUE

Configure em  `src/main.js`

```js
[...]

import axios from 'axios'
import { Model } from 'vue-api-query'

// injete a instância global do axios como cliente http do Model
Model.$http = axios

[...]
```

# Configuração

## Defina um modelo base

Seu modelo base deve estender da classe Model do pacote `vue-api-query`. Usar modelos base é uma boa prática uma vez que as configurações dos seus modelos de domínios são abstraídas. 

**models/Model.js**

```js
import { Model as BaseModel } from 'vue-api-query'

export default class Model extends BaseModel {

  // defina uma url base para a API REST
  baseURL () {
    return 'http://my-api.com'
  }

  // implemente o método de request padrão
  request (config) {
    return this.$http.request(config)
  }
}

```

## Defina seus modelos de domínio

Apenas estenda do seu modelo base ... e pronto! 

Ele automaticamente pluraliza baseado no nome da classe. Então, o recurso base da API REST para a classe `User` seria `/users`.


**models/User.js**

```js
import Model from './Model'

export default class User extends Model {

}
```

Se você precisa customizar o nome do recurso implemente o método `resource()`.

```js
import Model from './Model'

export default class User extends Model {

  resource()
  {
    return 'userz'
  }

}
```

Claro que você pode adicionar métodos extras e propriedades computadas desse jeito:

```js
import Model from './Model'

export default class User extends Model {
  
  // propriedades computadas são reativas -> user.fullname
  get fullname()
  {
    return `${this.firstname} ${this.lastname}`
  }

  // método -> user.makeBirthday()
  makeBirthday()
  {
    this.age += 1
  }

}
```

Você pode configurar relacionamentos:

```js
import Model from './Model'
import Post from './Post'

export default class User extends Model {

  posts () {
    return this.hasMany(Post)
  }
}
```

Tudo bem se, em algumas situações, você precisar chamar um recurso personalizado de um modelo já definido. Você pode sobrescrever dinamicamente o recurso padrão chamando o método `custom ()`.

```js
// GET /posts
let posts = await Post.get()

// GET /posts/latest
let latest = await Post
  .custom('posts/latest')
  .first()  
```

# Exemplo completo

**/models/Post.js**
```js
import Model from './Model'

export default class Post extends Model {
  // pronto :)
}
```
**/models/User.js**

```js
import Model from './Model'
import Post from './Post'

export default class User extends Model {  
  posts () {
    return this.hasMany(Post)
  }

  // propriedades computadas :)
  get fullname()
  {
    return `${this.firstname} ${this.lastname}`
  }

  // métodos :)
  makeBirthday()
  {
    this.age += 1
  }
}
```

Se o backend responde com ...

```js
// response from API for /users/1
{
  id: 1,
  firstname: "John",
  lastname: "Doe",
  age: 25
}
```

Nós podemos fazer isso:

```js
//GET /users/1
let user = await User.find(1)

console.log(user.fullname) // John Doe

user.makeBirthday()
user.save()
```

Então o método `save()` enviará de volta ao backend o seguinte payload:

```js
// PUT /users/1
{
  firstname: "John",
  lastname: "Doe",
  age: 26 //<--- alterado
}
```

Explore os relacionamentos:

```js
// GET /users/1
let user = await User.find(1)

// GET /users/1/posts
let posts = await user.posts().get()

// Sim, você pode fazer isso antes de recuperar os posts do usuário
let posts = await user
  .posts()
  .where(...)
  .append(...)
  .include(...)
  .orderBy(...)
  .get()
```

Você támbem pode fazer isso:
```js
//GET /posts?filter[status]=ACTIVE,ARCHIVED

let posts = await Post
  .whereIn('status', ['ACTIVE', 'ARCHIVED'])
  .get()

```

Se você gosta do estilo "promessa", faça assim:

```js

// objeto único

let user

User
  .where('status', 'ACTIVE')
  .first()
  .then(response => {
    user = response
  })

// array de objetos

let users

User
  .where('status', 'ACTIVE')
  .get()
  .then(response => {
    users = response
    
    // ou (dependendo da resposta do backend)

    users = response.data 
  })

```

E em alguma página/componente:

```js
<template>
  User: 
  <code>
    {{ user }}
  </code>

  Posts from user:
  <code>
    {{ posts }}
  </code>
</template>
<script>
import User from '@/models/User'

export default {
  data()
  {
    return {
      user: {},
      posts: {}
    }
  },
  async mounted()
  {
    this.user = await User.find(1)
    this.posts = await this.user.posts().get()
  }
}
</script>

```

# Paginação

```js
// GET /users?sort=firstname&page=1&limit=20

let users = await User        
        .orderBy('firstname')
        .page(1) 
        .limit(20)
        .$get() // algumas vezes você vai preferiar usar $get()

```

# Resposta do backend

Este pacote manipula automaticamente a resposta do backend e converte-a em uma instância de tal modelo.

## Objeto único

Se o seu backend responder com um único objeto como **ELEMENTO RAIZ** desse jeito:

```js
{
  id: 1,
  firstname: 'John',
  lastname: 'Doe',
  age: 25
}
```

Então, os métodos `find()` e `first()`  automaticamente converterão a resposta de backend em uma instância do modelo `User`.

```js
let user = await User.find(1)

// ou

let user = await User.first()

// funcionará, porque uma instância de User foi criada a partir da resposta

user.makeBirthday()
```

Isto **NÃO SERÁ** convertido em uma instância do modelo `User`, porque os dados principais não estão no elemento raiz.


```js
user: {  
    id: 1,
    firstname: 'John',
    lastname: 'Doe',
    age: 25
}
```

## Array de objetos

Um array de itens do backend seria convertido da mesma forma, **SOMENTE** se responder nesses formatos:


```js
let user = await User.get()
```

```js
// funciona - array de objeto é o elemento raiz
[
  {
    id: 1,
    firstname: 'John',
    lastname: 'Doe',
    age: 25
  },
  {
    id: 2,
    firstname: 'Mary',
    lastname: 'Doe',
    age: 22
  }
]
```

```js
// funciona - `data` existe na raiz e contém o array de objetos
{
  data: [
    {
      id: 1,
      firstname: 'John',
      lastname: 'Doe',
      age: 25
      },
    {
      id: 2,
      firstname: 'Mary',
      lastname: 'Doe',
      age: 22
    }
  ],
  someField: '',
  anotherOne: '',  
}

// Normalmente você lidaria com a resposta assim

let response = User.get()
let users = response.data


// ou assim

const { data } = User.get()
let users  = data

// mas você pode usar "fetch style request" com o método "$get()"

let users = await User
  .where('status', 'ACTIVE')
  .$get() // <---- AQUI
```

Isto **NÃO SERÁ** em uma array de modelos do tipo `User`.

```js
{
  users: [
    {
      id: 1,
      firstname: 'John',
      lastname: 'Doe',
      age: 25
      },
    {
      id: 2,
      firstname: 'Mary',
      lastname: 'Doe',
      age: 22
    }
  ],
  someField: '',
  anotherOne: '',  
}

```


# Agradecimentos

* Inspiração de [milroyfraser/sarala](https://github.com/milroyfraser/sarala).

* Elegância de [DavidDuwaer/coloquent](https://github.com/DavidDuwaer/Coloquent). 


Por quê outro pacote se já temos esses? Porque atualmente (março de 2018) eles restringem a resposta do backend à especificação JSON API.

# Contato

Twitter [@robsontenorio](https://twitter.com/robsontenorio)
