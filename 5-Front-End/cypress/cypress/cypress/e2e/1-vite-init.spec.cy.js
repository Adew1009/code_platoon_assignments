describe('Count button on Click', () => {
  it("Button click goes to 1", () => {
    cy.visit('/');
    cy.get('#numButton').click(); // Adjust the selector and text as needed
    cy.get('#numButton').should('contain', 'count is 1'); // Adjust the selector and text as needed
  });
});