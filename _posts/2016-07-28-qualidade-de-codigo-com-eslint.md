---
layout: post
title: 'Qualidade de código com ESLint'
main-class: 'dev'
date: 2016-07-28 12:08:45 
color: '#637a91'
tags: vue-js eslint
layout: post
author: 9
---

> Deveríamos saltar uma linha para abrir chaves ou não? E... quando formos separar argumentos em múltiplas linhas, deveríamos colocar a vírgula no final da linha ou no começo da próxima? *CamelCase*?

!["... Saltar uma linha para abrir chaves..."](/content/images/2016/07/brackets.gif)
<center>
Minha reação quando escuto: *"... saltar uma linha para abrir chaves ..."*
</center>

Todos nós desenvolvedores temos um certo padrão de escrita de código que mais agrada. Em grandes aplicações a padronização de estilo e qualidade de escrita de código não é um assunto fútil, mas sim, uma necessidade.

Atualmente uso o maravilhoso [Vue.js](http://vuejs.org/) em produção na empresa que trabalho. Por mais que a [modularização padrão de arquivos Vue](http://vuejs.org/guide/application.html#Single-File-Components) proposta seja bem organizada, ainda temos problemas na forma que cada desenvolvedor escreve o seu código. Para solucionar esse problema (em específico na escrita de código em **JavaScript**) propus e implementei o uso do ESLint. O resultado foi magnífico.

#### ESLint
[ESLint](http://eslint.org/docs/about/) busca e analisa padrões problemáticos ou certos estilos de codificação que não fazem parte de um estilo guia de escrita.
![](/content/images/2016/07/que-.gif)

Em outras palavras, este irá delatar o que está errado com a escrita do seu código e, se você usa algum arquivo de configuração ([.*rc](https://en.wikipedia.org/wiki/Configuration_file#UNIX.2FLinux)) que define como escrever métodos, declarar variáveis, e etc. o [lint](https://en.wikipedia.org/wiki/Lint_(software)) será responsável por marcar aquela linha que tem o problema e informar o mesmo. Com isso, todas as dúvidas (e possíveis discussões) que foram colocadas no início deste artigo são resolvidos. 

Para usar o ESLint no nosso projeto, usamos as seguintes ferramentas:

* A [IDE](https://en.wikipedia.org/wiki/Integrated_development_environment) [WebStorm](https://www.jetbrains.com/webstorm/) ou [PHPStorm](https://www.jetbrains.com/phpstorm/) (ambos da Jetbrains)
* node latest
* npm latest
* ESLint latest

Para instalar o ESLint basta executar o seguinte comando no diretório do seu projeto:
```bash
npm install --save-dev eslint eslint-plugin-jsx-a11y eslint-plugin-import eslint-plugin-react eslint-config-airbnb
```

O último pacote (*eslint-config-airbnb*) nada mais é um *preset* de regras que o ESLint usará para analisar o seu código ([veja todas as regras do airbnb documentadas aqui](https://github.com/airbnb/javascript)). Ele foi criado e é mantido pela empresa [Airbnb](https://www.airbnb.com) e, na minha opinião, é um dos melhores estilos de codificação disponíveis, especialmente porque cobre regras para o [ECMAScript 6](https://www.smashingmagazine.com/2015/10/es6-whats-new-next-version-javascript/).

O próximo passo é criar um arquivo **.eslintrc** e colocá-lo na raíz do projeto. Um exemplo de arquivo de configuração, neste cenário, é este:

```json
{
  "extends": "airbnb"
}
```

O comando *extends* importa as configurações do *preset airbnb*. Particularmente uso o exemplo abaixo. As linhas extras são [regras](http://eslint.org/docs/rules/) que modifiquei para agradar a minha equipe. 

```json
{
  "extends": "airbnb",
  "rules": {
    "one-var": 0,
    "comma-dangle": 0,
    "max-len": [0, 120, 4],
    "indent": [2, 4],
    "key-spacing": [2, {
      "beforeColon": false,
      "afterColon": true
    }]
  }
}
```

O último passo foi ativar o ESLint e fazer com que ele use o *.eslintrc* como regras base para analisar os arquivos fonte da aplicação. Usando o WebStorm ou PHPStorm basta ir em:

```
Preferences > Languages & Frameworks > JavaScript > Code Quality Tools > ESLint.
```

Clique em "Enable" e aponte o caminho do *Node Interpreter* e do pacote do ESLint previamente instalado na sua máquina. Depois, marque a opção *Configuration File* e busque pelo arquivo *.eslintrc* na raíz do projeto. Após alguns segundos, o ESLint analisará todos os arquivos e marcará todo o código fora do padrão descrito no arquivo de configuração.

Se você não usa nenhuma dessas IDE's, [recomendo-o que veja como usar o ESLint na sua preferida](http://eslint.org/docs/user-guide/integrations#editors).

Espero que este artigo ajude-o a melhorar a qualidade de código desenvolvida por você e sua equipe assim como tem melhorado para a minha.

##### Fontes:

* [ESLint](http://eslint.org/)
* [[NPM] ESLint](https://www.npmjs.com/package/eslint)
* [[NPM] ESLint Plugin Import](https://www.npmjs.com/package/eslint-plugin-import)
* [[NPM] ESLint Config Airbnb](https://www.npmjs.com/package/eslint-config-airbnb)
* [[NPM] ESLint Plugin JSX a11y](https://www.npmjs.com/package/eslint-plugin-jsx-a11y)
* [Airbnb JavaScript Style Guide](https://github.com/airbnb/javascript)

A versão deste artigo resumida em inglês pode ser encontrada no [meu medium](https://medium.com/tldr-tech/how-to-use-eslint-fbe68662f7b5#.r98jvlsn7).
