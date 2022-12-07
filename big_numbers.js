// Big nuumbers go weeee

console.log("Big Number Time");
console.log("---------------");

function big_num(x) {
  if (x > 0) {
    return(x + big_num(x - 1));
  } else {
    return 0;
  }
}

for (var n = 1; n < 100; n++) {
  const out = big_num(n);
  console.log(out);
}