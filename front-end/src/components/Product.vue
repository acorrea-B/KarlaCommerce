<template>
  <div class="col-6 col-12-narrower">
    <section class="box special">
      <span class="image featured product-image"
        ><img
          class="product-image"
          :src="product.image"
          alt=""
          v-if="product.image"/><PuSkeleton v-else
      /></span>
      <h3 v-if="product.name">{{ product.name }}</h3>
      <PuSkeleton v-else />
      <p>Descipcion: {{ product.description }}</p>
      Precio:
      <small v-if="product.value"> {{ product.value }} COP</small
      ><PuSkeleton v-else />
      <br />
      <button
        v-if="product"
        @click="addToCart()"
        class="btn btn-primary btn-block"
        :disabled="itemAlreadyInCart"
      >
        {{ itemAlreadyInCart ? "Added" : "Add to Cart" }}</button
      ><PuSkeleton v-else />
    </section>
  </div>
</template>

<script>
export default {
  name: "Product",
  props: ["product"],
  data() {
    return {
      cart: this.$store.getters.cart,
    };
  },
  computed: {
    itemAlreadyInCart() {
      let inCart = false;
      if (this.cart) {
        this.cart.forEach((item) => {
          if (item.id == this.product.id) {
            inCart = true;
          }
        });
      }

      return inCart;
    },
  },
  methods: {
    addToCart() {
      if (!this.itemAlreadyInCart) {
        this.$store.commit("addCartItem", this.product);
      } else {
        alert("Item already added to Cart");
      }
    },
  },
};
</script>
<style>
.product-image {
  width: 20%;
}
</style>
