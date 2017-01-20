/*-----------------------------------------------*\
            GLOBAL VARIABLES
\*-----------------------------------------------*/

// URLS
var url_grid = window.location.origin + "/api/movimientosdetalle/"
var url_editar = window.location.origin + "/entradas/editar/"
var url_articulos = window.location.origin + "/api/articulos2/"


// OBJS
var targeta_filtros = null
var targeta_resultados = null
var modal_detalle = null
var pagina = null


/*-----------------------------------------------*\
            LOAD
\*-----------------------------------------------*/

$(document).ready(function () {

    targeta_filtros = new TargetaFormulario()
    targeta_resultados = new TargetaResultados()
    modal_detalle = new ModalDetalle()

    pagina = new Pagina()
    pagina.init_Alertify()    
})

/*-----------------------------------------------*\
            OBJETO: Targeta Filtros
\*-----------------------------------------------*/

function TargetaFormulario() {

    this.$id = $('#id_panel')
    this.$operacion = $('#operacion')
    this.$cabecera = $('#id_cabecera')
    this.$descripcion = $('#id_descripcion')
    this.$fecha = $('#id_fecha')
    this.$almacen_origen = $('#id_almacen_origen')
    this.$almacen_destino = $('#id_almacen_destino')
    this.$persona_recibe = $('#id_persona_recibe')
    this.$persona_entrega = $('#id_persona_entrega')
    this.$estado = $('#id_estado')
    this.$boton_guardar = $('#boton_guardar')

    this.init()
}
TargetaFormulario.prototype.init = function () {

    this.$almacen_origen.select2()
    this.$almacen_destino.select2()
    this.$fecha.datepicker(
        {
            autoclose: true,
            language: 'es'
        }
    )
    
}
TargetaFormulario.prototype.get_Filtros = function (_page, _pageSize) {

    return {
        page: _page,
        pageSize: _pageSize,
        cabecera: this.$cabecera.val(),

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
        dataBound: this.set_Icons,      
    }
}
GridPrincipal.prototype.get_Campos = function (e) {

    return {
        articulo_clave: { type: "string" },
        cantidad: { type: "string" },
        
    }
}
GridPrincipal.prototype.get_Columnas = function (e) {

    return [
        { field: "articulo_clave" , title: "Articulo", width: "120px" },
        { field: "cantidad" , title: "Cantidad", width: "120px" },
        
        
        {
           command: [ 
                {
                   text: " Eliminar",
                   click: this.click_BotonEliminar,
                   className: "boton_eliminar fa fa-trash-o"
                },   
                             
            ],           
           title: " ",
           width: "40px"
        },
    ]
}
GridPrincipal.prototype.set_Icons = function (e) {

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

GridPrincipal.prototype.click_BotonEliminar = function (e) {
    e.preventDefault()
    var fila = this.dataItem($(e.currentTarget).closest('tr'))
    
    alertify.confirm(
        'Eliminar Registro',
        '¿Desea eliminar esta fila?', 

        function () {

            var url = url_grid + fila.pk + "/"

            $.ajax({
                url: url,
                method: "DELETE",
                success: function () {
                    alertify.success("Se eliminó registro correctamente")

                    targeta_resultados.grid.kfuente_datos.remove(fila)
                    
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
    this.$boton_nuevo = $('#boton_nuevo')
    this.$boton_exportar = $("#boton_exportar")

    this.init()
}
Toolbar.prototype.init = function (e) {

    this.$boton_nuevo.on("click", this, this.click_BotonNuevo)
    this.$boton_exportar.on("click", this, this.click_BotonExportar)
}

Toolbar.prototype.click_BotonExportar = function(e) {
    e.preventDefault()
    return null
}

Toolbar.prototype.click_BotonNuevo = function (e) {

    e.preventDefault()
    $('#modal_nuevo').modal('show');
}

function ModalDetalle() {

    this.$id = $('#modal_nuevo')
    this.$cabecera = $('#cabecera')
    this.$articulo = $('#id_articulo')
    this.$cantidad = $('#id_cantidad')
    this.$boton_guardar = $('#boton_guardar_detalle')
    this.$articulo_contenedor = $('#articulo_contenedor')
    this.$articulo_mensaje = $('#articulo_mensaje')
    this.$cantidad_contenedor = $('#cantidad_contenedor')
    this.$cantidad_mensaje = $('#cantidad_mensaje')

    this.init()

}

ModalDetalle.prototype.init = function () {
    this.$articulo.select2()
    this.$boton_guardar.on("click", this, this.click_BotonGuardar)
    this.$id.on('show.bs.modal', this, this.load)
    this.load_articulos()

}
ModalDetalle.prototype.load = function (e) {

    e.data.clear_Estilos()
    e.data.clear_Fields()
}
ModalDetalle.prototype.clear_Estilos = function () {

    this.$articulo_contenedor.removeClass("has-error")

    if(this.$articulo_mensaje.hasClass('hidden') != null) { 
        this.$articulo_mensaje.addClass('hidden')
    } 

    this.$cantidad_contenedor.removeClass("has-error")  

    if(this.$cantidad_mensaje.hasClass('hidden') != null) { 
        this.$cantidad_mensaje.addClass('hidden')
    } 
}
ModalDetalle.prototype.clear_Fields = function () {

    this.$articulo.val("").trigger('change')
    this.$cantidad.val("")
}
ModalDetalle.prototype.load_articulos = function () {
    var csrftoken = $("[name=csrfmiddlewaretoken]").val()
         $.ajax(
            {
                url: url_articulos,
                headers: { "X-CSRFToken": csrftoken },
                data: function (params) {
                      return {
                        id: params.id,
                        clave: params.clave,
                        descripcion: params.descripcion

                      }
                    },
                dataType:"json",
                type:"GET"
            }
        ).done(function(data)
            {
                $.each(data, function(index, item) 
                    {
                        $('#id_articulo').append($('<option>').attr('value',item.pk).text(item.clave+"–"+item.descripcion))
                    }
                )
                        
            }
        )
    

}
ModalDetalle.prototype.validar = function () {
    var bandera = true

    if ( this.$articulo.val() == "") {
        this.$articulo_contenedor.addClass("has-error")
        this.$articulo_mensaje.removeClass("hidden")
        bandera = false
    }

    if ( this.$cantidad.val() == "") {
        this.$cantidad_contenedor.addClass("has-error")
        this.$cantidad_mensaje.removeClass("hidden")
        bandera = false
    }

    return bandera
}

ModalDetalle.prototype.click_BotonGuardar = function (e) {
    if (e.data.validar()){

        articulo = e.data.$articulo.val()
        cantidad = e.data.$cantidad.val()
        cabecera = e.data.$cabecera.val()

        var csrftoken = $("[name=csrfmiddlewaretoken]").val()
        $.ajax({
                    headers: { "X-CSRFToken": csrftoken },
                    url: url_grid,
                    method: "POST",
                    data: {
                        cantidad: cantidad,
                        articulo: articulo,
                        cabecera: cabecera,
                    },
                    success: function (){
                        e.data.$id.modal('hide')
                        alertify.success("Detalle Registrado")
                        targeta_resultados.grid.kfuente_datos.read();
                       
                    },
                    error: function(e){

                        alertify.error("Error "+ e.status + " . No se guardó el registro")
                        e.data.$id.modal('hide')

                    }
                   
                            
                });

    }
}