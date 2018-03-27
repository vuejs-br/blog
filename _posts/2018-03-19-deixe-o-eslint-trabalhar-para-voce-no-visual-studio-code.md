---
layout: post
title: 'Deixe o ESLint trabalhar para você, no Visual Studio Code'
main-class: 'dev'
date: 2018-03-19 11:45:46 
color: '#637a91'
tags: eslint webpack vue vscode
layout: post
author: halfeld
---

Para quem não conhece o ESLint, podemos resumi-lo como um utilitário para o Javascript responsável em avaliar algumas, ou até dezenas, regras de formatação do seu código.

 > **Eba!** Toda segunda tem artigo sobre Vue no site Vuejs Brasil. Quer sugerir um tema? Acesse nosso [fórum oficial](https://github.com/vuejs-br/forum/issues/7) e faça sua sugestão

Através deste utilitário é possível saber se estamos utilizando a formatação correta para o projeto, se as chaves estão no lugar certo, se exite ou não um ponto-e-vírgula no final da linha, se existe um *import* não utilizado, dentre outras.

Para que o ESLint funcione adequadamente, é necessário além de possuir alguns pacotes instalados, uma certa configuração dizendo o que é certo e o que é errado, contendo exceções, entre outras configurações. 

Tudo isso pode se tornar complexo para você que quer apenas escrever código Javascript no padrão estabelecido, então podemos deixar qualquer detalhe técnico de lado e partir para o uso de um template no qual tudo estará funcionando adequadamente em poucos minutos. 

Como você já deve saber, vamos usar o `vue-cli` para criar esse projeto padrão, em conjunto com o webpack. Com o Node 8 ou superior instalado, faça:

```bash
npx vue-cli init webpack myProject
```

Se ainda não conhece o **npx**, esse é o momento! Ele é um *node package runner*, um "executador" dos pacotes do Node. Ao invés de fazermos um `npm install -g vue-cli` usamos o `npx` para executar o `vue-cli` diretamente. É apenas um atalho, se você deseja instalar o `vue-cli` no seu sistema de forma global, vá em frente.

Com o projeto criado, vamos executar os seguintes comandos:

```bash
cd myProject
npm install
code .
```

O npm install irá garantir que todos os pacotes, incluse os pacotes *dev*, estarão instalados. O comando `code .` irá abrir o *Visual Studio Code* no diretório corrente. Perceba que estamos usando *Visual Studio Code*, então se você ainda não o usa, reconsidere [usar](https://code.visualstudio.com/)!  

Ao abrir o VSCode, caso você tenha *literalmente* acabado de instalá-lo, abra o arquivo `src/App.vue` e perceba que a formatação do código está ruim, algo semelhante à figura a seguir:

![](http://i.imgur.com/KMY6asZ.png)

Inclusive o próprio VSCode já lhe avisa, no canto inferior direito, que existem *extensions* que podem lhe ajudar a lidar com arquivos `.vue`. Recomendamos instalar as seguintes extensões:

- Vue
- Vue 2 Snippets
- Vue Peek
- Vetur
- ESLint
- Editorconfig for VSCode

Este é o mínimo do mínimo para que tudo funcione! Após instalar estas extensões e reiniciar o VSCode, você já obtém um código um pouco melhor formatado, veja:

![](http://i.imgur.com/zhqQG9e.png)

Ainda não conseguimos habilitar o ESLint da forma correta! Para isso, devemos alterar um pouco o arquivo de preferências do VSCode, encontrado em `File>Preferences>Settings`. A princípio este arquivo está vazio, ou com algumas configurações suas, então vamos adicionar a parte interessante ligada ao ESLint:

```json
{
   "eslint.validate": [
        {
            "language": "vue",
            "autoFix": true
        },
        {
            "language": "html",
            "autoFix": true
        },
        {
            "language": "javascript",
            "autoFix": true
        }
    ]
}
```

Aqui estamos dizendo a extensão ESLint que valide estas três formas: vue, html, javascript. Após dizer isso ao VSCode, e retornar ao arquivo `src/App.vue`, aperte `ctrl+alt+f` no windows ou `ctrl+shift+i` no linux ou `ctrl+options+f` no mac para realizar uma formatação geral no código, e checar os erros que aparecem providos pelo ESLint.

![](http://i.imgur.com/NdXqq1P.png)

É claro que estes erros devem ser corrigidos automaticamente. Não é necessário corrigir cada erro manualmente (exceto se você for masoquista). Para isso, você pode pressionar `ctrl+shit+p` e selecionar `ESLint: Fix all problems`:

![](http://i.imgur.com/lODXBl1.png)

Ainda podemos melhorar essa situação. Imagine a todo momento ter que executar este comando? Vamos imaginar, o que nós devemos fazer a todo segundo quando estamos programando? Sim!! Salvar!! Volte ao arquivo de configuração do VSCode e adicione a seguinte entrada:

```json
{
    "eslint.autoFixOnSave": true,
    "eslint.validate": [
        {
            "language": "vue",
            "autoFix": true
        },
        {
            "language": "html",
            "autoFix": true
        },
        {
            "language": "javascript",
            "autoFix": true
        }
    ],
}
```

Ao adicionar o `eslint.autoFixOnSave` como true, estamos dizendo a extensão que execute o comando `ESLint: Fix all problems` sempre que salvarmos o arquivos. Para que este comportamento funcione, é necessário reiniciar o VSCode. Após o seu reinício, aguarde alguns segundos para que o serviço ESLint esteja disponível.

Ainda temos um pequeno detalhe a ser resolvido. Existe uma incompatibilidade entre formatar o documento e salvá-lo. Isso acontece porque, ao formatarmos o documento sem salvar, o ESLint não está sendo executado. A imagem a seguir mostra esse problema:

![eslint](https://user-images.githubusercontent.com/1509692/37372157-9560a59a-26f0-11e8-9b3e-1d4e6d875ae1.gif)

Nesta imagem, acionamos alternadamente o comando para Formatar o código (Format Code) e para salvar. O comando para formatar código ainda não está utilizando o ESLint, ele usa um formatador próprio do VSCode (ou um outro configurado como o prettier). Já o comando para salvar está usando o ESLint, graças ao `eslint.autoFixOnSave`. 

Para resolver esse problema precisamos adicionar mais algumas configurações relativas a extensão Vetur. São elas:

```json
 "vetur.format.defaultFormatter.js": "vscode-typescript",
 "vetur.format.defaultFormatter.html": "js-beautify-html",
 "javascript.format.insertSpaceBeforeFunctionParenthesis": true,
```

Através destas três entradas, deixamos a configuração correta para que o ESLint possa corrigir os erros de padrão automaticamente para você. A seguir deixo a configuração completa do arquivo de configuração:

```json
{
    "vetur.format.defaultFormatter.js": "vscode-typescript",
    "vetur.format.defaultFormatter.html": "js-beautify-html",
    "javascript.format.insertSpaceBeforeFunctionParenthesis": true,
    "eslint.autoFixOnSave": true,
    "eslint.validate": [
        {
            "language": "vue",
            "autoFix": true
        },
        {
            "language": "html",
            "autoFix": true
        },
        {
            "language": "javascript",
            "autoFix": true
        }
    ]
}
```

