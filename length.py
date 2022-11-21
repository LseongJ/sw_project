# 길이: mm, cm, m, km, ft, inch
# 넓이: m^2, km^2, 평
# 무게: mg, g, kg, t, lb
# 부피: cc, ml, l
# 온도: K, C, F
# 속도: m/s, km/h, kn, mach

print("Guide : Input calculator type : length / area / weight / volume / temperature / speed")
calculator_type = input()

print("Guide : Input what you want to convert 'from' :")
input_type = input()

print("Guide : Input what you want to convert 'to' :")
output_type = input()

print("Guide : Input <number> which will be converted.")
num = int(input())

if calculator_type == "length":
    
    def length(num):
        if input_type == "mm":             
            if output_type == "cm":
                return num * 0.1
            elif output_type == "m":
                return num * 0.001               
            elif output_type == "km":
                return num * 0.000001
            elif output_type == "ft":
                return num * 0.003281
            elif output_type == "inch":
                return num * 0.03937
        
        elif input_type == 'cm':          
            if output_type == "mm": 
                return num * 10
            elif output_type == "m":
                return num * 0.01              
            elif output_type == "km":
                return num * 0.00001
            elif output_type == "ft":
                return num * 0.032808
            elif output_type == "inch":
                return num * 0.393701
        
        elif input_type == "m":             
            if output_type == "mm":
                return num * 1000
            elif output_type == "cm":
                return num * 100             
            elif output_type == "km":
                return num * 0.001
            elif output_type == "ft":
                return num * 3.28084
            elif output_type == "inch":
                return num * 39.370079

        elif input_type == "km":             
            if output_type == "mm":
                return num * 1000000
            elif output_type == "cm":
                return num * 100000            
            elif output_type == "m":
                return num * 1000
            elif output_type == "ft":
                return num * 32808399
            elif output_type == "inch":
                return num * 393700787
        
        elif input_type == "ft":             
            if output_type == "mm":
                return num * 304.8
            elif output_type == "cm":
                return num * 30.48              
            elif output_type == "m":
                return num * 0.3048
            elif output_type == "km":
                return num * 0.000305
            elif output_type == "inch":
                return num * 12
        
        elif input_type == "inch":             
            if output_type == "mm":
                return num * 25.4
            elif output_type == "cm":
                return num * 2.54             
            elif output_type == "m":
                return num * 0.0254
            elif output_type == "km":
                return num * 0.000025
            elif output_type == "ft":
                return num * 0.083333
        
    print(num, input_type, "was converted to" ,length(num), output_type)            

if calculator_type == "area":   
    def area(num):
        if input_type == "m^2":
            if output_type == "km^2":
                return num * 0.000001
            elif output_type == "평":
                return num * 0.3025

        elif input_type == "km^2":
            if output_type == "m^2":
                return num * 1000000
            elif output_type == "평":
                return num * 302500

        elif input_type == "평":
            if output_type == "m^2":
                return num * 3.305785
            elif output_type == "km^2":
                return num * 3.305785 * 0.000001
            
    print(num, input_type, "was converted to" ,area(num), output_type)

        
