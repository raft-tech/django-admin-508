import { Then, When } from '@badeball/cypress-cucumber-preprocessor'

// Shared
When('The admin navigates to the users page', () => {
    cy.get('a[href="/admin/auth/user/"]').first().click().then(() => {
        cy.get('table[id="result_list"]').find("tr").should('have.length', 2)
    })
})

// Scenario: An Admin User can Filter Users
When('The admin filters for user ...', () => {
    cy.get('select[title="superuser status"]').select('Yes')
    cy.get('input[type="submit"]').last().click().then(() => {
        cy.get('table[id="result_list"]').find("tr").should('have.length', 2)
    })
})

Then('Only the filtered user is displayed', () => {
    cy.url().should('eq', `${Cypress.env('adminUrl')}/auth/user/?is_superuser__exact=1`)
    cy.get('table[id="result_list"]').find("tr").should('have.length', 2)
})

// Scenario: An Admin User can Create a New Filter and Use it
When('The admin creates a filter', () => {

})

Then('The admin uses the new filter', () => {

})

When('Only the filtered data is displayed', () => {

})
