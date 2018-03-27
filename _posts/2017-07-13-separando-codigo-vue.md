---
layout: post
title: 'Separando arquivos de código em produção'
main-class: 'dev'
date: 2017-07-13 16:45:04 
color: '#637a91'
tags: vue2 webpack desempenho
layout: post
author: daniel
---

Atualmente, com tantas opções *online* para resolver um mesmo problema, o usuário acaba optando por usar sites com o carregamento rápido, prova disso é essa reportagem do Uol de 2011: [Maioria dos usuários espera só 5 segundos para site abrir no celular](https://tecnologia.uol.com.br/ultimas-noticias/redacao/2011/07/27/internautas-moveis-esperam-so-5-segundos-pelo-carregamento-de-um-site-diz-pesquisa.jhtm).

Se em 2011 já encontrávamos esse cenário, 6 anos depois as coisas se tornaram 'pior', com sites cada vez mais velozes, a esperado do usuário acaba se tornando ainda mais restrita, e esse é um problema muito comum no mundo do *Vue*.

Ao compilar o seu sistema com o comando `npm run build`, é gerado o arquivo `build.js`, que em seus melhores dias apresenta cerca de 400Kb de tamanho.

Em uma conta rápida, supomos que 70% dos usuários usam o 3G para acessar a internet no telefone, que a velocidade média de uma conexão 3G em aparelhos com cota fica em torno de 150Kb/s e sem cota em torno de 40Kb/s (sendo generoso).

Sabemos que 90% deles nunca têm cota por conta do grande acesso a aplicativos de mídia social. Logo, para apenas 14,3% desses 70% o site se carregaria em menos de 5 segundos.

Então, de acordo com a informação do Uol e a conta tosca, menos da metade dos usuários esperariam um site feito com o *Vue* (puro) carregar no telefone.

Visando melhorar isso, e poder usar o *Vue* em projetos que preciso de agilidade, pesquisei um pouco até encontrar a técnica de **code splitting**. No webpack, ela se define em separar trechos de códigos independentes, em arquivos denominados **chunks**.

Então sem mais delongas, vamos criar nossos chunks em uma aplicação de exemplo no *Vue*. Nessa aplicação simularemos um sistema simples, com apenas duas páginas,  a *Home* e *About*, usando o *VueRouter* para trocar o acesso entre elas.

*Home.vue*:
```html
<template>
  <article>
    <h2>Home Page</h2>
  </article>
</template>

<script>
export default {
  name: 'home',
}
</script>
```

*About.vue*:
```html
<template>
  <article>
    <h2>About Page</h2>
  </article>
</template>

<script>
export default {
  name: 'home',
}
</script>
```

*App.vue*:
```html
<template>
  <div id="app">
    <router-link to="/">Home</router-link>
    <router-link to="about">About</router-link>
    <router-view></router-view>
  </div>
</template>

<script>
export default {
  name: 'app',
}
</script>
```

Até então tudo na normalidade que estamos acostumados, a mudança quando importamos nossos componentes para o *router*, aqui devemos usar o `System.import` para que o *webpack* identifique essa importação como um *chunk*:
```js
import Vue from 'vue'
import VueRouter from 'vue-router'
import App from './App.vue'

Vue.use(VueRouter)

const Home = () => System.import(/* webpackChunkName: "home" */'./components/Home.vue')
const About = () => System.import(/* webpackChunkName: "about" */'./components/About.vue')

const router = new VueRouter({
  routes: [
      {path: '/', component: Home},
      {path: '/about', component: About}
  ],
})

new Vue({
  el: '#app',
  render: h => h(App),
  router: router
})
```

Notem também que foi usado um comentário que funciona como anotação, onde podemos nomear nosso pedaço. Ao compilar o sistema com `npm run build` você verá que já temos algo funcionando, os arquivos foram separados:

```
leonardo@leonardo:~/dev/vue/splitting$ npm run build

> esqueleto@1.0.0 build /home/leonardo/dev/vue/splitting
> cross-env NODE_ENV=production webpack --progress --hide-modules

Hash: b03e8290e2443f170056
Version: webpack 2.7.0
Time: 18227ms
         Asset     Size  Chunks             Chunk Names
    0.build.js  3.65 kB       0  [emitted]  home
    1.build.js  3.66 kB       1  [emitted]  about
      build.js   109 kB       2  [emitted]  main
0.build.js.map  29.3 kB       0  [emitted]  home
1.build.js.map  29.3 kB       1  [emitted]  about
  build.js.map   876 kB       2  [emitted]  main
```

O ex-monstro `build.js` agora apresenta 109Kb, mas ainda temos dois problemas:

* Caso o sistema seja executado em um local que não seja a raiz do servidor, os arquivos `.js` não serão encontrados.
* Os nomes dos *chunks* não foram explícitos no nome dos arquivos gerados, pois foram gerados apenas id's.

Então, vamos corrigir ambos problemas em uma só martelada, no `webpack.config.js`, temos que realizar alguns ajustes no objeto `output` que nos dá a saída da compilação.

Primeiramente, altere o `publicPath` retirando-o da raiz, após isso, vamos acrescentar o atributo `chunkFilename` para criar um padrão de nome para os pedaços. Deixando-o assim:

```js
...
  output: {
    path: path.resolve(__dirname, './dist'),
    publicPath: './dist/',
    filename: 'build.js',
    chunkFilename: '[name].app.js',
  },
...
```

Precisamos, por fim, alterar um último detalhe, caso sua aplicação não esteja na raiz do servidor, altere o chamado do `script` no `index.html`, deixando-o no mesmo nível do arquivo e não mais na raiz:
```html
<script src="./dist/build.js"></script>
```

Agora ao executar o `npm run build` temos nossas importações separadas por arquivos:

```
leonardo@leonardo:~/dev/vue/splitting$ npm run build

> esqueleto@1.0.0 build /home/leonardo/dev/vue/splitting
> cross-env NODE_ENV=production webpack --progress --hide-modules

Hash: 304946d71317940f36d8
Version: webpack 2.7.0
Time: 18003ms
           Asset     Size  Chunks             Chunk Names
     home.app.js  3.65 kB       0  [emitted]  home
    about.app.js  3.66 kB       1  [emitted]  about
        build.js   109 kB       2  [emitted]  main
 home.app.js.map  29.3 kB       0  [emitted]  home
about.app.js.map  29.3 kB       1  [emitted]  about
    build.js.map   876 kB       2  [emitted]  main
```

Ao executar no navegador, observe o inspecionador de elementos, ao iniciar a aplciação na rota `/`, além do `build.js` será importado e incluído no *DOM* o arquivo `home.app.js`, ao clicar no link e mudar a rota para `/about` um novo script será incluído no *DOM*, indo para o arquivo `about.app.js`.

Sendo assim, é perceptível que estamos consumindo apenas os dados que realmente são usados. Ainda podemos ir além, realizando algumas ações para melhorar ainda mais o desempenho, como:

* Dividir um componente maior em *chunks*, fazendo com que, por exemplo, métodos só sejam declarados quando foram de fato usados.
* Extrair dependências de produção em arquivos distintos, assim podemos importar apenas onde é usual, despoluindo o arquivo `build.js`.


 E assim acabo esse artigo, espero que muitos possam usa-lo para melhorar suas aplicações. Além disso, deixem no comentários um *feedback* ou sugestões para postagens futuras.
