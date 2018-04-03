---
layout: post
title: 'Conheça o Vuetify - parte 2'
date: 2018-04-09 09:00:00 
tags: componentes vuetify css 
author: daniel-schmitz
---

Nesta segunda parte do nosso artigo sobre Vuetify estaremos analisando o componente `App.vue`, que contém alguns componentes do Vuetify que compõem a aplicação.


## Sumário 

<!-- TOC -->

- [Sumário](#sumário)
- [Comunidade](#comunidade)
- [Analisando o App.vue](#analisando-o-appvue)
- [VApp](#vapp)
- [VNavigationDrawer](#vnavigationdrawer)
    - [Propriedade Persistent](#propriedade-persistent)
    - [Propriedade MiniVariant](#propriedade-minivariant)

<!-- /TOC -->

 > **Eba!** Toda segunda tem artigo sobre Vue no site Vuejs Brasil. Quer sugerir um tema? Acesse nosso [fórum oficial](https://github.com/vuejs-br/forum/issues/7) e faça sua sugestão

## Comunidade

Já temos um grupo próprio do Vuetify em português no [Telegram](https://t.me/vuetifybr). Além deste grupo, temos toda uma [comunidade br](https://github.com/vuejs-br/comunidades) do Vue no qual você pode participar! 

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

