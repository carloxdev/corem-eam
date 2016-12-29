/*-----------------------------------------------*\
            GLOBAL VARIABLES
\*-----------------------------------------------*/

var url_grid = window.location.origin + "/api/mediciones/"
var url_nuevo = window.location.origin + "/mediciones/nuevo"
var targeta_filtros = null
var targeta_resultados = null
var url_actual = window.location.pathname

/*-----------------------------------------------*\
            LOAD
\*-----------------------------------------------*/

$(document).ready(function () {

    targeta_filtros = new TargetaFiltros()
    targeta_resultados = new TargetaResultados()
    console.log(url_actual)
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

function TargetaFiltros() {

    this.$id = $('#id_panel')

	this.$odometro = $('#id_odometro')
    this.$id_odometro = $('#id_odometro_requested')
    this.$boton_buscar =  $('#boton_buscar')
    this.$boton_limpiar =  $('#boton_limpiar')

	this.init()
}
TargetaFiltros.prototype.init = function () {

    this.$odometro.select2()

    this.$id.addClass('collapsed-box')

    this.$boton_buscar.on("click", this, this.click_BotonBuscar)
    this.$boton_limpiar.on("click", this, this.click_BotonLimpiar)
}
TargetaFiltros.prototype.get_Filtros = function (_page, _pageSize) {
    if (url_actual==='/mediciones/'){
        id_odometro = this.$odometro.val()
    }
    else {
        id_odometro = this.$id_odometro.val()
    }
    

    return {
        page: _page,
        pageSize: _pageSize,
        odometro: id_odometro,
        
    }
}
TargetaFiltros.prototype.click_BotonBuscar = function(e) {

    e.preventDefault()
    targeta_resultados.grid.buscar()
}
TargetaFiltros.prototype.click_BotonLimpiar = function (e) {

    e.preventDefault()

    e.data.$odometro.val("").trigger('change')
    
}

/*-----------------------------------------------*\
            OBJETO: RESULTADOS
\*-----------------------------------------------*/

function TargetaResultados() {

    this.toolbar = new Toolbar()
    this.grid = new GridPrincipal()
}


/*-----------------------------------------------*\
            OBJETO: GRID
\*-----------------------------------------------*/

function GridPrincipal() {

	this.$id = $("#grid_principal")
    this.kfuente_datos = null
    this.kgrid = null

    this.init()
}
GridPrincipal.prototype.init = function () {

	kendo.culture("es-MX")

    this.kfuente_datos = new kendo.data.DataSource(this.get_FuenteDatosConfig())

    this.kGrid = this.$id.kendoGrid(this.get_Config())
}
GridPrincipal.prototype.get_Config = function () {

    return {
        dataSource: this.kfuente_datos,
        columnMenu: false,
        groupable: false,
        sortable: false,
        editable: false,
        resizable: true,
        selectable: true,
        scrollable: false,
        columns: this.get_Columnas(),
        scrollable: true,
        pageable: true,
        noRecords: {
            template: "<div class='grid-empy'> No se encontraron registros </div>"
        },        
    }
}
GridPrincipal.prototype.get_Campos = function (e) {

    return {
        odometro: { type: "string" },
        udm: { type: "string" },
        equipo: { type: "string" },
        fecha: { type: "string" },
        lectura: { type: "string" },
    }
}
GridPrincipal.prototype.get_Columnas = function (e) {

    return [
        { field: "odometro" , title: "Odometro", width: "120px" },
        { field: "udm" , title: "Unidad de Medida", width: "120px" },
        { field: "equipo" , title: "Equipo", width: "120px" },
        { field: "fecha" , title: "Fecha", width: "120px" },
        { field: "lectura" , title: "Lectura", width: "120px" },
        
        {
           command: [
                {
<<<<<<< HEAD
                   text: "Agregar Lectura",
                   click: this.click_BotonLectura,
                   className: "boton_default"
=======
                   text: "Accion",
                   click: this.click_BotonAccion,
                   className: "boton_lectura"
>>>>>>> avances mediciones
                },              
            ],           
           title: " ",
           width: "120px"
        },
    ]
}
GridPrincipal.prototype.get_FuenteDatosConfig = function (e) {

    return {

        serverPaging: true,
        pageSize: 10,
        transport: {
            read: {

                url: url_grid,
                type: "GET",
                dataType: "json",
            },
            parameterMap: function (data, action) {
                if (action === "read") {

                    return targeta_filtros.get_Filtros(data.page, data.pageSize)
                }
            }
        },
        schema: {
            data: "results",
            total: "count",
            model: {
                fields: this.get_Campos()
            }
        },
        error: function (e) {
            alert("Status: " + e.status + "; Error message: " + e.errorThrown)
        },
    }
}
GridPrincipal.prototype.buscar =  function() {
    this.kfuente_datos.page(1)
}

/*-----------------------------------------------*\
            OBJETO: TOOLBAR
\*-----------------------------------------------*/

function Toolbar() {

    this.$boton_exportar = $("#boton_exportar")
    this.$boton_nuevo = $("#boton_nuevo")

    this.init()
}
Toolbar.prototype.init = function (e) {

    this.$boton_exportar.on("click", this, this.click_BotonExportar)
    this.$boton_nuevo.on("click", this, this.click_BotonNuevo)
}
Toolbar.prototype.click_BotonExportar = function(e) {
    e.preventDefault()
    return null
}
Toolbar.prototype.click_BotonNuevo = function (e) {

    e.preventDefault()
    window.location.href = url_nuevo
}