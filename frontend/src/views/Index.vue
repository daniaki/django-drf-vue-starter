<template>
  <div id="index-content">
    <h1 style="text-align: center">It works!</h1>
    <div style="text-align: center" id="logos">
      <span>
        <img id='django-logo' alt='Django logo' src="../assets/django.png">
      </span>
      <span>
        <img id='vue-logo' alt='Vue logo' src="../assets/vue.png">
      </span>
    </div>
  </div>
</template>

<script>
  export default {
    name: "Index",
    components: {},
    data() {
      return {};
    }
  }

</script>

<style scoped>
  #django-logo {
    height: 250px;
    width: 350px;
  }
  #vue-logo {
    height: 250px;
    width: 350px;
  }
</style>