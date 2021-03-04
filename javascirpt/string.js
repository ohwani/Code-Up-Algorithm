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
