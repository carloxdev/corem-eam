var archivo = null;
/*-----------------------------------------------*\
            LOAD
\*-----------------------------------------------*/

$(document).ready(function(){
	
	archivo = new Archivo()
	archivo.eliminar()
	//archivo.init()


})

function Archivo(){

	//this.$panel = $('#id_panel')
	
}
Archivo.prototype.init = function () {

	//this.$panel.addClass('collapsed-box')
}
Archivo.prototype.eliminar = function(){
	$('.eliminar').on('click', function(){
		id_anexo = $(this).attr('id');
		console.log(id_anexo);
		var csrftoken = $("[name=csrfmiddlewaretoken]").val();
		$('#id_anexo').val(id_anexo);
		$('#modal_eliminar').modal('show');
		$('#boton_eliminar').on('click', function(){
			$.ajax({
			url: '/api/ordenesanexotexto/'+id_anexo,
			headers: { "X-CSRFToken": csrftoken },
			method: "DELETE",
			success: function (){
				console.log("exito");
				$('#modal_eliminar').modal('hide');
				location.reload();
			},
			error: function(e){
				alert(e);
				$('#modal_eliminar').modal('hide')
			}
           
                    
        	});
		});
		
	}); 
}