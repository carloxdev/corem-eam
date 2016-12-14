/*-----------------------------------------------*\
            GLOBAL VARS
\*-----------------------------------------------*/

var url_grid = window.location.origin + "/api/anexo/equipo/imagen/?equipo="
var targeta_resultados = null

/*-----------------------------------------------*\
            LOAD
\*-----------------------------------------------*/

$(document).ready(function () {

    targeta_resultados = new TargetaResultados()
})


/*-----------------------------------------------*\
            OBJETO: RESULTADOS
\*-----------------------------------------------*/

function TargetaResultados() {

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

    this.kgrid = this.$id.kendoGrid({
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
            template: "<div class='grid-empy'> Sin Registros </div>"
        },
    })

    this.kgrid.data("kendoGrid").resize()
}
GridPrincipal.prototype.get_Campos = function (e) {

    return {
       
    }
}
GridPrincipal.prototype.get_Columnas = function (e) {

    return [      
        { field: "equipo" , title: "Equipo", width: "120px" },
        { field: "descripcion" , title: "Descripción", width: "120px"},
        {
           command: [
                {
                   text: "Editar",
                   click: this.click_BotonEditar,
                   className: "boton_editar"
                },
                {
                   text: "Eliminar",
                   click: this.click_BotonEliminar,
                   className: "boton_eliminar"
                },
                {
                   text: "Descargar",
                   click: this.click_BotonDescargar,
                   className: "boton_descargar"
                },
           ],
           title: " ",
           width: "120px"
        },
    ]
}
GridPrincipal.prototype.get_FuenteDatosConfig = function (e) {
    var id_equipo = $('#id_equipo').val()

    return {

        serverPaging: true,
        pageSize: 30,
        transport: {
            read: {

                url: url_grid+id_equipo,
                type: "GET",
                dataType: "json",
            },
            parameterMap: function (data, action) {
                if (action === "read") {

                    return {
                        page: data.page,
                        pageSize: data.pageSize,
                        
                    }
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
            alert("Valio gaver")
        },
    }
}
GridPrincipal.prototype.buscar =  function() {
  this.kfuente_datos.page(1)   
}
GridPrincipal.prototype.click_BotonEditar = function (e) {

    e.preventDefault()
    var fila = this.dataItem($(e.currentTarget).closest('tr'))
    console.log(fila);
    window.location.href = url_editar + fila.pk;
    e.preventDefault()
    var fila = this.dataItem($(e.currentTarget).closest('tr'))
    window.location.href = url_editar + fila.pk;
}
GridPrincipal.prototype.click_BotonEliminar = function (e) {

    e.preventDefault()
}
GridPrincipal.prototype.click_BotonDescargar = function (e) {

    e.preventDefault()
    //alert("descargar lel");
}


