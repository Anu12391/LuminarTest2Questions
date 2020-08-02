var name=prompt("enter the name");
var num1 = Number(prompt("enter first subject marks"));
var num2 = Number(prompt("enter second subject marks"));
var num3 = Number(prompt("enter third subject marks"));
var total = num1+num2+num3;

if (total >= 145){
   alert(name+ "Your total is"+total+"and grade is a+");
   }
else{
   if(total>=140){
      alert("Your total is"+total+"and grade is a");
      }
   else{
      if(total>=135){
          alert("Your total is"+total+"and grade is b+");
          }
       else if(total>=130){
          alert("Your total is"+ total+ "and grade is b");
          }
     else{       alert("Your total is"+ total+ "you failed");
     }
//
}
        }



























