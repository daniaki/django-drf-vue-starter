<template>
  <!-- This component adjusts body size to fill the viewport -->
</template>

<script>
  export default {
    name: "DynamicHeightMixin",
    data: function() {
      return {
        windowHeight: 0,
      }
    },
    mounted() {
      this.$nextTick(function() {
        window.addEventListener('resize', this.getWindowHeight);
        this.getWindowHeight();
      });
    },
    beforeDestroy() {
      window.removeEventListener('resize', this.getWindowHeight);
    },
    methods: {
      getWindowHeight(event) {
        this.windowHeight = document.documentElement.clientHeight;
      }
    },
  }
</script>

<style scoped>
</style>