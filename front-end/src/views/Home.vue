<template>
  <div class="home container">
    <div class="row">
      <div class="col-md-9 pt-5">
        <div
          class="row row-cols-1 row-cols-sm-2 row-cols-md-3 row-cols-lg-3 row-cols-xl-3"
        >
          <div v-for="(item, product) in products" :key="product.id">
            <Product :product="item" />
          </div>
        </div>
      </div>
      <div class="col-md-3 pt-5">
        <!-- <SideNav /> -->
        <Cart />
      </div>
    </div>
  </div>
</template>

<script>
// import SideNav from "../components/SideNav.vue";
import Product from "@/components/Product.vue";
import Cart from "@/components/Cart.vue";
import { ListProducts } from "@/services/graphQl/querys";

export default {
  name: "Home",
  components: {
    Product,
    Cart,
  },
  data() {
    return {
      cart: [],
      products: this.$store.getters.products,
    };
  },
  created() {
    this.getProducts();
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
          console.log(graphQLErrors);
        });
    },
  },
};
</script>
