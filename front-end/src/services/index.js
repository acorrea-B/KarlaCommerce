import Vue from 'vue'
import { ApolloClient } from 'apollo-client'
import { setContext } from 'apollo-link-context'
import { createHttpLink } from 'apollo-link-http'
import { InMemoryCache } from 'apollo-cache-inmemory'
import store from '@/store'
import VueApollo from 'vue-apollo'


// HTTP connection to the API
const httpLink = createHttpLink({
  // You should use an absolute URL here
  //uri: 'https://services.klcmpopayan.com/api/',
  uri: 'http://127.0.0.1:8000/api/',
})
// Error Handling


const authLink = setContext((_, { headers }) => {
  // get the authentication token from ApplicationSettings if it exists
  const token = store.getters.token;
  // return the headers to the context so HTTP link can read them
  return {
      headers: {
          ...headers,
          ...(token ? {authorization: `JWT ${token}`} : {})
      }
  }
})
// Create the apollo client
const apolloClient = new ApolloClient({
  link: authLink.concat(httpLink),
  cache: new InMemoryCache(),
})
Vue.use(VueApollo)
export const apolloProvider = new VueApollo({
    defaultClient: apolloClient
})