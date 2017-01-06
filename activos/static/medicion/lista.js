/*-----------------------------------------------*\
            GLOBAL VARIABLES
\*-----------------------------------------------*/

var url_grid = window.location.origin + "/api/mediciones/"
var targeta_filtros = null
var targeta_resultados = null
var modal= null

/*-----------------------------------------------*\
            LOAD
\*-----------------------------------------------*/

$(document).ready(function () {

    targeta_filtros = new TargetaFiltros()
    targeta_resultados = new TargetaResultados()
    modal = new Modal()


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

	this.$odometro = $('#id_odometro_requested') 
    this.$lectura_minima = $('#lectura_minima')
    this.$lectura_maxima = $('#lectura_maxima')
    this.$fecha_inicio = $('#fecha_inicio')
    this.$fecha_fin = $('#fecha_fin')
    this.$datepicker_formulario = $('#id_fecha')
    this.$boton_buscar =  $('#boton_buscar')
    this.$boton_limpiar =  $('#boton_limpiar')

	this.init()
}
TargetaFiltros.prototype.init = function () {

    //this.$odometro.select2()

    this.$id.addClass('collapsed-box')
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

    this.$boton_buscar.on("click", this, this.click_BotonBuscar)
    this.$boton_limpiar.on("click", this, this.click_BotonLimpiar)
}
TargetaFiltros.prototype.get_Filtros = function (_page, _pageSize) {

    return {
        page: _page,
        pageSize: _pageSize,
        odometro: this.$odometro.val(),
        fecha_inicio: this.$fecha_inicio.val(),
        fecha_fin: this.$fecha_fin.val(),
        lectura_minima: this.$lectura_minima.val(),
        lectura_maxima: this.$lectura_maxima.val(),
        
    }
}
TargetaFiltros.prototype.click_BotonBuscar = function(e) {

    e.preventDefault()
    targeta_resultados.grid.buscar()
    
}
TargetaFiltros.prototype.click_BotonLimpiar = function (e) {

    e.preventDefault()
    //e.data.$odometro.val("").trigger('change')
    e.data.$lectura_minima.val("")
    e.data.$lectura_maxima.val("")
    e.data.$fecha_inicio.val("")
    e.data.$fecha_fin.val("")

    
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
                   text: "Eliminar",
                   click: this.click_BotonEliminar,
                   className: "boton_eliminar"
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

GridPrincipal.prototype.click_BotonEliminar = function (e) {
    e.preventDefault()
    var fila = this.dataItem($(e.currentTarget).closest('tr'))

    alertify.confirm(
        'Eliminar Registro',
        '¿Desea Eliminar este registro?', 

        function () {

            var url = url_grid + fila.pk + "/"

            $.ajax({
                url: url,
                method: "DELETE",
                success: function () {
                    targeta_resultados.grid.kfuente_datos.remove(fila)
                    targeta_resultados.grid.kfuente_datos.sync()

                    alertify.success("Se eliminó registro correctamente")
                },
                error: function () {
                    
                    alertify.error("Ocurrió un error al eliminar")
                }
            })
        }, 
        null
    )
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
    $('#modal_nuevo').modal('show');
}

/*-----------------------------------------------*\
            OBJETO: MODAL
\*-----------------------------------------------*/

function Modal() {

    this.$odometro_medicion = $("#id_odometro_requested")
    this.$fecha_medicion = $("#id_fecha")
    this.$lectura_medicion = $("#id_lectura")
    this.$boton_guardar = $("#boton_guardar")

    this.init()
}

Modal.prototype.init = function (e) {

    this.$fecha_medicion.datepicker(
        {
            autoclose: true,
            language: 'es'
        }
    )
    this.$boton_guardar.on("click", this, this.click_BotonGuardar)
    
}

Modal.prototype.click_BotonGuardar = function(e) {
    var csrftoken = $("[name=csrfmiddlewaretoken]").val()
    e.preventDefault()
    odometro_medicion = e.data.$odometro_medicion.val()
    fecha_medicion = e.data.$fecha_medicion.val()
    lectura_medicion = e.data.$lectura_medicion.val()
    console.log(odometro_medicion)
    console.log(fecha_medicion)
    console.log(lectura_medicion)
    $.ajax({
            url: url_grid,
            headers: { "X-CSRFToken": csrftoken },
            method: "POST",
            data: {
                odometro: odometro_medicion,
                lectura: lectura_medicion,
                fecha: "2017-01-04T15:41:25" ,
            },
            success: function (){
                alertify.success("Se registró medición correctamente")
                $('#modal_nuevo').modal('hide');
                location.reload();
            },
            error: function(e){

                alertify.error("Error "+ e.status + " . No se guardó el registro")
                $('#modal_nuevo').modal('hide')
            }
           
                    
        });
}