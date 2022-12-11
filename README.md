# sw_project

### <1주차 11/17(목) ~ 11/23(수)>

#### 주제선정 : 단위 변환 계산기

#### 주제 세부 사항 - 단위 종류 : 길이(6개의 단위(cm, m 등)), 넓이(3개), 무게(5개), 부피(3개), 온도(3개), 속도(4개)

![image](https://user-images.githubusercontent.com/115673103/203234542-80afeb60-e75d-4f41-bdad-a300fd488c8e.png)

#### 역할분담 :

팀장: 뼈대코드 작성
팀 전체: <길이>의 6개 단위를 5명이서 골고루 분담하여 단위 변환 함수 작성

#### 예시 코드 :

```python
if calculator_type == "length":
  
    def length(num):
        if input_type == "mm":
            if output_type == "cm":
                return num / 10
            elif output_type == "m":
                return num / 1000         
            elif output_type == "km":
                return num / 1000000
            elif output_type == "ft":
                return num * 0.003281
            elif output_type == "inch":
                return num * 0.03937
      
    # 이런식으로 calculator_type을 정하고 input_type을 기준으로 단위를 변환
```

#### 문제 및 해결:

입력단위에 소수점이 존재할 경우, int로 받아 오류가 생겼던 점을 float으로 입력을 받아 오류수정.

### <2주차 11/24(목) ~ 11/30(수)>

#### 활동내용: 코드 작성 및 코드 개선

#### 역할 분담:

이성재(팀장): <속도>단위 코드작성, readme.md수정
구민관(팀원): <넓이>단위 코드작성
박유민(팀원): <무게>단위 코드작성
정수종(팀원): <온도>단위 코드작성
김지민(팀원): <부피>단위 코드작성
팀 전원: 개선 사항 및 버그 수정에 대한 의견제시 및 코드 작성

#### 문제 및 해결:

개선사항: 입력을 도와줄 가이드라인을 출력 후 입력 받음
![image](https://user-images.githubusercontent.com/115673103/204733181-7ad90448-5e8a-417d-b7a3-019cfb505ba6.png)

버그수정

1. calculator_type에서 입력 문자열 구성이 영어가 아닌 경우에도 다음단계로 진행되는 버그수정

```python
calculator_type = input()
while cal_type == True:
	if calculator_type.isalpha() == True:
		cal_type = False
	else:
		print("Input Error : please input correct calculator type in guide:")
		calculator_type = input()
```

2. input_type, output_type에서 입력 문자열 구성이 영어가 아닌 경우에도 다음단계로 진행되는 버그 수정
3. 속도변환, 넓이변환에서 km/h, km^2와 같이 특수문자(^, /)에 대한 예외처리를 if문으로 해결
   ```python
   elif input_type.isalpha() == False:
           if input_type == 'km^2' or input_type == 'm^2' or input_type == 'm/s' or input_type == 'km/h':  
               in_type = False
   ```

### <3주차 12/1(목) ~ 12/7(수)>

#### 활동내용: 각종 버그 수정 및 코드 개선

#### 역할 분담

이성재(팀장): readme.md수정
팀장 포함 팀 전원: 버그수정 및 개선사항 의견제시 + 코드 수정

#### 문제 및 해결

개선사항: 입력 오류에 대한 가이드라인을 명확하게 제시
![image](https://user-images.githubusercontent.com/115673103/204733418-e19f42c7-d925-4a0e-b8bb-9dfe39038f92.png)

버그수정:

1. type류 입력 시 지정된 문자열만을 받을 수 있게 수정

   ```python
   calculator_type = input()
   while cal_type == True:
   	if calculator_type.isalpha() == True:
   		if (calculator_type == "length") or (calculator_type == "area") or (calculator_type == "weight") or (calculator_type == "volume") or (calculator_type == "temperature") or (calculator_type == "speed"):
   			cal_type = False
   	else:
   		print("Input Error : please input correct calculator type in guide:")
   		calculator_type = input()
   ```
2. num입력 시 실수판정과 양수판정을 예외처리(try, except)를 사용하여 각각 해결

   ```python
   #--------------------숫자 입력--------------------#   
   print("Guide : Input <positive float number> which will be converted:")   
   while is_positive == True:
       try:
           num = float(input())
       except ValueError:
           print("Input Error : please input 'positive float' again:")

       if (num > 0) and (num is not ValueError):
           is_positive = False
       elif (num < 0 or num == 0):
           print("Sign Error : please input positive number: ")
   ```

### <4주차 12/8(목) ~ 12/14(수)>

#### 활동내용: GUI구현

#### 역할 분담

이성재(팀장): readme.md수정, GUI구현
팀장 포함 팀 전원: GUI구현에 따른 버그수정 및 개선

#### 문제 및 해결

개선사항: GUI를 구현함으로써 기존 콘솔에서 아쉬웠던 편의성 부분을 개선

버그수정: 최초 1회 실행에서 결과가 나온 후, 결과를 초기화 하지 않고 2차 실행을 할 경우
‘결과’값이 올바르지 않게 나오는 버그 수정(“결과 초기화” 버튼 구현) 

### GUI버전 설명
GUI_guide.txt참조
### 프로젝트 평가 및 향후 과제

1.계획과 결과에 대한 평가                            
<1> 1주차에 짰던 코드개요를 중심으로 버그 수정 및 코드 개선을 했고, 그 결과 팀원들이
원했던 방향으로 프로젝트를 진행한 점이 만족스러웠다.                        

<2> 처음 코드를 짤 때 버그가 많았다는 점에서 아쉽긴 했어도 팀원들의 집단지성으로
여러 오류들을 개선했다는 점이 팀워크 부분에서 만족스러웠다.     

2.현 프로젝트에서 내세우고 싶은 점                        
<1> 코드를 실행시키면 나오는 입출력 가이드를 자세하게 구현했다는 점을 내세우고 싶다.                 

<2> 콘솔의 부족한 편의성을 GUI로 구현했다는 점이 잘한 것 같다.

3.프로젝트의 개선 또는 발전 방향 제시
<1> GUI버전에서, 버튼에 대한 좀 더 자세한 설명을 추가할 수 있을 것 같다.                       

<2> 단순히 '길이' <--> '길이' 변환이 아닌, '길이' <--> '넓이'같이 다른 단위끼리도
변환할 수 있게 개선하면 좋을 것 같다.                                              

<3> 간단한 계산기 임에도 불구하고 여러 케이스를 고려하다보니 코드가 500줄이 넘어갔는데, 이를 class구문을 이용하여 간소화시켜야할 것 같다.


