/*-----------------------------------------------*\
            GLOBAL VARIABLES
\*-----------------------------------------------*/

formulario = null

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

	this.$clave = $('#clave')

	this.$equipo= $("#id_equipo")
	this.$observaciones = $('#id_observaciones')
	this.$fecha_estimada_inicio = $('#id_fecha_estimada_inicio')
	this.$fecha_estimada_fin = $('#id_fecha_estimada_fin')
	this.$fecha_real_inicio = $('#id_fecha_real_inicio')
	this.$fecha_real_fin = $('#id_fecha_real_fin')

	this.$tab_actividades = $("#tab_actividades")
	this.$tab_materiales = $("#tab_materiales")
	this.$tab_servicios = $("#tab_servicios")
	this.$tab_mano_obra = $("#tab_mano_obra")

	this.init()

}
TargetaFormulario.prototype.init = function () {

	this.$equipo.select2()

	this.$observaciones.wysihtml5({
        toolbar: {
            "font-styles": true,
            "emphasis": true,
            "lists": true,
            "html": false,
            "link": false,
            "image": false,
            "color": false,
            "blockquote": false,
        }
    })

	this.$fecha_estimada_inicio.datepicker(
        {
            autoclose: true,
            language: 'es'
        }
    )	
	this.$fecha_estimada_fin.datepicker(
        {
            autoclose: true,
            language: 'es'
        }
    )	
	this.$fecha_real_inicio.datepicker(
        {
            autoclose: true,
            language: 'es'
        }
    )	
	this.$fecha_real_fin.datepicker(
        {
            autoclose: true,
            language: 'es'
        }
    )	

	this.$tab_actividades.on("click", this, this.click_Tab_Activiades )
	this.$tab_materiales.on("click", this, this.click_Tab_Materiales )
	this.$tab_servicios.on("click", this, this.click_Tab_Servicios )
	this.$tab_mano_obra.on("click", this, this.click_Tab_Mano_Obra )

	this.deshabilitar_Tabs()
	// this.activar_Tabs()
}
TargetaFormulario.prototype.click_Tab_Activiades = function(e) {

	if (e.data.$clave.text() == ' ') {

		e.preventDefault()
		alertify.warning("Primero debe guardar la Orden")
	}	
}
TargetaFormulario.prototype.click_Tab_Materiales = function(e) {
	if (e.data.$clave.text() == ' ') {

		e.preventDefault()
		alertify.warning("Primero debe guardar la Orden")
	}	
}
TargetaFormulario.prototype.click_Tab_Servicios = function(e) {
	if (e.data.$clave.text() == ' ') {

		e.preventDefault()
		alertify.warning("Primero debe guardar la Orden")
	}	
}
TargetaFormulario.prototype.click_Tab_Mano_Obra = function(e) {
	if (e.data.$clave.text() == ' ') {

		e.preventDefault()
		alertify.warning("Primero debe guardar la Orden")
	}	
}
TargetaFormulario.prototype.deshabilitar_Tabs = function () {
	this.$tab_actividades.attr("data-toggle","")
	this.$tab_materiales.attr("data-toggle","")
	this.$tab_servicios.attr("data-toggle","")
	this.$tab_mano_obra.attr("data-toggle","")
}
TargetaFormulario.prototype.activar_Tabs = function () {
	this.$tab_actividades.attr("data-toggle","tab")
	this.$tab_materiales.attr("data-toggle","tab")
	this.$tab_servicios.attr("data-toggle","tab")
	this.$tab_mano_obra.attr("data-toggle","tab")
}

// $("#campo").attr('disabled', 'disabled');



