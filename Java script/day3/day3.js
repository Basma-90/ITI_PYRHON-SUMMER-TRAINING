function first(a)
{
    let b=a[0].toUpperCase();
    let bool=false;
    for(let i=1;i<a.length;i++)
    {
        if(bool)
        {
          b+=a[i].toUpperCase();
          bool=false;
        }
        else
        {
            b+=a[i];
        }
     if(a[i]==' '){
          bool=true;
        }
    }
    return b;
}
function second (b)
{
    let a=b.split(" ");
    let maxx=0;
    let maxsent='';
    for(const t of a)
    {
     if(t.length>maxx)
     {
        maxx=t.length;
        maxsent=t;
     }
    }
    return maxsent;
}
function third (c)
{
  let b=c.toLowerCase().split('');
   
  return b.sort().join('');
}
function fourth(c)
{
    
    let b=[];
    for(let i=0;i<c;i++)
    {
      b[i]=(Math.round(Math.random()*10));
    }
    return b;
}