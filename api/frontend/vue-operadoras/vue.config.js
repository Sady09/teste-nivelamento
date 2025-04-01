const { defineConfig } = require('@vue/cli-service')
module.exports = defineConfig({
  transpileDependencies: true,
  devServer: {
    proxy: {
      '/buscar': {
        target: 'http://localhost:8000',
        changeOrigin: true,
      },
    },
  },
})