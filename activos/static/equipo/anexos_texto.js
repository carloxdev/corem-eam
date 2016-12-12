/*-----------------------------------------------*\
            GLOBAL VARS
\*-----------------------------------------------*/

var url_grid = window.location.origin + "/api/equipos/anexos/texto/"
var url_editar = window.location.origin + "/ubicaciones/editar/"
var pagina = null


/*-----------------------------------------------*\
            LOAD
\*-----------------------------------------------*/

$(document).ready(function () {

    pagina = new Pagina()

})

// $(window).resizable


/*-----------------------------------------------*\
            OBJETO: PAGINA
\*-----------------------------------------------*/

function Pagina() {

    this.grid_principal = new GridPrincipal()
}
// Pagina.prototype.set_PageActive = function () {


// }


/*-----------------------------------------------*\
            OBJETO: GRID
\*-----------------------------------------------*/

function GridPrincipal(_id) {

    this.$id = $("#grid_principal")
    this.kFields = null
    this.kFuenteDatos = null
    this.kColumns = null
    this.kGrid = null

    this.init()
}
GridPrincipal.prototype.init = function () {

    kendo.culture("es-MX")

    this.kFields = {
        texto: { type: "string"},
        equipo: { type: "string" },
    }


    this.kFuenteDatos = new kendo.data.DataSource({

        serverPaging: true,
        pageSize: 30,
        transport: {
            read: {

                url: url_grid,
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
                fields: this.kFields    
            }
        },
        error: function (e) {
            // alertify.notify("Status: " + e.status + "; Error message: " + e.errorThrown)
            alert("Error")
        },
    })

    this.kColumns = [
        { field: "texto" , title: "texto", width: "120px" },
        { field: "equipo" , title: "equipo", width: "120px" },
        {
           command: {
               text: "Editar",
               click: this.editar,
           },
           title: " ",
           width: "110px"
        },        
    ]    


    this.kGrid = this.$id.kendoGrid({
        dataSource: this.kFuenteDatos,
        columnMenu: false,
        groupable: false,
        sortable: false,
        editable: false,
        resizable: true,
        selectable: true,
        scrollable: false,
        columns: this.kColumns,
        scrollable: true,
        pageable: true,
        
    })

    this.kGrid.data("kendoGrid").resize()
}
GridPrincipal.prototype.nuevo = function (e) {
    window.location.href = url_nuevo
}
GridPrincipal.prototype.editar = function (e) {

    e.preventDefault()
    var fila = this.dataItem($(e.currentTarget).closest('tr'))
    console.log(fila);
    window.location.href = url_editar + fila.pk;
}
