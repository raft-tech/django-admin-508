import { Then } from '@badeball/cypress-cucumber-preprocessor'

Then('The admin sees DAC home page', () => {
    cy.contains('Site administration').should('exist')
    cy.contains('Admin Interface').should('exist')
    cy.contains('Authentication and Authorization').should('exist')
})
