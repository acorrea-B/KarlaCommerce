<template>
  <div id="app"
  class="h-100"
  >
    <component :is="layout">
      <router-view />
    </component>
  </div>
</template>

<script>

import { localize } from 'vee-validate'
import es from 'vee-validate/dist/locale/es.json'


const LayoutFull = () => import('@/layouts/LayoutDefault')

localize('es', es)

export default {
  name: 'App',
  components: {
    LayoutFull,
  },computed:{
      layout() {
       return 'layout-full'
    }
    }
}
</script>
