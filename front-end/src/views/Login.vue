<template>
  <section id="banner">
    <h2>Alpha</h2>
    <p>Another fine responsive site template freebie by HTML5 UP.</p>
    <ul class="actions special">
      <li><a href="#" class="button primary">Sign Up</a></li>
      <li><a href="#" class="button">Learn More</a></li>
    </ul>
  </section>
</template>

<script>
export default {
  name: "HelloWorld",
  props: {
    msg: String,
  },
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
h3 {
  margin: 40px 0 0;
}
ul {
  list-style-type: none;
  padding: 0;
}
li {
  display: inline-block;
  margin: 0 10px;
}
a {
  color: #42b983;
}
</style>
