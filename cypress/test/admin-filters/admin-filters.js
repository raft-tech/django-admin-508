import { Then, When } from '@badeball/cypress-cucumber-preprocessor'

When('The admin navigates to the users page', () => {
    cy.get('a[href="/admin/auth/user/"]').first().click().then(() => {
        cy.get('table[id="result_list"]').find("tr").should('have.length', 2)
    })
})

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
