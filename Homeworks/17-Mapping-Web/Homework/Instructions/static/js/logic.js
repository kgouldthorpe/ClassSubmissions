function createMap(earthquakes) {
    // Create the tile layer that will be the background of our map
    var lightmap = L.tileLayer("https://api.mapbox.com/styles/v1/mapbox/light-v9/tiles/256/{z}/{x}/{y}?access_token={accessToken}", {
        attribution: "Map data &copy; <a href=\"http://openstreetmap.org\">OpenStreetMap</a> contributors, <a href=\"http://creativecommons.org/licenses/by-sa/2.0/\">CC-BY-SA</a>, Imagery © <a href=\"http://mapbox.com\">Mapbox</a>",
        maxZoom: 18,
        id: "mapbox.light",
        accessToken: API_KEY
    });    
    // Create a baseMaps object to hold the lightmap layer
    var baseMaps = {
        "Light Map": lightmap
    };

    // Create an overlayMaps object to hold the bikeStations layer
    var overlayMaps = {
        "Earthquake Locations": earthquakes
    };

    // Create the map object with options
    var map = L.map("map", {
        center: [39.82, -98.57],
        zoom: 4,
        layers: [lightmap, earthquakes]
    });

    // Create a layer control, pass in the baseMaps and overlayMaps. Add the layer control to the map
    L.control.layers(baseMaps, overlayMaps, {
        collapsed: false
    }).addTo(map);
}

function createMarkers(response_usgs) {
     
    // Initialize an array to hold bike markers
    var quakeMarkers = [];

    // Loop through data for each of variable
    for (var index = 0; index < response_usgs.length; index++) {
        var epicenters = response_usgs.properties[index];

        // For each epicenter, create a marker and bind a popup with information on the quake
        var quakeMarker = L.marker(epicenters.coordinates)
        .bindPopup("<h3>" + epicenters.title + "<h3><h3>Magnitude: " + epicenters.mag + "<h3>");
    
        // Add the marker to the quakeMarkers array
        quakeMarkers.push(quakeMarker);
    }
    
    // Create a layer group made from the quake markers array, pass it into the createMap function
    createMap(L.layerGroup(quakeMarkers));
}

// Perform an API call. Call createMarkers when complete
d3.json("https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/all_month.geojson", createMarkers);

