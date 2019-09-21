// trace1 high_jump
var trace1 = {
    x: data.year,
    y: data.high_jump,
    mode: "markers",
    name: "High Jump",
    marker: {
        color: "#e377c2",
        symbol: "diamond"
    }
};

//trace2 long_jump
var trace2 = {
    x: data.year,
    y: data.long_jump,
    mode: "markers",
    name: "Long Jump",
    marker: {
        color: "#1f77b4",
        symbol: "circle"
    }
};

// trace3 discus_throw
var trace3 = {
    x: data.year,
    y: data.discus_throw,
    mode: "markers",
    name: "Discus Throw",
    marker: {
        color: "#9467bd",
        symbol: "square"
    }
};

// set up the data variable
var data = [trace1, trace2, trace3];

// set up the layout variable
var layout = {
  title: "Olympics Analysis"
};

// Render the plot to the div tag with id "plot"
Plotly.newPlot("plot", data, layout);
