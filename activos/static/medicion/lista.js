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
                cache: false

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
    var csrftoken = $("[name=csrfmiddlewaretoken]").val()
    alertify.confirm(
        'Eliminar Registro',
        '¿Desea Eliminar este registro?', 

        function () {

            var url = url_grid + fila.pk + "/"

            $.ajax({
                url: url,
                headers: { "X-CSRFToken": csrftoken },
                method: "DELETE",
                success: function () {
                    alertify.success("Se eliminó registro correctamente")
                    targeta_resultados.grid.kfuente_datos.remove(fila)
                    targeta_resultados.grid.kfuente_datos.sync()

                    
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
    this.$hora_medicion =$("#id_hora")
    this.$lectura_medicion = $("#id_lectura")
    this.$boton_guardar = $("#boton_guardar")
    this.$fecha_contenedor = $("#fecha_contenedor")
    this.$fecha_mensaje = $("#fecha_mensaje")
    this.$lectura_contenedor = $("#lectura_contenedor")
    this.$lectura_mensaje = $("#lectura_mensaje")
    
    this.init()
}

Modal.prototype.init = function (e) {

    this.$fecha_medicion.datepicker(
        {
            autoclose: true,
            language: 'es',
            
        }
    )

    this.$hora_medicion.timepicker(
        {
            showInputs: false
        }
    )
    
    this.$boton_guardar.on("click", this, this.click_BotonGuardar)
    modal.clear_Estilos()
    
}

Modal.prototype.clear_Estilos = function () {
    
    this.$fecha_contenedor.removeClass("has-error")
    
    if(this.$fecha_mensaje.hasClass('hidden') != null) { 
        this.$fecha_mensaje.addClass('hidden')
    } 

    this.$lectura_medicion.removeClass("has-error")  

    if(this.$lectura_mensaje.hasClass('hidden') != null) { 
        this.$lectura_mensaje.addClass('hidden')
    } 
}

Modal.prototype.validar = function () {

    var bandera = true

    if ( this.$fecha_medicion.val() == "") {
        this.$fecha_contenedor.addClass("has-error")
        this.$fecha_mensaje.removeClass("hidden")
        bandera = false
    }

    if ( this.$lectura_medicion.val() == "") {
        this.$lectura_contenedor.addClass("has-error")
        this.$lectura_mensaje.removeClass("hidden")
        bandera = false
    }

    return bandera
}

Modal.prototype.get_Hora = function (_hora){
    this.hora = _hora
    var horas = parseInt(this.hora.substr(0, 2));
    if(this.hora.indexOf('AM') != -1 && horas == 12) {
        this.hora = this.hora.replace('12', '0');
    }
    if(this.hora.indexOf('PM')  != -1 && horas < 12) {
        this.hora = this.hora.replace(horas, (horas + 12));
    }
    return this.hora.replace(/(AM|PM)/, '');
}

Modal.prototype.click_BotonGuardar = function(e) {
    if (e.data.validar()){
        var csrftoken = $("[name=csrfmiddlewaretoken]").val()
        e.preventDefault()
        odometro_medicion = e.data.$odometro_medicion.val()
        fecha_medicion = e.data.$fecha_medicion.val()
        hora_medicion = e.data.$hora_medicion.val()
        hora_medicion =e.data.get_Hora(hora_medicion).trim()
        hora_medicion = "T"+hora_medicion+":00"
        lectura_medicion = e.data.$lectura_medicion.val()
        console.log(odometro_medicion)
        console.log(fecha_medicion)
        console.log(lectura_medicion)
        console.log(hora_medicion)
        $.ajax({
                url: url_grid,
                headers: { "X-CSRFToken": csrftoken },
                method: "POST",
                data: {
                    odometro: odometro_medicion,
                    lectura: lectura_medicion,
                    fecha: fecha_medicion+hora_medicion,
                },
                success: function (){
                    $('#modal_nuevo').modal('hide');
                    alertify.success("Se registró medición correctamente")
                    targeta_resultados.grid.kfuente_datos.read();
                    e.data.$fecha_medicion.val("")
                    e.data.$hora_medicion.val("")
                    e.data.$lectura_medicion.val("")
                   
                },
                error: function(e){

                    alertify.error("Error "+ e.status + " . No se guardó el registro")
                    $('#modal_nuevo').modal('hide')
                }
               
                        
            });
    } 
}