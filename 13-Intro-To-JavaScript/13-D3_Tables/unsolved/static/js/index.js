// ================ PART 1 ================ //
// Create a variable called presTBody and select the element based on its ID in html.
var presTBody = d3.select("#president_tbody");

// Console log the imported data from data.js
console.log(presData);

// Append each president to the table.
// HINT: 1 table row per president, with multiple table data elements in each row.
presData.forEach(row => {
  presTBody.append("tr");
  presTBody.append("td").text(row.number);
  presTBody.append("td").text(row.president);
  presTBody.append("td").text(row.birth_year);
  presTBody.append("td").text(row.death_year);
  presTBody.append("td").text(row.took_office);
  presTBody.append("td").text(row.left_office);
  presTBody.append("td").text(row.party);
});


// ================ Challenge ================ //
// Create a variable called 'addBtn' and select the element with an id of 'add_btn'.
var addBtn = d3.select("#add_btn");

// Create an on click listener for the "add_btn" ID on your html.
addBtn.on("click", function(){

  // Prevent the page from refreshing
  d3.event.preventDefault();
  
  // Store the values of each id into separate variables.
  var number = d3.select("#add_number").property("value");
  var president = d3.select("#add_president").property("value");
  var birthYear = d3.select("#add_birthYear").property("value");
  var deathYear = d3.select("#add_deathYear").property("value");
  var tookOffice = d3.select("#add_tookOffice").property("value");
  var leftOffice = d3.select("#add_leftOffice").property("value");
  var party = d3.select("#add_party").property("value");

  // Create an object called "input_data" as an object containing the keys of "number", "president", "birth_year", "death_year", "took_office", "left_office", "party"
  // Set their values corresponding to the variables you set earlier.
  var input_data = {number: number,
                    president: president,
                    birth_year: birthYear,
                    death_year: deathYear,
                    took_office: tookOffice,
                    left_office: leftOffice,
                    party: party};
    
  // Create a table row and append each cell's value from input_data as table data.
  presTBody.append("tr")
  presTBody.append("tr");
  presTBody.append("td").text(input_data.number);
  presTBody.append("td").text(input_data.president);
  presTBody.append("td").text(input_data.birth_year);
  presTBody.append("td").text(input_data.death_year);
  presTBody.append("td").text(input_data.took_office);
  presTBody.append("td").text(input_data.left_office);
  presTBody.append("td").text(input_data.party);

});

// FINALLY If you haven't done so, add bootstrap CDN to your index.html and make it pretty.