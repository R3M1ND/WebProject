/*console.log("Hello Js");   //คล้ายๆ printf
alert("Hello Js");  //alert bar

//variable
var x = "Hello";   //var สามารถกำหนด type ได้เลย , ตั้งซ้ำได้
var x = 10;
console.log(x);

let x = 10;  //ใช้ไม่ได้ จะ error
let x = "Hello";
console.log(x);
const x = 10; 

{
    var x = 20; //ใช้ได้
    let x = 10; //ใช้ไม่ได้เพราะไม่ได้ประกาศไว้ด้านนอก
    const x = 10; // ใช้ไม่ได้เพราะไม่ได้ประกาศไว้ด้านนอก
}
console.log(x);

console.log(10**2); //is multiply

var x = "Hello";
var y = "Js";
console.log(x+y); //เอา string มาต่อกัน or เอา num หรือ string มาต่อกันก็ได้

//Boolean
var x =10;
var y = 10;
console.log(x==y); //true

var x =10;
var y = "10";
console.log(x==y); //true

var x =10;
var y = "10";
console.log(x===y); //false , เอา type มาเทียบด้วย 

//function
var x = 10;
var y = 10;

function sum(num1,num2)
{
    return num1+num2;
}
console.log(sum(50,70));

// Object
var x =
{
    num : 12345,
    num2 : "54321"
}
console.log(x.num);
console.log(x["num2"]);

//Event
function sum(num1,num2)
{
    alert(num1+num2);
}

// Array
var x = [10,20,30];
console.log(x[0]);

// Loop
var x = [];
for(var i = 0;i<10;i++)
{
    console.log(i);
}
var x =[10,20,30,40,50]
for(y in x) // for in = position of number ->0 1 2 3 4 
{
    console.log(y);
}
var x = [10,20,30,40,50] //for of = number -> 10 20 30 40 50
for(y of x)
{
    console.log(y);
}
*/
document.getElementById("h1").innerHTML = 5 + 6 , "<br>" , 7+1; //ใส่แท็กของhtmlได้