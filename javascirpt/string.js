/*
String의 slice()도 자주 사용되는 문자열 함수 중 하나입니다.

먼저 slice에 대한 설명을 가볍게 읽어봅시다.

(https://www.w3schools.com/jsref/jsref_slice_string.asp)

그 후 sliceCityFromAddress 함수를 구현해 주세요.

sliceCityFromAddress 함수는 address 인자를 받습니다.

address 인자에는 주소를 나타내는 string이 주어집니다.

주어진 주소가 어느 도시인지를 찾아내서, 해당 주소에서 도시 부분만 삭제한 새로운 주소를 리턴해 주세요.

주소는 무조건 "시" 로 끝납니다. 예를 들어, "서울시".

"도" 와 "시" 는 주소에 한번 밖에 포함되어 있지 않습니다.
예를 들어, 다음과 같은 주소가 주어졌다면;

"경기도 성남시 분당구 중앙공원로 53"
"경기도 성남시 분당구 중앙공원로 53"
다음과 같은 값이 리턴되어야 합니다:

"경기도 분당구 중앙공원로 53"
*/

function sliceCityFromAddress(address) {
    space = address.indexOf(" ")
    city = address.indexOf("시")
    if (space < city){
      let firstsentence = address.slice(0,space);
      let laststentence = address.slice(city+2, address.length)
      return firstsentence + " " + laststentence
    }else {
      return address.slice(city+2,address.length)
    }

sliceCityFromAddress("서울특별시 강남구 테헤란로 427 위워크타워")


/*
우리나라는 국민연금을 만 65세 부터 받을 수 있습니다.

nationalPensionRemainingYearCount 함수를 구현해주세요.

nationalPensionRemainingYearCount 는 age_string 이라는 input을 받습니다.

age_string은 나이 값인데 string형 값으로 되어 있습니다.

주어진 나이부터 몇년이 지나야 국민연금을 받을수 있는지 리턴해주세요.

리턴 값으로는 다음 문장 처럼 리턴해야 합니다.

"앞으로 20년 남으셨습니다"
"앞으로 20년 남으셨습니다"
예를 들어, age_string 값이 다음과 같다면:

"35"
"35"
리턴 값은 다음과 같아야 합니다.

"앞으로 30년 남으셨습니다"

Number형에서 String형으로 변환하고 싶을 수도 있습니다. 어떻게 할까요?
a = 123 + ""
typeof(a) // string

String형에서 Number형으로 변환하고 싶을 수도 있습니다. 어떻게 할까요?
b = "123"-0 
typeof(b) // number
*/

function nationalPensionRemainingYearCount(age_string) {
    // Your code here
    age = age_string-0;
    if (age < 65){
      let remaining_year = 65-age; 
      return "앞으로 " + remaining_year + "년 남으셨습니다" 
    }else{
      return "앞으로 0년 남으셨습니다" 
    } 
  }

/*
앞으로 랜덤함수를 쓸 일이 정말 많습니다.

그런데 Math.random()으로는 내가 원하는 범위의 랜덤수를 얻을 수가 없습니다.

항상 0.0000000000000000에서 0.9999999999999999 사이 값에서만 return해주기 때문이죠.

최소(min), 최대값(max)을 받아 그 사이의 랜덤수를 return하는 함수를 구현해주세요.

함수는 짧지만, 이번에는 수학의 뇌를 조금 써야 하는 assignment입니다.
Tip!

이 문제는 구글에서 검색해서 풀고 이해하는 방법을 추천드립니다 :)
*/

function getRandomNumber (min, max) {
    let random_number = Math.random();
    return (random_number * (max-min)) + min
}

