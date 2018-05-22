---
layout: post
title: 'Conheça o Vuetify - parte 3'
date: 2018-04-23 08:00:00 
tags: componentes vuetify css tollbar  
author: daniel-schmitz
---

Esta é a terceira parte do nosso tutorial sobre o Vuetify. Neste artigo conheceremos melhor o Toolbar e a sua importância para a aplicação como um todo. 

Toda aplicação necessita de uma barra de títulos e essa é uma das tarefas do toolbar, exibir um título. Além disso, também é possível adicionar botões e caixas de texto para realizar buscas.

## Exemplo básico

O desenho básico de uma toolbar é:

<p align="center">
<img src="https://i.imgur.com/1XVvBPj.png">
</p>

Nessa toolbar, temos um botão com um ícone, um título e três botões extras no final da barra. O código para desenhar esta tool bar é:

```html
 <v-toolbar>
    <v-toolbar-side-icon></v-toolbar-side-icon>
    <v-toolbar-title>Title</v-toolbar-title>
    <v-spacer></v-spacer>
    <v-toolbar-items class="hidden-sm-and-down">
      <v-btn flat>Link One</v-btn>
      <v-btn flat>Link Two</v-btn>
      <v-btn flat>Link Three</v-btn>
    </v-toolbar-items>
  </v-toolbar>
```

O botão em formato de menu é criado através do componente `<v-toolbar-side-icon>`, o título usa o componente `<v-toolbar-title>`. Já o `<v-spacer>` adiciona um espaço após o título forçando tudo que vier depois do *spacer* estar na parte direita da barra. Os próximos três botões estão agrupados pelo `v-toolbar-items`, que possui a classe `hidden-sm`, no qual irá esconder os itens em ambientes mobile (sm = small). 

## Toolbar da aplicação

 Agora vamos dar uma olhada no nosso *Toolbar* da aplicação que criamos na parte [1 do artigo](http://vuejs-brasil.com.br/conheca-o-vuetify-tutorial-dicas-parte-1/). 

 ```html
 <v-toolbar
      app
      :clipped-left="clipped"
    >
  <v-toolbar-side-icon @click.stop="drawer = !drawer"></v-toolbar-side-icon>
  
  <v-btn icon @click.stop="miniVariant = !miniVariant">
    <v-icon v-html="miniVariant ? 'chevron_right' : 'chevron_left'"></v-icon>
  </v-btn>
  <v-btn icon @click.stop="clipped = !clipped">
    <v-icon>web</v-icon>
  </v-btn>
  <v-btn icon @click.stop="fixed = !fixed">
    <v-icon>remove</v-icon>
  </v-btn>
  <v-toolbar-title v-text="title"></v-toolbar-title>
  <v-spacer></v-spacer>
  <v-btn icon @click.stop="rightDrawer = !rightDrawer">
    <v-icon>menu</v-icon>
  </v-btn>
</v-toolbar>
```

Esta toolbar está com bastantes ícones, e apresenta a seguinte forma:

<p align="center">
<img src="https://i.imgur.com/YcD2cXC.png">
</p>

O primeiro detalhe que vemos nesta aplicação é a presença do atributo `app`. Esse atributo informa que esta toolbar faz parte do layout de toda a aplicação (o componente v-app) ajustando assim o seu tamanho e posição de forma correta. A toolbar ficará sempre na parte superior da aplicação e responderá melhor aos eventos de resize da tela.

O tributo `clipped-left` informa que esta toolbar está ligada ao NavigationDrawer representado pela variável `clipped`. Na parte [2 do artigo](http://vuejs-brasil.com.br/conheca-o-vuetify-tutorial-dicas-parte-2/) vimos o NavigationDrawer à esquerda da aplicação, que possui o atributo `:clipped="clipped"`. O primeiro botão da Toolbar é o elemento `<v-toolbar-side-icon>` que, ao clicar, alterna o valor da propriedade `drawer`. Esta propriedade controla se o menu da esquerda está visível ou não. 

O próximo botão é formado pelo elemento `<v-btn icon>` que controla uma funcionalidade do menu chamada `mini-variant`, vista no [artigo anterior](http://vuejs-brasil.com.br/conheca-o-vuetify-tutorial-dicas-parte-2/#propriedade-minivariant). Ele usa variável `miniVariant` para este controle. 

O próximo botão controla a funcionalidade chamada `clipped`, vista no [artigo anterior](http://vuejs-brasil.com.br/conheca-o-vuetify-tutorial-dicas-parte-2/#propriedade-clipped). Depois temos outro botão que controle a propriedade `fixed`. Então temos o `<v-toolbar-title v-text="title">` que exibe o título da aplicação. Após o título, como de costume, temos um `<v-spacer></v-spacer>` e tudo após ele é exibido na parte direta do toolbar, como o botão que controla o menu direito.

## Propriedades importantes

- **app** Define que a toolbar é da aplicação, então ela fica fixa no topo. 
- **card** Adere ao elemento "v-card", removendo a sombra da barra inferior 
- **color** Cor da toolbar
- **dark** Aplica a variação de cores "dark", geralmente o título fica com a cor branca no texto do título
- **dense** Reduz a altura da toolbar, deixando-a mais fina
- **extended** Estende a toolbar para baixo, sem o uso de slot
- **extension-height** A altura, em pixels, da barra estendida
- **flat** Remove a borda com sombra
- **floating** Deixa a barra flutuando sobre a página
- **light** aplica o tema light
- **prominent** Aumenta a altura da toolbar

## Exemplo integrando Toolbar e Tabs

Neste exemplo temos o uso do ToolBar com abas. Para que esta combinação seja possível, deve-se criar adicionar as abas no slot *extension* da Toolbar.

<p data-height="265" data-theme-id="dark" data-slug-hash="pVJwRw" data-default-tab="html,result" data-user="danielschmitz" data-embed-version="2" data-pen-title="Vuetify Example Pen" class="codepen">See the Pen <a href="https://codepen.io/danielschmitz/pen/pVJwRw/">Vuetify Example Pen</a> by Daniel Schmitz (<a href="https://codepen.io/danielschmitz">@danielschmitz</a>) on <a href="https://codepen.io">CodePen</a>.</p>
<script async src="https://static.codepen.io/assets/embed/ei.js"></script>
