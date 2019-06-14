var map = L.map('map', {
    crs: L.CRS.Simple,
    maxZoom: 3,
    minZoom: 1,
}).setView([-60, 100], 3);

map.setMaxBounds([[-0.875, 0.375], [-249.5, 249.25]]);

var map_test = document.getElementById("map-canvas");

var tile = L.tileLayer('/media/Image/Maps/tiles/{z}/{x}/{y}.png', {
    attribution: 'Карта Сталинграда',
}).addTo(map);


var featureGroup = L.featureGroup().addTo(map);

var drawControl = new L.Control.Draw({
    edit: {
        featureGroup: featureGroup
    }
}).addTo(map);

map.on('draw:created', function (e) {
    var type = e.layerType,
        layer = e.layer,
        shape = layer.toGeoJSON(),
        shape_for_db = JSON.stringify(shape);
    // Each time a feaute is created, it's added to the over arching feature group
    featureGroup.addLayer(layer);
    if (type === 'rectangle') {
        var bounds = layer.getBounds();
        layer.bindPopup(bounds.getNorthWest().toString() + "NW" + bounds.getSouthEast().toString() + "SE");
    }
});

map.on('draw:edited', function (e) {
    var layers = e.layers;

    layers.eachLayer(function (layer) {
        // do whatever you want to each layer, here update LatLng
        if (layer instanceof L.Rectangle) {
            var bounds = layer.getBounds();
            layer.bindPopup(bounds.getNorthWest().toString() + " NW<br>" + bounds.getSouthEast().toString() + " SE");
        }
    });
});


// on click, clear all layers
document.getElementById('delete').onclick = function (e) {
    featureGroup.clearLayers();
};

document.getElementById('export').onclick = function (e) {
    // Extract GeoJson from featureGroup
    var data = featureGroup.toGeoJSON();

    // Stringify the GeoJson
    var convertedData = 'text/json;charset=utf-8,' + encodeURIComponent(JSON.stringify(data));

    // Create export
    document.getElementById('export').setAttribute('href', 'data:' + convertedData);
    document.getElementById('export').setAttribute('download', 'data.geojson');
};

L.geoJSON(JSON.parse(shape_for_db)).addTo(mymap);