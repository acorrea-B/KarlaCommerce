<template>
  <section class="box special features">
    <div class="subtotalBox">
      <div class="subtotal">
        <ul>
          <li class="totalRow">
            <span class="label">Subtotal</span
            ><span class="value">{{ toCurrency(totalPrice) }}</span>
          </li>

          <li class="totalRow final">
            <span class="label">Valor total</span
            ><span class="value">{{ toCurrency(totalPrice) }}</span>
          </li>
          <li class="totalRow" @click="newPurchase">
            <a :href="redirect" @click="func(0)" class="btn continue"
              >Revisar</a
            >
          </li>
        </ul>
      </div>
    </div>
  </section>
</template>

<script>
export default {
  data() {
    return {
      redirect: "#",
    };
  },
  computed: {
    cart: function() {
      return this.$store.getters.cart;
    },
    totalPrice() {
      return this.cart.reduce((total, next) => {
        let value = next.value ? total + next.amount * next.value : total + 0;

        return value;
      }, 0);
    },
  },
  methods: {
    toCurrency(value) {
      return (
        "$ " + value.toFixed(2).replace(/\d(?=(\d{3})+\.)/g, "$&,") + " COP"
      );
    },
    newPurchase() {
      if (this.cart.length > 0) {
        this.$store.commit("setpurchase", {
          products: this.cart,
          total_value: this.totalPrice,
        });
        this.redirect = "/purchase";
      } else {
        this.$toast.open({
          message:
            "!Hooo noo¡ aun no hay productos en el carrito, primero intenta agregar los para realizar la compra.",
          type: "warning",
          duration: 5000,
        });
      }
    },
  },
};
</script>
<style lang="scss">
@import url("https://fonts.googleapis.com/css?family=Droid+Serif:400,400italic|Montserrat:400,700");

$fontSans: "Montserrat", sans-serif;
$fontSerif: "Droid Serif", serif;
@mixin transition($transition-property, $transition-time, $method) {
  -webkit-transition: $transition-property $transition-time $method;
  -moz-transition: $transition-property $transition-time $method;
  -ms-transition: $transition-property $transition-time $method;
  -o-transition: $transition-property $transition-time $method;
  transition: $transition-property $transition-time $method;
}

.btn {
  &:link,
  &:visited {
    text-decoration: none;
    font-family: $fontSans;
    letter-spacing: -0.015em;
    font-size: 1em;
    padding: 1em 3em;
    color: #fff;
    background: #82ca9c;
    font-weight: bold;
    border-radius: 50px;
    float: right;
    text-align: right;
    @include transition(all, 0.25s, linear);
  }
  &:after {
    content: "\276f";
    padding: 0.5em;
    position: relative;
    right: 0;
    @include transition(all, 0.15s, linear);
  }
  &:hover,
  &:focus,
  &:active {
    background: #f69679;
    &:after {
      right: -10px;
    }
  }
}
.subtotalBox {
  width: 100%;
  min-height: 150px;
}
.subtotal {
  float: right;
  width: 40%;
  .totalRow {
    list-style: none;
    padding: 0.5em;
    text-align: right;

    &.final {
      font-size: 1.25em;
      font-weight: bold;
    }
    span {
      display: inline-block;
      padding: 0 0 0 1em;
      text-align: right;
    }
    .label {
      font-family: $fontSans;
      font-size: 0.85em;
      text-transform: uppercase;
      color: #777;
    }
    .value {
      letter-spacing: -0.025em;
      width: 50%;
    }
  }
}
@media only screen and (max-width: 39.375em) {
  .subtotal {
    width: 100%;
  }

  a.btn.continue {
    width: 100%;
    text-align: center;
  }
}
</style>
