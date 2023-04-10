let nombre = document.getElementById("your_name")
let cedula = document.getElementById("#your_id")
let compania = document.getElementById("#company")


nombre.addEventListener("change",(e)=>{
    const result = document.querySelector(".result");
    result.textContent ='You like ${Event.target}';
    
    console.log(e.target.value)
})

//! Pendiente de verificación.
// Realizar función de comprobar los campos antes de hacer botón