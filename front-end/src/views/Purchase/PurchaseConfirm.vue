<template>
  <section id="cta">
    <h2>Datos del comprador</h2>
    <p>
      Un último paso para rgistrar tu compra, para eso necsitamos unos datos
      basicos tuyos para poder identificarte.
    </p>

    <loading :show="show" :label="label"> </loading>
    <form @submit.prevent="newPurchase">
      <div class="row gtr-50 gtr-uniform">
        <div class="col-8 col-12-mobilep">
          <input
            type="text"
            name="firstName"
            id="firstName"
            placeholder="Nombres"
            v-model="costumer.firstName"
          />
        </div>
        <div class="col-8 col-12-mobilep">
          <input
            type="text"
            name="lastName"
            id="lastName"
            placeholder="Apellidos"
            v-model="costumer.lastName"
          />
        </div>
        <div class="col-8 col-12-mobilep">
          <input
            type="text"
            name="identification"
            id="identification"
            placeholder="Número de cédula"
            v-model="costumer.identification"
          />
        </div>
        <div class="col-8 col-12-mobilep">
          <input
            type="email"
            name="email"
            id="email"
            placeholder="Correo electrónico"
            v-model="costumer.email"
          />
        </div>

        <div class="col-4 col-12-mobilep">
          <input v-if="!linkPayment" type="submit" value="Listo" class="fit" />
          <input
            v-else
            type="submit"
            value="Ir a pagar"
            @click="goPay"
            class="fit"
          />
        </div>
      </div>
    </form>
  </section>
</template>

<script>
import { NewPurchase } from "@/services/graphQl/mutations";
import loading from "vue-full-loading";

export default {
  data() {
    return {
      purchase: this.$store.getters.purchase,
      costumer: {},
      show: false,
      label: "Estamos procesando tu compra",
      linkPayment: "",
    };
  },
  components: {
    loading,
  },
  methods: {
    goPay() {
      window.location.href = this.linkPayment;
    },
    async newPurchase() {
      if (
        this.costumer.firstName &&
        this.costumer.lastName &&
        this.costumer.identification &&
        this.costumer.email
      ) {
        this.show = true;
        this.purchase.costumer = this.costumer;
        this.$store.commit("setpurchase", this.purchase);
        /*eslint-disable */
        let products = [];
        for (const item in this.purchase.products) {
          products.push({
            productId: this.purchase.products[item].id,
            amount: this.purchase.products[item].amount,
          });
        }
        let response = await this.$apollo
          .mutate({
            mutation: NewPurchase,
            variables: {
              total_value: this.purchase.total_value,
              costumer: this.purchase.costumer,
              products: products,
            },
          })
          .then((result) => {
            this.linkPayment = result.data.newPurchase.payment.tpagaPaymentUrl;
            this.show = false;
            console.log(result.data.newPurchase.purchase.id);
            this.purchase.id = result.data.newPurchase.purchase.id;
          })
          .catch(({ graphQLErrors }) => {
            this.show = false;
            console.log(graphQLErrors);
            this.$toast.open({
              message:
                "!Ooops¡ Estamos teniendo problemas houston, intentalo nuevamente",
              type: "error",
              duration: 5000,
            });
          });
        //console.log(JSON.stringify(this.purchase));
      } else {
        this.show = false;
        this.$toast.open({
          message:
            "!Aun nos faltan datos¡ Procura ingresar todos los datos del comprador",
          type: "warning",
          duration: 5000,
        });
      }
    },
  },
};
</script>
