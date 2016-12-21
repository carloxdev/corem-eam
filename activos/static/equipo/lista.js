/*-----------------------------------------------*\
            GLOBAL VARIABLES
\*-----------------------------------------------*/

var url_grid = window.location.origin + "/api/equipos/"
var url_nuevo = window.location.origin + "/equipos/nuevo/"
var url_editar = window.location.origin + "/equipos/editar/"
var url_anexos = window.location.origin + "/equipos/anexos/"
var url_estructura = window.location.origin + "/equipos/arbol/"
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

	this.$tag = $('#id_tag')
	this.$serie = $('#id_serie')
	this.$estado = $('#id_estado')
	this.$padre = $('#id_padre')
	this.$sistema = $('#id_sistema')
	this.$ubicacion = $('#id_ubicacion')
	this.$descripcion = $('#id_descripcion')

    this.$boton_buscar =  $('#boton_buscar')
    this.$boton_limpiar =  $('#boton_limpiar')

	this.init()
}
TargetaFiltros.prototype.init = function () {

    this.$padre.select2()
    this.$ubicacion.select2()

    this.$id.addClass('collapsed-box')

    this.$boton_buscar.on("click", this, this.click_BotonBuscar)
    this.$boton_limpiar.on("click", this, this.click_BotonLimpiar)
}
TargetaFiltros.prototype.get_Filtros = function (_page, _pageSize) {

    return {
        page: _page,
        pageSize: _pageSize,
        tag: this.$tag.val(),
        serie: this.$serie.val(),
        estado: this.$estado.val(),
        padre: this.$padre.val(),
        sistema: this.$sistema.val(),
        ubicacion: this.$ubicacion.val(),
        descripcion: this.$descripcion.val(),
    }
}
TargetaFiltros.prototype.click_BotonBuscar = function(e) {

    e.preventDefault()
    targeta_resultados.grid.buscar()
}
TargetaFiltros.prototype.click_BotonLimpiar = function (e) {

    e.preventDefault()

    e.data.$tag.val("")
    e.data.$serie.val("")
    e.data.$estado.val("")
    e.data.$padre.val("").trigger('change')
    e.data.$sistema.val("")
    e.data.$ubicacion.val("").trigger('change')
    e.data.$descripcion.val("")
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

    this.kGrid = this.$id.kendoGrid({
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
    })
}
GridPrincipal.prototype.get_Campos = function (e) {

    return {
        tag: { type: "string" },
        descripcion: { type: "string" },
        serie: { type: "string" },
        tipo: { type: "string" },
        estado: { type: "string" },
        padre: { type: "string" },
        empresa: { type: "string" },
        sistema: { type: "string" },
        ubicacion: { type: "string" },
    }
}
GridPrincipal.prototype.get_Columnas = function (e) {

    return [
        { field: "tag" , title: "Tag", width: "120px" },
        { field: "descripcion" , title: "Descripcion", width: "250px" },
        { field: "serie" , title: "Serie", width: "120px" },
        { field: "tipo" , title: "Tipo", width: "120px" },
        { field: "estado" , title: "Estado", width: "120px" },
        { field: "padre" , title: "Padre (Tag)", width: "100px" },
        { field: "empresa" , title: "Empresa", hidden: "true" },
        { field: "sistema" , title: "Sistema", width: "100px" },
        { field: "ubicacion" , title: "Ubicacion", width: "100px" },
        
        {
           command: [
                {
                   text: "Editar",
                   click: this.click_BotonEditar,
                   className: "boton_editar"
                },
                {
                    text: "Estructura",
                    click: this.click_BotonEstructura,
                },
                {
                    text: "Anexos",
                    click: this.click_BotonAnexos,
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
            alert("Este es un ejemplo")
            // alertify.notify("Status: " + e.status + "; Error message: " + e.errorThrown)
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
GridPrincipal.prototype.click_BotonAnexos = function (e) {

    e.preventDefault()
    var fila = this.dataItem($(e.currentTarget).closest('tr'))
    window.location.href = url_anexos + fila.pk + "/texto/"
}
GridPrincipal.prototype.click_BotonEstructura =  function (e) {
    e.preventDefault()
    var fila = this.dataItem($(e.currentTarget).closest('tr'))
    window.location.href = url_estructura + fila.pk + "/"
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
