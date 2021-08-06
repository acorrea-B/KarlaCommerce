<template>
  <div>
    <section id="banner">
      <h2>Karla Accesorios</h2>
      <p>Ventas</p>
    </section>

    <section id="main" class="container">
      <div class="row">
        <div
          class="col-5 col-12-narrower"
          v-for="(item, purchase) in purchases"
          :key="purchase"
        >
          <Purchase :purchase="item" />
        </div>
      </div>
    </section>
  </div>
</template>

<script>
// import SideNav from "../components/SideNav.vue";
import Purchase from "@/components/Purchase.vue";
import { Purchases } from "@/services/graphQl/querys";

export default {
  name: "Home",
  components: {
    Purchase,
  },
  data() {
    return {
      purchases:
        this.$store.getters.purchases.legth > 0
          ? this.$store.getters.purchases
          : [Object, Object],
    };
  },
  created() {
    this.getPurchases();
  },

  methods: {
    async getPurchases() {
      /*eslint-disable */
      let response = await this.$apollo
        .query({
          query: Purchases,
        })
        .then((result) => {
          this.loading = false;
          this.$store.commit("setPurchases", result.data.purchases);
          console.log("productos obtenidos");
          console.log(result.data.purchases);
          this.purchases = result.data.purchases;
        })
        .catch(({ graphQLErrors }) => {
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
