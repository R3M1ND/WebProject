//-----------------------JSON----------------
/*const data = { //JSON 
    "firstName" : "J0ohn",
//value and keys
//เก็บออปเจคในออปเจคก็ได้
    "address" : 
    {   
        "city" : "Vakanda"
    },
    "lastName" : "Young"
}
console.log(data.firstName)
//console.log(data.phone[0].type) <- ใช้กับ Array 

//--------------function---------------
function num()
{

}

let myFunc = function()
{

}
//Arrow function
let myFunc2 = () =>
{
    
}
let myFunc3 = num =>
{

}

console.log(function() {return "Hello"})
console.log(num => {}) //Arrow

*/
const apiUrl = " https://pokeapi.co/api/v2/pokemon/"
let input_id = document.querySelector('.input-id');
let pokemon_img = document.querySelector('.pokemon-img');
let name_pokemon = document.querySelector('.name-pokemon');
let gender_pokemon = document.querySelector('.gender-pokemon');

function getdata()
{
    axios.get(apiUrl + input_id.value).then(function(response)
    {   
        name_pokemon.innerHTML = response.data.forms[0].name;    
        pokemon_img.src = response.data.sprites.front_default;  
        gender_pokemon.innerHTML = response.data.baby_trigger_item;
    })
    .catch(function(error)
    {
        name_pokemon.innerHTML = "ERROR"
        pokemon_img.src = "";
        gender_pokemon.innerHTML = "ERROR"
    })
}

let button_submit = document.querySelector('.button-submit');
button_submit.addEventListener('click',getdata); 