<template>
  <div
    id="profile-content"
    v-bind:style="{ height: windowHeight + 'px' }">
    <div style="width: 100%; text-align: center;">
      <h1>Hi {{ username }}</h1>
    </div>
    <div style="width: 100%; text-align: center;">
      <p> This is your profile dashboard. </p>
    </div>
  </div>
</template>

<script>
  import DynamicHeightMixin from "../mixins/DynamicHeightMixin"
  
  import { getDjangoData } from "../utilities"
  
  export default {
    name: "ProfileDashboardView",
    mixins: [DynamicHeightMixin, ],
    data () {
      return {};
    },
    computed: {
      username() {
        return getDjangoData().username;
      }
    }
  }
</script>

<style scoped>
</style>