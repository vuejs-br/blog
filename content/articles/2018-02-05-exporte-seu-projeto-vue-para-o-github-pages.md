---
layout: post
title: 'Exporte seu projeto Vue para o GitHub Pages'
main-class: 'dev'
date: 2018-02-05 12:27:35 
color: '#637a91'
tags: vue deploy github git
author: daniel-schmitz
---

Neste artigo usaremos uma das diversas funcionalidades do GitHub, que é o GitHub Pages. Nele, é possível hospedar páginas web que podem se ser usadas inclusive para hospedar domínios reais, como o meu [danielschmitz.com.br](http://danielschmitz.com.br).

Neste artigo, iremos criar um pequeno exemplo onde será possível exportar uma app em extjs para o Github Pages, de forma que somente a build será exportada. 

## Conhecendo o GitHub Pages

Primeiro, é preciso conhecer um pouco sobre o Github Pages. Quando criamos um repositório no GitHub Pages, podemos definir uma *branch* que será definida como se fosse a sua webroot. Ou seja, quando o repositório é acessado, ao invés da página do GitHub, teremos a página web desta *branch*.

Como exemplo, crie um repositório chamado *teste* e, após a sua criação, crie o arquivo index.html:


![](https://user-images.githubusercontent.com/1509692/35783134-bd154452-09e9-11e8-9ad6-99da7f8bfb9f.png)

O arquivo `index.html` contém o seguinte código:

<script src="https://gist.github.com/danielschmitz/e8ed33aaef827f42be28f9aa8db2f924.js"></script>

Agora acesse as configurações deste projeto, através da seção `Options` > `Settings`, e navegue até o item `GitHub Pages`.

Veremos algo parecido como a imagem a seguir:

![](https://user-images.githubusercontent.com/1509692/35783225-d1cbf886-09ea-11e8-8994-33a3de66b2d9.png)

Ao acessarmos o item **Source**, temos uma caixa de seleção onde será possível definir em qual branch o webroot estará visível. Vamos escolher `Master Branch` e clicar no botão `Save`. 

Após salvar, volte no item `GitHub Pages` e verifique o status do website, você encontrará algo como: `Your site is ready to be published at https://<usuario>.github.io/teste`. Você poderá, inclusive, clicar neste link e conferir se o a página foi carregada. 

Ao invés do branch `master`, podemos definir que o website estará no branch `gh-pages`, que é um padrão do GitHub Pages.

## Criando o projeto Vue no Github

Agora vamos criar o projeto no Github que irá hospedar o projeto Vue. No site do GitHub (com você devidamente logado), clique no botão `New repository` e na próxima tela, adicione o nome do repositório, que aqui iremos chamar de `vue-push-dir`. Lembre-se, isso é apenas um teste, e já já você saberá do porquê do nome `push-dir`. Claro que você pode usar outro nome. Neste momento, **não clique na caixa de seleção** *Initialize this repository with a README*. A tela de criação do repositório deve ser semelhante a esta:

![](https://user-images.githubusercontent.com/1509692/35801303-f6d70acc-0a52-11e8-9d0e-9187bd2c5c1f.png)

Após clicar no botão `Create repository`, temos a seguinte tela:

![](https://user-images.githubusercontent.com/1509692/35801353-2f214cda-0a53-11e8-85ed-46f582223a09.png)

Perceba que criamos apenas o local onde o repo vai ficar, mas ainda não criamos nenhum arquivo.

## Criando o projeto Vue

Agora vamos para o Vue. Lembrando que, neste momento, é necessário conhecimentos básicos em Vue e em Git. Você precisa ter o Git instalado em sua máquina, o Node+Npm, e o Vue-cli. No seu sistema operacional, abra uma shell e digite:

```
$ vue init webpack vue-push-dir
```

Este comando irá criar o projeto Vue baseado no template Webpack. Uma resposta a esse comando é exibida a seguir:

![](https://user-images.githubusercontent.com/1509692/35801600-0e2cc206-0a54-11e8-9c33-b07b24ac27f0.png)

Após a criação do projeto, como de costume, precisamos realizar o comando `npm install` para instalar as dependências do mesmo.

```
cd vue-push-dir
npm install
```

## Associando o projeto ao GitHub

Com as dependências instaladas, vamos associar este projeto ao Github. Lembra que já criamos o repo? Vamos aproveitar a "colinha" que o Github nos deixa e executar os seguintes comandos:

![](https://user-images.githubusercontent.com/1509692/35802005-93657160-0a55-11e8-96a6-4fe2682f5b15.png)


```
$ git init
$ git add .
$ git commit -m "first commit"
$ git remote add origin git@github.com:<seu-login>/vue-push-dir.git
$ git push -u origin master
```

> **Atenção** Você pode escolher como acessar o seu repositório através de HTTPs ou SSH. Com HTTPs, o git irá lhe perguntar o login/senha da sua conta, geralmente uma  única vez, e armazenar isso no seu sistema. Se for por SSH, você terá que configurar uma chave pública para o acesso.

Volte ao GitHub e verifique se os arquivos estão no repositório, algo semelhante a figura a seguir:

![](https://user-images.githubusercontent.com/1509692/35802285-a712cf5e-0a56-11e8-9afe-bd6fff3aa288.png)

## Configurando o deploy

Chegou o momento de configurar o deploy do Vue no GitHub. Para isso, iremos usar uma biblioteca chamada **push-dir** que pode ser facilmente instalada pelo *npm*, veja:


```
$ npm install --save-dev push-dir
```

Após a instalação, vamos abrir o arquivo `packages.json` no seu editor de textos preferido, e dar uma olhada na seção `scripts`. Lá temos vários scripts que podem ser criados através do `npm run`, dentre eles temos o build, veja:

![](https://user-images.githubusercontent.com/1509692/35802509-86049a4e-0a57-11e8-9422-60a3f7040326.png)

Ao executá-lo, temos uma resposta semelhante a esta:

![image](https://user-images.githubusercontent.com/1509692/35802553-b1ccd790-0a57-11e8-9707-ed64402a3fc6.png)

O diretório dist foi criado juntamente com os arquivos de produção, veja:

![image](https://user-images.githubusercontent.com/1509692/35802618-ee91edfa-0a57-11e8-888a-312b9f8b9b14.png)

Voltando ao `packages.json`, vamos adicionar um novo script, chamado de deploy:

```
"deploy": "push-dir --dir=dist --branch=gh-pages --cleanup"
```
Onde:

- `dir` é o diretório de origem a ser enviado
- `branch` é o branch de destino, nao é necessário criá-lo previamente
- `cleanup` é usado para remover os arquivos temporários que push-dir criar.

Teremos a seção `scripts` semelhante a figura a seguir:

![image](https://user-images.githubusercontent.com/1509692/35802807-bbd4ec90-0a58-11e8-9e23-0d6c4a523008.png)

Após criar o script deploy, vamos comitar nosso progresso, veja:

```
$ git add .
$ git commit -m "Script de deploy"
$ git push
```

E, finalmente, poderemos usar o script, da seguinte forma:

```
$ npm run deploy
```

Após executar este comando, você perceberá que uma nova branch foi criada no repositório do github, que é a `gh-pages`. Ao acessá-la, pelo GitHub, teremos algo semelhante a figura a seguir:


![image](https://user-images.githubusercontent.com/1509692/35802967-4068c9e0-0a59-11e8-8186-a3ac396db72b.png)

Perceba que selecionamos o Branch `gh-pages` e que somente o conteúdo da pasta `dist` está presente! Como dissemos no início deste artigo, o conteúdo do `gh-pages` fica visível como um webroot, então podemos acessá-lo. Para obter a URL, basta clicar no menu `Settings` e e encontrar o item `GitHub pages`


![image](https://user-images.githubusercontent.com/1509692/35803105-bb067706-0a59-11e8-94e2-6b77cee59098.png)

Vamos acessar este link, no seu caso, deve ser algo como:

```
https://<usuario>.github.io/vue-push-dir/
```

Na primeira vez que acessamos, encontramos uma página em branco! Ok, um erro! Voltando ao arquivo `index.html` do branh `gh-pages`, vemos o seguinte:

![image](https://user-images.githubusercontent.com/1509692/35803272-42b5a136-0a5a-11e8-81f0-9f1319ba850d.png)

Percebeu que o arquivo javascript está sendo adicionado com o caminho `/static/js/.....` ? Como a url possui o diretório `vue-push-dir`, ou seja, `https://<usuario>.github.io/vue-push-dir/`, o `index.html` está tentando adicionar `https://<usuario>.github.io/static/js/.....` quando o correto seria `https://<usuario>.github.io/vue-push-dir/static/js/`. 

Para revolver este problema, devemos dizer a ferramenta que gerou a build que existe um diretório intermediário na url, e que ele deve incluí-la. Vamos usar um pouquinho do nosso conhecimento em webpack (que é "o cara" que gera os arquivos na pasta dist), e abrir o arquivo `config/index.js`. Ao abrir este arquivo, localize o código na seção `build`, por volta da linha 53, veja:

![image](https://user-images.githubusercontent.com/1509692/35803486-1ece9092-0a5b-11e8-8d13-ee2d58c2faf6.png)

Altere a propriedade `assetsPublicPath` para `/vue-push-dir`, deixando o código desta forma:

![image](https://user-images.githubusercontent.com/1509692/35803552-505bb72a-0a5b-11e8-9d15-fe4e2364f351.png)

Com a nova configuração, execute novamente:

```
& npm run build
```

Comite o novo `config/index.js`

```
$ git commit -am "fix absolute path at build deploy"
$ git push
```

E finalmente execute:

```
$ npm run deploy
```

Novamente o `push-dir` entra em ação e o branch `gh-pages` será atualizado. Desta vez, com o caminho para a inclusão dos arquivos estará correta:

![image](https://user-images.githubusercontent.com/1509692/35803781-318c0e7a-0a5c-11e8-828d-47734883468f.png)

E, ao acessarmos a url do repositório, teremos a app vue funcionando:

![image](https://user-images.githubusercontent.com/1509692/35803831-5fd17072-0a5c-11e8-889b-85f9d5bb6133.png)

Parabéns! Você acabou de fazer um deploy de uma app Vue para o GitHub Pages!

## Algumas considerações

- O `push-dir` pode ser usado para qualquer tipo de projeto. Ele não tem vínculo nenhum com o Vue. Pode-se usá-lo no angular, react etc. Sua funcionalidade é levar um diretório do seu projeto a um branch específico do Github. 
- Você pode adicionar o comando `npm run build` antes de executar o  `push-dir`, ficando desta forma: `"deploy":"npm run build; push-dir --dist.......`
- Este artigo foi inspirado no artigo original [Deploy Vue to GitHub pages-the easy way!](https://medium.com/@codetheorist/vue-up-your-github-pages-the-right-way-955486220418), que saiu no último [Vuejs Feed](https://vuejsfeed.com/), que é um ótimo lugar para você conhecer as últimas novidades do Vue.
- Caso queira acessar o repo desse artigo, está aqui: https://github.com/treinamento-daniel-schmitz/vue-push-dir










