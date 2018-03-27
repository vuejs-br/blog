---
layout: post
title: 'Indexando páginas no Google de sua SPA Vue.js'
main-class: 'dev'
date: 2016-07-05 12:12:43 
color: '#637a91'
tags: vue-js single-page-application
layout: post
author: vinicius
---

Um dos temas mais discutidos quando envolve aplicações de página única (SPA) e a otimização para mecanismos de busca (SEO) é a dificuldade de indexar as páginas no índice e fazer com que os bots reconheçam as meta tags que foram modificadas dinamicamente através da aplicação Javascript.

Hoje em dia existem serviços online que ajudam com esse problema, como o [Prerender](https://prerender.io/) e o [SEO4Ajax](https://www.seo4ajax.com/). Ambos permitem utilizar uma conta free, porem com algum limite. Eles provem uma forma automática de detecção de links na página e criam um cachê de cada uma para servir aos bots. Esses serviços precisam de um servidor para configurar e sincronizar com o serviço.

No meu blog pessoal, que é uma SPA feito com Vue.js, uso uma hospedagem gratuita e incrivelmente poderosa que se chama [Surge](https://surge.sh/) e só é possível utilizar arquivos estáticos, nesse caso, não tenho acesso ao servidor e com isso não posso utilizar esses serviços citados acima para me ajudar a indexar minhas página.

Parti para métodos alternativos e utilizei o plugin [vue-head](https://github.com/ktquez/vue-head) para alterar dinamicamente a descrição e o título da página na rota correspondente.

Veja esse código de exemplo: *(Sintaxe atualizada v2.0+)*
```javascript
// components/page/contact.vue

...
export default {
    // Omitido ...
    head: {
      title: {
        inner: 'Será um prazer'
      },
      meta: [
        { name: 'description', content: '...My description...', id: 'description' }
      ]
    }
}
...

```

O `vue-head` disponibiliza um objeto dentro de cada componente e com ele podemos definir uma gama de meta tags, link, title e etc. No exemplo acima foi usado informações fixas, mas essas informações podem ser carregadas através de um servidor (API) que também funcionará corretamente.

Podemos ver que foi definido o title da página:
```javascript
title: {
   inner: 'Será um prazer'
}
```

E a meta tag de descrição:
```javascript
meta: {
  name: [
        { name: 'description', content: '...My description...', id: 'description' }
  ]
}
```

Com isso ao acessar a URL de contato no blog, o título e a descrição passará a ser modificada, dando maior sentido ao contexto onde o usuário está navegando.

Com tudo configurado, sai em busca e testei várias possibilidades e uma delas eu encontrei no próprio [Google search console](https://www.google.com/webmasters/tools/googlebot-fetch).

- Ao acessar vá até o menu Rastreamento > Buscar como o Google.  
- Digite a URL que deseja enviar para índice   
- Clique no botão `Buscar e Renderizar`

![Renderizando e indexando](/content/images/2016/07/indexar-paginas-google-spa-vue-js-1.jpg)

- Aguarde que esteja disponível, pois durante o processo você verá o status do link como `Pendente`
- Quando concluído o processo, clique no botão `Enviar ao índice`

Irá aparecer uma janela como essa:
![Rastreando links](/content/images/2016/07/indexar-paginas-google-spa-vue-js2-1.jpg)

> Utilize nas páginas mais importantes à opção "Rastrear este URL e seus links diretos", ele é mais eficiente, não é a toa que o Google só disponibiliza 10 inserções mensais

Após isso em poucas horas sua página estará no índice e com as informações corretas, como mostra a imagem abaixo.

![Página no índice](/content/images/2016/07/indexar-paginas-google-spa-vue-js3-1.jpg)

### Outras configurações que são essenciais
**Use o Mode HTML5**  
Se está utilizando o Vue.js, provavelmente estará utilizando *Vue-router*, com ele é possível configurar um modo mais amigável para URLs.

```javascript
const router = new VueRouter({
  history: true
})
```

Saiba mais em [http://router.vuejs.org/en/options.html#history](http://router.vuejs.org/en/options.html#history)

**Sitemaps em sua aplicação é essencial**  
Estruture corretamente todos os links do seu site em um sitemap.xml e disponibilize na sua aplicação, ele informa aos mecanismos todas as URLs que você deseja indexar.

Você também pode enviar a cada atualização de link, no próprio [Google Search Console](https://www.google.com/webmasters/tools/sitemap-list) 

- Ao acessar vá até o menu Rastreamento > Sitemaps
- Vá até o botão Adicionar/testar Sitemap
- Adicione a URL que contém um arquivo sitemap.xml

![Adicionando sitemap](/content/images/2016/07/img-post2-1.jpg)

O importante também de saber e como deu para notar, é um processo manual e que se aplica somente para o Google, futuramente teremos algo semelhante em outros mecanismos, pois SPA está ficando mais comuns na web e merece uma atenção urgente para esse tipo de problema.

>Foi utilizado o vue-head no Vue.js, mas em qualquer outro framework, lib ou Javascript puro é possível modificar as meta informações da página.

Se você conhece mais maneiras de ajudar o SEO de single pages ou alguma dúvida no processo, deixa o comentário.





