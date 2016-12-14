/*-----------------------------------------------*\
            GLOBAL VARS
\*-----------------------------------------------*/

var url_grid = window.location.origin + "/api/ubicaciones/"
var url_nuevo = window.location.origin + "/ubicaciones/nuevo/"
var url_editar = window.location.origin + "/ubicaciones/editar/"
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
            OBJETO: FILTROS
\*-----------------------------------------------*/

function TargetaFiltros() {

    this.$filtro = $('#filtro');
    this.$boton_buscar =  $('#boton_buscar');
    
    this.init()
}
TargetaFiltros.prototype.init = function () {

    this.$boton_buscar.on("click", this, this.click_BotonBuscar)
}
TargetaFiltros.prototype.click_BotonBuscar = function(e) {

    e.preventDefault()
    targeta_resultados.grid.buscar()
}
TargetaFiltros.prototype.get_Filtros = function () {

    return {
        search: this.$filtro.val()
        
    }
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

    this.kgrid = this.$id.kendoGrid({
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
        noRecords: {
            template: "<div class='grid-empy'> No se encontraron registros </div>"
        },
    })
}
GridPrincipal.prototype.get_Campos = function (e) {

    return {
        clave: { type: "string"},
        descripcion: { type: "string" },
    }
}
GridPrincipal.prototype.get_Columnas = function (e) {

    return [      
        { field: "clave" , title: "Clave" },
        { field: "descripcion" , title: "Descripcion"},
        {
           command: {
               text: "Editar",
               click: this.click_BotonEditar,
               className: "boton_editar"
           },
           title: " ",
           width: "90px"
        },
    ]
}
GridPrincipal.prototype.get_FuenteDatosConfig = function (e) {

    return {
        transport: {
            read: {

                url: url_grid,
                type: "GET",
                dataType: "json",
            },
            parameterMap: function (data, action) {
                if (action === "read") {
                    return targeta_filtros.get_Filtros()
                }
            }
        },
        schema: {
            model: {
                fields: this.get_Campos()
            }
        },
        error: function (e) {
            // alertify.notify("Status: " + e.status + "; Error message: " + e.errorThrown)
            alert("Valio gaver")
        },
    }
}
GridPrincipal.prototype.buscar =  function() {
  this.kfuente_datos.read()
}
GridPrincipal.prototype.click_BotonEditar = function (e) {

    e.preventDefault()
    var fila = this.dataItem($(e.currentTarget).closest('tr'))
    window.location.href = url_editar + fila.pk;
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


