$(document).on('ready', function(){
	$('.eliminar').on('click', function(){
		id_anexo = $(this).attr('id');
		console.log(id_anexo);
		var csrftoken = $("[name=csrfmiddlewaretoken]").val();
		$('#id_anexo').val(id_anexo);
		$('#modal_eliminar').modal('show');
		$('#boton_eliminar').on('click', function(){
			$.ajax({
			url: '/api/anexosarchivo/'+id_anexo,
			headers: { "X-CSRFToken": csrftoken },
			method: "DELETE",
			success: function (){
				console.log("exito");
				$('#modal_eliminar').modal('hide');
				location.reload();
			},
			error: function(){
				console.log("Error");
				$('#modal_eliminar').modal('hide')
			}
           
                    
        	});
		});
		
	});
});
	