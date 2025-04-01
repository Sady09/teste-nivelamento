<template>
  <div id="app">
    <header>
      <h1>Busca de Operadoras</h1>
    </header>
    <main>
      <OperadoraSearch />
    </main>
  </div>
</template>

<script>
import OperadoraSearch from "./components/OperadoraSearch.vue"

export default {
  name: "App",
  components: {
    OperadoraSearch,
  },
}
</script>

<style>
#app {
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
header {
  background: #42b983;
  padding: 20px;
  color: white;
}
main {
  padding: 20px;
}
</style>
