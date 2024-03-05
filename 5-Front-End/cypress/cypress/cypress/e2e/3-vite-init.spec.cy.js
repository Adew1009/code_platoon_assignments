describe("See if the nav bar works", () => {
  it("Navbar drop down contains items", () => {
    cy.visit('/');
    cy.get("#default-checkbox").click(); // Adjust the selector and text as needed
    cy.get("#default-checkbox").should('be.checked');
    cy.get("#default-checkbox").click(); // Adjust the selector and text as needed
    cy.get("#default-checkbox").should('not.be.checked');
});
});

describe("See if the nav bar works", () => {
  it("Navbar drop down contains items", () => {
    cy.visit('/');
    cy.get("#default-radio").click(); // Adjust the selector and text as needed
    cy.get("#default-radio").should('be.checked');
});
});

