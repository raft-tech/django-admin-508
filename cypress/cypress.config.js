const { defineConfig } = require('cypress')
const webpack = require('@cypress/webpack-preprocessor')
const preprocessor = require('@badeball/cypress-cucumber-preprocessor')

module.exports = defineConfig({
  e2e: {
    baseUrl: 'http://localhost:8000',
    specPattern: '**/*.feature',
    supportFile: 'test/support/e2e.js',

    env: {
      adminUrl: 'http://localhost:8000/admin',
      adminUsername: 'admin',
      adminEmail: 'admin@fakeemail.com',
      adminPassword: 'fakepassword'
    },

    async setupNodeEvents(on, config) {
      // implement node event listeners here
      await preprocessor.addCucumberPreprocessorPlugin(on, config)

      const webpackOptions = {
        resolve: {
          extensions: ['.ts', '.js'],
        },
        module: {
          rules: [
            {
              test: /\.feature$/,
              use: [
                {
                  loader: '@badeball/cypress-cucumber-preprocessor/webpack',
                  options: config,
                },
              ],
            },
          ],
        },
      }

      on('file:preprocessor', webpack({ webpackOptions }))

      return config
    },
  },
})
