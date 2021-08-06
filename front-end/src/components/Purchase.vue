<template>
  <section class="box special">
    <h3 v-if="purchase.id">{{ toCurrency(purchase.totalValue) }}</h3>
    <PuSkeleton v-else />
    <p v-if="purchase.state">Estado de la compra: {{ purchase.state }}</p>
    <PuSkeleton v-else />
    <p v-if="purchase.purchaseDate">
      Fecha de la compra: {{ purchase.purchaseDate }}
    </p>
    <PuSkeleton v-else />
    <p v-if="purchase.purchaseDate">
      Cliente: {{ purchase.costumer.firstName }}
      {{ purchase.costumer.lastName }}
    </p>
    <p v-if="purchase.products">Numero de productos: {{ items }}</p>
    <PuSkeleton v-else />
    <br />
    <br />
    {{ purchase.id }}
    <div class="col-8 col-12-mobilep">
      <input
        type="submit"
        :value="'Reembolsar'"
        class="fit"
        v-if="purchase.state == 'paid'"
        @click="refund()"
      />
    </div>
  </section>
</template>

<script>
import { RefoundPayment } from "@/services/graphQl/mutations";
export default {
  name: "Purchase",
  props: ["purchase"],
  data() {
    return {};
  },
  computed: {
    items: function() {
      return this.purchase.products.edges.length;
    },
  },
  methods: {
    toCurrency(value) {
      return (
        "$ " + value.toFixed(2).replace(/\d(?=(\d{3})+\.)/g, "$&,") + " COP"
      );
    },
    async refund() {
      /*eslint-disable */
      this.show = true;
      let response = await this.$apollo
        .mutate({
          mutation: RefoundPayment,
          variables: {
            purchase_id: this.purchase.id,
          },
        })
        .then((result) => {
          console.log(result.data.purchase);
          this.purchase = result.data.purchase;
        })
        .catch(({ graphQLErrors }) => {
          this.show = false;
          console.log(graphQLErrors);
          this.$toast.open({
            message: "Credenciales erroneas, intentalo nuevamente",
            type: "error",
            duration: 5000,
          });
        });
    },
  },
};
</script>
