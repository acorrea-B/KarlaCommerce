<template>
  <section id="cta">
    <h2>Datos del comprador</h2>
    <p>
      Un último paso para rgistrar tu compra, para eso necsitamos unos datos
      basicos tuyos para poder identificarte.
    </p>

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
          <input type="submit" value="Listo" class="fit" />
        </div>
      </div>
    </form>
  </section>
</template>

<script>
export default {
  data() {
    return {
      purchase: this.$store.getters.purchase,
      costumer: {},
    };
  },
  methods: {
    newPurchase() {
      if (
        this.costumer.firstName &&
        this.costumer.lastName &&
        this.costumer.identification &&
        this.costumer.email
      ) {
        this.purchase.costumer = this.costumer;
        this.$store.commit("setpurchase", this.purchase);
        console.log(JSON.stringify(this.purchase));
      } else {
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
