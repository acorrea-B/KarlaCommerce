<template>
  <div>
    <div class="purchase">
      <h2>Karla Accesorios</h2>
      <p>Carrito de compras</p>
    </div>
    <div class=" container">
      <div class="row">
        <div class="col-12 pt-5">
          <CartItem
            v-for="product in cart"
            :product="product"
            :key="product.id"
          />
        </div>
        <div class="col-12 pt-5">
          <Cart />
        </div>
      </div>
    </div>
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
  data() {
    return {
      cart: this.$store.getters.cart,
    };
  },
};
</script>

<style scoped>
.purchase {
  padding: 6% 2%;
  text-align: center;
  position: inherit;
  background-color: #7fcdb8;
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
