---
layout: post
title: 'Alternativas em relação ao Vuex'
main-class: 'dev'
date: 2018-02-26 11:58:16 
color: '#637a91'
tags: 
layout: post
author: 4
---

Você já deve ter lido que o [Vuex](https://vuex.vuejs.org/en/) é a melhor forma de manter o estado global de uma aplicação em Vue. E realmente é. É vital que você compreenda o Vuex e sua filosofia [Flux](https://facebook.github.io/flux/docs/overview.html) para poder criar aplicações poderosas e com um excelente gerenciamento de estado, inclusive pelo Vue DevTools.


> **Eba!** Toda segunda tem artigo sobre Vue no site vuejs-brasil.com. Quer sugerir um tema? Acesse nosso [fórum oficial](https://github.com/vuejs-br/forum/issues/7) e faça sua sugestão

Mas dominar o Vuex não é, necessariamente, motivo para usá-lo em todos os seus projetos. Por exemplo, se você está apenas criando um protótipo, ou se você quer gerenciar apenas algumas variáveis globais na app, ou até mesmo se você ainda não compreendeu o Vuex e quer partir para algo mais simples, podemos dizer que existem soluções para isso

## Proposta deste artigo

Apresentar duas alternativas simples em relação ao Vuex, de forma que possa ser utilizada em seus projetos mais simplórios.

## Alternativa 1: Services

O conceito de services no Vue é um pouco mais amplo em relação ao Angular. Abordei o Angular porque naquele framework os services são estruturados de forma a implementar o padrão de projeto ioc, onde o service era **injetado** nos componentes do Angular. 

No Vue não existe a ioc (talvez Vue 3?), então um service pode ser caracterizado como um arquivo em Javascript que você pode usá-lo em qualquer parte da sua aplicação. Graças ao Webpack podemos facilmente exportar um JS para usá-lo. 

**Vamos ao código?**

Primeiro, Node 8 instalado em sua máquina, vamos criar uma app simples:

```
npx vue-cli init webpack alternativa1
```

O template *webpack* cria um projeto padrão, onde o código principal está no diretório **src**.

![](https://i.imgur.com/OTTmYqU.png)

Aqui temos dois arquivos que fazem parte do projeto Vue, o `App.vue` e o `HelloWorld.vue`. Imagine a situação em que deseja-se compartilhar informações entre estes dois componentes. Para isso, podemos criar um *Service* que mantém um estado "state" da aplicação. Esse arquivo pode se chamar `src/store.js`, e é definido da seguinte forma:

<script src="https://gist.github.com/danielschmitz/f5f660d4e3312ec27ac595c6c24b856a.js"></script>

Neste arquivo, criamos uma constante chamada `store`, que será exportada através do `export default` na última linha. Com isso podemos importá-la em qualquer arquivo Js ou Vue da aplicação.

No store, criamos três variáveis "privadas": `_username`, `_email` e `_token`. Coloquei privadas entre aspas porque elas estão acessíveis publicamente, mas é uma convenção não acessar variáveis que começam com "_". 

Claro que, para cada variável privada podemos criar o seu respectivo get/set:

```js
set username (str) {
    this._username = str
    localStorage.setItem('username',str)
},
  get username () {
    return this._username || localStorage.getItem('username')
}
```

Como *bônus*, ainda incluí o `localstorage` que é uma forma simples de persistir dados no navegador, através do recurso de chave/valor. Com isso, se o usuário recarregar a página, o estado estará mantido.

Com o *store* pronto, podemos partir para a implementação. No arquivo `src/App.vue`, vamos criar dois botões que irão simular a funcionalidade de Login e Logout no sistema. 

<script src="https://gist.github.com/danielschmitz/0dcbfa4eb6bbcc4bd1c9399460afcbef.js"></script>

O método `setFakeLogin` usa a variável `this.store`, que foi definida no `data` da instância Vue do componente e por sua vez o `store` do *data* é importado pelo comando `import store from './store'`

Perceba que os métodos *fake* apenas preenchem informações mock. Mas nesse ponto poderia-se usar outro serviço para realizar o login no servidor.

Com a *App.vue* pronta, podemos partir para o componente `HelloWorld.vue`, no qual nosso interesse maior é observar o estado do `store` e reagir a ele. Veja:

<script src="https://gist.github.com/danielschmitz/2ac39c96c6863e87f5a435d45a3e08e7.js"></script>

Assim como fizemos no *App.vue*, importamos o store usando `import store from '../store'`  (perceba o caminho subindo um nível no diretório) e o usamos na propriedade *data* da instância Vue para referenciá-lo. Aliás, lembre que

```js
data () {
 return {
    store
  }
}
```

é o mesmo que:

```js
data () {
 return {
    store: store
  }
}
```

No template, usamos `<div v-if="store.isLogged()">` para exibir a div somente se o método retornar true. Assim, temos uma garantia que podemos exibir conteúdo quando o usuário estiver logado! 

Execute a sua aplicação (npm run dev) e alterne entre os botões de Login e Logout, percebendo a alteração do conteúdo de acordo com o estado do *store*.

Você pode testar esse código [nesta demo](https://danielschmitz.com.br/vue-sem-vuex/alternativa1/index.html#/)


## Alternativa 2: Usando o Vue Stash

Outra forma de compartilhar o estado global de uma aplicação é utilizando este simples plugin, chamado de Vue Stash.

Primeiro, vamos criar uma nova app:

```
npx vue-cli init webpack alternativa2
```
 
Após a instalação, vamos instalar o plugin:

```
cd alternativa2
npm i -S vue-stash
```

Com o plugin instalado, abra o arquivo `src/main.js` e configure o plugin na instância do vue:

<script src="https://gist.github.com/danielschmitz/905b041e6ef53c96377ce30d113ec695.js"></script>

A ideia aqui é compartilhar o mesmo `store` que criamos na primeira alternativa, então vamos criar o arquivo `store.js` no diretório `src`:

<script src="https://gist.github.com/danielschmitz/f5f660d4e3312ec27ac595c6c24b856a.js"></script>

Para terminar de configurar o plugin, precisamos, no arquivo `src/main.js`, importar o store e usá-lo diretamente na definição da instância Vue, veja:

<script src="https://gist.github.com/danielschmitz/f68a37c8c6ecb8ccea987d909730fe6.js"></script>

A partir deste momento, o store está disponível de forma global na aplicação. Vamos repetir as funcionalidades do exemplo da Alternativa 1 para analisarmos como o VueStash funciona.

Primeiro, alterando o arquivo `src/App.vue` para:

<script src="https://gist.github.com/danielschmitz/00ddbd0f950198f3ae328e1c6fc4d964.js"></script>

Perceba que, ao invés de referenciar as informações do `store` no data, usamos:

```js
 store: ['username', 'email', 'token']
```

Isso irá expor estas três variáveis do `store` no componente. Assim, podemos usá-lo no `template` ou no `script`. O arquivo HelloWorld.vue pode ser refatorado para:

<script src="https://gist.github.com/danielschmitz/f0b3aa1f8599f69e49ae7f361bcd8e4d.js"></script>

Neste código expomos as variáveis `username`, `token` e o método `isLogged`. 

Tanto Alternativa1 quanto Alternativa2 possuem o mesmo comportamento no navegador, mas a forma como tratamos as variáveis globais sem o uso do Vuex muda bastante. Qual é a melhor? Isso fica ao seu gosto, ambas são aceitas para aplicações mais simples.

Você pode testar esse código [nesta demo](https://danielschmitz.com.br/vue-sem-vuex/alternativa2/index.html#/)





 






