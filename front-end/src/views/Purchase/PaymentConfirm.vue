<template>
  <section id="banner">
    <loading :show="show" :label="label"> </loading>
    <h2>Karla Accesorios</h2>
    <p v-if="confirmed">
      {{ costumer.firstName }} tu pago ha sido éxitoso, gracias por preferirnos,
      enviaremos a tu Correo electrónico el voucher de tu compra
    </p>
    <p v-else>
      {{ costumer.firstName }} tu pago se encuentra pendiente de confirmación.
    </p>
    <ul class="actions special">
      <li><a href="/products" class="button primary">Comprar</a></li>
      <li><a href="/" class="button">Log in</a></li>
    </ul>
  </section>
</template>
<script>
import { PurchaseInfo } from "@/services/graphQl/querys";
import loading from "vue-full-loading";

export default {
  data() {
    return {
      purchase: this.$store.getters.purchase,
      costumer: { firstName: "" },
      show: false,
      label: "Estamos procesando tu compra",
      confirmed: false,
    };
  },
  components: {
    loading,
  },
  async mounted() {
    this.show = true;
    /*eslint-disable */
    let response = await this.$apollo
      .query({
        query: PurchaseInfo,
        variables: {
          purchase_id: this.$route.query.purchase,
        },
      })
      .then((result) => {
        if (result.data.purchase.state == "paid") {
          this.confirmed = true;
          this.costumer = resul.data.purchase.costumer;
          this.$store.commit("setpurchase", {});
        }
        this.show = false;
      })
      .catch(({ graphQLErrors }) => {
        this.show = false;
      });
    //console.log(JSON.stringify(this.purchase));
  },
};
</script>
