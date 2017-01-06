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
    this.$ubicacion = $("#id_ubicacion")

    this.$boton_editar_ubicacion = $("#btn_edit_ubicacion")

    this.modal_ubicacion = new VentanaUbicacion()

	this.init()
}
TargetaFormulario.prototype.init = function () {

    this.$padre.select2()

    this.validar_Ubicacion()
    this.$ubicacion.on("change", this, this.change_Ubicacion)
}
TargetaFormulario.prototype.change_Ubicacion = function (e) {

	if (e.data.$ubicacion.val() == "") {
		e.data.$boton_editar_ubicacion.addClass("disabled")
	}
	else {
		e.data.$boton_editar_ubicacion.removeClass("disabled")
	}
}
TargetaFormulario.prototype.validar_Ubicacion = function () {

	if (this.$ubicacion.val() == "") {
		this.$boton_editar_ubicacion.addClass("disabled")
	}
	else {
		this.$boton_editar_ubicacion.removeClass("disabled")
	}
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

	// Se asoscia eventos al abrir el modal
	this.$id.on('show.bs.modal', this, this.load)
}
VentanaUbicacion.prototype.load = function (e) {

	var event_owner = $(e.relatedTarget)

	// Se eliminan eventos viejos
	e.data.$boton_guardar.off("click")

	// Se limpian estilos
	e.data.clear_Estilos()

	// Asosciar Eventos segun corresponda
	if (event_owner.context.id == "btn_new_ubicacion") {

		// Se limpiar el formulario
		e.data.clear()

		// Se modifica el titulo
		e.data.$id.find('.modal-title').text('Nueva Ubicacion')
		
		// Se asoscia el evento que se utilizara para guardar
		e.data.$boton_guardar.on(
			"click", 
			e.data, 
			e.data.nuevo
		)
	}
	else if (event_owner.context.id == "btn_edit_ubicacion") {

		// Se llenan los controles

		// Se modifica el titulo
		e.data.$id.find('.modal-title').text('Editar Ubicacion')

		// Se asoscia el evento que se utilizara para guardar
		e.data.$boton_guardar.on(
			"click", 
			e.data, 
			e.data.editar
		)
	}
}
VentanaUbicacion.prototype.clear = function () {

	this.$clave.val("")
	this.$descripcion.val("")
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