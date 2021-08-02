import Vue from 'vue'
import Vuex from 'vuex'
import createPersistedState from "vuex-persistedstate"
import SecureLS from "secure-ls"
// Modules

var ls = new SecureLS({
    encodingType: "aes",
    isCompression: true
  });

Vue.use(Vuex)


export default new Vuex.Store({
    modules: {
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