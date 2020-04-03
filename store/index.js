import posts from '../tmp/posts.json'

export const SET_POSTS = 'SET_POSTS'

export const state = () => ({
  posts: []
})

export const actions = {
  setPosts ({ commit }, posts) {
    commit(SET_POSTS, posts)
  },
  nuxtServerInit ({ dispatch }) {
    console.log('* Set posts from backend')
    dispatch('setPosts', posts)
  }
}

export const mutations = {
  [SET_POSTS] (state, posts) {
    state.posts = posts
  }
}
