<template>
  <div>
    <div class="purchase">
      <h2>Karla Accesorios</h2>
      <p>Carrito de compras</p>
      <ul class="actions special">
        <li>
          <a href="/products" class="button primary">Seguir comprando</a>
        </li>
      </ul>
    </div>
    <section id="main" class="container">
      <div class="row">
        <div
          class="col-5 col-12-narrower"
          v-for="product in cart"
          :key="product.id"
        >
          <CartItem :product="product" />
        </div>
      </div>
      <div class="row">
        <div class="col-12 pt-5">
          <Cart />
        </div>
      </div>
    </section>
  </div>
</template>

<script>
// import SideNav from "../components/SideNav.vue";
import CartItem from "@/components/CartItem.vue";
import Cart from "@/components/Cart.vue";
export default {
  name: "ShoppingCart",
  components: {
    //SideNav,
    CartItem,
    Cart,
  },
  computed: {
    cart: function() {
      return this.$store.getters.cart;
    },
  },
};
</script>

<style scoped>
.purchase {
  padding: 6% 2%;
  text-align: center;
  position: inherit;
  background-color: #666;
  color: #ffffff;
}
.purchase h2,
h3,
h4,
h5,
h6 {
  color: #fff;
}
</style>
