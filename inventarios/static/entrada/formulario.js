/*-----------------------------------------------*\
            GLOBAL VARIABLES
\*-----------------------------------------------*/

// URLS
var url_grid = window.location.origin + "/api/entradasdetalle/"
var url_nuevo = window.location.origin + "/entradas/nuevo/"
var url_editar = window.location.origin + "/entradas/editar/"

// OBJS
var targeta_filtros = null
var targeta_resultados = null
var pagina = null


/*-----------------------------------------------*\
            LOAD
\*-----------------------------------------------*/

$(document).ready(function () {

    targeta_formulario = new TargetaFormulario()
    targeta_detalle = new TargetaFormularioDetalle()
    pagina = new Pagina()
    pagina.init_Alertify()    
})

// Asigna eventos a teclas
$(document).keypress(function (e) {

    // Tecla Enter
    if (e.which == 13) {

        targeta_resultados.grid.buscar()
    }
})


/*-----------------------------------------------*\
            OBJETO: Targeta Filtros
\*-----------------------------------------------*/

function TargetaFormulario() {

    this.$id = $('#id_panel')
    this.$cabecera = $('#id_cabecera')
    this.$clave = $('#id_clave')
    this.$descripcion = $('#id_descripcion')
    this.$fecha = $('#id_fecha')
    this.$almacen = $('#id_almacen')
    this.$boton_guardar = $('#boton_guardar')

    this.init()
}

TargetaFormulario.prototype.init = function () {

    this.$almacen.select2()
    this.$fecha.datepicker(
        {
            autoclose: true,
            language: 'es'
        }
    )

    this.$boton_guardar.on("click", this, this.click_BotonGuardar)
}

TargetaFormulario.prototype.click_BotonGuardar = function (e){
    e.preventDefault()
    e.data.$clave.attr("disabled", true)
    e.data.$descripcion.attr("disabled", true)
    e.data.$fecha.attr("disabled", true)
    e.data.$almacen.attr("disabled", true)
    e.data.$boton_guardar.attr("disabled", true)
    targeta_detalle.$formulario_detalle.show()
    
}

/*-----------------------------------------------*\
            OBJETO: DETALLE
\*-----------------------------------------------*/

function TargetaFormularioDetalle(){
    this.$formulario_detalle = $('#formulario_detalle')
    this.$articulo = $('#id_articulo')
    this.$cantidad = $('#id_cantidad')
    this.$boton_guardar = $('#boton_guardar_detalle')

    this.init()
}

TargetaFormularioDetalle.prototype.init = function(){
    this.$articulo.select2()
}
