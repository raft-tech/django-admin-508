/* eslint-disable no-undef */

// ***********************************************
// This example commands.js shows you how to
// create various custom commands and overwrite
// existing commands.
//
// For more comprehensive examples of custom
// commands please read more here:
// https://on.cypress.io/custom-commands
// ***********************************************
//
//
// -- This is a parent command --
// Cypress.Commands.add('login', (email, password) => { ... })
//
//
// -- This is a child command --
// Cypress.Commands.add('drag', { prevSubject: 'element'}, (subject, options) => { ... })
//
//
// -- This is a dual command --
// Cypress.Commands.add('dismiss', { prevSubject: 'optional'}, (subject, options) => { ... })
//
//
// -- This will overwrite an existing command --
// Cypress.Commands.overwrite('visit', (originalFn, url, options) => { ... })


Cypress.Commands.add('adminApiLogin', () => {
  cy.request({
    url: `${Cypress.env('adminUrl')}/login`,
    method: 'GET' // cookies are in the HTTP headers, so HEAD suffices
  }).then(() => {
    cy.getCookie('sessionid').should('not.exist')
    cy.getCookie('csrftoken').its('value').then((token) => {
      cy.request({
        method: 'POST',
        url: `${Cypress.env('adminUrl')}/login`,
        form: true,
        body: {
          username: Cypress.env('adminUsername'),
          token: Cypress.env('adminPassword'),
          csrfmiddlewaretoken: token
        },
      }).then((response) => {
        cy.getCookie('sessionid').its('value').as('adminSessionId')
        cy.getCookie('csrftoken').its('value').as('adminCsrfToken')
      })
    })
  })
})

Cypress.Commands.add('adminLogin', () => {
  cy.visit(`${Cypress.env('adminUrl')}/login`).then(() => {
    cy.get('input[name="username"]').type(Cypress.env('adminUsername'))
    cy.get('input[name="password"]').type(Cypress.env('adminPassword'))
    cy.get('input[type="submit"]').click()
  })
})
