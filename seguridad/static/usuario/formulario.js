/*-----------------------------------------------*\
            GLOBAL VARIABLES
\*-----------------------------------------------*/

// OBJS
var formulario = null


/*-----------------------------------------------*\
            LOAD
\*-----------------------------------------------*/

$(document).ready(function () {

    formulario = new TargetaFormulario() 
})


/*-----------------------------------------------*\
            OBJETO: Targeta Filtros
\*-----------------------------------------------*/

function TargetaFormulario() {

	this.$comentarios = $('#id_comentarios')
	this.$fecha_nacimiento = $('#id_fecha_nacimiento')
    this.$imagen = $('#id_imagen')
    this.$imagen_preview = $('#img_preview')

	this.init()
}
TargetaFormulario.prototype.init = function () { 
	
    this.$imagen.on("change",this, this.set_PreviewImagen)

	this.$comentarios.wysihtml5({
        toolbar: {
            "font-styles": true,
            "emphasis": true,
            "lists": true,
            "html": false,
            "link": false,
            "image": false,
            "color": false,
            "blockquote": false,
        }
    })

    this.$fecha_nacimiento.datepicker(
        {
            autoclose: true,
            language: 'es'
        }
    )	
}
TargetaFormulario.prototype.set_PreviewImagen = function (e) {

    if (this.files && this.files[0]) {
        
        var reader = new FileReader()

        reader.onload = function (e) {
            formulario.$imagen_preview.attr('src', e.target.result)
        }

        reader.readAsDataURL(this.files[0])

    }
}

