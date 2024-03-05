describe("See if the nav bar works", () => {
  it("Navbar drop down contains items", () => {
    cy.visit('/');
    cy.get("#basic-nav-dropdown").click(); // Adjust the selector and text as needed

    const menuList = ["Action", "Something", "Another action","Separated link"]
    menuList.forEach(word => { cy.get('a').contains(word).should('be.visible')});

    cy.get("#basic-nav-dropdown").click();

    menuList.forEach(word => { cy.get('a').contains(word).should('be.hidden')});

});
});