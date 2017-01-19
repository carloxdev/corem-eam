/*-----------------------------------------------*\
            GLOBAL VARIABLES
\*-----------------------------------------------*/


// URLS
var url_servicios = window.location.origin + "/api/servicioexterno/"
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
    this.modal = new VentanaModal()
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
        descripcion : { type: "string" },
        clave_jde : { type:"string" },        
        comentarios: { type:"string" },
    }
}
GridPrincipal.prototype.get_Columnas = function (e) {

    return [
        { field: "descripcion", title: "Descripcion" },
        { field: "clave_jde", title: "Clave JDE", width: "150px" },
        { field: "comentarios", title: "Comentarios", format: '{0:n2}' },
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
                url: url_servicios,
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
    targeta_resultados.modal.set_Id(fila.pk)
    targeta_resultados.modal.mostrar()
}
GridPrincipal.prototype.click_BotonEliminar = function (e) {

    e.preventDefault()
    var fila = this.dataItem($(e.currentTarget).closest('tr'))

    alertify.confirm(
        'Eliminar Registro',
        '¿Desea Eliminar este registro?', 
        function () {

            var url = url_servicios + fila.pk + "/"

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

    this.$pk = $("#modal_record_id")

    this.$desc =  $('#mod_desc')
    this.$desc_contenedor =  $('#mod_desc_contenedor')
    this.$desc_mensaje =  $('#mod_desc_mensaje')

    this.$clave_jde = $('#mod_clavejde')
    this.$clave_jde_contenedor = $('#mod_clavejde_contenedor')
    this.$clave_jde_mensaje =  $('#mod_clavejde_mensaje')    

    this.$comments = $('#mod_comments')
    this.$comments_contenedor = $('#mod_comments_contenedor')
    this.$comments_mensaje =  $('#mod_comments_mensaje')

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
VentanaModal.prototype.clear_Fields = function () {

    this.$desc.val("")
    this.$clave_jde.val("")
    this.$comments.val("")
}
VentanaModal.prototype.clear_Estilos = function () {
    
    this.$desc_contenedor.removeClass("has-error")
    if(this.$desc_mensaje.hasClass('hidden') != null) { 
        this.$desc_mensaje.addClass('hidden')
    }
}
VentanaModal.prototype.validar = function () {

    var bandera = true

    if ( this.$desc.val() == "") {
        this.$desc_contenedor.addClass("has-error")
        this.$desc_mensaje.removeClass("hidden")
        bandera = false
    }

    return bandera
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
        e.data.$id.find('.modal-title').text('Editar Servicio')

        // Se busca el registro y se llenan los controles
        modal = e.data

        $.ajax({
            url: url_servicios,
            method: "GET",
            data: {
                "id": e.data.$pk.val()
            },
            success: function (response) {

                modal.$desc.val(response[0].descripcion)
                modal.$clave_jde.val(response[0].clave_jde)                
                modal.$comments.val(response[0].comentarios)
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
            e.data.$id.find('.modal-title').text('Nuevo Servicio')
            
            // Se asoscia el evento que se utilizara para guardar
            e.data.$boton_guardar.on(
                "click", 
                e.data, 
                e.data.nuevo
            )
        }        
    }
}
VentanaModal.prototype.nuevo = function (e) {

    if (e.data.validar()) {

        $.ajax({
            url: url_servicios,
            method: "POST",
            data: {
                "orden" :  url_ordenes + $ot_clave.text() + "/",
                "descripcion" : e.data.$desc.val(),
                "clave_jde" : e.data.$clave_jde.val(),
                "comentarios" : e.data.$comments.val(),
            },
            success: function (response) {

                alertify.success("Registro exitosamente guardado")

                targeta_resultados.grid.kfuente_datos.read()

                // Ocultar Modal
                e.data.$id.modal('hide')

            },
            error: function (response) {

                if (response.readyState == 4 && response.status == 500) {
                    alertify.error("El registro ya existe en la BD")
                }
                else {
                    alertify.error("Ocurrio error al modificar registro")
                }
            }
        })
    }
}
VentanaModal.prototype.editar = function (e) {

    if (e.data.validar()) {

        var url_update = url_servicios + e.data.$pk.val() + "/"

        $.ajax({
            url: url_update,
            method: "PUT",
            data: {
                "orden" :  url_ordenes + $ot_clave.text() + "/",
                "descripcion" : e.data.$desc.val(),
                "clave_jde" : e.data.$clave_jde.val(),
                "comentarios" : e.data.$comments.val(),
            },
            success: function (response) {

                alertify.success("Registro exitosamente guardado")

                targeta_resultados.grid.kfuente_datos.read()

                e.data.$id.modal('hide')
            },
            error: function (response) {

                if (response.readyState == 4 && response.status == 500) {
                    alertify.error("El registro ya existe en la BD")
                }
                else {
                    alertify.error("Ocurrio error al modificar registro")
                }
            }
        })
    }
}
