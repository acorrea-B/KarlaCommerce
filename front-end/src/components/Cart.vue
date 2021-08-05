<template>
  <section class="box special">
    <div class="subtotal">
      <ul>
        <li class="totalRow">
          <span class="label">Subtotal</span
          ><span class="value">{{ totalPrice }}</span>
        </li>

        <li class="totalRow final">
          <span class="label">Valor total</span
          ><span class="value">{{ totalPrice }}</span>
        </li>
        <li class="totalRow"><a href="#" class="btn continue">Revisar</a></li>
      </ul>
    </div>
    <div v-if="cart.length == 0">
      <ul class="actions special">
        <li><a href="/products" class="button primary">Productos</a></li>
      </ul>
    </div>
  </section>
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
.subtotal {
  float: right;
  width: 35%;
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
