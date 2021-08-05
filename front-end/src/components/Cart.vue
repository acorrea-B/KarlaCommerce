<template>
  <div class="card">
    <div class="card-body">
      <h5 class="card-title">Detalle de compra</h5>
      <p v-if="cart.length == 0">
        Aun no hay productos en tu carrito
      </p>
    </div>
    <ul class="list-group list-group-flush">
      <li
        v-for="item in cart"
        :key="item.id"
        class="list-group-item d-flex justify-content-between align-items-center"
      >
        {{ item.name }}
        <span class="badge badge-primary badge-pill">{{ item.amount }}</span>
      </li>
      <li
        class="list-group-item d-flex justify-content-between align-items-center"
      >
        Valor total <b>{{ totalPrice }}</b>
      </li>
    </ul>

    <div v-if="cart.length == 0">
      <ul class="actions special">
        <li><a href="/products" class="button primary">Productos</a></li>
      </ul>
    </div>
    <div v-else>
      <ul class="actions special">
        <li><a href="/shop" class="button primary">Revisar</a></li>
      </ul>
    </div>
  </div>
</template>

<script>
export default {
  computed: {
    cart: function() {
      return this.$store.getters.cart;
    },
    totalPrice() {
      return this.cart.reduce((total, next) => {
        let value = total + next.amount * next.value;
        return (
          "$ " + value.toFixed(2).replace(/\d(?=(\d{3})+\.)/g, "$&,") + " COP"
        );
      }, 0);
    },
  },
};
</script>
