class Engine
{
     source;
    constructor(source)
    {
        this.source=source;
        Engine.count++;
    }
    }
class car extends Engine
{
top;
constructor(left,top)
{
  super(left);
  this.top=top;
}
set top(value)
{
    this.top=value;
}
set left(value)
{
  this.source=left;
}
// get top()
// {
    // return this.top;
// }
// get left()
// {
    // return this.source;
// }
Mleft()
{
  this.source+=1;
} 
Mright()
{
  this.source-=1;
}
}
const my_instance=new car(12,10);
console.log(my_instance);
///////////////////////////////////////////
 (async function(){
 try{
    let data=await fetch("https://jsonplaceholder.typicode.com/users");
    let dJson=await data.json();
    let list=["username","email","company.name","address.geo.lat"];
    console.log(dJson);
    let cnt=0;
    for(let i=0;i<dJson.length;i++)
    {
      let tr=document.createElement("tr");
      for(let y=0;y<4;y++)
      {
        let td=document.createElement("td");
       // td.innerText=dJson[i].list[y];
       // tr.appendChild(td);
       let fieldPath = list[y].split('.');
       let value = dJson[i];
       for (let field of fieldPath) {
           value = value[field];
       }
       td.innerText = value;
       tr.appendChild(td);
      }
      document.getElementById("table1").children[1].appendChild(tr);
     }    
 }
 catch(error)
 {
    console.error("Error:", error);
 console.log("smth is wrong");
 }})()