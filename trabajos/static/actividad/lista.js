/*-----------------------------------------------*\
            GLOBAL VARIABLES
\*-----------------------------------------------*/


// URLS
var url_grid = window.location.origin + "/api/actividades/"

var url_ordenes = window.location.origin + "/api/ordenestrabajo/"

// OBJS
var targeta_resultados = null
var $ot_clave = null

/*-----------------------------------------------*\
            LOAD
\*-----------------------------------------------*/

$(document).ready(function () {

    $ot_clave = $('#ot_clave')

    targeta_resultados = new TargetaResultados()
})



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
        noRecords: {
            template: "<div class='grid-empy'> No se encontraron registros </div>"
        },
        dataBound: this.apply_Estilos
    }
}
GridPrincipal.prototype.get_Campos = function (e) {

    return {
        numero : { type: "string" },
        descripcion : { type: "string" },
        horas_estimadas : { type: "string" },
        horas_reales: { type: "string" },
    }
}
GridPrincipal.prototype.get_Columnas = function (e) {

    return [
        { field: "numero", title: "Numero", width: "200px" },
        { field: "descripcion", title: "Descripcion", width: "200px" },
        { field: "horas_estimadas", title: "Horas Estimadas", width: "200px" },
        { field: "horas_reales", title: "Horas Reales", width: "200px" },

        {
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
           width: "190px"
        },
    ]
}
GridPrincipal.prototype.apply_Estilos = function (e) {

    // Aplicar iconos
    e.sender.tbody.find(".k-button.fa.fa-pencil").each(function(idx, element){
        $(element).removeClass("fa fa-pencil").find("span").addClass("fa fa-pencil")
    })

    e.sender.tbody.find(".k-button.fa.fa-trash-o").each(function(idx, element){
        $(element).removeClass("fa fa-trash-o").find("span").addClass("fa fa-trash-o")
    })
}
GridPrincipal.prototype.get_FuenteDatosConfig = function (e) {

    return {
        serverFiltering: true,
        transport: {
            read: {
                url: url_grid,
                type: "GET",
                dataType: "json",
            },
            parameterMap: function (data, action) {
                if (action === "read") {

                    return {
                        orden: $ot_clave.text()
                    }
                }
            }
        },
        schema: {
            model: {
                id: "pk",
                fields: this.get_Campos()
            }
        },
        error: function (e) {
            alertify.error("Status: " + e.status + "; Error message: " + e.errorThrown)
        },
    }
}
GridPrincipal.prototype.buscar =  function() {
  this.kfuente_datos.page(1)
}
GridPrincipal.prototype.click_BotonEditar = function (e) {

    e.preventDefault()
    var fila = this.dataItem($(e.currentTarget).closest('tr'))
    // window.location.href = url_editar + fila.id + "/"
}
GridPrincipal.prototype.click_BotonEliminar = function (e) {

    e.preventDefault()
    var fila = this.dataItem($(e.currentTarget).closest('tr'))
}



/*-----------------------------------------------*\
            OBJETO: TOOLBAR
\*-----------------------------------------------*/

function Toolbar() {

    this.$boton_nuevo = $("#boton_nuevo")
    this.$boton_exportar = $("#boton_exportar")

    this.modal = new VentanaModal()

    this.init()
}
Toolbar.prototype.init = function (e) {

    this.$boton_exportar.on("click", this, this.click_BotonExportar)
}
Toolbar.prototype.click_BotonExportar = function(e) {
    e.preventDefault()
    return null
}


/*-----------------------------------------------*\
            OBJETO: Ventana UDM
\*-----------------------------------------------*/

function VentanaModal() {

    this.$id = $('#win_modal')

    this.$numero = $('#act_numero')
    this.$numero_contenedor = $('#act_numero_contenedor')
    this.$numero_mensaje =  $('#act_numero_mensaje')

    this.$descripcion =  $('#act_desc')
    this.$desc_contenedor =  $('#act_desc_contenedor')
    this.$desc_mensaje =  $('#act_desc_mensaje')

    this.$hrs_est = $('#act_hrs_est')
    this.$hrs_est_contenedor = $('#act_hrs_est_contenedor')
    this.$hrs_est_mensaje =  $('#act_hrs_est_mensaje')

    this.$hrs_real = $('#act_hrs_real')
    this.$hrs_real_contenedor = $('#act_hrs_real_contenedor')
    this.$hrs_real_mensaje =  $('#act_hrs_real_mensaje')

    this.$boton_guardar = $('#btn_modal_save')

    this.init()
}
VentanaModal.prototype.init = function () {

    // Se asoscia eventos al abrir el modal
    this.$id.on('show.bs.modal', this, this.load)

    this.$boton_guardar.on("click", this, this.click_BotonSave)
}
VentanaModal.prototype.load = function (e) {

    e.data.clear_Fields()
    e.data.clear_Estilos()
}
VentanaModal.prototype.clear_Fields = function () {

    this.$numero.val("")
    this.$descripcion.val("")
    this.$hrs_est.val("")
    this.$hrs_real.val("")
}
VentanaModal.prototype.clear_Estilos = function () {
    
    this.$numero_contenedor.removeClass("has-error")
    
    if(this.$numero_mensaje.hasClass('hidden') != null) { 
        this.$numero_mensaje.addClass('hidden')
    } 

    this.$desc_contenedor.removeClass("has-error")  

    if(this.$desc_mensaje.hasClass('hidden') != null) { 
        this.$desc_mensaje.addClass('hidden')
    } 

    this.$hrs_est_contenedor.removeClass("has-error")  

    if(this.$hrs_est_mensaje.hasClass('hidden') != null) { 
        this.$hrs_est_mensaje.addClass('hidden')
    }     
}
VentanaModal.prototype.validar = function () {

    var bandera = true

    if ( this.$numero.val() == "") {
        this.$numero_contenedor.addClass("has-error")
        this.$numero_mensaje.removeClass("hidden")
        bandera = false
    }

    if ( this.$descripcion.val() == "") {
        this.$desc_contenedor.addClass("has-error")
        this.$desc_mensaje.removeClass("hidden")
        bandera = false
    }

    if ( this.$hrs_est.val() == "") {
        this.$hrs_est_contenedor.addClass("has-error")
        this.$hrs_est_mensaje.removeClass("hidden")
        bandera = false
    }

    return bandera
}
VentanaModal.prototype.click_BotonSave = function (e) {

    if (e.data.validar()) {

        $.ajax({
            url: url_grid,
            method: "POST",
            data: {
                "orden" :  url_ordenes + $ot_clave.text() + "/",
                "numero" : e.data.$numero.val(),
                "descripcion" : e.data.$descripcion.val(),
                "horas_estimadas" : e.data.$hrs_est.val(),
                "horas_reales" : e.data.$hrs_real.val(),
            },
            success: function (response) {

                // Ocultar Modal
                e.data.$id.modal('hide')

                // Agregar registro al Grid:
            },
            error: function (response) {

                alertify.error("Ocurrio error agregar Actividad")
            }
        })
        
    }
}
