// Define SVG area dimensions
var svgWidth = 960;
var svgHeight = 660;

// Define the chart's margins as an object
var chartMargin = {
  top: 30,
  right: 30,
  bottom: 30,
  left: 30
};

// Define dimensions of the chart area
var chartWidth = svgWidth - chartMargin.left - chartMargin.right;
var chartHeight = svgHeight - chartMargin.top - chartMargin.bottom;

// Select body, append SVG area to it, and set the dimensions
var svg = d3.select("body")
  .append("svg")
  .attr("height", svgHeight)
  .attr("width", svgWidth);

// Append a group to the SVG area and shift ('translate') it to the right and to the bottom
var chartGroup = svg.append("g")
  .attr("transform", `translate(${chartMargin.left}, ${chartMargin.top})`)

// Load data from height_of_rollercoasters.csv
d3.csv("heights_of_rollercoasters.csv", function(error, coasterData) {
  if (error) throw error;
  
  // Cast the rollercoaster heights as numbers
  coasterData.forEach(function(d){
    d.height = +d.height;
  });

  // Sort the rollercoasters alphabetically
  coasterData.sort(function(a, b){
    if(a.rollercoaster < b.rollercoaster) { return -1; }
    if(a.rollercoaster > b.rollercoaster) { return 1; } 
    return 0;
  });

  console.log(coasterData);

  // Build a bar chart using the information in heights_of_rollercoasters.csv
  var xScale = d3.scaleBand()
    .domain(coasterData.map(d => d.rollercoaster))
    .range([0, chartWidth])
    .padding(.1);
  var xAxis = d3.axisBottom(xScale);
  chartGroup.append("g")
    .attr("transform", `translate(0, ${chartHeight})`)
    .call(xAxis);

  var yScale = d3.scaleLinear()
    .domain([0, d3.max(coasterData.map(d => d.height))])
    .range([chartHeight, 0]);
  var yAxis = d3.axisLeft(yScale);
  chartGroup.append("g")
    .call(yAxis);

  chartGroup.selectAll(".bar")
    .data(coasterData)
    .enter()
    .append("rect")
    .attr("class", "bar")
    .attr("x", d => xScale(d.rollercoaster))
    .attr("y", d => yScale(d.height))
    .attr("width", xScale.bandwidth())
    .attr("height", d => chartHeight - yScale(d.height));
});

