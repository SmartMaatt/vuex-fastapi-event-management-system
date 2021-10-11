export default {
  buildModules: [
    "@nuxtjs/vuetify"
  ],
  modules: [
      "@nuxtjs/axios"
  ],
  components: true,
  publicRuntimeConfig: {
    middlewareUrl: 'http://localhost:8000'
  }
}
