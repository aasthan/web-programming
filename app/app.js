function displayMap()
{
	var canvas = document.getElementById("map");
	var options = {
		center: new google.maps.LatLng(51.5, -0.2),
		zoom: 10
	};
	var map = new google.maps.Map(canvas, options);
}

//Todo: get google api