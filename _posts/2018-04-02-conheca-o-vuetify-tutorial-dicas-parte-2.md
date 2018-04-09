---
layout: post
title: 'Conheça o Vuetify - parte 2'
date: 2018-04-09 09:00:00 
tags: componentes vuetify css 
author: daniel-schmitz
---

Nesta segunda parte do nosso artigo sobre Vuetify estaremos analisando o componente `App.vue`, mais precisamente o componente VNavigationDrawer.

 > **Eba!** Toda segunda tem artigo sobre Vue no site Vuejs Brasil. Quer sugerir um tema? Acesse nosso [fórum oficial](https://github.com/vuejs-br/forum/issues/7) e faça sua sugestão

> **Comunidade** Já temos um grupo próprio do Vuetify em português no [Telegram](https://t.me/vuetifybr). Além deste grupo, temos toda uma [comunidade br](https://github.com/vuejs-br/comunidades) do Vue no qual você pode participar! 

## Analisando o App.vue

O componente App contém toda a aplicação Vuetify. Analisando a imagem a seguir:

<p align="center">
<img src="https://i.imgur.com/JpbO03r.png">
</p>

Podemos destacar os seguintes componentes:

## VApp 

É o componente que compreende toda a aplicação Vuetify. Este componente é praticamente obrigatório em uma aplicação Vuetify, e através dele pode-se criar diversos tipos de design. Vamos abordar um pouco mais do VApp a sgeuir. Uma aplicação básica pode conter o seguinte código:

```html
<v-app>
  <v-navigation-drawer app></v-navigation-drawer>
  <v-toolbar app></v-toolbar>
  <v-content>
    <v-container fluid>
      <router-view></router-view>
    </v-container>
  </v-content>
  <v-footer app></v-footer>
</v-app>
```

## VNavigationDrawer

É um componente capaz de desenhar um menu, onde este menu está integrado ao Vue Router:

<p align="center">
<img src="https://i.imgur.com/faXB48C.png">
</p>

Na aplicação, temos o Navigation Drawer definido da seguinte forma:

```html
<v-navigation-drawer
      persistent
      :mini-variant="miniVariant"
      :clipped="clipped"
      v-model="drawer"
      enable-resize-watcher
      fixed
      app
    >
```

### Propriedade Persistent

A propriedade `persistent` exibe a forma como ele se comporta quando a página é carregada. Se for `persistent`, o componente será exibido assim que a página é carregada (exceto se estiver e um dispositivo mobile). Caso não queria esse comportamento, deixando o componente invisível no carregamento da página, altere de `persistent` para `temporary`

### Propriedade MiniVariant

Esta propriedade "condensa" o menu de forma que fique somente com os ícones. Por exemplo:

<p align="center">
<img src="https://i.imgur.com/jFkeQjW.png">
<br/><i>mini-variant: true</i>
</p>

<p align="center">
<img src="https://i.imgur.com/k7NYBsO.png">
<br/><i>mini-variant: false</i>
</p>

No caso da aplicação, temos o uso do `:mini-variant` com dois pontos no início para indicar que a propriedade está observando uma variável no `this.data.miniVariant` do Vue. Esta propriedade é alternada através de um botão no menu do cabeçalho (toolbar):

<p align="center">
<img src="https://i.imgur.com/mabXV89.gif">
</p>

### Propriedade clipped

Determina se o Panel do Drawer (vamos chamar de menu) está sobre o toolbar ou sob ele. Uma imagem vale por mil palavras:

<p align="center">
<img src="https://i.imgur.com/vTywUAv.gif">
</p>

Novamente usa-se um bind `:clipped="clipped"` para que o valor seja observado através do `this.data.clipped`.

### Propriedade v-model

A propriedade `v-model` do *Navigation Drawer* indica se ele está presente ou não na aplicação. Pode-se usar essa propriedade para, por exemplo, exibir o menu somente através de um contexto, como o usuário logado.

### Propriedade enable-resize-watcher (deprecidada)

Este propriedade indica se o *Navigation Drawer* deve fechar automaticamente caso o tamanho da tela diminua. Em uma recente atualização do Vuetify, esta propriedade foi alterada para *disable-resize-watcher*. Então altere o *enable-resize-watcher* para *disable-resize-watcher*.

### Propriedade fixed

Esta propriedade determina se a posição do elemento (neste caso o *Navigation Drawer*) é fixa. 

### Propriedade app

Esta propriedade determina que o *Navigation Drawer* é pertencente ao *v-app*. Sem ela, o menu nao esta pertencente a aplicação como um todo. Isso ocorre porque podemos criar um   *Navigation Drawer* que é pertencente a algum menu interno e que é de uma tela qualquer, e não da app. 

### Outras propriedades importantes

- **dark** Usa o tema "dark", que pode ser combinado com o dark de outros componentes.
- **height** A altura do componente, cujo padrão é '100%'
- **light** Outro variação do tema
- **mobile-break-point** Informa a largura em pixels da definição sobre o que é mobile ou não. O valor padrão é 1264, se a largura da app for menor que isso, o componente se comporta como um mobile.
- **permanent** O componente fica permanentemente visível na tela. 
- **right** Posiciona o componente no lado direito da tela
- **stateless** Remove todo  o controle automático do componente frente as interações da tela, a largura e a mudança de rota. Todo o controle seria manual. 
- **touchless** Desabilita os eventos touch do dispositivo mobile, como o arrastar para a direta fazendo a o componente surgir na tela
- **value** Controla a visibilidade do componente

### Configurando o menu

O menu interno ao *Navigation Drawer* pode ser configurado de diferentes formas. Neste caso específico, temos:

```html
<v-navigation-drawer>
  <v-list>
    <v-list-tile
      value="true"
      v-for="(item, i) in items"
      :key="i"
    >
      <v-list-tile-action>
        <v-icon v-html="item.icon"></v-icon>
      </v-list-tile-action>
      <v-list-tile-content>
        <v-list-tile-title v-text="item.title"></v-list-tile-title>
      </v-list-tile-content>
    </v-list-tile>
  </v-list>
</v-navigation-drawer>
```

Temos então um `VList` em conjunto com um `VListTile`, e neste temos o `v-for` do Vue iterando em uma lista chamada `items`. Esta lista é criada no `this.data`, veja:

```html
<script>
export default {
  data () {
    return {
      clipped: false,
      drawer: true,
      fixed: false,
      items: [{
        icon: 'bubble_chart',
        title: 'Inspire'
      }],
      miniVariant: false,
      right: true,
      rightDrawer: false,
      title: 'Vuetify.js'
    }
  },
  name: 'App'
}
</script>
```

A princípio temos apenas um item, chamado de "Inspire". No componente, após o uso do `v-for`, temos um `v-list-tile-action` e um `v-list-tile-content` ambos usando os dados da lista de `items`. 

## Criando a integração com o Vue Router

Até o momento temos apenas uum item no VueRouter, definido no arquivo `src/router/index.js`:

```js
export default new Router({
  routes: [
    {
      path: '/',
      name: 'HelloWorld',
      component: HelloWorld
    }
  ]
})
```

E precisamos adicionar no menu da direita um link para essa rota. Primeiro, devemos alterar o `v-list-tile` do *Navigation Drawer* adicionando a propriedade `to`, da seguinte forma:

```html
 <v-list-tile
          value="true"
          v-for="(item, i) in items"
          :key="i"
          :to="item.to"
        >
```

A propriedade `to`, nativa do `v-list-tile`, integra-se ao Vue Router e ao `<router-link>`, provendo assim o acesso ao roteamento do Vue. Para finalizar, altere a lista de itens para:

```js
...
items: [{
  icon: 'bubble_chart',
  title: 'Hello World',
  to: '/'
}],
...
```

Perceba que adicionamos no item a propriedade `to`, que trabalha em conjunto com o `<v-list-tile>`. Agora, se adicionarmos mais um item, por exemplo:

```js
 items: [{
        icon: 'bubble_chart',
        title: 'Hello World',
        to: '/'
      },
      {
        icon: 'vpn_key',
        title: 'Login',
        to: '/login'
      } ],
```

Temos o seguinte resultado:

<p align="center">
<img src="https://i.imgur.com/dReqHYn.png">
</p>

Claro que, ao clicar neste item, nenhuma página será carregada, pois o componente ainda não foi criado. No próximo artigo conheceremos mais sobre outro importante componente, o VToolbar. Até lá!

