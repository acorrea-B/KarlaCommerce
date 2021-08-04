<template>
  <div id="app" class="h-100">
    <div id="nav">
      <nav class="navbar navbar-expand-lg navbar-dark bg-dark">
        <router-link to="/" class="navbar-brand"
          >The Identity Store - Define your Style</router-link
        >

        <button
          class="navbar-toggler"
          type="button"
          data-toggle="collapse"
          data-target="#navbarText"
          aria-controls="navbarText"
          aria-expanded="false"
          aria-label="Toggle navigation"
        >
          <span class="navbar-toggler-icon" />
        </button>
      </nav>
    </div>
    <router-view />
  </div>
</template>

<script>
import { localize } from "vee-validate";
import es from "vee-validate/dist/locale/es.json";

const LayoutFull = () => import("@/layouts/LayoutDefault");

localize("es", es);

export default {
  name: "App",
  components: {
    LayoutFull,
  },
  computed: {
    layout() {
      return "layout-full";
    },
  },
};
</script>
