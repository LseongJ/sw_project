# sw_project
### <1주차 11/17(목) ~ 11/23(수)>
1.주제선정 : 단위 변환 계산기

2.주제 세부 사항 - 단위 종류 : 길이(6개의 단위(cm, m 등)), 넓이(3개), 무게(5개), 부피(4개), 온도(3개), 속도(4개)

3.역할분담 : 
팀장: 뼈대코드 작성,
팀 전체: <길이>의 6개 단위를 5명이서 골고루 분담하여 단위 변환 함수 작성 

4.예시 코드 : 
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
            
    # 이런식으로 input_type을 기준으로 단위를 변환
```
