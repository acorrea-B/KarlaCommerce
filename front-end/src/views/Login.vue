<template>
  <div>
    <loading :show="show" :label="label"> </loading>
    <section id="banner">
      <loading :show="show" :label="label"> </loading>
      <h2>Karla Accesorios</h2>
      <p>
        Ingreso para operadores
      </p>
    </section>
    <section id="main" class="container">
      <form @submit.prevent="autOperator">
        <div class="row gtr-50 gtr-uniform">
          <div class="col-8 col-12-mobilep">
            <input
              type="text"
              name="identification"
              id="identification"
              placeholder="Número de cédula"
              v-model="operator.identification"
            />
          </div>
          <div class="col-8 col-12-mobilep">
            <input
              type="password"
              name="password"
              id="password"
              placeholder="Contraseña"
              v-model="operator.password"
            />
          </div>
          <div class="col-4 col-12-mobilep">
            <input type="submit" value="Ingresar" class="fit" />
          </div>
        </div>
      </form>
    </section>
  </div>
</template>

<script>
import { Auth } from "@/services/graphQl/mutations";
import loading from "vue-full-loading";
import router from "@/router/index";
export default {
  data() {
    return {
      purchase: this.$store.getters.purchase,
      operator: {},
      show: false,
      label: "Estamos procesando tu compra",
      linkPayment: "",
    };
  },
  components: {
    loading,
  },
  methods: {
    async autOperator() {
      /*eslint-disable */
      this.show = true;
      let response = await this.$apollo
        .mutate({
          mutation: Auth,
          variables: {
            identification: this.operator.identification,
            password: this.operator.password,
          },
        })
        .then((result) => {
          this.$store.commit("setToken", result.data.tokenAuth.token);
          this.$store.commit("setAuth", true);
          router.push({ name: "PurchasesOperator" });
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

>
<style scoped>
.loginOperator {
  position: inherit;
  top: 100%;
  width: 100%;
  text-align: center;
}
</style>
