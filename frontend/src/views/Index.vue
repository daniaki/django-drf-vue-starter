<template>
  <div id="index-content">
    <p>It works!</p>
    <div id="logos">
      <img id='django-logo' alt='Django logo' src="../assets/django.png">
      <img id='vue-logo' alt='Vue logo' src="../assets/vue.png">
    </div>
  </div>
</template>

<script>
  export default {
    name: "Index",
    components: {},
    data() {
      return {}
    }
  }

</script>

<style scoped>
  #django-logo {
    height: 127px;
    width: 351px;
    float: right;
  }
  #vue-logo {
    height: 127px;
    width: 351px;
    float: left;
  }
</style>