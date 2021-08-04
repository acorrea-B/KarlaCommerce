import router from './router'
import store from './store'
import Vue from 'vue'
import App from './App.vue'
import VueCompositionAPI from '@vue/composition-api'
import { apolloProvider } from '@/services/index.js'
import Skeleton from 'vue-loading-skeleton';
import './global-components'

Vue.use(Skeleton)
import VueMoment from 'vue-moment'
import moment from 'moment-timezone'

Vue.use(VueCompositionAPI)
require('moment/locale/es')

Vue.use(VueMoment, {
    moment
})

import bootstrapvue from 'bootstrap-vue'
Vue.use(bootstrapvue)

Vue.config.productionTip = false

new Vue({
  router,
  store,
  apolloProvider,
  render: h => h(App),
}).$mount('#app')
