$( init );
function init() {
  $('#makeMeDraggable').draggable();
  $('#makeMeDroppable').droppable( {
    drop: handleDropEvent
  } );
}
function handleDropEvent( event, ui ) {
  var draggable = ui.draggable;
  alert( 'The square with ID "' + draggable.attr('id') + '" was dropped onto me!' );
}
