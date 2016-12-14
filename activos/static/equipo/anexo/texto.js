/*-----------------------------------------------*\
            GLOBAL VARS
\*-----------------------------------------------*/

var url_grid = window.location.origin + "/api/anexo/equipo/texto/?equipo="
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
        clave: { type: "string"},
        descripcion: { type: "string" },
    }
}
GridPrincipal.prototype.get_Columnas = function (e) {

    return [      
        { field: "equipo" , title: "Equipo", width: "120px" },
        { field: "texto" , title: "Texto", width: "200px" },
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
           ],
           title: " ",
           width: "90px"
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
GridPrincipal.prototype.click_BotonEditar = function (e) {

    e.preventDefault()
    // TODO: Crear vista en el servidor para edición de anexos

}