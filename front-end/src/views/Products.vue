<template>
  <div>
    <section id="banner">
      <h2>Karla Accesorios</h2>
      <p>Nuestros productos</p>
    </section>

    <section id="main" class="container">
      <div class="row">
        <div
          class="col-6 col-12-narrower"
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
