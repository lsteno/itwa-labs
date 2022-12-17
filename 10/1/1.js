"use strict";
let v = [18, 27, 22, 30, 25, 24, 29];

let unchanged = [...v];
let media = [...v];
let temp = 0;

function avg(array)
{
  let temp = 0;
  //calcolo media 
  for(const a of array)
  {
    temp += a;
  }
  temp = (temp/array.length);
  return temp;
}

v.sort();

//elimino il voto più alto e più basso dell'array
v.shift();
v.pop();

temp = avg(media)
//inserisco la media nei primi due slot dell'array
media.unshift(temp);
media.unshift(temp);

console.log("array e media originali");
console.log(unchanged);
console.log(avg(unchanged));

console.log("array e media depurati")
console.log(v);
console.log(avg(v));

console.log("array e media media")
console.log(media);
console.log(media[1]);