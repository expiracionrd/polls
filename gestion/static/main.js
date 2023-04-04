let nombre = document.getElementById("your_name")
let cedula = document.getElementById("#your_id")
let compania = document.getElementById("#company")


console.log(nombre)
nombre.addEventListener("change",(e)=>{
    console.log(e.target.value)
})

//! Pendiente de verificación.
// Realizar función de comprobar los campos antes de hacer botón