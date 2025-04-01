<template>
  <div class="operadora-search">
    <input
      v-model="query"
      @input="handleInput"
      placeholder="Buscar operadora..."
    />
    <button @click="searchOperadoras">Pesquisar</button>
    <ul v-if="operadoras.length">
      <li v-for="(operadora, index) in operadoras" :key="index">
        <p>Razão Social: {{ operadora.Razao_Social }}</p>
        <p>Nome Fantasia: {{ operadora.Nome_Fantasia }}</p>
        <p>Modalidade: {{ operadora.Modalidade }}</p>
      </li>
    </ul>
    <p v-else>Nenhum resultado encontrado.</p>
  </div>
</template>

<script>
import axios from "axios"

export default {
  data() {
    return {
      query: "",
      operadoras: [],
    }
  },
  methods: {
    handleInput() {
      if (this.query.length >= 2) {
        this.searchOperadoras()
      } else {
        this.operadoras = []
      }
    },
    async searchOperadoras() {
      try {
        const response = await axios.get(`http://localhost:8000/buscar/`, {
          params: { query: this.query },
        })
        this.operadoras = response.data
      } catch (error) {
        console.error("Erro ao buscar operadoras:", error)
      }
    },
  },
}
</script>

<style scoped>
.operadora-search {
  max-width: 600px;
  margin: 0 auto;
}
.operadora-search input {
  width: calc(100% - 100px);
  padding: 10px;
  margin-bottom: 20px;
  border: 1px solid #ccc;
  border-radius: 4px;
}
.operadora-search button {
  padding: 10px;
  margin-left: 10px;
  border: 1px solid #ccc;
  border-radius: 4px;
  background-color: #42b983;
  color: white;
  cursor: pointer;
}
.operadora-search ul {
  list-style-type: none;
  padding: 0;
}
.operadora-search li {
  padding: 10px;
  border: 1px solid #ccc;
  margin-bottom: 10px;
  border-radius: 4px;
}
</style>
