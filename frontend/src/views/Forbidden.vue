<template>
  <div
    id="forbidden-content"
    v-bind:style="{ height: windowHeight + 'px' }">
    <div style="width: 100%; text-align: center;">
      <h1>Restricted access!</h1>
    </div>
    <div style="width: 100%; text-align: center;">
      <p>
        Please <a href="/login/?next=profile/">login</a> to contine.
      </p>
    </div>
  </div>
</template>

<script>
  import DynamicHeightMixin from "../mixins/DynamicHeightMixin"
  
  export default {
    name: "Forbidden",
    mixins: [DynamicHeightMixin, ],
    data () {
      return {};
    }
  }
</script>

<style scoped>
</style>