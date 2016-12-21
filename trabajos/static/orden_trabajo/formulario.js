/*-----------------------------------------------*\
            GLOBAL VARIABLES
\*-----------------------------------------------*/



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

	this.$observaciones = $('#id_observaciones')

	this.init()
}
TargetaFormulario.prototype.init = function () {

	this.$observaciones.wysihtml5()
}



