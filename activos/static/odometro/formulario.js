/*-----------------------------------------------*\
            GLOBAL VARIABLES
\*-----------------------------------------------*/


// URLS
var url_grid = window.location.origin + "/api/equipos/"
var url_nuevo = window.location.origin + "/equipos/nuevo/"
var url_editar = window.location.origin + "/equipos/editar/"
var url_anexos = window.location.origin + "/equipos/anexos/"
var url_estructura = window.location.origin + "/equipos/arbol/"

// OBJS
var targeta_filtros = null
var targeta_resultados = null


/*-----------------------------------------------*\
            LOAD
\*-----------------------------------------------*/

$(document).ready(function () {

    $('#id_equipo').select2()
})



