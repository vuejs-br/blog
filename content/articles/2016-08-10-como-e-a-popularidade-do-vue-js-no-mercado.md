---
layout: post
title: 'Como é a popularidade do Vue.JS no mercado?'
main-class: 'dev'
date: 2016-08-10 20:05:50 
color: '#637a91'
tags: evan-you quora traducao mercado
author: vinicius
---

Este post é uma tradução livre da [resposta](https://www.quora.com/How-popular-is-VueJS-in-the-industry/answer/Evan-You-3) do criador do VueJS [**Evan You**](https://github.com/yyx990803) a uma pergunta feita no Quora: [**How popular is VueJS in the industry?**](https://www.quora.com/How-popular-is-VueJS-in-the-industry)

----

Vou tentar ser objetivo e responder essa pergunta com estatísticas. Note que a maioria das estatísticas quando vistas isoladamente serão imprecisas até certo ponto, porém uma combinação de todas elas fornecerá um quadro bastante convincente do estado atual do Vue.js.

## Google Trends

O Google Trends não é a ferramenta mais apurada, mas fornece um bom "índice de relevância". Vue teve uma considerável ascensão durante o ano passado (2015), superando *Ember* e *Meteor*, sem nenhuma tendencia que indique uma diminuição do interesse.

Obviamente não esta no mesmo nível que Angular/React (note que eu omiti angular do gráfico porque diminui todos os outros), porém repare que Vue é relativamente novo com sua primeira versão em fevereiro de 2014, e atualmente esta crescendo a uma taxa muito consistente.

![Google Trends](/content/images/2016/08/google-trends-01.png)

## GitHub Trend Statistics

Aqui está o gráfico de crescimento de estrelas no GitHub do Angular 1 x React x Vue:

![GitHub Trends](/content/images/2016/08/github-trends-01.png)

Você vai notar uma tendência similar aqui, onde a curva do React é deslocada cerca de 1.5 anos para a direita do Angular, e a do Vue se desloca 1.5 anos do React.

Outro muito útil e talvez mais cientifico que as baseadas no GitHub é o  [JS.ORG | STATS](https://stats.js.org/) - Vue atualmente está na 28º posição, no *rank de todos os tempos* (all-times ranking), e mais importante tem estado constantemente na lista dos *10 mais* mensal e semanal por vários meses. E se você considerar apenas os projetos que já existem nos rankings semanais/mensais ele estará constantemente entre os 3 projetos com *melhor colocação* 


## Estatísticas de Usuários

Além das "estatísticas vaidosas", vamos olhar algumas estatísticas de uso real. Recentemente o Vue passou de 1 milhão de downloads no NPM, com uma contagem mensal de 120~150k. Como referência esse numero representa cerca de 1/4 do angular 1 e 1/12 do React. Se considerar que o Vue é amplamente usado sem um gerenciador de pacotes, esse número provavelmente deve dobrar.

A [documentação oficial](http://vuejs.org/) do Vue tem atualmente ~150k de visitantes únicos ~450k de visualizações de página por mês, segundo o Google Analytics:

![Google Analytics](/content/images/2016/08/google-analytics.png)

Outro número interessante de se olhar, é o número de usuários ativos semanalmente no plugin oficial para Chrome o [Vue.js devtools](https://chrome.google.com/webstore/detail/vuejs-devtools/nhdogjmejiglipccpnnnanhbledajbpd?hl=pt-BR):

![Vue devtools](/content/images/2016/08/devtools.png)

Está métrica é importante porque é o numero de desenvolvedores usando Vue sériamente (não apenas baixou para testa-lo). Para referência, esse número é cerca de 1/10 do React devtools e 1/2 do Ember devtools.

## Empresas Usando Vue em Produção

Se você olhar individualmente para empresas do *Silicon Valley*, não vai encontrar empresas grandes usando Vue, porque elas naturalmente tendem a usar tecnologias *apoiadas* por empresas como Facebook e Google. No entanto tem uma presença boa em empresas de desenvolvimento/consultoria, há [um projeto feito por terceiros para o Facebook](https://newsfeed.fb.com/) (sim, essa página foi feita com Vue).  
Se tratando do uso empresarial, o Vue tem uma lista muito mais internacional, incluindo a *"big three"* chinesa de tecnologia: Alibaba, Baidu e Tencent, e algumas empresas de destaque mais valorizadas no momento, por exemplo [Xiaomi](https://www.crunchbase.com/organization/xiaomi), [Ele.me](https://www.crunchbase.com/organization/ele-me) e DJI. (Grande parte disso é por que sou muito ativo na comunidade chinesa de JS)  
No Japão, Vue também é usado por empresas mais conceituadas como Line corp & Nintendo. No Reino Unido a Sainsbury’s esta começando a usar Vue.js em larga escala também.

Além disso, existem ótimos projetos de código aberto que agora usam Vue.js extensivamente, por exemplo: [Laravel](http://react-etc.net/entry/php-framework-laravel-selects-vue-js-as-default-javascript-framework), [GitLab](https://about.gitlab.com/jobs/frontend-engineer/) e [PageKit](https://pagekit.com/).

Ah! e aqui esta uma empresa que [mudou para Vue](https://isl.co/2016/07/three-major-reasons-we-decided-to-ditch-angularjs/).

Então se sua principal preocupação é se *"existem empresas usando Vue.js"* a resposta é *yeah*, há várias.

## Vagas

Algumas pessoas gostam de julgar o Vue com base em estatísticas de emprego. Isso é, na minha opinião, uma visão muito míope por várias razoes:

- Como você pode ver, Vue é usado fortemente no cenário internacional, a busca de vagas centrada nos EUA não vai refletir a adoção real.
- A curva de crescimento de vagas esta sempre atrasada com relação a  popularidade (ex: gráfico de estrelas no GitHub), isso por que a *"grande industria"* esta sempre um passo mais lento do que os *early adopters* e empresas mais ágeis, como *startups* e *software houses* de pequeno/médio porte. Nesse momento Vue acaba de conquistar popularidade suficiente para ser notado por não  *early adopters*, a curva de crescimento de vagas não se iniciou ainda. Comparar as vagas de Vue com as atuais demandas do React/Angular é portanto injusto. Considerar a quantidade de vagas para React disponíveis no mercado dois anos atrás é uma história completamente diferente. 
- A demanda de vagas é muito influenciada pelas *"marcas"*, de modo que o apoio do Google/Facebook no Angular/React tem um papel muito grande na quantidade de vagas. Isso é algo que eu não possuo maneira nenhuma de compensar, porém não há correlação direta com o potencial e qualidade do *framework* em si.

---------

## Conclusão

Vue.js é muito popular (com forte presença internacional) e continua crescendo rapidamente. Você o verá cada vez mais popular nos próximos anos.

Você vai notar que eu não fiz nenhuma comparação técnica, pois isso possui pouca relevância com a pergunta. Porém se você tiver interesse, eu terei uma conversa bem detalhada sobre o Vue no *Midwest JS* na próxima semana, e eu vou atualizar esta resposta com os slides depois.

----

Traduzido em 10/08/2016



