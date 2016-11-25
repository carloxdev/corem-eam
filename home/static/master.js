/*-----------------------------------------------*\
            LOAD
\*-----------------------------------------------*/

$(document).ready(function () {

	pagina = new Pagina()	    

})


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

}