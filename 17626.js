const fs = require('fs');
const input = fs.readFileSync('/dev/stdin').toString();
// const input = 34567

let n = input * 1;
let dp = new Array(n).fill(0);


for(let i=1; i<=n; i++){
    let r = parseInt(Math.sqrt(i));
    if(r**2 === i){
        dp[i] = 1
        continue;
    }else{
        dp[i] = i
    }
    for(let j=1; j<=r; j++){
        dp[i] = Math.min(dp[i], dp[i - j**2] + 1)
    }
}

console.log(dp[n])