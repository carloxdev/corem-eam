/*-----------------------------------------------*\
            GLOBAL VARIABLES
\*-----------------------------------------------*/

var url_datos = window.location.origin + "/equipos/arbol/json"
var tree = null


/*-----------------------------------------------*\
            LOAD
\*-----------------------------------------------*/

$(document).ready(function () {

    tree = new Arbol()
})


/*-----------------------------------------------*\
            OBJETO: Arbol
\*-----------------------------------------------*/

function Arbol() {

    this.$id = $("#tree")

    this.init()
}
Arbol.prototype.init = function () {

  $.ajax({
    url: url_datos,
    data: {},
    dataType: "json",
    type: "GET",
    contentType: "application/json; charset=utf-8",
    context: this,
    success: function (_respuesta) {  //--- Se establecio conexion con el servidor

      this.$id.treeview({
        data: _respuesta
      })
     
    },
    error: function (_respuesta) {
      alert("Fallo")
    }
    // this.FailRequest   //--- Fallo peticion al servidor
  })         
}