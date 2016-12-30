/*-----------------------------------------------*\
            GLOBAL VARIABLES
\*-----------------------------------------------*/

var url_grid = window.location.origin + "/api/odometros/"
var url_nuevo = window.location.origin + "/odometros/nuevo/"
var url_editar = window.location.origin + "/odometros/editar/"
var url_medicion = window.location.origin + "/mediciones/"
var targeta_filtros = null
var targeta_resultados = null


/*-----------------------------------------------*\
            LOAD
\*-----------------------------------------------*/

$(document).ready(function () {

    targeta_filtros = new TargetaFiltros()
    targeta_resultados = new TargetaResultados()
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

	this.$equipo = $('#id_equipo')
	this.$clave = $('#id_clave')
	this.$descripcion = $('#id_descripcion')
	this.$udm = $('#id_udm')

    this.$boton_buscar =  $('#boton_buscar')
    this.$boton_limpiar =  $('#boton_limpiar')

	this.init()
}
TargetaFiltros.prototype.init = function () {

    this.$equipo.select2()
    this.$udm.select2()

    this.$id.addClass('collapsed-box')

    this.$boton_buscar.on("click", this, this.click_BotonBuscar)
    this.$boton_limpiar.on("click", this, this.click_BotonLimpiar)
}
TargetaFiltros.prototype.get_Filtros = function (_page, _pageSize) {

    return {
        page: _page,
        pageSize: _pageSize,
        equipo: this.$equipo.val(),
        clave: this.$clave.val(),
        descripcion: this.$descripcion.val(),
        udm: this.$udm.val(),
    }
}
TargetaFiltros.prototype.click_BotonBuscar = function(e) {

    e.preventDefault()
    targeta_resultados.grid.buscar()
}
TargetaFiltros.prototype.click_BotonLimpiar = function (e) {

    e.preventDefault()

    e.data.$equipo.val("").trigger('change')
    e.data.$clave.val("")
    e.data.$descripcion.val("")
    e.data.$udm.val("").trigger('change')
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
        equipo: { type: "string" },
        clave: { type: "string" },
        descripcion: { type: "string" },
        udm: { type: "string" },
        
    }
}
GridPrincipal.prototype.get_Columnas = function (e) {

    return [
        { field: "equipo" , title: "Equipo", width: "120px" },
        { field: "clave" , title: "Clave", width: "120px" },
        { field: "descripcion" , title: "Descripción", width: "250px" },
        { field: "udm" , title: "UDM", width: "120px" },
        { field: "esta_activo" , title: "Activo", width: "120px" },

       
        
        {
           command: [
                {
                   text: "Editar",
                   click: this.click_BotonEditar,
                   className: "boton_editar"
                }, 
                {
                   text: "Eliminar",
                   click: this.click_BotonEliminar,
                   className: "boton_eliminar"
                },   
                {
                   text: "Medicion",
                   click: this.click_BotonMedicion,
                   className: "boton_default"
                },               
            ],           
           title: " ",
           width: "260px"
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
GridPrincipal.prototype.click_BotonEditar = function (e) {

    e.preventDefault()
    var fila = this.dataItem($(e.currentTarget).closest('tr'))
    window.location.href = url_editar + fila.pk + "/"
}
GridPrincipal.prototype.click_BotonMedicion = function (e) {
    e.preventDefault()
    window.location.href = url_medicion

}

/*-----------------------------------------------*\
            OBJETO: TOOLBAR
\*-----------------------------------------------*/

function Toolbar() {

    this.$boton_nuevo = $("#boton_nuevo")
    this.$boton_exportar = $("#boton_exportar")

    this.init()
}
Toolbar.prototype.init = function (e) {

    this.$boton_nuevo.on("click", this, this.click_BotonNuevo)
    this.$boton_exportar.on("click", this, this.click_BotonExportar)
}
Toolbar.prototype.click_BotonNuevo = function (e) {

    e.preventDefault()
    window.location.href = url_nuevo
}
Toolbar.prototype.click_BotonExportar = function(e) {
    e.preventDefault()
    return null
}
