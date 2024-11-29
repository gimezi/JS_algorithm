function solution(clothes) {
    cloth = {}
    for (let i = 0; i < clothes.length; i++) {
        const [name, type] = clothes[i]
        console.log(cloth)
        if (cloth[type]) {
            cloth[type] += 1
        } else {
            cloth[type] = 1
        }
    }
    
    const val = Object.values(cloth)
    let ans = 1
    for (let j = 0; j < val.length; j++) {
        ans *= val[j] + 1
    }
    
    return ans - 1
}