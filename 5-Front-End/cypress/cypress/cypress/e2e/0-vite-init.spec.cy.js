// cypress/integration/myFirstTest.cy.jsx
describe('My First Cypress Test', () => {
  it('Visits the app and asserts title', () => {
    cy.visit('/'); // Replace with your app's URL
    cy.get('h1').should('contain', 'Vite + React'); // Adjust the selector and text as needed
  });
});


describe('Count button initializes at 0', () => {
  it('Visits the button === "0"', () => {
    cy.visit('/');
    cy.get('#numButton').should('contain', 'count is 0'); // Adjust the selector and text as needed
  });
});

describe('Correct Background Color', () => {
  it('Visits site and determines background matches', () => {
    cy.visit('/');
    cy.get(":root").should('have.css', 'color',  'rgba(255, 255, 255, 0.87)'); 
  });
});
