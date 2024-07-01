import { When } from '@badeball/cypress-cucumber-preprocessor'

When('The admin logs in', () => {
  cy.adminLogin()
})
