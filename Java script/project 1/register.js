let submit=document.getElementById("sub");
let frm1=document.getElementById("form1");
submit.onclick =(e) =>
{
 let namee=document.getElementById("unamee").value;
 let pass=document.getElementById("passs").value;
 let uservalid=false;
 let passvalid=false;
 let msgs=[];
 if(namee!=="")
 {
    uservalid=true;
 }
 else
 {
  msgs.push("wrong user name");
 }
 if(pass!=="" &&pass.length>=6)
 {
    passvalid=true;
 }
 else{
    msgs.push("wrong password format");
 }
 if(msgs.length>0)
 {
   let p= msgs.join(', ');
   alert(p);
 }
 if (uservalid === false || passvalid === false)
{
    e.preventDefault();
}
else{
localStorage.setItem("username",namee);
localStorage.setItem("password",pass);
document.getElementById("unamee").value = "";
document.getElementById("passs").value = "";
window.location.href="index.html";
}
}