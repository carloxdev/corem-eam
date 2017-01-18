/*-----------------------------------------------*\
            GLOBAL VARIABLES
\*-----------------------------------------------*/


// URLS
var url_materiales = window.location.origin + "/api/materiales/"
var url_ordenes = window.location.origin + "/api/ordenestrabajo/"
var url_articulos = window.location.origin + "/api/articulos2/"

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
        articulo : { type:"string" },
        cantidad_estimada : { type: "number" },
    }
}
GridPrincipal.prototype.get_Columnas = function (e) {

    return [
        { field: "articulo", title: "Articulo" },
        { field: "cantidad_estimada", title: "Cantidad Estimada", format: '{0:n2}' },
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
        transport: {
            read: {
                url: url_materiales,
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
                fields: this.get_Campos()
            }
        },
        error: function (e) {
            alertify.error("Status: " + e.status + "; Error message: " + e.errorThrown)
        },
    }
}
GridPrincipal.prototype.buscar = function() {
    this.kfuente_datos.read()
}
GridPrincipal.prototype.click_BotonEditar = function (e) {

    e.preventDefault()
    var fila = this.dataItem($(e.currentTarget).closest('tr'))
    targeta_resultados.toolbar.modal.set_Id(fila.pk)
    targeta_resultados.toolbar.modal.mostrar()
}
GridPrincipal.prototype.click_BotonEliminar = function (e) {

    e.preventDefault()
    var fila = this.dataItem($(e.currentTarget).closest('tr'))

    alertify.confirm(
        'Eliminar Registro',
        '¿Desea Eliminar este registro?', 
        function () {

            var url = url_materiales + fila.pk + "/"

            $.ajax({
                url: url,
                method: "DELETE",
                success: function () {
                    alertify.success("Se elimino registro correctamente")
                    
                    targeta_resultados.grid.kfuente_datos.remove(fila)

                },
                error: function () {
                    
                    alertify.error("Ocurrio un error al eliminar")
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
            OBJETO: Ventana Modal
\*-----------------------------------------------*/

function VentanaModal() {

    this.$id = $('#win_modal')

    this.$pk = $("#mat_id")

    this.$articulo = $('#mat_articulo')
    this.$articulo_contenedor = $('#mat_articulo_contenedor')
    this.$articulo_mensaje =  $('#mat_articulo_mensaje')

    this.$cantidad_estimada =  $('#mat_cant_esti')
    this.$cant_est_contenedor =  $('#mat_cant_esti_contenedor')
    this.$cant_est_mensaje =  $('#mat_cant_esti_mensaje')

    this.$boton_guardar = $('#btn_modal_save')

    this.init()
}
VentanaModal.prototype.init = function () {

    // Se asoscia eventos al abrir el modal
    this.$id.on('show.bs.modal', this, this.load)
}
VentanaModal.prototype.set_Id = function (_value) {

    this.$pk.val(_value)
}
VentanaModal.prototype.mostrar = function (e) {
    this.$id.modal()
}
VentanaModal.prototype.load = function (e) {


    e.data.$articulo.select2()

    // Se eliminan eventos viejos
    e.data.$boton_guardar.off("click")

    // Se limpian estilos
    e.data.clear_Estilos()

    // Se limpiar el formulario
    e.data.clear_Fields()  

    e.data.fill_Articulos()

    // Asosciar Eventos segun corresponda
    var event_owner

    if ( e.relatedTarget == undefined ) {

        // Se modifica el titulo
        e.data.$id.find('.modal-title').text('Editar Actividad')

        // Se llenan los controles
        // var url = url_actividad + "?id=" + formulario.$udm.val()

        modal = e.data

        $.ajax({
            url: url_materiales,
            method: "GET",
            data: {
                "id": e.data.$pk.val()
            },
            success: function (response) {

                // modal.$articulo.val(response[0].articulo)
                modal.$cantidad_estimada.val(response[0].cantidad_estimada)

            },
            error: function (response) {
                
                alertify.error("Ocurrio error al consultar")
            }
        })
        // Se asoscia el evento que se utilizara para guardar
        e.data.$boton_guardar.on(
            "click", 
            e.data, 
            e.data.editar
        )        
    }
    else {
        event_owner = $(e.relatedTarget) 

        if (event_owner.context.id == "boton_nuevo") {

            // Se modifica el titulo
            e.data.$id.find('.modal-title').text('Nueva Actividad')
            
            // Se asoscia el evento que se utilizara para guardar
            e.data.$boton_guardar.on(
                "click", 
                e.data, 
                e.data.nuevo
            )
        }        
    }
}
VentanaModal.prototype.clear_Fields = function () {

    this.$articulo.val("")
    this.$cantidad_estimada.val("")
}
VentanaModal.prototype.clear_Estilos = function () {
    
    this.$articulo_contenedor.removeClass("has-error")
    
    if(this.$articulo_mensaje.hasClass('hidden') != null) { 
        this.$articulo_mensaje.addClass('hidden')
    } 

    this.$cant_est_contenedor.removeClass("has-error")  

    if(this.$cant_est_mensaje.hasClass('hidden') != null) { 
        this.$cant_est_mensaje.addClass('hidden')
    } 
}
VentanaModal.prototype.fill_Articulos = function () {

    // Obtenemos articulos
    $.ajax({
        url: url_articulos,
        data: {
            "estado" :  "ACT"
        },
        method: "GET",
        success: function (response) {

            


        },
        error: function (response) {
            
            alertify.error("Ocurrio error al consultar")
        }
    })    
}
VentanaModal.prototype.validar = function () {

    var bandera = true

    if ( this.$articulo.val() == "") {
        this.$articulo_contenedor.addClass("has-error")
        this.$articulo_mensaje.removeClass("hidden")
        bandera = false
    }

    if ( this.$cantidad_estimada.val() == "") {
        this.$cant_est_contenedor.addClass("has-error")
        this.$cant_est_mensaje.removeClass("hidden")
        bandera = false
    }

    return bandera
}
VentanaModal.prototype.nuevo = function (e) {

    if (e.data.validar()) {

        $.ajax({
            url: url_materiales,
            method: "POST",
            data: {
                "orden" :  url_ordenes + $ot_clave.text() + "/",
                "articulo" : e.data.$articulo.val(),
                "cantidad_estimada" : e.data.$cantidad_estimada.val(),
            },
            success: function (response) {

                targeta_resultados.grid.kfuente_datos.read()

                // Ocultar Modal
                e.data.$id.modal('hide')

            },
            error: function (response) {

                alertify.error("Ocurrio error agregar Actividad")
            }
        })
    }
}
VentanaModal.prototype.editar = function (e) {

    if (e.data.validar()) {

        var url_update = url_materiales + e.data.$pk.val() + "/"

        $.ajax({
            url: url_update,
            method: "PUT",
            data: {
                "orden" :  url_ordenes + $ot_clave.text() + "/",
                "articulo" : e.data.$articulo.val(),
                "cantidad_estimada" : e.data.$cantidad_estimada.val(),
            },
            success: function (response) {

                targeta_resultados.grid.kfuente_datos.read()

                e.data.$id.modal('hide')
            },
            error: function (response) {

                alertify.error("Ocurrio error al modificar registro")
            }
        })
    }
}
