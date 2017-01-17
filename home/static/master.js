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
	this.init_Alertify()
}
Pagina.prototype.set_PageActive = function () {

	// Se marca la pagina activa en el menu
	if ( this.$titulo.text() == "Dashboard") {
		
		this.activar_Opcion("opt_dashboard")
	}
	else if ( this.$titulo.text() == "Equipos") {

		this.activar_Arbol("tree_activos")
		this.activar_Opcion("opt_equipos")
	}
	else if ( this.$titulo.text() == "Ubicaciones") {
		
		this.activar_Arbol("tree_activos")
		this.activar_Opcion("opt_ubicaciones")
	}
	else if ( this.$titulo.text() == "Odómetros") {
		
		this.activar_Arbol("tree_activos")
		this.activar_Opcion("opt_odometros")
	}	
	else if ( this.$titulo.text() == "Mediciones") {
		
		this.activar_Arbol("tree_activos")
		this.activar_Opcion("opt_odometros")
	}
	else if ( this.$titulo.text() == "UDM de Odometro") {
		
		this.activar_Arbol("tree_activos")
		this.activar_Opcion("opt_odometros_udm")
	}		
	else if ( this.$titulo.text() == "Almacenes") {

		this.activar_Arbol("tree_inventarios")
		this.activar_Opcion("opt_almacenes")
	}
	else if ( this.$titulo.text() == "UDM de Articulo") {
		
		this.activar_Arbol("tree_inventarios")
		this.activar_Opcion("opt_articulo_udm")
	}			
	else if ( this.$titulo.text() == "Articulos") {

		this.activar_Arbol("tree_inventarios")
		this.activar_Opcion("opt_articulos")
	}
	else if ( this.$titulo.text() == "Ordenes de Trabajo") {

		this.activar_Arbol("tree_trabajos")
		this.activar_Opcion("opt_ordenes")
	}
}
Pagina.prototype.activar_Arbol = function (_tree) {

	var $arbol = $("#" + _tree)
	$arbol.addClass("active")
}
Pagina.prototype.activar_Opcion = function (_option) {

	var $opcion = $("#" + _option)
	$opcion.addClass("active")
}
Pagina.prototype.init_Alertify = function () {

    alertify.set('notifier', 'position', 'top-right')
    alertify.set('notifier', 'delay', 10)	

	alertify.defaults.theme.ok = "btn btn-success";
	alertify.defaults.theme.cancel = "btn btn-default";
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