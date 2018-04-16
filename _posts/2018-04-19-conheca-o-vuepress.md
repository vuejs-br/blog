---
layout: post
title: 'Conheça o Vuepress'
date: 2018-04-19 08:00:00 
tags: vue vuepress gerador site  
author: daniel-schmitz
---

Na semana passada Evan You, o criador do Vue, [anunciou](https://twitter.com/youyuxi/status/984918079598710784) uma nova ferramenta chamada Vuepress. Neste artigo vamos aprender tudo o que é necessário saber sobre ela.

 > **Eba!** Toda segunda tem artigo sobre Vue no site Vuejs Brasil. Quer sugerir um tema? Acesse nosso [fórum oficial](https://github.com/vuejs-br/forum/issues/7) e faça sua sugestão

 <p align="center">
 <img src="https://pbs.twimg.com/media/DamKGD5WkAEGEz0.png:large">
 </p>
 
 O [Vuepress](https://vuepress.vuejs.org/) é um gerador de sites estáticos, assim como o Jekyll, Hexo, Gatsby, entre outros. Mas não é só isso! Ele usa diversas funcionalidades implícitas do Vue,como por exemplo:

 - Estende as funcionalidades padrão do Markdown
 - Usa Vue, Vue Router e Webpack
 - 100% SSR
 - 100% SEO
 - Pode-se usar o Vue em suas páginas, como por exemplo `{{1+1}}`
 - Pode-se criar componentes Vue e adicioná-los a sua página
 - Os temas usam extensivamente o Vue
 - Suporte a PWA
 - Integração com o Google Analytics
 - **O tema padrão é focado para documentar o seu projeto**
    - Responsivo
    - Página "Home" opcional
    - Possui um cabeçalho com busca
    - Navbar e Sidebar customizadas
    - Pode gerar links do tipo "editar esta página"

Um fator importante  ser observado é que esta ferramenta é muito nova, tem 1 semana de vida, então muitas coisas ainda virão com o tempo. Ou seja, alterar aquele seu blog em jekyll neste momento não pode ser uma boa ideia, até porque você precisará criar um tema que seja no estilo Blog. 

Mas existe uma área em que o Vuepress já pode ser usado: Documentação! Sim, o Vuepress nasceu com o propósito *inicial* de servir de base para criação de documentação técnica. Um exemplo é o próprio site [https://vuepress.vuejs.org](https://vuepress.vuejs.org) criado 100% com Vuepress.

## Instalação

O Vuepress pode ser instalado globalmente:

```bash
npm i -g vuepress
```

Ou então localmente no seu projeto, no `devDependencies`

```bash
npm i -D vuepress
```

## Uso básico

Vamos criar um projeto básico e ver o VuePress em ação. Primeiro, crie um diretório, vamos chamá-lo de `vptest`

```bash
mkdir vptest
```

Após a criação do diretório, vamos criar o arquivo `README.md`, com o seguinte texto:

```
# Hello Vuepress

Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.

Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.
```

Após a criação do arquivo, já podemos gerar um site base com o comando:

```bash
$ vuepress dev .
```
<p align="center">
<img src="https://i.imgur.com/Z0FJc2b.png">
</p>

O servidor criado no localhost está escutando as modificações no código fonte, regerando o site quando necessário.

Ao acessar o endereço fornecido, temos:

<p align="center">
<img src="https://i.imgur.com/ezkcdMl.png">
</p>

Percebeu na imagem acima o ícone do Vue?? Sim!! Esta página, por estar sendo servida no modo "dev", possui toda a estrutura de uma aplicação Vue, veja:

<p align="center">
<img src="https://i.imgur.com/Bk7DqCe.png">
</p>


## Deploy

A fase do deploy significa que vamos exibir o site gerado pelo vue em modo de produção. Aqui o VuePress se encarrega de gerar todo o conteúdo da forma mais otimizada possível. O comando para gerar o site no modo de produção é:

```bash
$ vuepress build .
```

<p align="center">
<img src="https://i.imgur.com/olzHcGM.png">
</p>

Perceba que o site foi gerado no `.vuepress/dist`:

<p align="center">
<img src="https://i.imgur.com/jbTnK7R.png">
</p>

Neste ponto, basta apontar o servidor web para este diretório e voialá, teremos o nosso site 100% estático com SSR, SEO e PWA!

## Configurando o título do site

Ok, nosso site Vuepress ainda está muito básico. Temos apenas uma página e não vemos, a princípio, uma barra de títulos, uma barra de menu etc.

Para adicionar essas configurações, é necessário criar no diretório `.vuepress` o arquivo `config.js`, inicialmente com o seguinte código:

```js
module.exports = {
    title: 'Hello VuePress',
    description: 'Just playing around'
}
```

> **Atenção**: Se você estiver usando o `vuepress dev .`, e criar o arquivo de configuração, ele não irá perceber esta criação e não irá recriar os arquivos. É necessário cancelar o comando e executá-lo novamente! Assim o arquivo config.js entra para a lista e passa a ser observado

Após a criação desta configuração, voltamos ao site e temos:

<p align="center">
<img src="https://i.imgur.com/ucEVt7e.png">
</p>

## Configurando a página de entrada

O tema padrão do Vuepress permite que criemos uma página de "entrada" contendo informações sobre o seu projeto. Para que possamos criá-la, é necessário adicionar as seguintes informações no início do arquivo README.md

```md
---
home: true
heroImage: https://i.imgur.com/hDs8z8r.png
actionText: Começar →
actionLink: /main.md
features:
- title: Titulo 1
  details: Detalhe 1
- title: Titulo 2
  details: Detalhe 2
- title: Titulo 3
  details: Detalhe 3
footer: Copyright © 2018-present Evan You
---
```

A chave `home: true` indica ao Vuepress para criar uma página de entrada. Configuramos uma imagem, um texto para ir para uma outra página, além de 3 blocos com textos e um rodapé. Ao salvar o arquivo README, o site é refeito (se a opção `vuepress dev` estiver ativa), exibindo algo como:

<p align="center">
<img src="https://i.imgur.com/BSXknRm.png">
</p>

## Configurando o menu

Neste ponto você já deve estar compreendendo como o Vuepress funciona. Se deseja configurar um menu, já sabe que deve editar o arquivo .vuepress/config.js. 

No tema padrão do Vuepress temos dois tipos de menu: Navbar (parte superior) e Sidebar (parte esquerda). Eles podem ser configurados da seguinte forma:

```js
module.exports = {
    title: 'Hello VuePress',
    description: 'Just playing around',
    themeConfig: {
        nav: [
            { text: 'Home', link: '/' },
            { text: 'Google', link: 'https://google.com' },
        ],
        sidebar: [
            '/',
            '/pag1'
        ]
    }
}
```

A configuração acima produz o seguinte resultado:

<p align="center">
<img src="https://i.imgur.com/Zse3Aku.png">
</p>

Para configurar menus mais complexos, você pode ter como exemplo o [menu do próprio site do VuePress](https://github.com/vuejs/vuepress/blob/master/docs/.vuepress/config.js)

## Melhorias no markdown

O VuePress traz algumas pequenas extensões para a linguagem Markdown, pois usa o [Markdown It](https://github.com/markdown-it/markdown-it).

Vamos destacar algumas delas:

**Emojis** Pode-se usar como :tada: ou :100: Uma lista deles pode ser encontrada [aqui](https://gist.github.com/rxaviers/7360908).

**Table of contents** Se você adicionar `[[toc]]` no início do arquivo o VuePress irá adicionar um sumário da página, contendo os links para os subtítulos da mesma.

**Containers** Pode-se adicionar os seguintes containers de texto:

```
::: tip
This is a tip
:::

::: warning
This is a warning
:::

::: danger
This is a dangerous warning
:::
```

Isso irá produzir o seguinte resultado:

<p align="center">
<img src="https://i.imgur.com/LyNegh3.png">
</p>

 Se desejar configurar o título, pode-se fazer da seguinte forma:

```
::: danger STOP
Danger zone, do not proceed
:::
```

**Destacando linhas de código**

Para destacar uma (ou várias) linhas de um código, usamos:

````
``` js{4}
export default {
  data () {
    return {
      msg: 'Highlighted!'
    }
  }
}
```
````

A linha 4 será marcada, conforme a imagem a seguir:

<p align="center">
<img src="https://i.imgur.com/Hxa0v3M.png">
</p>

## VuePress e Github Pages

Exportar o seu projeto VuePress para o GitHub Pages é fácil com uma biblioteca node adicional, chamada `push-dir`. Após concluir o seu site usando VuePress, você deverá executar o comando `vuepress build .` para gerar o site estático no diretório `.vuepress/dist`. Então, após esta etapa, faça:

```bash
npx push-dir --dir=.vuepress/dist branch=gh-pages --cleanup --allow-unclean
```

Desta forma, o conteúdo estático gerado será copiado para o branch `gh-pages` do github, que poderá ser exibido como um site através de uma url. Para mais detalhes, leia este [artigo](http://vuejs-brasil.com.br/exporte-seu-projeto-vue-para-o-github-pages/).

> Lembre-se que no github pages a url do projeto é no seguinte formato: https://<usuario>.github.io/<projeto>/, então é preciso dizer ao VuePress que  site está sendo visualizado dentro do diretório /<projeto>/. Isso é feito no .vuepress/config.js utilizando a propriedade `base`. 

## VuePress e Netlify

O Netlify é um serviço web que fica "escutando" o seu repositório github e, quando existe alguma modificação nele, como um push ou merge, o serviço pode executar algum comando node.



## Próximos passos

Ainda existem muitos detalhes para serem absorvidos. Se você gostou do que viu até o momento, então é hora de ir até o [VuePress](https://vuepress.vuejs.org/guide/) e ler a documentação, que aliás foi criada usando Vuepress ;)



