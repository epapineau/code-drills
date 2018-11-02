var gabumon = {
    digivolutions: [
      {
        stage: 1,
        name: "Garurumon"
      },
      {
        stage: 2,
        name: "WereGarurumon"
      },
      {
          stage: 3,
          name: "MetalGarurumon"
      },
      {
          stage: 4,
          name: "ZeedGarurumon"
      }
    ],
    image: "https://vignette.wikia.nocookie.net/digimon/images/d/d1/Gabumon_b.jpg/revision/latest?cb=20171127121438"
  };


// Select the div with a class of tagline
var tagline = d3.select(".tagline");

// console.log the text within the tagline
console.log(tagline.text());

// replace the text with "D3gimon are the Champions!"
tagline.text("D3gimon are the Champions!");

// Capture the HTML link for "D3 D3 D3givolve"
// Select the child element for the link
// Capture the child element's href attribute
var digiLink = d3.select(".digi-link>a");
console.log(digiLink.attr("href"));

// Change the link to any digimon related video
digiLink.attr("href", "https://www.youtube.com/watch?v=c51j1tfiLIA");

// using the same selection, change the link's text to and href to the digimon wikipedia page
digiLink.attr("href", "https://en.wikipedia.org/wiki/Digimon");
digiLink.text("Digipedia");

// Create a new <li> element and and append it to the <ul>, give this new element text of "Victory Greymon"
var digiList = d3.select("ul");
digiList.append("li").text("Victory Greymon");

// Use chaining to create another new element and set its text as "Omnimon"
digiList.append("li").text("Omnimon");

// Select the div with an id of "agumon" and append a new <img> element
var agumon = d3.select("#agumon");
agumon.append("img")
  .attr("src", "https://vignette.wikia.nocookie.net/digimon/images/6/68/Agumon_b.jpg/revision/latest?cb=20170210150934");

// Challenge section!
var gabumonSel = d3.select("#gabumon")
gabumonSel.append("img")
  .attr("src", gabumon.image);

gabumonSel.append("ul");

console.log()
for(i = 0; i < gabumon.digivolutions.length; i++){
  gabumonSel.select("ul")
    .append("li")
    .text(gabumon.digivolutions[i].name);
}
d3.selectAll("li").style("color", "orange")