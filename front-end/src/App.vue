<template>
  <div id="app" class="landing is-preload">
    <section class="cartProducts">
      <a href="/shop"> <span class="icon solid major fa-cart-plus"></span></a>
    </section>
    <router-view />
    <section id="cta">
      <h2>Sign up for beta access</h2>
      <p>
        Blandit varius ut praesent nascetur eu penatibus nisi risus faucibus
        nunc.
      </p>

      <form>
        <div class="row gtr-50 gtr-uniform">
          <div class="col-8 col-12-mobilep">
            <input
              type="email"
              name="email"
              id="email"
              placeholder="Email Address"
            />
          </div>
          <div class="col-4 col-12-mobilep">
            <input type="submit" value="Sign Up" class="fit" />
          </div>
        </div>
      </form>
    </section>
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
  position: absolute;
  top: 1%;
  left: 94%;
}
@media only screen and (max-width: 600px) {
  .cartProducts {
    position: absolute;
    top: 1%;
    left: 85%;
  }
}
</style>
