
# Javascript 기본 문법

## 실행 방법
Node.js 파일은 .js 확장자를 가지며, 아래의 명령어로 실행할 수 있습니다.
```bash
node 파일이름.js
```

# JavaScript에서 객체(딕셔너리) 다루기

## 예제

### 예제 1: 객체 생성
```javascript
let obj = {}; // 빈 객체 생성
console.log(obj); // {} 출력
```

### 예제 2: 객체에 키-값 추가
```javascript
let obj = {}; 
obj["name"] = "John"; // 'name' 키에 'John' 값 추가
console.log(obj); // { name: 'John' } 출력
```

### 예제 3: 객체에서 키-값 가져오기
```javascript
let obj = {name: "John", age: 25}; 
console.log(obj["name"]); // 'John' 출력
console.log(obj["age"]); // 25 출력
```

## 연습 문제

### 연습 문제 1:
1. `book`이라는 이름의 빈 객체를 생성하세요.
2. `book` 객체에 `title`이라는 키와 `The Great Gatsby`라는 값을 추가하세요.
3. `book` 객체의 `title` 값을 출력하세요.

### 연습 문제 2:
1. `movie`라는 이름의 객체를 생성하되, 이 객체는 `title`이라는 키에 `Inception`, `director`라는 키에 `Christopher Nolan`이라는 값을 가지도록 만드세요.
2. `movie` 객체의 `title`과 `director` 값을 출력하세요.

### 연습 문제 3:
1. `student`라는 이름의 객체를 생성하되, 이 객체는 `name`이라는 키에 `Alice`, `age`라는 키에 `20`, `major`라는 키에 `Computer Science`라는 값을 가지도록 만드세요.
2. `student` 객체의 `name`, `age`, `major` 값을 출력하세요.
3. `student` 객체에 `grade`라는 키와 `A`라는 값을 추가하세요.
4. `student` 객체의 `grade` 값을 출력하세요.


# 딕셔너리 안에 딕셔너리

JavaScript에서 객체(딕셔너리와 유사)는 값으로 다른 객체를 가질 수 있습니다. 이는 중첩된 객체, 또는 딕셔너리 안에 딕셔너리라고 볼 수 있습니다. 이런 구조를 사용하면 더 복잡한 데이터를 표현할 수 있습니다.

### 예제 4: 딕셔너리 안에 딕셔너리
```javascript
let outerObj = {
  innerObj: {
    key1: 'value1',
    key2: 'value2'
  }
};
console.log(outerObj); // { innerObj: { key1: 'value1', key2: 'value2' } }
console.log(outerObj.innerObj.key1); // 'value1' 출력
```

### 연습 문제 4:
1. `school`이라는 이름의 객체를 생성하세요. 이 객체는 `student`라는 키에 또 다른 객체를 가지도록 만드세요. 내부 객체는 `name`이라는 키에 `Alice`, `age`라는 키에 `20`을 가지도록 하세요.
2. `school` 객체의 `student` 객체의 `name`과 `age` 값을 출력하세요.
3. `school` 객체에 `teacher`라는 키를 추가하세요. `teacher` 키는 또 다른 객체를 가지며, 이 객체는 `name`이라는 키에 `Bob`, `subject`라는 키에 `Math`를 가지도록 하세요.
4. `school` 객체의 `teacher` 객체의 `name`과 `subject` 값을 출력하세요.


# 조건문 (`if`)

JavaScript에서 `if`문은 주어진 조건이 참(`true`)일 때 코드 블록을 실행합니다.

### 예제 5: `if`문
```javascript
let number = 10;
if (number > 5) {
  console.log(number + " is greater than 5"); // '10 is greater than 5' 출력
}
```

### 연습 문제 5:
1. `age`라는 변수를 생성하고, 그 값으로 `20`을 할당하세요.
2. `if`문을 작성하여 `age`가 `18` 이상일 때 "You are an adult."라는 문장을 출력하세요.

### 연습 문제 6:
1. `temperature`라는 변수를 생성하고, 그 값으로 `30`을 할당하세요.
2. `if`문을 작성하여 `temperature`가 `25` 이상일 때 "It's hot outside."라는 문장을 출력하세요.

# 반복문 (`for`)

JavaScript에서 `for`문은 코드 블록을 특정 횟수만큼 반복하여 실행합니다.

### 예제 6: `for`문
```javascript
for (let i = 0; i < 5; i++) {
  console.log(i); // 0부터 4까지 순서대로 출력
}
```

### 연습 문제 7:
1. `for`문을 사용하여 0부터 10까지의 숫자를 출력하세요.

### 연습 문제 8:
1. `for`문을 사용하여 1부터 10까지의 숫자 중 홀수만 출력하세요.
