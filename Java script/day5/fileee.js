let img = document.getElementsByTagName("img")[0];
let btnLeft = document.getElementById("left");
let btnRight = document.getElementById("right");
let stopbtn=document.getElementById("stop");
let startbtn=document.getElementById("start");
let name=document.getElementById("nam");
let age=document.getElementById("ag");
let btnadd=document.getElementById("btn3");
let btndel=document.getElementById("btn4");
let settime;
let imgArr = ["images.jpeg", "images2.jpeg", "images3.jpeg", "Untitled.jpeg","images4.jpeg"];
let count = 0;
img.src = imgArr[count];
btnRight.onclick = () =>
{
   if(count>=imgArr.length)
   {
    count=0;
   }
   img.src=imgArr[count++];
}
btnLeft.onclick = () =>
{
    if(count<=0)
    {
        count=imgArr.length-1;
    }
    img.src=imgArr[count--];
}
startbtn.onclick = () =>
{
    settime = setInterval(() => {
        btnRight.click(); 
    }, 3000); 
}
stopbtn.onclick = () =>
{
  clearInterval(settime);
};
let inputs=document.getElementsByClassName("input");
btnadd.onclick= () =>
{
if(isNaN(inputs[0].value)&&isFinite(inputs[1].value))
{
let tr1=document.createElement("tr");
for(let i=0;i<inputs.length;i++)
{
    let td=document.createElement("td");
    td.innerText=inputs[i].value;
    tr1.appendChild(td);
}
let td2=document.createElement("td");
tr1.appendChild(btndel);
document.getElementById("table1").children[1].appendChild(tr1);
}
else
{
   alert("invalid input!");s                      
}
}
btndel.onclick= (event) =>
{
    const button = event.target; 
    const row = button.closest("tr"); 
    if (row) {
        row.remove();
    }
}

