<template>
  <section class="box special">
    <span class="image featured"
      ><img :src="product.image" alt="" v-if="product.image"/><PuSkeleton v-else
    /></span>
    <h3>{{ product.name }}</h3>
    <p v-if="product.value">Descripcion: {{ product.description }}</p>
    <PuSkeleton v-else />
    <p v-if="product.value">Precio: {{ toCurrency(product.value) }}</p>
    <PuSkeleton v-else />
    <div>Cantidad: {{ product.amount }}</div>

    <div>
      <input
        type="submit"
        :value="'Eliminar'"
        class="fit"
        v-if="product"
        @click="removeItem()"
      />
    </div>
  </section>
</template>

<script>
export default {
  name: "CartItem",
  props: ["product"],
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
    toCurrency(value) {
      return (
        "$ " + value.toFixed(2).replace(/\d(?=(\d{3})+\.)/g, "$&,") + " COP"
      );
    },
    removeItem() {
      this.$store.commit("removeCartItem", this.product);
      this.cart;
    },
  },
};
</script>
<style scoped>
.purchaseDetail {
  padding: 6% 2%;
  text-align: center;
  position: inherit;
  background-color: #ffffff;
}
.purchase h2,
h3,
h4,
h5,
h6 {
  color: #fff;
}
</style>
