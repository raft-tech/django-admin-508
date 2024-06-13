import { Then, When } from '@badeball/cypress-cucumber-preprocessor'

// Scenario: An Admin User can Filter Users
When('The admin navigates to the users page', () => {
    cy.get('a[href="/admin/auth/user/"]').first().click()
    cy.get('table[id="result_list"]').find("tr").should('have.length', 2)
})

When('The admin filters for user ...', () => {
    cy.get('select[title="superuser status"]').select('Yes')
    cy.get('input[type="submit"]').last().click()
    cy.get('table[id="result_list"]').find("tr").should('have.length', 2)
})

Then('Only the filtered user is displayed', () => {
    cy.url().should('eq', `${Cypress.env('adminUrl')}/auth/user/?is_superuser__exact=1`)
    cy.get('table[id="result_list"]').find("tr").should('have.length', 2)
})

// Scenario: An Admin User can use the MultiSelectFilter
When('The admin navigates to the dummies page', () => {
    cy.get('a[href="/admin/tests/dummymodel/"]').first().click()
    cy.get('table[id="result_list"]').find("tr").should('have.length', 5)
})

Then('The admin uses the multiselect filter', () => {
    cy.get('a[href="?name=Bill"]').first().click()
    cy.get('table[id="result_list"]').find("tr").should('have.length', 2)
    cy.get('a[href="?name=Bill%2CDiane"]').first().click()
})

When('Only the filtered data is displayed', () => {
    cy.get('table[id="result_list"]').find("tr").should('have.length', 3)
    cy.url().should('eq', `${Cypress.env('adminUrl')}/tests/dummymodel/?name=Bill%2CDiane`)
})

// Scenario: An Admin User can clear Filters
Then('The admin clears the filters', () => {
    cy.get('a[href="?"]').first().click()
    cy.get('table[id="result_list"]').find("tr").should('have.length', 5)
    cy.url().should('eq', `${Cypress.env('adminUrl')}/tests/dummymodel/?`)
})
