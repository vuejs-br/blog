---
layout: post
title: 'Electron-vue'
main-class: 'dev'
date: 2016-09-11 12:25:56 
color: '#637a91'
tags: vue-js electron electron-vue
layout: post
author: 9
---

#### O que é?
[Electron](http://electron.atom.io/) é um framework para criar aplicações desktop nativas usando tecnologias como JavaScript, HTML e CSS. O [Electron-vue](https://github.com/SimulatedGREG/electron-vue) é este framework com o poder do Vue.js.

#### Como usar?
Recomenda-se instalar o [wine](https://www.winehq.org/) se o desenvolvimento da aplicação não for feito no Windows. Wine é uma camada de compatibilidade que dá a capacidade de rodar aplicações Windows em vários sistemas operacionais, como Linux, Mac OSX e BSD.

Para instalar o wine no Mac:
```
brew cask install xquartz
brew install wine
```

Para instalar o wine no Linux (debian based):
```
apt-get install wine
```

Após ter o wine instalado, basta instalar o electron e o vue-cli. Use o vue-cli para criar o projeto electron-vue.

```bash
npm install electron vue-cli -g

vue init simulatedgreg/electron-vue hello-electronvue
```

Feito isso, entre no diretório e instale as dependências.

```
cd hello-electronvue
npm install
npm run dev
```

Quando o comando ``run dev`` for executado, uma janela como a abaixo será mostrada.

![](/content/images/2016/09/Screen-Shot-2016-09-03-at-9-29-09-AM.png)

Para gerar os executáveis (build) da aplicação criada:
```
npm run build
```
Se deseja criar um executável específico para uma plataforma, execute o comando abaixo:
```
npm run build:PLATAFORMA
```

Onde ``PLATAFORMA`` pode ser:

 * darwin (OS X)
 * mas (OS X)
 * linux 
 * win32

Todos os executáveis serão gerados e colocados no diretório ``build``.

##### Dois package.json
Electron-vue tem [dois arquivos package.json separados](https://simulatedgreg.gitbooks.io/electron-vue/content/docs/project_structure.html). O primeiro, que está na raíz do projeto, contém as dependências do próprio Electron, como por exemplo, os plugins que fazem interface com os sistemas operacionais.
O segundo package.json, que encontra-se no diretório app, contém as dependências da aplicação sendo desenvolvida, como o próprio vue.js, vuex, entre outros.

**Recomenda-se manter os arquivos separados**. Quando uma build for criada, o Electron-vue saberá empacotar e criar os executáveis da maneira correta.

##### vuex e vue-router
O vuex e o vue-router já vêm pré-instalados no electron-vue. A estrutura padrão deste projeto é que, cada página deve ter um componente pai e um diretório onde componentes filhos serão declarados. Veja o exemplo da estrutura abaixo:
```
app
├── src
    ├── App.vue
    ├── components
    │   ├── LandingPageView
    │   │   ├── CurrentPage.vue
    │   └── LandingPageView.vue
```

No caso acima, temos uma página chamada LandingPageView.vue e esta possui um diretório com mesmo nome onde componentes filhos são declarados.

Suponha que eu queira criar uma página Electron-vue nova chamada ShoppingPageView. Para isso, eu criaria um componente pai chamado ShoppingPageView.vue na raíz do diretório components e criaria outro diretório chamado ShoppingPageView, que conteria todos os outros componentes que constituem a página ShoppingPageView.vue que possuo. Logo, a estrutura de arquivos ficaria desta forma:

```
app
├── src
    ├── App.vue
    ├── components
    │   ├── ShoppingPageView
    │   │   ├── Listing.vue
    │   ├── ShoppingPageView.vue
    │   ├── LandingPageView
    │   │   ├── CurrentPage.vue
    │   └── LandingPageView.vue
```



Esta foi a primeira vez que usei o Electron e já comecei usando-o com o Vue.js instalado. Todo o processo de instalação, desenvolvimento e de gerar uma build do projeto foi feito com muita facilidade e sem dores de cabeça. Não usei este framework como um projeto que será lançado em produção, porém, brincar e conhecer uma tecnologia nova foi uma grande experiência.

Este artigo foi criado somente para demonstrar o framework em questão, visto que, qualquer desenvolvedor que saiba vue.js e vuex conseguirão escrever aplicações Electron-vue com muita facilidade. Porém, em breve pretendo escrever um artigo para criar uma aplicação simples.

##### Fontes:

* [Electron-vue](https://github.com/SimulatedGREG/electron-vue)
* [Electron-vue Guidebook](https://www.gitbook.com/book/simulatedgreg/electron-vue/details)
* [Electron-vue Getting Started](https://simulatedgreg.gitbooks.io/electron-vue/content/docs/getting_started.html)
