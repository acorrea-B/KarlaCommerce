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
import HelloWorld from './components/HelloWorld.vue'
import { watch } from '@vue/composition-api'
import store from '@/store'
import { localize } from 'vee-validate'
import es from 'vee-validate/dist/locale/es.json'

localize('es', es)

export default {
  name: 'App',
  components: {
    HelloWorld
  }
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
