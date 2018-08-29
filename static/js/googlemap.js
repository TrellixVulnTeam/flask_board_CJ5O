 function initialize() {
    var Y_point = 37.579622; // Y 좌표
    var X_point = 126.890379; // X 좌표
    var zoomLevel = 17; // 첫 로딩시 보일 지도의 확대 레벨
    var markerTitle = "라이온 브리지"; // 현재 위치 마커에 마우스를 올렸을때 나타나는 이름
    var markerMaxWidth = 300; // 마커를 클릭했을때 나타나는 말풍선의 최대 크기

    // 말풍선 내용
    var contentString = '<div id="content">' +
                            '<div id="siteNotice">' +
                            '</div>' +
                            '<h3 id="firstHeading" class="firstHeading">라이온 브리지</h3>' +
                            '<div id="bodyContent">' +
                                '<p>서울특별시 마포구 상암동 1605<br />' +
                                'Tel. Tel 02-787-9500</p>' +
                            '</div>' +
                        '</div>';

    var myLatlng = new google.maps.LatLng(Y_point, X_point);
    var mapOptions = {
        zoom: zoomLevel,
        center: myLatlng,
        mapTypeId: google.maps.MapTypeId.ROADMAP
    }
    var map = new google.maps.Map(document.getElementById('map_view'), mapOptions);

    var marker = new google.maps.Marker({
        position: myLatlng,
        map: map,
        title: markerTitle
     });

    var infowindow = new google.maps.InfoWindow({
                                                content: contentString,
                                                maxWidth: markerMaxWidth
                                             });

    google.maps.event.addListener(marker, 'click', function() {
        infowindow.open(map, marker);
     });
 }

$(document).ready(function(){
    console.log($('#homdDiv').length);
    if($('#homdDiv').length > 0){
        initialize();
    };
})