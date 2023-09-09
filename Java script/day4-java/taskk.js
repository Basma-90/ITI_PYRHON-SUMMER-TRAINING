let openWindowBtn = document.getElementById("btn"); // Button that opens the window
let nameInput = document.getElementById("name");
let ageInput = document.getElementById("age");
let submitBtn = document.getElementById("btnn"); // Submit button in the form

openWindowBtn.onclick = () => {
  let b = window.open("", "_blank", "width=200,height=200");
  b.document.write("basma sabry");
  let imgg = document.createElement("img");
  imgg.src = "images44.jpeg";
  b.document.body.appendChild(imgg);
  let p = document.createElement("p");
  p.innerText = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Lorem ipsum dolor sit amet, consectetur adipiscing elit.";
  b.document.body.appendChild(p);

  b.onload = () => {
    setInterval(() => {
      b.scrollTo(0, 200);
    }, 9000);
  };
  setTimeout(() => {
    b.scrollTo(0, 200);
  }, 9000);

  if (b && !b.closed) {
    b.close();
  }
};
/////////////////////////////////////
let imggs=document.images;
let immgs2=document.body.childNodes;  // indexed list from which i can reach images
let imgg3=document.querySelector("img");
/////////////////
let ops=document.getElementsByTagName("option");
let ops2=document.querySelectorAll("#mySelect option");
/////////////////////////////
let td=document.getElementsByTagName("td");
let td2=document.querySelectorAll("#table1 td")
///////////////////////////////
let ele=document.getElementsByClassName(".fontBlue.Bgrey")
////date
function updateTitle()
{
  let now= new Date();
  document.title=now.toLocaleString();
}
setInterval(updateTitle,1000);
submitBtn.onclick = () => {
  console.log(nameInput.value);
  console.log(ageInput.value);
};
