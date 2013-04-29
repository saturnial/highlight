$( init );
function init() {
  $('.draggable').draggable();
  $('.droppable').droppable( {
    drop: handleDropEvent
  } );
}

function handleDropEvent( event, ui ) {
  var highlights = $('#receiveHighlight');
  var draggable = ui.draggable;
  var id = draggable.attr('id');
  var block = $('#' + id)
  var text = block.html()
  highlights.append('<br/>' + text);
  block.hide();

}

$(document).ready(function() {

  $("#possible_venues").autocomplete({
    source: function(request, response) {
      $.ajax({
        type: 'GET',
        dataType: 'json',
        url: '/lite/ajax/get_possible_venues',
        data: {query: request.term},
        success: response
      });
    },
    minLength: 3,
    delay: 0
  });

});
