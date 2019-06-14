var mymap = L.map('mapid', {
    crs: L.CRS.Simple,
    maxZoom: 5,
    minZoom: 1,
}).setView([-60, 100], 3);

mymap.setMaxBounds([[-0.875, 0.375], [-249.5, 249.25]]);

// var map_test = eval($("#map-canvas").attr('data-place'));
var map_test = document.getElementById("map-canvas");
// var tile = L.tileLayer('/media/Image/Maps/'+map_test+'/{z}/{x}/{y}.png', {
var tile = L.tileLayer('/media/Image/Maps/tiles/{z}/{x}/{y}.png', {
    attribution: 'Карта Сталинграда',
    // continuousWorld: true,
    // noWrap: true,
    // maxBoundsViscosity: 1.0,
}).addTo(mymap);

var popup = L.popup();

function onMapClick(e) {
    popup
        .setLatLng(e.latlng)
        .setContent("Клинул мышкой по координатам " + e.latlng.toString())
        .openOn(mymap);
}

mymap.on('click', onMapClick);