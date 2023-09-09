  localvar=90;
function printVariables(val1=0,val2=0,val3=0)
{
    for(let i=0;i<arguments.length;i++)
    {
      console.log(arguments[i]);
    }
 let arr=[];
 arr[0]=val1;
 arr[1]=val2;
 arr[2]=val3;
 //console.log(localvar); //h3-undefined h4-same answers 
 var localvar=3;
  testingvar=5;
 return arr;
}
// step 1 and 2 
/*
const printVariables=function(val1,val2,val3)
{
for(let i=0;i<arguments.length;i++)
{
  console.log(arguments[i]);
}
return [val1,val2,val3];
}
*/
//arrow function
/*
const printVariablesArrow = (val1, val2, val3) => {
    for(let i=0;i<arguments.length;i++)
{
  console.log(arguments[i]);
}
    return [value1, value2, value3];
};
*/
               // Bonus
function count(a)
{
    const vowels = "aeiouAEIOU";
    let cnt=0;
    for(const t of a)
    {
        if(vowels.includes(t))
        {
            cnt++;
        }
    }
    return cnt;sss
}
 
 
 
 
 


