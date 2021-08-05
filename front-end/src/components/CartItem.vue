<template>
  <div class="row cart-item-row">
    <div class="col-12">
      <Product :product="product" cartButton="true" />
    </div>
    <div class="col-12">
      <div class="col-12 col-12-mobilep" v-if="!cartButton">
        <input
          type="submit"
          :value="'Eliminar'"
          class="fit"
          v-if="product"
          @click="removeItem()"
        />
      </div>
    </div>
  </div>
</template>

<script>
import Product from "./Product.vue";
export default {
  name: "CartItem",
  props: ["product"],
  components: {
    Product,
  },
  computed: {
    cart: function() {
      return this.$store.getters.cart;
    },
    itemQuantity() {
      let get_product = this.cart.filter((item) => item.id == this.product.id);
      return get_product[0].quantity;
    },
  },
  methods: {
    removeItem() {
      this.$store.commit("removeCartItem", this.product);
      this.cart;
    },
  },
};
</script>
