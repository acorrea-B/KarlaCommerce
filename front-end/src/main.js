import router from './router'
import store from './store'
import Vue from 'vue'
import App from './App.vue'
import VueCompositionAPI from '@vue/composition-api'
import { apolloProvider } from '@/services/index.js'
import Skeleton from 'vue-loading-skeleton';
import VueToast from 'vue-toast-notification';
import './global-components'

Vue.use(Skeleton)
import VueMoment from 'vue-moment'
import moment from 'moment-timezone'
require('vue-toast-notification/dist/theme-sugar.css')

Vue.use(VueToast);
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
  VueToast,
  apolloProvider,
  render: h => h(App),
}).$mount('#app')
