---
layout: post
title: 'Conheça o Vuetify - parte 1'
date: 2018-04-02 09:00:00 
tags: componentes vuetify css 
author: daniel-schmitz
---

O Vuetify é um framework responsivo em Vue, baseado no Material Design. Já possui uma boa gama de componentes e uma documentação sólida. Neste artigo iremos conhecê-lo através de um tutorial completo, criando uma pequena aplicação para ler dados de uma conta no GitHub.

## Comunidade

Já temos um grupo próprio do Vuetify em português no [Telegram](https://t.me/vuetifybr). Além deste grupo, temos toda uma [comunidade br](https://github.com/vuejs-br/comunidades) do Vue no qual você pode participar! 

## Criando a aplicação

Precisamos basicamente do Node, versão 8 ou superior, e de um editor de textos como o Visual Studio Code. Com tudo isso pronto, podemos criar o projeto Vuetify escolhendo os mais diversos templates existentes:

<p align="center">
<img src="https://i.imgur.com/ApVRDTu.png">
</p>

Vamos usar o template **Webpack**, criando o projeto através do seguinte comando:

```bash
npx vue-cli init vuetifyjs/webpack vuetifyproject
```

Responda as perguntas e aguarde todas as dependências serem instaladas. Após isso, acesse o diretório do projeto e execute `code .` para abrir o Visual Studio Code, e `npm run build` para executar o projeto no modo desenvolvedor. O navegador será aberto com o design do projeto semelhante a este:

<p align="center">
<img src="https://i.imgur.com/GAJJzxz.png">
</p>

No caso acima, estou usando a extensão para o Google Chrome chamada [Vue DevTools](https://github.com/vuejs/vue-devtools) que exibe diversas informações sobre a instância Vue do projeto. A esquerda podemos ver o Vuetify em ação, já com um menu flutuante, uma barra de títulos, um menu flutuante na parte direita, e um rodapé.

## Estrutura de diretórios

Sempre que eu estou estudando um novo framework, gosto de analisar bem a estrutura de diretórios que ele trabalha. Com isso terei a base necessária para expandir o meu sistema criando os componentes no lugar certo, além de conhecer suas limitações. Conhecer bem o framework antes de utilizá-lo em um projeto real é fundamental para o sucesso do seu projeto.

<p align="center">
<img src="https://i.imgur.com/KOcJvtx.png">
</p>

No primeiro nível de diretório do projeto, temos:

- **build** Contém os arquivos responsáveis pelo processo de compilação do projeto. Todos os arquivos *.js*, *.vue*, *.css* são "compilados" em um conjunto muito pequeno de arquivos, são minificados e impossíveis de ler a um ser humano.

- **config** É no diretório *config* que informamos algumas configurações de projeto, como por exemplo a URL de acesso a API do backend. Este [artigo](http://vuejs-brasil.com.br/trabalhando-com-arquivos-env-no-vue/) explica como funciona o processo.

- **node_modules** Quando executamos `npm install`, todas as bibliotecas de projeto são baixadas da internet para esse diretório. Não altere nada nesse diretório, sempre que quiser baixr uma nova versão de alguma biblioteca, altere o arquivo `package.json` e execute `npm install` novamente.

- **src** O diretório src contém todo o código do projeto. Será detalhado mais tarde nesse artigo.

- **static** Coloque neste diretório imagens e arquivos que não serão "compilados" no projeto, mas estarão presentes no resultado final. Qualquer arquivo adicionado aqui será literalmente copiado para o projeto final.

Além destes diretórios, temos  arquivos importantes na raiz do projeto, são eles:

- **index.html** Contém uma *div* com o id *app*. É aqui que tudo começa na aplicação, onde o Vue será instanciado. 

- **package.json** Contém diversas informações sobre o projeto, como a definição dos comandos que o node pode executar, os pacotes npm a serem instalados, entre outros.

- **.esointrc.js** Contém informações sobre como o ESLint deve se comportar no projeto. Veja [este artigo](http://vuejs-brasil.com.br/deixe-o-eslint-trabalhar-para-voce-no-visual-studio-code/) para maiores detalhes.

Agora vamos dar uma olhada no diretório `src`, que é onde temos todos os arquivos do projeto em si. 

<p align="center">
<img src="https://i.imgur.com/eFQ2NMS.png">
</p>

- **assets** Contém arquivos que serão transpilados para javascripts e injetados no projeto. Pode-se dicionar aqui o logotipo ou pequenas imagens do projeto. Não adicione fotos ou imagens muito grandes já que tudo irá se tornar javascript! Para imagens grandes, como fotos, use o diretório **static**.

- **components** Inicialmente adicionamos os componentes Vue neste diretório, o que não precisa ser um padrão. Em projetos muito grandes podemos dividir os componentes em diversos níveis. Neste projeto vamos continuar usando a estrutura simples, então qualquer componente `.vue` do projeto será adicionado neste diretório.

E os arquivos:

- **router** Este diretório possui apenas o arquivo `index.js` que contém as rotas de cada componente do projeto, já que o Vuetify usa o Vue Router.

- **App.vue** Este é o componente principal da aplicação. É ele que "desenha" todas as funcionalidades que vimos na execução do projeto. Os menus flutuantes, o cabeçalho, rodapé e corpo da aplicação. Daremos uma especial atenção a este arquivo em breve.

- **main.js** Este arquivo importa e cria a instância Vue, associando ele àquela *div id='app'*. O *router* também é iniciado, onde os demais arquivos *vue* serão instanciados. Possivelmente você irá alterar este arquivo em algum momento do projeto, adicionando mais bibliotecas.

No próximo artigo veremos um pouco mais sobre os componentes que estão presentes no `App.vue`, até lá!


