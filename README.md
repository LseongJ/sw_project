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
		if (calculator_type == "length") or (calculator_type == "area") or (calculator_type == "weight") or (calculator_type == "volume") or (calculator_type == "temperature") or (calculator_type == "speed"):
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

버그수정: “type”류 입력 시 지정된 문자열만을 받을 수 있게 수정, num입력 시 양의 실수 판정과 양수판정을 예외처리(try, except)를 사용하여 각각 해결
![image](https://user-images.githubusercontent.com/115673103/204733496-b5351b1e-97d4-4019-8aab-966447112d73.png)

11
