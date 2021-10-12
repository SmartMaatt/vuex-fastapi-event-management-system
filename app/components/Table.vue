<template>
  <v-data-table :headers="headers" :items="users">
    <template v-slot:[`item.edit`]="{item}">
      <v-btn color="primary" @click="editItem(item)">Edit</v-btn>
    </template>
    <template v-slot:[`item.delete`]="{item}">
      <v-btn color="primary" @click="deleteItem(item.id)"> Delete </v-btn>
    </template>
  </v-data-table>
</template>

<script>
  export default {
    data () {
      return {
        headers: [
          { text: 'Name', value: 'name' },
          { text: 'Email', value: 'email' },
          { text: 'Password', value: 'password' },
          { text: 'Edit', value: 'edit' },
          { text: 'Delete', value: 'delete' },
        ]
      }
    },
    computed: {
      users() {
        console.log(this.$store.state.users.data)
        return this.$store.state.users.data
      }
    },
    async fetch() {
      this.$store.commit('users/storeData', (await this.$axios.get('http://localhost:8000')).data)
    },
    methods: {
      editItem(user) {
        this.$store.commit("user/storeId", user.id)
        this.$store.commit("user/storeName", user.name)
        this.$store.commit("user/storeEmail", user.email)
        this.$store.commit("user/storePassword", user.password)
        console.log(user)
      },
      async deleteItem(id) {
        await this.$axios.delete('http://localhost:8000/' + id)
        .catch(({ response }) => {
            alert("Error: " + response.data.detail)
            console.error(response)
        })
        this.$store.commit('users/storeData', (await this.$axios.get('http://localhost:8000')).data)
      }
    }
  }
</script>
