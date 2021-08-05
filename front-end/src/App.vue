<template>
  <div id="app" class="landing is-preload">
    <router-view />

    <footer id="footer">
      <ul class="icons">
        <li>
          <a href="#" class="icon brands fa-twitter"
            ><span class="label">Twitter</span></a
          >
        </li>
        <li>
          <a href="#" class="icon brands fa-facebook-f"
            ><span class="label">Facebook</span></a
          >
        </li>
        <li>
          <a href="#" class="icon brands fa-instagram"
            ><span class="label">Instagram</span></a
          >
        </li>
        <li>
          <a href="#" class="icon brands fa-github"
            ><span class="label">Github</span></a
          >
        </li>
        <li>
          <a href="#" class="icon brands fa-dribbble"
            ><span class="label">Dribbble</span></a
          >
        </li>
        <li>
          <a href="#" class="icon brands fa-google-plus"
            ><span class="label">Google+</span></a
          >
        </li>
      </ul>
      <ul class="copyright">
        <li>&copy; Untitled. All rights reserved.</li>
        <li>Design: <a href="http://html5up.net">HTML5 UP</a></li>
      </ul>
    </footer>
  </div>
</template>

<script>
import { localize } from "vee-validate";
import es from "vee-validate/dist/locale/es.json";

localize("es", es);
export default {
  name: "App",
};
</script>
<style lang="scss">
@import "assets/css/main.css";
.cartProducts {
  position: fixed;
  z-index: 1000000000000;
  top: 1%;
  left: 94%;
}
@media only screen and (max-width: 600px) {
  .cartProducts {
    position: fixed;
    z-index: 1000000000000;
    top: 85%;
    left: 80%;
  }
}
</style>
