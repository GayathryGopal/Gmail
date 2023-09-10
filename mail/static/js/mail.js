function myfunction(){
var x=document.getElementById("d");
var y=document.getElementById("e");
if(x.type=="password" & y.type=="password"){
    x.type="text";
    y.type="text";

}
else{
    x.type="password"; 
    y.type="password";
}
}

 function next(){
    
    document.getElementById('sb').style.display='block'
     document.getElementById('sa').style.display='none'
     var a=document.getElementById('d').value
    var b=document.getElementById('e').value
    if(a!=b){
       document.getElementById('h').innerHTML="Password Incorrect";
    }
    else if(a!==10)
    {
         document.getElementById("h").innerHTML="invalid";
     }
 }
function flower(){
    
     document.getElementById('sc').style.display='block'
     document.getElementById('sb').style.display='none'
 }
function use(){
    var i=document.getElementById('d').value
    var j=document.getElementById('e').value
    if(i!=j){
       document.getElementById('h').innerHTML="Password Incorrect";
    }
    
     else if(i==j){
        document.getElementById("h").innerHTML="valid";
     }


}

function word(){
    var m=document.getElementById('x').value
    var n=document.getElementById('y').value
    if(m!=n){
        document.getElementById('z').innerHTML="invalid";
     }
     else if(m==n)
     {
          document.getElementById("z").innerHTML="correct";
      }
}

function passhow(){
    var x=document.getElementById("pas");
    
    if(x.type=="password" ){
        x.type="text";
        
    }
    else{
        x.type="password"; 
    }
}
function nextfun(){
    
    document.getElementById('spage').style.display='block'
    document.getElementById('fpage').style.display='none'

     
 }
 function compose(){
    
    document.getElementById('t1').style.display='block'
    document.getElementById('t2').style.display='none'
     
 }




// function color(){
//     var a=document.getElementById("star").value
//     if(a.style.color=="black"){
//         a.style.color="yellow"
//     }

// }


function changecolor(){
    document.getElementById("star").style.color = "black";
  
}
function animation(){
    document.getElementById('animationspage').style.display='block'
    document.getElementById('animationfpage').style.display='none'
  }

  function show1(){
    document.getElementById("forward").style.display='block'
    document.getElementById("frwd").style.display="none"
    document.getElementById("rply").style.display="none"
  }

  function show()
  {
     
      document.getElementById("reply").style.display="block"
      document.getElementById("rply").style.display="none"
      document.getElementById("frwd").style.display="none"
  }  
  
function subbuttn()
{
    location.href="regist.html"
}