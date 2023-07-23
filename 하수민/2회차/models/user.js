import fs from 'fs'

const dbData =  fs.readFileSync('./data/db.json')
const userDb = JSON.parse(dbData)

// 인자, 파라미터, 아규먼트
function addUser(
    email, 
    password,
    name, 
    grade, 
    age
) {
    userDb[email] = {
        name,
        password,
        grade,
        age
    }

    // 쓰는 것 : 숙제, 구글링

}

function getUser(email) {
    return userDb[email]
}

function forTest() {
    addUser('aaa@mail.com',  '조환희', 'admin', 30)
    const user = getUser('aaa@mail.com')
    console.log(user);
}

export {
    addUser,
    getUser
}