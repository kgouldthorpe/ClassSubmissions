// @TODO: Complete the following sections

// Sort the data array using the greekSearchResults value
data.sort((a,b) => b.greekSearchResults-a.greekSearchResults);

// Slice the first 10 objects for plotting
data = data.slice(0,11);

// Trace1 for the Greek Data
var trace1 = {
    x: data.map(row => row.greekSearchResults),
    y: data.map(row => row.greekName),
    text: data.map(row => row.greekName),
    type: "bar"
};

// set up the data variable
var data = [trace1];

// set up the layout variable
var layout = {
  title: "Top 10 Greek Gods"
};

// Render the plot to the div tag with id "plot"
Plotly.newPlot("plot", data, layout);