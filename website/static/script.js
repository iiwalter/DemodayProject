var map
var markers = []
function initMap() {
    var sp = { lat: -23.5489, lng: -46.6388 };
    var map = new google.maps.Map(
        document.getElementById('map'), { zoom: 11, center: sp });
        var marker = new google.maps.Marker({position: sp, map: map});
        // Add a marker clusterer to manage the markers.
        
    }
    initMap();
// function marcadores() {
//     $.each(points, function (key, point) {
//         var position = new google.maps.LatLng(point.lat, point.lng);
//         var marker = new google.maps.Marker(
//             {
//                 position: position,
//                 map: map
//             })

//             markers.push(marker)

//         });
// }

function myFunction() {
    var x = document.getElementById("myTopnav");
    if (x.className === "topnav") {
      x.className += " responsive";
    } else {
      x.className = "topnav";
    }
  }




