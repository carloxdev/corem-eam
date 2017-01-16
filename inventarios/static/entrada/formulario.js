/*-----------------------------------------------*\
            GLOBAL VARIABLES
\*-----------------------------------------------*/

// URLS
var url_grid = window.location.origin + "/api/entradasdetalle/"
var url_articulos = window.location.origin + "/api/articulosform/"
var url_editar = window.location.origin + "/entradas/editar/"

// OBJS
var targeta_filtros = null
var targeta_resultados = null
var pagina = null


/*-----------------------------------------------*\
            LOAD
\*-----------------------------------------------*/

$(document).ready(function () {

    targeta_filtros = new TargetaFormulario()
    targeta_resultados = new TargetaResultados()
    targeta_detalle = new TargetaDetalle()

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

function TargetaFormulario() {

    this.$id = $('#id_panel')
    this.$cabecera = $('#id_cabecera')
    this.$clave = $('#id_clave')
    this.$descripcion = $('#id_descripcion')
    this.$fecha = $('#id_fecha')
    this.$almacen = $('#id_almacen')
    this.$boton_guardar = $('#boton_guardar')

    this.init()
}
TargetaFormulario.prototype.init = function () {

    this.$almacen.select2()
    this.$fecha.datepicker(
        {
            autoclose: true,
            language: 'es'
        }
    )

    if(this.$cabecera.val() != 0){
        this.$clave.attr("disabled", true)
        this.$descripcion.attr("disabled", true)
        this.$fecha.attr("disabled", true)
        this.$almacen.attr("disabled", true)
        this.$boton_guardar.attr("disabled", true)
    }
    
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
GridPrincipal.prototype.click_BotonEditar = function (e) {

    e.preventDefault()
    var fila = this.dataItem($(e.currentTarget).closest('tr'))
    window.location.href = url_editar + fila.pk + "/"
}


/*-----------------------------------------------*\
            OBJETO: TOOLBAR
\*-----------------------------------------------*/

function Toolbar() {

    this.$boton_exportar = $("#boton_exportar")

    this.init()
}
Toolbar.prototype.init = function (e) {

    this.$boton_exportar.on("click", this, this.click_BotonExportar)
}

Toolbar.prototype.click_BotonExportar = function(e) {
    e.preventDefault()
    return null
}

function TargetaDetalle() {
    this.$cabecera = $('#cabecera')
    this.$articulo = $('#id_articulo')
    this.$cantidad = $('#id_cantidad')
    this.$boton_guardar = $('#boton_guardar_detalle')
    this.$articulo_contenedor = $('#articulo_contenedor')
    this.$articulo_mensaje = $('#articulo_mensaje')
    this.$cantidad_contenedor = $('#cantidad_contenedor')
    this.$cantidad_mensaje = $('#cantidad_mensaje')

    this.init()

    this.$boton_guardar.on("click", this, this.click_BotonGuardar)
}

TargetaDetalle.prototype.init = function () {
    var csrftoken = $("[name=csrfmiddlewaretoken]").val()
    this.$articulo.select2(
        { 
            language: "es",
        }
    )

     $.ajax(
        {
            url: url_articulos,
            headers: { "X-CSRFToken": csrftoken },
            data: function (params) {
                  return {
                    id: params.id, // search term
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
                    $("#id_articulo").append($('<option>').attr('value',item.pk).text(item.clave+"–"+item.descripcion))
                }
            )
                    
        }
    )  

}

TargetaDetalle.prototype.click_BotonGuardar = function (e) {
    e.preventDefault()
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
                    articulo: 1,
                    cabecera: cabecera,
                },
                success: function (){
                    alertify.success("Detalle Registrado")
                    targeta_resultados.grid.kfuente_datos.read();
                   
                },
                error: function(e){

                    alertify.error("Error "+ e.status + " . No se guardó el registro")
                }
               
                        
            });

}