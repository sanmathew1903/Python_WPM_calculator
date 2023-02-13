var clickcount=0;
function func()
{
    alert("you are about to get fucked");
    
    var c=document.getElementById("headbar");            
    c.innerHTML="";
    
    document.getElementById("best").innerHTML="<b><h1 style='font-size:10vw'>fuck you</h1></b><img src='funny-middle.gif'> <figcaption>Congratulations you have been fucked</figcaption>";
}

function login()
{
    var c="jk";
    c=document.getElementById("loginname").value;
    alert(c);
    
}
function openNav() 
{  
    clickcount++;
    if(clickcount%2==0)
    {
        
        document.getElementById("sidebar").style.width="0";
        document.getElementById("rightbar").style.width="100%";
        document.getElementById("rightbar").style.marginLeft="0%";                        
        
    }
    else
    {   
        /* document.getElementById("sidebar").style.position="fixed";   */ 
        document.getElementById("sidebar").style.width="20%";   
        document.getElementById("rightbar").style.width="80%";                        
        document.getElementById("rightbar").style.marginLeft="20%";                        
        
    }
}