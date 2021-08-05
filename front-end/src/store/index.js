import Vue from 'vue'
import Vuex from 'vuex'
import createPersistedState from "vuex-persistedstate"
import SecureLS from "secure-ls"
import products from './products'
import purchases from './purchases'
import operator from './operator'
import cart from './cart'
// Modules

var ls = new SecureLS({
    encodingType: "aes",
    isCompression: true
  });

Vue.use(Vuex)


export default new Vuex.Store({
    modules: {
        products,
        purchases,
        operator,
        cart
    },
    plugins: [createPersistedState(
      {
        key: 'EG',
        storage: {
          getItem: key => ls.get(key),
          setItem: (key, value) => ls.set(key, value),
          removeItem: key => ls.remove(key)
        }
      }
    )],
    strict: process.env.DEV,
  })