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


