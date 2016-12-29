/*-----------------------------------------------*\
            GLOBAL VARIABLES
\*-----------------------------------------------*/

var url_grid = window.location.origin + "/api/articulos/"
var url_nuevo = window.location.origin + "/articulos/nuevo/"
var url_editar = window.location.origin + "/articulos/editar/"
var url_anexos = window.location.origin + "/articulos/anexos/"
var targeta_filtros = null
var targeta_resultados = null


/*-----------------------------------------------*\
            LOAD
\*-----------------------------------------------*/

$(document).ready(function () {

    this.$id = $('#id_filtros')

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

    this.$clave = $('#id_clave')
    this.$descripcion = $('#id_descripcion')
    this.$tipo = $('#id_tipo')
    this.$udm = $('#id_udm')
    this.$clave_jde = $('#id_clave_jde')

    this.$boton_buscar =  $('#boton_buscar')
    this.$boton_limpiar =  $('#boton_limpiar')

	this.init()
}
TargetaFiltros.prototype.init = function () {
    
    this.$udm.select2()

    this.$id.addClass('collapsed-box')

    this.$boton_buscar.on("click", this, this.click_BotonBuscar)
    this.$boton_limpiar.on("click", this, this.click_BotonLimpiar)
}
TargetaFiltros.prototype.get_Filtros = function (_page, _pageSize) {

    return {
        page: _page,
        pageSize: _pageSize,

        clave: this.$clave.val(),
        descripcion: this.$descripcion.val(),
        tipo: this.$tipo.val(),
        udm: this.$udm.val(),
        clave_jde: this.$clave_jde.val(),
    }
}
TargetaFiltros.prototype.click_BotonBuscar = function(e) {

    e.preventDefault()
    targeta_resultados.grid.buscar()
}
TargetaFiltros.prototype.click_BotonLimpiar = function (e) {

    e.preventDefault()

    e.data.$clave.val("")
    e.data.$descripcion.val("")
    e.data.$tipo.val("")
    e.data.$udm.val("").trigger('change')
    e.data.$clave_jde.val("")

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
        clave: { type: "string" },
        descripcion: { type: "string" },
        tipo: { type: "string" },
        udm: { type: "string" },
        clave_jde: { type: "string" },
    }
}
GridPrincipal.prototype.get_Columnas = function (e) {

    return [

        { field: "clave", title: "Clave", width: "120px" },
        { field: "descripcion", title: "Descripcion", width: "250px" },
        { field: "tipo", title: "Tipo", width: "120px" },
        { field: "udm", title: "UDM", width: "120px" },
        { field: "clave_jde", title: "Clave JDE", width: "120px" },
        {
           command: [
                {
                   text: "Editar",
                   click: this.click_BotonEditar,
                   className: "boton_editar"
                },
                {
                    text: "Anexos",
                    click: this.click_BotonAnexos,
                    className: "boton_default"
                },                
            ],           
           title: " ",
           width: "200px"
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
GridPrincipal.prototype.click_BotonAnexos = function (e) {

    e.preventDefault()
    var fila = this.dataItem($(e.currentTarget).closest('tr'))
    window.location.href = url_anexos + fila.pk + "/texto/"
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
