<template>
  <v-app>
    <v-main>
      <v-container justify="center" align="center">
        <v-app-bar color="blue" dense></v-app-bar>
        <client-only>
          <Nuxt />
        </client-only>
      </v-container>
    </v-main>
  </v-app>
</template>

<script>
export default {}
</script>

<style>

</style>
