var texto = null;
/*-----------------------------------------------*\
            LOAD
\*-----------------------------------------------*/

$(document).ready(function(){
	
	texto = new Texto()
	texto.eliminar()
	texto.init()


})

function Texto(){

	this.$textarea = $('#id_texto')
	//this.$panel = $('#id_panel')

}

Texto.prototype.init = function (){

	this.$textarea.wysihtml5();
	//this.$panel.addClass('collapsed-box')


}
Texto.prototype.eliminar = function(){
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