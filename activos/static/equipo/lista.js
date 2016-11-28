/*-----------------------------------------------*\
            GLOBAL VARS
\*-----------------------------------------------*/

var url_grid = window.location.origin + "/api/equipos/"
var url_nuevo = window.location.origin + "/equipos/nuevo/"
var url_editar = window.location.origin + "/equipos/editar/"
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

	this.targetaFiltros = new TargetaFiltros()
	this.grid_principal = new GridPrincipal()
}
// Pagina.prototype.set_PageActive = function () {


// }

/*-----------------------------------------------*\
            OBJETO: FILTROS
\*-----------------------------------------------*/

function TargetaFiltros() {

	this.$tag = $('#id_tag')
	this.$serie = $('#id_serie')
	this.$estado = $('#id_estado')
	this.$empresa = $('#id_empresa')
	this.$padre = $('#id_padre')
	this.$sistema = $('#id_sistema')
	this.$ubicacion = $('#id_ubicacion')
	this.$descripcion = $('#id_descripcion')

	this.init()
}
TargetaFiltros.prototype.init = function () {
	this.$empresa.select2();
    this.$padre.select2();
    this.$ubicacion.select2();
}

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
		tag: { type: "string" },
		descripcion: { type: "string" },
		serie: { type: "string" },
		tipo: { type: "string" },
		estado: { type: "string" },
		padre: { type: "string" },
		empresa: { type: "string" },
		sistema: { type: "string" },
		ubicacion: { type: "string" },
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
			alert("Valio gaver")
        },
    })

    this.kColumns = [
		{ field: "tag" , title: "tag", width: "120px" },
		{ field: "descripcion" , title: "descripcion", width: "120px" },
		{ field: "serie" , title: "serie", width: "120px" },
		{ field: "tipo" , title: "tipo", width: "120px" },
		{ field: "estado" , title: "estado", width: "120px" },
		{ field: "padre" , title: "padre", width: "120px" },
		{ field: "empresa" , title: "empresa", width: "120px" },
		{ field: "sistema" , title: "sistema", width: "120px" },
		{ field: "ubicacion" , title: "ubicacion", width: "120px" },
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
        toolbar: [
            { template: kendo.template($("#template").html()) }
        ],
    })

    this.kGrid.data("kendoGrid").resize()
}
GridPrincipal.prototype.nuevo = function (e) {
    window.location.href = url_nuevo
}
GridPrincipal.prototype.editar = function (e) {

    e.preventDefault()
    var fila = this.dataItem($(e.currentTarget).closest('tr'))
    window.location.href = url_editar + fila.pk;
}


