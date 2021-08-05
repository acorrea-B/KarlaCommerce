<template>
  <section class="box special">
    <span class="image featured"
      ><img :src="product.image" alt="" v-if="product.image"/><PuSkeleton v-else
    /></span>
    <h3 v-if="product.name">{{ product.name }}</h3>
    <PuSkeleton v-else />
    <p>Descripcion: {{ product.description }}</p>
    Precio: {{ toCurrency(product.value) }}
    <br />
    <br />

    <integer-plusminus
      :min="ipm_min"
      :max="ipm_max"
      :step="ipm_step"
      :vertical="ipm_vertical"
      v-model="ipm_value"
    >
      {{ ipm_value }}

      <template slot="decrement">-</template>

      <template slot="increment">+ </template>
    </integer-plusminus>
    <br />

    <div class="col-8 col-12-mobilep">
      <input
        type="submit"
        :value="itemAlreadyInCart ? 'Agregado' : 'Agregar'"
        class="fit"
        v-if="product"
        @click="addToCart(ipm_value)"
      /><PuSkeleton v-else />
    </div>
  </section>
</template>

<script>
import { IntegerPlusminus } from "vue-integer-plusminus";
export default {
  name: "Product",
  props: ["product"],
  components: { IntegerPlusminus },
  data() {
    return {
      ipm_min: 0,
      ipm_max: 5,
      ipm_step: 1,
      ipm_value: 0,
      ipm_vertical: false,
    };
  },
  created() {
    window.addEventListener("resize", this.wRiseze);
    this.ipm_vertical =
      document.documentElement.clientWidth > 600 ? false : true;
  },
  destroyed() {
    window.removeEventListener("resize", this.wRiseze);
  },
  computed: {
    cart: function() {
      return this.$store.getters.cart;
    },
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
  watch: {
    ipm_value: function(val) {
      console.log(val);
    },
  },
  methods: {
    wRiseze(e) {
      console.log(e);
      if (document.documentElement.clientWidth > 600) {
        this.ipm_vertical = false;
      } else {
        this.ipm_vertical = true;
      }
    },
    toCurrency(value) {
      return (
        "$" + value.toFixed(2).replace(/\d(?=(\d{3})+\.)/g, "$&,") + " COP"
      );
    },
    addToCart(amount) {
      console.log(amount);
      if (amount == 0) {
        if (this.itemAlreadyInCart) {
          this.$store.commit("removeCartItem", this.product);
        }
      } else {
        this.product.amount = amount;
        if (!this.itemAlreadyInCart) {
          this.$store.commit("addCartItem", this.product);
        } else {
          this.$store.commit("updateCartItem", this.product);
        }
      }
    },
  },
};
</script>
