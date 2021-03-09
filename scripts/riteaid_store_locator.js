//https://www.riteaid.com/locations/search.html
$('.location-title').toArray().map(e=>{
    var tokens = $(e).text().split(' ');
    index = tokens.indexOf('Aid');
    var address = $(e).siblings('.location-info-wrapper').children('.location-info-address').text()
    var id = tokens[index+1].replace('#','');
     return {[id]:address};
});