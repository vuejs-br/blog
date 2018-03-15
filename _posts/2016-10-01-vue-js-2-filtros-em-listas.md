---
layout: post
title: 'Vue.js 2 - Filtros em Listas'
main-class: 'dev'
date: 2016-10-01 19:13:22 
description: derscricao
color: '#637a91'
tags: vuejs2
 -vue2
 -listas
 -colections
 -arrays
 -axios
 -lodash
 -computeds
layout: post
introduction: introducao
---

Com a nova versão do Vue.js a possibilidade de aplicar filtros no `v-for` deixou de existir. Porém esse recurso sempre trouxe certa confusão e até mesmo perda de performance.

Isso não é motivo de pânico para ninguém, a alternativa já existia muito antes da remoção desse recurso: [**computeds properties**](http://vuejs.org/guide/computed.html#Computed-Properties)

Com *computeds properties* você ganha a habilidade de criar propriedades baseadas em outras propriedades do componente.

<iframe width="100%" height="400" src="//jsfiddle.net/fhv6gbg4/embedded/js,html,result/" allowfullscreen="allowfullscreen" frameborder="0"></iframe>

Nesse exemplo criamos a propriedade `fullName` a partir de `firstName` e `lastName`. Este é um recurso muito útil e poderoso, além de performático. O Vue.js faz cache do resultado, só alterando ele quando as dependências dele são alteradas (`firstName` e `lastName`).

O mesmo procedimento pode ser feito com listas, criando listas dinâmicas a partir de outros dados.

## Ordenando

Consumir uma API com Vue.js é muito simples. Dessa vez vamos usar o [axios](https://github.com/mzabriskie/axios), saiba mais sobre ele em [Vue.js e Serviços](https://blog.codecasts.com.br/vue-js-e-servicos-4d4439320a2)

<iframe width="100%" height="500" src="//jsfiddle.net/vinicius73/cwqpxbf1/2/embedded/js,html,result/" allowfullscreen="allowfullscreen" frameborder="0"></iframe>


Porém essa lista não possui uma ordem definida, nesse momento vamos combinar o poder das *computeds properties* com a simplicidade e do javascript.

Vamos também usar o [*lodash*](https://lodash.com) para ajudar na tarefa, mesmo que essa seja uma tarefa simples para o um script javascript puro, no dia-a-dia você vai usar bastante esta *lib*, então vamos praticar com ela.

<iframe width="100%" height="500" src="//jsfiddle.net/vinicius73/cwqpxbf1/3/embedded/js,html,result/" allowfullscreen="allowfullscreen" frameborder="0"></iframe>

Foi criada a *computed property* `list` e trocamos `repos` por ela na nossa template. Agora a lista esta esta ordenada por nome, porém podemos deixar isso mais dinâmico.

<iframe width="100%" height="500" src="//jsfiddle.net/vinicius73/cwqpxbf1/5/embedded/js,html,result/" allowfullscreen="allowfullscreen" frameborder="0"></iframe>

Agora temos um controle dinâmico da ordenação da lista.

# Filtrando

Temos a ordem do nossa lista pronta, agora vamos pesquisar dentro dela.

<iframe width="100%" height="550" src="//jsfiddle.net/vinicius73/cwqpxbf1/7/embedded/js,html,result/" allowfullscreen="allowfullscreen" frameborder="0"></iframe>

Agora nós temos a habilidade de ordenar e filtrar nossa lista.

## Reaproveitamento

No começo isso pode parecer difícil, até mesmo ruim, porém com um pouco mais de abstração fica bem mais simples.

```javascript
// helpers/strings.js
import { deburr, isEmpty } from 'lodash';
export const sanitize = deburr;
export const sanitizeAndLower = value => sanitize(value).toLowerCase();
export const contains = (st, value) => sanitizeAndLower(st).indexOf(sanitizeAndLower(value)) > -1;
```

```javascript
// helpers/filters/by-prop.js
import { filter } from 'lodash';
import { contains } from '../strings';

export const makeFilterByProp = key => (list, st) => filter(list, row => contains(row[key], st));
export default (key, list, st) => filter(list, row => contains(row[key], st));
```

```javascript
// helpers/by-name.js
import { makeFilterByProp } from './by-prop';

export default makeFilterByProp('name');
```

```javascript
// an component
import { orderBy, isEmpty } from 'lodash';
import filterByName from '../helpers/filters/by-name';

// omit

computed: {
  listOrdened() {
    const { orderBy as by, order } = this.configs;
    
    return orderBy(this.repos, by, order);
  },
  list() {
    const filter = this.configs.filter;
    if (isEmpty(filter)) {
      return this.listOrdened;
    }

    return filterByName(this.listOrdened, filter);
  },
},
```

Esse conjunto de scripts prevê os principais problemas na hora de filtrar uma coleção, e deixa tudo abstraído para facilitar o uso em vários locais. Tudo isso é javascript puro e agnóstico, pode ser utilizado em vários locais e situações. Link para o [gist aqui](https://gist.github.com/vinicius73/c10297ca3c14dae7b8095cbad5747da7).

---------

Participe da comunidade

- https://telegram.me/vuejsbrasil
- http://slack.vuejs-brasil.com.br
- https://www.facebook.com/groups/vuejsbr/
- https://forum.codecasts.com.br/t/vuejs

---------

Se quiser saber mais sobre meu trabalho visite [codecasts.com.br](https://codecasts.com.br). Lá você vai ver vídeos sobre [Javascript](https://codecasts.com.br/lesson/domine-this-01-scopes), [jQuery](https://codecasts.com.br/lesson/javascript-jquery-vol1-01-resolvendo-o-problema), [Gulp](https://codecasts.com.br/lesson/gulp-level01-compilando-e-minificando-sass), [ES6](https://codecasts.com.br/lesson/ES6-00-o-que-e-es6), [Vue.JS](https://codecasts.com.br/lesson/vue-init-01-hello-world), [Docker](https://codecasts.com.br/lesson/docker-na-pratica-ola-docker) e muito mais.

-------

