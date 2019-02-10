<template>
  <div
    id="not-found-content"
    v-bind:style="{ height: windowHeight + 'px' }">
    <div style="width: 100%; text-align: center;">
      <h1>Page not found!</h1>
    </div>
    <div style="width: 100%; text-align: center;">
      <p>The page you are looking does not exist.</p>
    </div>
  </div>
</template>

<script>
  import DynamicHeightMixin from "../mixins/DynamicHeightMixin"
  
  export default {
    name: "PageNotFound",
    mixins: [DynamicHeightMixin, ],
    data () {
      return {};
    }
  }
</script>

<style scoped>
</style>