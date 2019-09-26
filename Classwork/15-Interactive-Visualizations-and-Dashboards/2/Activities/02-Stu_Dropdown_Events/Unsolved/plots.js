function init() {
  var data = [{
    values: [19, 26, 55, 88],
    labels: ["Spotify", "Soundcloud", "Pandora", "Itunes"],
    type: "pie"
  }];

  var layout = {
    height: 600,
    width: 800
  };

  Plotly.plot("pie", data, layout);
}

function updatePlotly(newdata) {
  var PIE = document.getElementById("pie");
  Plotly.restyle(PIE, "values", [newdata]);
}

function getData(dataset) {
  var data = [];
  switch (dataset) {
  case "dataset1":
    data = [9, 10, 19, 88];
    break;
  case "dataset2":
    data = [5, 21, 19, 90];
    break;
  case "dataset3":
    data = [1, 14, 19, 94];
    break;
  default:
    data = [0, 0, 0, 0];
  }
  updatePlotly(data);
}

init();
