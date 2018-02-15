function initMap()
{
	var canvas = document.getElementById("map");
	var options = {
		center: new google.maps.LatLng(42, -72),
		zoom: 15
	};
	var map = new google.maps.Map(canvas, options);
	var marker = new google.maps.Marker({
		position: new google.maps.LatLng(42,-72),
		map: map
	});
}

