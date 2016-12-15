$(document).on('ready', function(){
	$('.eliminar').on('click', function(){
		id_anexo = $(this).attr('id');
		console.log(id_anexo);
		
		$('#id_anexo').val(id_anexo);
		$('#modal_eliminar').modal('show')
		
	});
});