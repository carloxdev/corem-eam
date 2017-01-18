/*-----------------------------------------------*\
            GLOBAL VARIABLES
\*-----------------------------------------------*/


// URLS
var url_actividades = window.location.origin + "/api/actividades/"
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
        numero : { type:"number" },
        descripcion : { type: "string" },
        horas_estimadas : { type:"number" },
        horas_reales: { type:"number" },
    }
}
GridPrincipal.prototype.get_Columnas = function (e) {

    return [
        { field: "numero", title: "Numero", width: "50px" },
        { field: "descripcion", title: "Descripcion", width: "200px" },
        { field: "horas_estimadas", title: "Horas Estimadas", width: "200px", format: '{0:n2}' },
        { field: "horas_reales", title: "Horas Reales", width: "200px", format: '{0:n2}' },
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
                url: url_actividades,
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
GridPrincipal.prototype.buscar =  function() {
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

            var url = url_actividades + fila.pk + "/"

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

    this.$pk = $("#id_actividad")

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
}
VentanaModal.prototype.set_Id = function (_value) {

    this.$pk.val(_value)
}
VentanaModal.prototype.mostrar = function (e) {
    this.$id.modal()
}
VentanaModal.prototype.load = function (e) {

    // Se eliminan eventos viejos
    e.data.$boton_guardar.off("click")

    // Se limpian estilos
    e.data.clear_Estilos()

    // Se limpiar el formulario
    e.data.clear_Fields()  

    // Asosciar Eventos segun corresponda
    var event_owner

    if ( e.relatedTarget == undefined ) {

        // Se modifica el titulo
        e.data.$id.find('.modal-title').text('Editar Actividad')

        // Se llenan los controles
        // var url = url_actividad + "?id=" + formulario.$udm.val()

        modal = e.data

        $.ajax({
            url: url_actividades,
            method: "GET",
            data: {
                "id": e.data.$pk.val()
            },
            success: function (response) {

                // modal.$pk.val(response[0].pk)
                modal.$numero.val(response[0].numero)
                modal.$descripcion.val(response[0].descripcion)
                modal.$hrs_est.val(response[0].horas_estimadas)
                modal.$hrs_real.val(response[0].horas_reales)
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
VentanaModal.prototype.nuevo = function (e) {

    if (e.data.validar()) {

        $.ajax({
            url: url_actividades,
            method: "POST",
            data: {
                "orden" :  url_ordenes + $ot_clave.text() + "/",
                "numero" : e.data.$numero.val(),
                "descripcion" : e.data.$descripcion.val(),
                "horas_estimadas" : e.data.$hrs_est.val(),
                "horas_reales" : e.data.$hrs_real.val(),
            },
            success: function (response) {

                alertify.success("Registro exitosamente guardado")

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

        var url_update = url_actividades + e.data.$pk.val() + "/"

        $.ajax({
            url: url_update,
            method: "PUT",
            data: {
                "orden" :  url_ordenes + $ot_clave.text() + "/",
                "numero" : e.data.$numero.val(),
                "descripcion" : e.data.$descripcion.val(),
                "horas_estimadas" : e.data.$hrs_est.val(),
                "horas_reales" : e.data.$hrs_real.val(),
            },
            success: function (response) {

                alertify.success("Registro exitosamente guardado")

                targeta_resultados.grid.kfuente_datos.read()

                e.data.$id.modal('hide')
            },
            error: function (response) {

                alertify.error("Ocurrio error al modificar registro")
            }
        })
    }
}
