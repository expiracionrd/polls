function captura(){
    var votoSel = document.querySelector('formu');
    votoSel.addEventListener('submit'), function(){
        let error = false;

        if (!document.querySelector('input[name="elección"]:checked')) {
            alert('¡Debe seleccionar una de las opciones!');
            error = true;
        }

        if (error){
            Event.preventDefault();
            return false
        }

        console.log(document.querySelector('input[name="elección"]:checked').value);
        Event.preventDefault();

    }
}