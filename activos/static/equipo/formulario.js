/*-----------------------------------------------*\
            GLOBAL VARIABLES
\*-----------------------------------------------*/
var formulario = null

/*-----------------------------------------------*\
            LOAD
\*-----------------------------------------------*/

$(document).ready(function () {

    formulario = new TargetaFormulario()
})


/*-----------------------------------------------*\
            OBJETO: Targeta Filtros
\*-----------------------------------------------*/

function TargetaFormulario() {

    this.$padre = $('#id_padre')
    this.modal_ubicacion = new VentanaUbicacion()

	this.init()
}
TargetaFormulario.prototype.init = function () {

    this.$padre.select2()

    

    // this.$boton_buscar.on("click", this, this.click_BotonBuscar)
    // this.$boton_limpiar.on("click", this, this.click_BotonLimpiar)
}



/*-----------------------------------------------*\
            OBJETO: Ventana Ubicacion
\*-----------------------------------------------*/

function VentanaUbicacion() {

	this.$id = $('#win_ubicacion')
	this.$boton_guardar = $('#bnt_ubi-save')

	this.$clave = $('#ubi_clave')
	this.$clave_contenedor = $('#ubi_clave_contenedor')
	this.$clave_mensaje =  $('#ubi_clave_mensaje')

	this.$descripcion =  $('#ubi_descripcion')
	this.$desc_contenedor =  $('#ubi_desc_contenedor')
	this.$desc_mensaje =  $('#ubi_desc_mensaje')

	this.init()
}
VentanaUbicacion.prototype.init = function () {

	this.$id.on('show.bs.modal', function (event) {

		var button = $(event.relatedTarget)

		var modal = $(this)

		formulario.modal_ubicacion.$boton_guardar.off("click")
		formulario.modal_ubicacion.clear_Estilos()

		if (button.context.id == "btn_new_ubicacion") {
			modal.find('.modal-title').text('Nueva Ubicacion')
			formulario.modal_ubicacion.$boton_guardar.on(
				"click", 
				formulario.modal_ubicacion, 
				formulario.modal_ubicacion.nuevo
			)
		}
		else if (button.context.id == "btn_edit_ubicacion") {
  			modal.find('.modal-title').text('Editar Ubicacion')
  			formulario.modal_ubicacion.$boton_guardar.on(
  				"click", 
  				formulario.modal_ubicacion, 
  				formulario.modal_ubicacion.editar
  			)
		}
	})
}
VentanaUbicacion.prototype.clear_Estilos = function () {
	
	this.$clave_contenedor.removeClass("has-error")
	
	if(this.$clave_mensaje.hasClass('hidden') != null) { 
		this.$clave_mensaje.addClass('hidden')
	} 

	this.$desc_contenedor.removeClass("has-error")	

	if(this.$desc_mensaje.hasClass('hidden') != null) { 
		this.$desc_mensaje.addClass('hidden')
	} 
}
VentanaUbicacion.prototype.validar = function () {

	var bandera = true

	if ( this.$clave.val() == "") {
		this.$clave_contenedor.addClass("has-error")
		this.$clave_mensaje.removeClass("hidden")
		bandera = false
	}

	if ( this.$descripcion.val() == "") {
		this.$desc_contenedor.addClass("has-error")
		this.$desc_mensaje.removeClass("hidden")
		bandera = false
	}

	return bandera
}
VentanaUbicacion.prototype.nuevo = function (e) {

	if (e.data.validar()) {
		e.data.$id.modal('hide')
		alert("Guardar")	
	}
	
}
VentanaUbicacion.prototype.editar = function (e) {

	if (e.data.validar()) {
		e.data.$id.modal('hide')
		alert("Editar")
	}
}




// $('#exampleModal').on('show.bs.modal', function (event) {
//   var button = $(event.relatedTarget) // Button that triggered the modal
//   var recipient = button.data('whatever') // Extract info from data-* attributes
//   // If necessary, you could initiate an AJAX request here (and then do the updating in a callback).
//   // Update the modal's content. We'll use jQuery here, but you could use a data binding library or other methods instead.
//   var modal = $(this)
//   modal.find('.modal-title').text('New message to ' + recipient)
//   modal.find('.modal-body input').val(recipient)
// }