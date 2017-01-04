/*-----------------------------------------------*\
            GLOBAL VARIABLES
\*-----------------------------------------------*/
pagina = null

/*-----------------------------------------------*\
            LOAD
\*-----------------------------------------------*/

$(document).ready(function () {

	pagina = new Pagina()

})

// Spinner en Ajax
$(document).ajaxStart(function() { Pace.restart(); });

/*-----------------------------------------------*\
            OBJETO: PAGINA
\*-----------------------------------------------*/

function Pagina() {

	this.$titulo = $('#titulo')

	this.set_PageActive()
}
Pagina.prototype.set_PageActive = function () {

	// Se marca la pagina activa en el menu
	if ( this.$titulo.text() == "Dashboard") {

		var $opcion = $("#opt_dashboard")
		$opcion.addClass("active")
	}
	else if ( this.$titulo.text() == "Equipos") {

		var $arbol = $("#tree_activos")
		$arbol.addClass("active")

		var $opcion = $("#opt_equipos")
		$opcion.addClass("active")
	}
	else if ( this.$titulo.text() == "Ubicaciones") {
		
		var $arbol = $("#tree_activos")
		$arbol.addClass("active")

		var $opcion = $("#opt_ubicaciones")
		$opcion.addClass("active")
	}
	else if ( this.$titulo.text() == "Almacenes") {

		var $arbol = $("#tree_inventarios")
		$arbol.addClass("active")

		var $opcion = $("#opt_almacenes")
		$opcion.addClass("active")
	}
	else if ( this.$titulo.text() == "Articulos") {

		var $arbol = $("#tree_inventarios")
		$arbol.addClass("active")

		var $opcion = $("#opt_articulos")
		$opcion.addClass("active")
	}
}
Pagina.prototype.init_Alertify = function () {

    alertify.set('notifier', 'position', 'top-right')
    alertify.set('notifier', 'delay', 10)	

	alertify.defaults.theme.ok = "btn btn-primary";
	alertify.defaults.theme.cancel = "btn btn-danger";
	alertify.defaults.theme.input = "form-control";
}
Pagina.prototype.get_DatePickerConfig = function () {

	return {
	    autoSize: true,
	    dayNames: ['Domingo', 'Lunes', 'Martes', 'Miércoles', 'Jueves', 'Viernes', 'Sábado'],
	    dayNamesMin: ['Dom', 'Lu', 'Ma', 'Mi', 'Je', 'Vi', 'Sa'],
	    firstDay: 1,
	    monthNames: ['Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo', 'Junio', 'Julio', 'Agosto', 'Septiembre', 'Octubre', 'Noviembre', 'Diciembre'],
	    monthNamesShort: ['Ene', 'Feb', 'Mar', 'Abr', 'May', 'Jun', 'Jul', 'Ago', 'Sep', 'Oct', 'Nov', 'Dic'],
	    dateFormat: 'yy-mm-dd',
	    changeMonth: true,
	    changeYear: true,
	}
}