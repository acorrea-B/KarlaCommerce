const path = require('path')

module.exports = {
  publicPath: '/',
  css: {
    loaderOptions: {
      sass: {
        sassOptions: {
          includePaths: ['./node_modules', './src/assets', './src/images'],
        },
      },
    },
  },
  devServer: { https: false } 
}