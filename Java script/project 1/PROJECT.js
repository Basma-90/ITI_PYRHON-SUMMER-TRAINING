let img = document.getElementsByTagName("img")[0];
let btnLeft = document.getElementById("left");
let btnRight = document.getElementById("right");
let unm=document.getElementById("namm");
(async function()
{
    try
    {
        let data=await fetch("https://dummyjson.com/products");
        let djson=await data.json();
        let product=djson.products;
        let imgs=product[0].images;
        console.log(product.length);
        console.log(imgs);
        let cards=document.getElementsByClassName("cards")[0];
        for(let i=0;i<product.length;i++)
        {
            let divv=document.createElement('div');
            divv.classList.add('product');
            let h5=document.createElement('h5');
            h5.innerText=product[i].title;
            let p=document.createElement('p');
            p.classList.add('des');
            p.innerText=product[i].description;
            let p2=document.createElement('p');
            p2.innerText= `$${product[i].price.toFixed(2)}`; 
            p2.classList.add("price");
            let p3=document.createElement('p');
            p3.classList.add('brand');
            p3.innerText=product[i].brand;
            let divv2=document.createElement('div');
            divv2.classList.add("pictures");
            let imagess=product[i].images;
            let imge=document.createElement("img");
            let btnl=document.createElement("button");
            btnl.classList.add('btnl');
            let leftArrow = document.createTextNode('<');
            btnl.appendChild(leftArrow);
            let btnr=document.createElement("button");
            let rightArrow = document.createTextNode('>');
            btnr.appendChild(rightArrow);
            btnr.classList.add("btnr");
            divv.appendChild(btnr);
            imge.classList.add('picimg');
            imge.src=imagess[0];  
            divv2.appendChild(imge);
            divv.appendChild(divv2);
            divv.appendChild(btnl);
            let count=0;
            btnr.onclick = () =>
             {
                if(count>=imagess.length)
                {
                 count=0;
                }
                imge.src=imagess[count++];
             }
             btnl.onclick = () =>
             {
                 if(count<=0)
                 {
                     count=imagess.length-1;
                 }
                 imge.src=imagess[count--];
             }
             let discele=document.createElement('p');
             discele.classList.add("disc");
             let money=product[i].discountPercentage/100;
             let total=money*product[i].price;
             let final=product[i].price-total;
             discele.innerText=`$${final.toFixed(2)}`;
             let b=document.createElement('b');
             b.setAttribute("id","starcont");
             let span2=document.createElement("span");
             span2.setAttribute("id","stars");
             function getStars(rating) {

                // Round to nearest half
                rating = Math.round(rating * 2) / 2;
                let output = [];
              
                // Append all the filled whole stars
                for (var i = rating; i >= 1; i--)
                  output.push('<i class="fa fa-star" aria-hidden="true" style="color: gold;"></i>&nbsp;');
              
                // If there is a half a star, append it
                if (i == .5) output.push('<i class="fa fa-star-half-o" aria-hidden="true" style="color: gold;"></i>&nbsp;');
              
                // Fill the empty stars
                for (let i = (5 - rating); i >= 1; i--)
                  output.push('<i class="fa fa-star-o" aria-hidden="true" style="color: gold;"></i>&nbsp;');
              
                return output.join('');
              
              }
              span2.innerHTML=getStars(product[i].rating);
             b.appendChild(span2);
             divv.appendChild(b);
             divv.appendChild(h5);
             divv.appendChild(p);
             divv.appendChild(p2);
             divv.appendChild(discele);
             divv.appendChild(p3);
             cards.appendChild(divv);
        }
    }
    catch
    {
     console.log("error");
    }
})()
unm.textContent=localStorage.getItem("username");
