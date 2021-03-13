---
layout: post
title: 'CRUD básico com Vue.js e json-server #4'
main-class: 'dev'
date: 2016-07-27 11:34:00 
color: '#637a91'
tags: vue-js
author: daniel-schmitz
---

Após realizar a paginação no [artigo anterior](http://www.vuejs-brasil.com.br/crud-basico-com-vue-js-e-json-server-3/), podemos implementar a busca pelo nome da cervejarias. Voltando ao código html das cervejarias, temos:

```html
<p class="control has-addons">
 <input class="input is-expanded" type="text" placeholder="Procure pelo nome" v-model="search">
 <a class="button is-info" @click.prevent="searchBreweries">Search</a>
</p>
```

O método `searchBreweries` possui uma característica peculiar. Sua única função é chamar novamente o método `loadBreweries`, que será responsável em realizar a busca. O método `searchBreweries` existe unicamente para que você possa tratar algo na variável `this.search`, caso necessite, e então chamar o `loadBreweries`.

Iremos implementar no método `loadBreweries` a funcionalidade para realizar uma busca. No json-server, uma busca full text pode ser executada repassando a variável "q" na url. Por exemplo, ao realizar "/breweries?q=foo", somente as cervejarias que contenham "foo" em algum campo do registro, será retornado. 

Para implementar a busca junto com a paginação, podemos realizar o seguinte *truque*:

```
...
 loadBreweries(){

        let t = this
        this.showLoading()

        let start = (this.page * this.itensPerPage) - (this.itensPerPage)
        let end = this.page * this.itensPerPage
        let qString = "";

        if (this.search){
          qString = `&q=${this.search}`
        }

        this.$http.get(`/breweries?_start=${start}&_end=${end}${qString}`).then(
         response=>{
           t.breweries = response.json()
           t.total = response.headers['X-Total-Count']
         },
         error=>{
           console.log(error)
         }).finally(function () {
          t.hideLoading();
        })

       },
       searchBreweries(){
        this.loadBreweries()
       }
     },
     created(){
      this.loadBreweries();
    },
...
```

Observe o código adicionado:

```
 if (this.search){
          qString = `&q=${this.search}`
        }
```

Na url de acesso ao json server, inserimos o `qString` somente se `this.search` estiver preenchida. Quando a variável `this.search` está preenchida, significa que algo foi digitado no campo de busca, pois estão ligados pelo `v-model`. A busca é enviada ao json-server e este se encarrega de realizá-la. A busca é realizada em todos os campos, uma característica do json-server.

 




