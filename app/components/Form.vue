<template>
  <v-form>
    <v-text-field v-if="id" v-model="id"></v-text-field>
    <v-text-field v-model="name" label="Name"></v-text-field>
    <v-text-field v-model="email" label="Email"></v-text-field>
    <v-text-field v-model="password" label="Password"></v-text-field>
    <v-btn color="success" @click="submitUser({id, name, email, password})">
      {{id ? 'Edit' : 'Submit'}}
    </v-btn>
  </v-form>
</template>

<script>
  export default {
    computed: {
      id: {
        get(){
          return this.$store.state.user.id
        },
        set(value){
          this.$store.commit("user/storeId", value)
        }
      },
      name: {
        get(){
          return this.$store.state.user.name
        },
        set(value){
          this.$store.commit("user/storeName", value)
        }
      },
      email: {
        get(){
          return this.$store.state.user.email
        },
        set(value){
          this.$store.commit("user/storeEmail", value)
        }
      },
      password: {
        get(){
          return this.$store.state.user.password
        },
        set(value){
          this.$store.commit("user/storePassword", value)
        }
      }
    },
    methods: {
      async submitUser(user) {
        if(user.id) {
          await this.$axios.put("http//localhost:8000/" + user.id, user)
        }
        else {
          console.log(user)
          // await this.$axios.post("http//localhost:8000/", user)
        }
        await this.resetForm({id: 0, name: "", email: "", password: ""})
        await this.$store.commit("users/storeData", (await this.$axios.get("http//localhost:8000/")).data)
      },
      resetForm(user) {
        this.$store.commit("user/storeId", user.id)
        this.$store.commit("user/storeName", user.name)
        this.$store.commit("user/storeEmail", user.email)
        this.$store.commit("user/storePassword", user.password)
      }
    }
  };
</script>
