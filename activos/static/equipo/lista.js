/*-----------------------------------------------*\
            GLOBAL VARIABLES
\*-----------------------------------------------*/

var url_grid = window.location.origin + "/api/equipos/"
var url_nuevo = window.location.origin + "/equipos/nuevo/"
var url_editar = window.location.origin + "/equipos/editar/"
var url_anexos = window.location.origin + "/equipos/anexos/"
var targeta_filtros = null
var targeta_resultados = null


/*-----------------------------------------------*\
            LOAD
\*-----------------------------------------------*/

$(document).ready(function () {

	this.targeta_filtros = new TargetaFiltros()
    
    this.targeta_resultados = new TargetaResultados()
})



/*-----------------------------------------------*\
            OBJETO: Targeta Filtros
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
            OBJETO: Grid Principal
\*-----------------------------------------------*/

function TargetaResultados() {

    this.grid_principal = new GridPrincipal()
}


/*-----------------------------------------------*\
            OBJETO: Grid Principal
\*-----------------------------------------------*/

function GridPrincipal() {

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
        {
            command: {
                text: "Anexos",
                click: this.anexos,
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
GridPrincipal.prototype.anexos = function (e) {

    e.preventDefault()
    var fila = this.dataItem($(e.currentTarget).closest('tr'))
    id_equipo = fila.pk
    var id_input = document.createElement("INPUT");
    id_input.setAttribute("type", "hidden");
    id_input.setAttribute("value", id_equipo);
    window.location.href = url_anexos + id_input.value;


}

