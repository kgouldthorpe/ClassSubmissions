// Create a map object
var myMap = L.map("map", {
  center: [37.09, -95.71],
  zoom: 5
});

// Add a tile layer
L.tileLayer("https://api.tiles.mapbox.com/v4/{id}/{z}/{x}/{y}.png?access_token={accessToken}", {
  attribution: "Map data &copy; <a href=\"https://www.openstreetmap.org/\">OpenStreetMap</a> contributors, <a href=\"https://creativecommons.org/licenses/by-sa/2.0/\">CC-BY-SA</a>, Imagery © <a href=\"https://www.mapbox.com/\">Mapbox</a>",
  maxZoom: 18,
  id: "mapbox.streets",
  accessToken: API_KEY
}).addTo(myMap);

// City markers

// Add code to create a marker for each city below and add it to the map
// newyork;
var NYmarker = L.marker([40.6247, -74.1637], {
  draggable: true,
  title: "New York City"
}).addTo(myMap);
// chicago;
var CHmarker = L.marker([41.7363, -87.5372], {
  draggable: true,
  title: "Chicago"
}).addTo(myMap);
// houston;
var HOmarker = L.marker([29.0696, -96.1678], {
  draggable: true,
  title: "Houston"
}).addTo(myMap);
// la;
var LAmarker = L.marker([33.7916, -118.2297], {
  draggable: true,
  title: "Los Angeles"
}).addTo(myMap);
// omaha;
var OMmarker = L.marker([41.0575, -97.8052], {
  draggable: true,
  title: "Omaha"
}).addTo(myMap);
