
function calculate()
{
    var sumGrade = 0.0;
    var sumUnit = 0.0;
    var GPA = 0.0;
    var alertList = document.querySelectorAll('.alert')
   for(var i = 0;i<=10;i++)
   {
        var grade = document.getElementById("grade"+i).value;
        var unit = document.getElementById("unit"+i).value;
        unit = parseFloat(unit);
        if(grade === '' )
        {
            break;
        }
        grade = parseFloat(grade);
        sumGrade += grade*unit;
        sumUnit += unit; 
   }
   console.log("sumGrade: "+sumGrade);
   console.log("sumUnit: "+sumUnit);
   GPA = sumGrade/sumUnit;    
   console.log("GPA : "+GPA);
   if (!isNaN(GPA)) 
    { 
        document.getElementById("showGrade").innerHTML = GPA.toFixed(2); //ทศนิยม2ตำแหน่ง
    }
   
}

function del()
{
    for(var i = 0;i<=10;i++)
    {
        document.getElementById("subject"+i).value = '';
        document.getElementById("unit"+i).value = '1';
        document.getElementById("grade"+i).value = '';        
    }
    console.log("Clear ja e sus");
}
 