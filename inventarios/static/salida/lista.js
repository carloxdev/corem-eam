/*-----------------------------------------------*\
            GLOBAL VARIABLES
\*-----------------------------------------------*/

// URLS
var url_grid = window.location.origin + "/api/movimientos/"
var url_nuevo = window.location.origin + "/salidas/nuevo/"

// OBJS
var targeta_filtros = null
var targeta_resultados = null
var pagina = null


/*-----------------------------------------------*\
            LOAD
\*-----------------------------------------------*/

$(document).ready(function () {

    targeta_filtros = new TargetaFiltros()
    targeta_resultados = new TargetaResultados()

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

function TargetaFiltros() {

    this.$id = $('#id_panel')

    this.$clave = $('#id_clave')
    this.$descripcion = $('#id_descripcion')
    this.$fecha_inicio = $('#fecha_inicio')
    this.$fecha_fin = $('#fecha_fin')
    this.$almacen_origen = $('#id_almacen_origen')
    this.$almacen_destino = $('#id_almacen_destino')
    this.$persona_recibe = $('#id_persona_recibe')
    this.$persona_entrega = $('#id_persona_entrega')
    this.$estado = $('#id_estado')
    this.$tipo = $('#id_tipo')
    this.$boton_buscar =  $('#boton_buscar')
    this.$boton_limpiar =  $('#boton_limpiar')

    this.init()
}
TargetaFiltros.prototype.init = function () {

    this.$almacen_origen.select2()
    this.$almacen_destino.select2()
    this.$fecha_inicio.datepicker(
        {
            autoclose: true,
            language: 'es'
        }
    )
    this.$fecha_fin.datepicker(
        {
            autoclose: true,
            language: 'es'
        }
    )
    this.$id.addClass('collapsed-box')

    this.$boton_buscar.on("click", this, this.click_BotonBuscar)
    this.$boton_limpiar.on("click", this, this.click_BotonLimpiar)
}
TargetaFiltros.prototype.get_Filtros = function (_page, _pageSize) {
    tipo = "SAL"
    return {
        page: _page,
        pageSize: _pageSize,
        clave: this.$clave.val(),
        descripcion: this.$descripcion.val(),
        fecha_inicio: this.$fecha_inicio.val(),
        fecha_fin: this.$fecha_fin.val(),
        almacen_origen: this.$almacen_origen.val(),
        almacen_destino: this.$almacen_destino.val(),
        persona_recibe: this.$persona_recibe.val(),
        persona_entrega: this.$persona_entrega.val(),
        estado: this.$estado.val(),
        tipo: tipo,

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
    e.data.$fecha_inicio.val("")
    e.data.$fecha_fin.val("")
    e.data.$almacen_origen.val("").trigger('change')
    e.data.$almacen_destino.val("").trigger('change')
    e.data.$persona_recibe.val("")
    e.data.$persona_entrega.val("")
    e.data.$estado.val().trigger('change')

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
        scrollable: true,
        columns: this.get_Columnas(),
        scrollable: true,
        pageable: true,
        noRecords: {
            template: "<div class='grid-empy'> No se encontraron registros </div>"
        },  
        dataBound: this.set_Icons,      
    }
}
GridPrincipal.prototype.get_Campos = function (e) {

    return {
        fecha: { type: "string" },
        clave: { type: "string" },
        descripcion: { type: "string" },
        almacen_origen: { type: "string" },
        almacen_destino: { type: "string" },
        
    }
}
GridPrincipal.prototype.get_Columnas = function (e) {

    return [
        { field: "fecha" , title: "Fecha", width: "80px", template: "#= kendo.toString(kendo.parseDate(fecha), 'dd MMM yyyy') #" },
        { field: "clave" , title: "Clave", width: "120px" },
        { field: "descripcion" , title: "Descripción", width: "250px" },
        { field: "almacen_origen" , title: "Almacen Origen", width: "120px" },
        { field: "almacen_destino" , title: "Almacen Destino", width: "120px" },
        { field: "persona_recibe" , title: "Persona Recibe", width: "120px" },
        { field: "persona_entrega" , title: "Persona Entrega", width: "120px" },
        { field: "estado" , title: "Estado", width: "120px" },

        /*{
           command: [
                {
                   text: " Editar",
                   click: this.click_BotonEditar,
                   className: "boton_editar fa fa-pencil"
                }, 
                {
                   text: " Eliminar",
                   click: this.click_BotonEliminar,
                   className: "boton_eliminar fa fa-trash-o"
                },   
                             
            ],           
           title: " ",
           width: "170px"
        },*/
    ]
}
GridPrincipal.prototype.set_Icons = function (e) {

    e.sender.tbody.find(".k-button.fa.fa-pencil").each(function(idx, element){
        $(element).removeClass("fa fa-pencil").find("span").addClass("fa fa-pencil")
    })

    e.sender.tbody.find(".k-button.fa.fa-trash-o").each(function(idx, element){
        $(element).removeClass("fa fa-trash-o").find("span").addClass("fa fa-trash-o")
    })
    
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
/*GridPrincipal.prototype.click_BotonEditar = function (e) {

    e.preventDefault()
    var fila = this.dataItem($(e.currentTarget).closest('tr'))
    window.location.href = url_editar + fila.pk + "/"
}*/


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