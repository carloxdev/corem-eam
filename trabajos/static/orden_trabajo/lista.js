/*-----------------------------------------------*\
            GLOBAL VARIABLES
\*-----------------------------------------------*/

// URLS
var url_grid = window.location.origin + "/api/ordenestrabajo/"
var url_nuevo = window.location.origin + "/ordenes/nuevo/"
var url_editar = window.location.origin + "/ordenes/editar/"
var url_anexos = window.location.origin + "/ordenes/anexos/"

var url_ot = window.location.origin + "/media/files/ot.xlsx"
var url_mantenimiento = window.location.origin + "/media/files/actividades.pdf"


// OBJS
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

    this.$equipo = $('#id_equipo')
    this.$descripcion = $('#id_descripcion')
    this.$tipo = $('#id_tipo')
    this.$estado = $('#id_estado')
    this.$responsable = $('#id_responsable')

    this.$boton_buscar =  $('#boton_buscar')
    this.$boton_limpiar =  $('#boton_limpiar')

	this.init()
}
TargetaFiltros.prototype.init = function () {
    
    this.$equipo.select2()
    this.$tipo.select2()
    this.$estado.select2()

    this.$id.addClass('collapsed-box')

    this.$boton_buscar.on("click", this, this.click_BotonBuscar)
    this.$boton_limpiar.on("click", this, this.click_BotonLimpiar)
}
TargetaFiltros.prototype.get_Filtros = function (_page, _pageSize) {

    return {
        page: _page,
        pageSize: _pageSize,

        clave: this.$equipo.val(),
        descripcion: this.$descripcion.val(),
        tipo: this.$tipo.val(),
        estado: this.$estado.val(),
        responsable: this.$responsable.val(),
    }
}
TargetaFiltros.prototype.click_BotonBuscar = function(e) {

    e.preventDefault()
    targeta_resultados.grid.buscar()
}
TargetaFiltros.prototype.click_BotonLimpiar = function (e) {

    e.preventDefault()

    e.data.$equipo.val("").trigger('change')
    e.data.$descripcion.val("")
    e.data.$tipo.val("").trigger('change')
    e.data.$estado.val("").trigger('change')
    e.data.$responsable.val("")
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

    this.kgrid = this.$id.kendoGrid(this.get_Config())
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
        dataBound: this.apply_Estilos
    }

}
GridPrincipal.prototype.get_Campos = function (e) {

    return {
        equipo: { type: "string" },
        tipo: { type: "string" },
        estado: { type: "string" },
        descripcion: { type: "string" },
        responsable: { type: "string" },
    }
}
GridPrincipal.prototype.get_Columnas = function (e) {

    return [

        { field: "equipo", title: "Equipo", width: "200px" },
        { field: "descripcion", title: "Descripcion", width: "250px" },
        { field: "tipo", title: "Tipo", width: "120px" },
        { field: "estado", title: "Estado", width: "120px" },
        { field: "responsable", title: "Responsable", width: "120px" },
        { field: "fecha_estimada_inicio", title: "Fecha Estimada Inicio", width: "140px" },
        { field: "fecha_estimada_fin", title: "Fecha Estimada Fin", width: "140px" },
        { field: "fecha_real_inicio", title: "Fecha Real Inicio", width: "120px" },
        { field: "fecha_real_fin", title: "Fecha Real Fin", width: "120px" },
        { field: "es_template", title: "¿Template?", width: "120px", template: "#= targeta_resultados.grid.change_IsTemplate(es_template) #" },

        {
           command: [
                {
                   text: " Editar",
                   click: this.click_BotonEditar,
                   className: "boton_editar fa fa-pencil"
                },
                {
                    text: " Anexos",
                    click: this.click_BotonAnexos,
                    className: "boton_default fa fa-paperclip"
                },
                {
                   text: " Imprimir OT",
                   click: this.click_BotonImprimirOT,
                   className: "boton_default fa fa-wrench"
                },
                {
                    text: " Reporte Mantenimiento",
                    click: this.click_ReporteMantenimiento,
                    className: "boton_default fa fa-gear"
                },                            
            ],           
           title: " ",
           width: "490px"
        },
    ]
}
GridPrincipal.prototype.apply_Estilos = function (e) {

    // Aplicar iconos
    e.sender.tbody.find(".k-button.fa.fa-pencil").each(function(idx, element){
        $(element).removeClass("fa fa-pencil").find("span").addClass("fa fa-pencil")
    })

    e.sender.tbody.find(".k-button.fa.fa-paperclip").each(function(idx, element){
        $(element).removeClass("fa fa-paperclip").find("span").addClass("fa fa-paperclip")
    }) 

    // Aplicar iconos
    e.sender.tbody.find(".k-button.fa.fa-wrench").each(function(idx, element){
        $(element).removeClass("fa fa-wrench").find("span").addClass("fa fa-wrench")
    })

    e.sender.tbody.find(".k-button.fa.fa-gear").each(function(idx, element){
        $(element).removeClass("fa fa-gear").find("span").addClass("fa fa-gear")
    })           

    // Aplicar formato a columna:
    $('td').each( function () {
        if($(this).text()=='CAPTURA'){ 
            $(this).addClass('cell--reparacion')
        }
        else if($(this).text()=='CERRADA'){ 
            $(this).addClass('cell--deshabilitado')
        }
        else if($(this).text()=='TERMINADA'){ 
            $(this).addClass('cell--terminada')
        }
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
GridPrincipal.prototype.click_BotonImprimirOT = function (e) {
    e.preventDefault()

    // Obteniedo informacion del registro
    var win = window.open(url_ot, '_blank')
    win.focus()
}
GridPrincipal.prototype.click_ReporteMantenimiento = function (e) {
    e.preventDefault()

    // Obteniedo informacion del registro
    var win = window.open(url_mantenimiento, '_blank')
    win.focus()
}
GridPrincipal.prototype.change_IsTemplate = function (_value) {

    if (_value == "True") {
        return "SI"    
    }
    else {
        return "NO"
    }
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
