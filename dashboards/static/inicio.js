 /*-----------------------------------------------*\
            GLOBAL VARIABLES
\*-----------------------------------------------*/

// URLS
var url_last_ordenes = window.location.origin + "/api/ordenestrabajolast/"

// OBJS
var last_ordenes = null
var calendar = null
var grafica_costos = null
var mensajes = null


/*-----------------------------------------------*\
            LOAD
\*-----------------------------------------------*/

$(document).ready(function () {

	last_ordenes = new ListOrdenes()
    calendar = new Calendario()
    grafica_costos = new GraficaCostos()
    mensajes = new Chat()
})

/*-----------------------------------------------*\
            OBJETO: ListOrdenes
\*-----------------------------------------------*/

function ListOrdenes() {

	this.$contenido = $('#tabla_contenido')

	this.init()
}
ListOrdenes.prototype.init = function () {

	// Consultamos Ordenes
    $.ajax({
        url: url_last_ordenes,
        method: "GET",
        context: this,
        success: function (response) {
        	this.fill_Contenido(response)
        },
        error: function (response) {
            
            alertify.error("Ocurrio error al consultar las ultimas ordenes")
        }
    })
}
ListOrdenes.prototype.fill_Contenido = function (_data) {

	var tabla_contenio = this.$contenido

	$.each(_data, function (i, item) {

		var url_editar_orden = tabla_contenio.data("ordenes")
		var url_editar_equipo = tabla_contenio.data("equipos")

		var url_ordenes = url_editar_equipo.replace("0", item.pk)
		var url_equipos = url_editar_equipo.replace("0", item.equipo_id)

		var clase_estado = ""

		if (item.estado == "ABIERTA") {
			clase_estado = "label-success"
		}
		else if (item.estado == "TERMINADA") {
			clase_estado = "label-info"
		}
		else if (item.estado == "CERRADA") {
			clase_estado = "label-default"
		}
		else if (item.estado == "PENDIENTE") { 
			clase_estado = "label-warning"
		}

		var elemento = "<tr>" +
			"<td><a href='#'>clave</a></td>".replace("clave", item.pk).replace('#', url_ordenes) +
			"<td>descripcion</td>".replace("descripcion", item.descripcion) +
			"<td><a href='#'>equipo</a></td>".replace("equipo", item.equipo).replace('#', url_equipos) +
			"<td><span class='label label-color'>estado</span></td>".replace("estado", item.estado).replace("label-color", clase_estado) +
		"</tr>"

		tabla_contenio.append(elemento)
	})
}


/*-----------------------------------------------*\
            OBJETO: GraficaCostos
\*-----------------------------------------------*/


function GraficaCostos() {

	this.$id = $("#salesChart")

	this.init()
}
GraficaCostos.prototype.init = function () {

	//-----------------------
	//- MONTHLY SALES CHART -
	//-----------------------

	// Get context with jQuery - using jQuery's .get() method.
	var salesChartCanvas = this.$id.get(0).getContext("2d");
	// This will get the first returned node in the jQuery collection.
	var salesChart = new Chart(salesChartCanvas);

	var salesChartData = {
	labels: ["January", "February", "March", "April", "May", "June", "July"],
	datasets: [
	  {
	    label: "Electronics",
	    fillColor: "rgb(210, 214, 222)",
	    strokeColor: "rgb(210, 214, 222)",
	    pointColor: "rgb(210, 214, 222)",
	    pointStrokeColor: "#c1c7d1",
	    pointHighlightFill: "#fff",
	    pointHighlightStroke: "rgb(220,220,220)",
	    data: [65, 59, 80, 81, 56, 55, 40]
	  },
	  {
	    label: "Digital Goods",
	    fillColor: "rgba(60,141,188,0.9)",
	    strokeColor: "rgba(60,141,188,0.8)",
	    pointColor: "#3b8bba",
	    pointStrokeColor: "rgba(60,141,188,1)",
	    pointHighlightFill: "#fff",
	    pointHighlightStroke: "rgba(60,141,188,1)",
	    data: [28, 48, 40, 19, 86, 27, 90]
	  }
	]
	};

	var salesChartOptions = {
	//Boolean - If we should show the scale at all
	showScale: true,
	//Boolean - Whether grid lines are shown across the chart
	scaleShowGridLines: false,
	//String - Colour of the grid lines
	scaleGridLineColor: "rgba(0,0,0,.05)",
	//Number - Width of the grid lines
	scaleGridLineWidth: 1,
	//Boolean - Whether to show horizontal lines (except X axis)
	scaleShowHorizontalLines: true,
	//Boolean - Whether to show vertical lines (except Y axis)
	scaleShowVerticalLines: true,
	//Boolean - Whether the line is curved between points
	bezierCurve: true,
	//Number - Tension of the bezier curve between points
	bezierCurveTension: 0.3,
	//Boolean - Whether to show a dot for each point
	pointDot: false,
	//Number - Radius of each point dot in pixels
	pointDotRadius: 4,
	//Number - Pixel width of point dot stroke
	pointDotStrokeWidth: 1,
	//Number - amount extra to add to the radius to cater for hit detection outside the drawn point
	pointHitDetectionRadius: 20,
	//Boolean - Whether to show a stroke for datasets
	datasetStroke: true,
	//Number - Pixel width of dataset stroke
	datasetStrokeWidth: 2,
	//Boolean - Whether to fill the dataset with a color
	datasetFill: true,
	//String - A legend template
	legendTemplate: "<ul class=\"<%=name.toLowerCase()%>-legend\"><% for (var i=0; i<datasets.length; i++){%><li><span style=\"background-color:<%=datasets[i].lineColor%>\"></span><%=datasets[i].label%></li><%}%></ul>",
	//Boolean - whether to maintain the starting aspect ratio or not when responsive, if set to false, will take up entire container
	maintainAspectRatio: true,
	//Boolean - whether to make the chart responsive to window resizing
	responsive: true
	};

	//Create the line chart
	salesChart.Line(salesChartData, salesChartOptions);

	//---------------------------
	//- END MONTHLY SALES CHART -
	//---------------------------   
}

/*-----------------------------------------------*\
            OBJETO: Chat
\*-----------------------------------------------*/

function Chat() {

	this.$id = $('#chat-box')

	this.init()
}
Chat.prototype.init = function () {

	this.$id.slimScroll({
	    height: '547px'
	})
}


/*-----------------------------------------------*\
            OBJETO: Calendario
\*-----------------------------------------------*/

function Calendario() {

  this.$id = $("#calendar")

  this.init()
}
Calendario.prototype.init = function () {

	this.$id.fullCalendar({
      header: {
        left: 'prev,next today',
        center: 'title',
        right: 'month,agendaWeek,agendaDay'
      },
      buttonText: {
        today: 'today',
        month: 'month',
        week: 'week',
        day: 'day'
      },
      editable: true,
    })
}
