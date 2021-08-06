<template>
  <div>
    <section id="banner">
      <h2>Karla Accesorios</h2>
      <p>Nuestros productos</p>
      <section class="cartProducts">
        <a href="/shop"> <span class="icon solid major fa-cart-plus"></span></a>
        <span class="purchaseItems">{{ itemNumber }}</span>
      </section>
    </section>

    <section id="main" class="container">
      <div class="row">
        <div
          class="col-5 col-12-narrower"
          v-for="(item, product) in products"
          :key="product.id"
        >
          <Product :product="item" />
        </div>
      </div>
    </section>
  </div>
</template>

<script>
// import SideNav from "../components/SideNav.vue";
import Product from "@/components/Product.vue";
import { ListProducts } from "@/services/graphQl/querys";

export default {
  name: "Home",
  components: {
    Product,
  },
  data() {
    return {
      products:
        this.$store.getters.products.legth > 0
          ? this.$store.getters.products
          : [Object, Object],
    };
  },
  created() {
    this.getProducts();
  },
  computed: {
    cart: function() {
      return this.$store.getters.cart;
    },
    itemNumber() {
      return this.cart.length;
    },
  },
  methods: {
    async getProducts() {
      /*eslint-disable */
      let response = await this.$apollo
        .query({
          query: ListProducts,
        })
        .then((result) => {
          this.loading = false;
          this.$store.commit("setproducts", result.data.listProducts);
          console.log("productos obtenidos");
          console.log(this.products);
          this.products = result.data.listProducts;
        })
        .catch(({ graphQLErrors }) => {
          this.products = [Object, Object];
          console.log(graphQLErrors);
        });
    },
  },
};
</script>
<style scoped>
.purchaseItems {
  position: absolute;
  left: -10%;

  width: 1.5em;
  line-height: 1.5em;
  height: 1.5em;
  text-align: center;
  background: #7fcdb8;
  border-radius: 100%;
}
</style>
