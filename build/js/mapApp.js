function initAutocomplete() {
      var canvas = document.getElementById("map");
      var geocoder = new google.maps.Geocoder();
      var address = document.getElementById('pac-input').value;
      var latitude;
      var longitude;
      var loc;

      geocoder.geocode({ 'address': address }, function (results, status) {
        if (status == google.maps.GeocoderStatus.OK) {
          console.log(results[0]);
          latitude = results[0].geometry.location.lat();
          longitude = results[0].geometry.location.lng();

          loc = results[0].geometry.location;
          map.setCenter(loc);
        }
      });

      var map = new google.maps.Map(document.getElementById('map'), {
        zoom: 17,
        mapTypeId: 'roadmap'
      });
    }