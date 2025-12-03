#ROBERTO EMILIANO ORTIZ CUMPIAN 
#MATRICULA: 2530167
#GRUPO: A:104


#RESUMEN EJECUTIVO 
""" - ¿Qué son los tipos int y float en Python y en qué se diferencian?
Los tipos int y float en Python se diferencian principalmente en que int representa números enteros (sin decimales) 
y float representa números de punto flotante (con decimales). float es necesario para cálculos que requieren precisión decimal,
mientras que int se utiliza para números enteros positivos o negativos. 
- ¿Qué es un booleano (True/False) y cómo se obtiene a partir de comparaciones?
Un valor booleano es un tipo de dato fundamental en informática que solo puede tener uno de dos valores
posibles: True (verdadero) o False (falso). Su propósito es representar los dos valores de verdad de la lógica y el álgebra booleana,
llamada así por George Boole. 
¿Cómo se obtiene un valor booleano a partir de comparaciones?
Los valores booleanos se obtienen comúnmente como el resultado de utilizar operadores de comparación (también conocidos como relacionales).
Estos operadores evalúan una relación entre dos expresiones o valores y devuelven automáticamente un valor booleano (True o False) basado
en si la condición es cierta o no. 
- ¿Por qué es importante validar rangos y evitar división entre cero?
La validación de rangos y la prevención de la división por cero son prácticas fundamentales en programación para garantizar la estabilidad,
seguridad e integridad de los datos del software. 
- ¿Qué cubrirá tu documento?: descripción de cada problema, diseño de entradas y salidas, validaciones aplicadas y uso de enteros,
  flotantes y booleanos para tomar decisiones.
"""

#Problem 1: Temperature converter and range flag
#Description: 2–4 lines explaining what the program does.
'''
Convierte una temperatura en grados Celsius (float) a Fahrenheit 
y Kelvin. Además, determina un valor booleano is_high_temperature 
que sea true si la temperatura en Celsius es mayor o igual que 30.0
y false en caso contrario.
'''
"""
Inputs:- temp_c (float; temperatura en °C).

- ...

Outputs:- "Fahrenheit:" <temp_f>
- "Kelvin:" <temp_k>
- "High temperature:" true|false

- ...

Validations:Verificar que temp_c pueda convertirse a float.
- No permitir temperaturas físicas imposibles en Kelvin (por ejemplo, temp_k < 0.0).
- ...

Test cases:
1) Normal: ...fahrenheit: 77.0
kelvin: 298.15
is_high_temperature: False
2) Border: ...fahrenheit: -148.0
kelvin: 173.14999999999998
is_high_temperature: False
3) Error: ...Enter temperature in celsius: avc
error: invalid input
"""
'''
AMSOLUTE_ZERO_C=273.15
temp_c_yoyo= input("Enter temperature in celsius: ")
try:
    temp_c=float(temp_c_yoyo)
except ValueError:
    print("error: invalid input")
    exit()

temp_k=temp_c+273.15
if temp_k < 0.0:
    print("error: temperature below physical limit")
    exit()

temp_f = temp_c * 9 / 5 + 32
temp_k = temp_c + 273.15
is_high_temperature = (temp_c >= 30.0)

print("fahrenheit:", temp_f)
print("kelvin:", temp_k)
print("is_high_temperature:", (is_high_temperature))
'''


#Problem 2: Work hours and overtime payment
#Description: 2–4 lines explaining what the program does.
"""Calcula el pago total semanal de un trabajador. Hasta 40 horas se pagan
 a hourly_rate (float). Las horas extra (> 40) se pagan al 150% de la tarifa normal.
 Además, genera un booleano has_overtime que indique si el trabajador hizo horas extra."""
"""
Inputs:- hours_worked (float; horas trabajadas en la semana). - hourly_rate (float; pago por hora).
- ...

Outputs:- "Regular pay:" <regular_pay>
 - "Overtime pay:" <overtime_pay> 
 - "Total pay:" <total_pay> - "Has overtime:" true|false
- ...

Validations:hours_worked >= 0 
- hourly_rate > 0 
- Si alguno no cumple, mostrar "Error: invalid input".
- ...

Test cases:
1) Normal: enter hours worked: 35
enter hourly rate: 20
Regular pay: 700.0
Overtime pay: 0.0
Total pay: 700.0
Has overtime: False
2) Border: enter hours worked: 40
enter hourly rate: 10
Regular pay: 400.0
Overtime pay: 0.0
Total pay: 400.0
Has overtime: False
3) Error:enter hours worked: -1
enter hourly rate: 20
error: invalid input
"""
"""
hours_input = input("enter hours worked: ")
rate_input = input("enter hourly rate: ")

try: 
    hours_worked = float(hours_input)
    hourly_rate = float(rate_input)
except ValueError:
    print("error invalid input")
    exit()

if hours_worked < 0 or hourly_rate <=0:
    print("error: invalid input")
    exit()

regular_hours = min(hours_worked, 40.0)
overtime_hours = max(hours_worked - 40.0, 0.0)

regular_pay = regular_hours * hourly_rate
overtime_pay = overtime_hours * hourly_rate * 1.5
total_pay = regular_pay + overtime_pay
has_overtime = (hours_worked > 40.0)

print("Regular pay:", regular_pay)
print("Overtime pay:", overtime_pay)
print("Total pay:", total_pay)
print("Has overtime:", str(has_overtime))
"""



#Problem  3: Discount eligibility with booleans
#Description: 2–4 lines explaining what the program does.
"""Determina si un cliente obtiene un descuento en su compra.
Calcula también el total a pagar aplicando un 10% de descuento cuando sea elegible.
"""
"""
Inputs:- purchase_total (float; total de la compra).
- is_student_text (string; "YES" o "NO").
- is_senior_text (string; "YES" o "NO").

- ...

Outputs:- "Discount eligible:" true|false
- "Final total:" <final_total>

- ...

Validations:- purchase_total >= 0.0
- Normalizar is_student_text e is_senior_text a mayúsculas y convertir a booleanos is_student, is_senior.
- Si el texto no es "YES" ni "NO", mostrar "Error: invalid input".

- ...

Test cases:
1) Normal:enter purchase total: 750.0
is student? (yes/no): yes
is senior? (yes/no): no
Discount eligible: true
Final total: 675.0
2) Border: enter purchase total: 1000.0
is student? (yes/no): no
is senior? (yes/no): no
Discount eligible: true
Final total: 900.0
3) Error: enter purchase total: 500.0
is student? (yes/no): maybe
is senior? (yes/no): no
Error: invalid input
"""
"""
purchase_total_input = input("enter purchase total: ")
is_student_text = input("is student? (yes/no): ")
is_senior_text = input("is senior? (yes/no): ")
try:
    purchase_total = float(purchase_total_input)
except ValueError:
    print("error: invalid input")
    exit()
if purchase_total < 0.0:
    print("error: invalid input")
    exit()

is_student_text = is_student_text.strip().upper()
is_senior_text = is_senior_text.strip().upper()

if is_student_text not in ("YES", "NO") or is_senior_text not in ("YES", "NO"):
    print("Error: invalid input")
    exit()

is_student = (is_student_text == "YES")
is_senior = (is_senior_text == "yes")
discount_eligible = is_student or is_senior or (purchase_total >= 1000.0)

if discount_eligible:
    final_total = purchase_total * 0.9
else:
    final_total = purchase_total

print("Discount eligible:", str(discount_eligible).lower())
print("Final total:", final_total)
"""

#Problem 4: Basic statistics of three integers
#Description: 2–4 lines explaining what the program does.
"""
Inputs:
- n1 (int)
- n2 (int)
- n3 (int)

- ...

Outputs:
- "Sum:" <sum_value>
- "Average:" <average_value>
- "Max:" <max_value>
- "Min:" <min_value>
- "All even:" true|false


Validations:- Verificar que los tres valores se puedan convertir a int.
- No se requieren restricciones adicionales (se permiten negativos).
- ...

Test cases:
1) Normal:Enter integer 1: 4
Enter integer 2: 10
Enter integer 3: 6
Sum: 20
Average: 6.666666666666667
Max: 10
Min: 4
2) Border:Sum: 21
Average: 7.0
Max: 7
Min: 7
All even: false

3) Error: ...Error: invalid input

"""
#probem 4
# Algorithm: basic_statistics_three_integers

# Algorithm: basic_statistics_three_integers

"""
n1_input = input("Enter integer 1: ")
n2_input = input("Enter integer 2: ")
n3_input = input("Enter integer 3: ")


try:
    n1 = int(n1_input)
    n2 = int(n2_input)
    n3 = int(n3_input)
except ValueError:
    print("Error: invalid input")
    exit()


sum_value = n1 + n2 + n3
average_value = sum_value / 3
max_value = max(n1, n2, n3)
min_value = min(n1, n2, n3)
all_even = (n1 % 2 == 0) and (n2 % 2 == 0) and (n3 % 2 == 0)


print("Sum:", sum_value)
print("Average:", average_value)
print("Max:", max_value)
print("Min:", min_value)
print("All even:", str(all_even).lower())

#Problem 5: Loan eligibility (income and debt ratio)
#Description: 2–4 lines explaining what the program does.
#Determina si una persona es elegible para un préstamo 
""" 

"""
Inputs:- monthly_income (float; ingreso mensual).
- monthly_debt (float; pagos mensuales de deuda).
- credit_score (int; puntaje de crédito).
- ...

Outputs:- "Debt ratio:" <debt_ratio>
- "Eligible:" true|false
- ...

Validations:- monthly_income > 0.0 (evitar división entre cero).
- monthly_debt >= 0.0
- credit_score >= 0
- Si no se cumple, mostrar "Error: invalid input".

- ...

Test cases:
1) Normal: ...monthly_income = 9000.0
monthly_debt = 2000.0
credit_score = 700
Debt ratio: 0.2222222222
Eligible: true
2) Border: ...monthly_income = 8000.0
monthly_debt = 3200.0
credit_score = 650
Debt ratio: 0.4
Eligible: true
3) Error: monthly_income = 0
monthly_debt = 1000
credit_score = 700
Error: invalid input

"""
#problem 5 :
"""
monthly_income_text = input("Enter monthly income: ")
monthly_debt_text = input("Enter monthly debt: ")
credit_score_text = input("Enter credit score: ")

try:
    monthly_income = float(monthly_income_text)
    monthly_debt = float(monthly_debt_text)
    credit_score = int(credit_score_text)
except:
    print("Error: invalid input")
    exit()

if monthly_income <= 0.0 or monthly_debt < 0.0 or credit_score < 0:
    print("Error: invalid input")
    exit()

debt_ratio = monthly_debt / monthly_income

eligible = (
    monthly_income >= 8000.0 and
    debt_ratio <= 0.4 and
    credit_score >= 650
)

print("Debt ratio:", debt_ratio)
print("Eligible:", str(eligible).lower())
"""

#Problem X: <short title>
#Description: 2–4 lines explaining what the program does.
"""
Inputs:
- ...

Outputs:
- ...

Validations:
- ...

Test cases:
1) Normal: ...weight_kg = 70.0
height_m = 1.75
BMI: 22.86
Underweight: false
Normal: true
Overweight: false
2) Border: weight_kg = 57.0
height_m = 1.75
BMI: 18.61
Underweight: false
Normal: true
Overweight: false
3) Error: weight_kg = 0
height_m = 1.70
Error: invalid input
"""
# Problem 6: Body Mass Index (BMI) and category flag

"""
weight_text = input("Enter weight in kg: ")
height_text = input("Enter height in meters: ")

try:
    weight_kg = float(weight_text)
    height_m = float(height_text)
except:
    print("Error: invalid input")
    exit()

if weight_kg <= 0.0 or height_m <= 0.0:
    print("Error: invalid input")
    exit()

bmi = weight_kg / (height_m * height_m)
bmi_rounded = round(bmi, 2)

is_underweight = (bmi < 18.5)
is_normal = (bmi >= 18.5 and bmi < 25.0)
is_overweight = (bmi >= 25.0)

print("BMI:", bmi_rounded)
print("Underweight:", str(is_underweight).lower())
print("Normal:", str(is_normal).lower())
print("Overweight:", str(is_overweight).lower())
"""

#concluciones 
"""
- Cómo los enteros y flotantes se usan de forma conjunta para cálculos reales.
se usan conjunta mente el calculos reales mediante un proceso de convercion donde 
el valor entero se convierte automaticamente a flotantes antes de que se realise la operasion

- Cómo las comparaciones generan booleanos y permiten tomar decisiones (if).
Las comparaciones generan valores booleanos (True/False o Verdadero/Falso), que son el
fundamento de la toma de decisiones en la programación a través de estructuras como las 
sentencias if. 

- Por qué es importante validar rangos y evitar divisiones entre cero.
para que el programa no marque error o tambien puede matar al programa.
- Qué aprendiste sobre el diseño de condiciones combinadas con and, or, not.
aprendi que al utilisar esas condiciones se pueden construir logicas boleanas mas
complejas en la plogramacion. y para la toma de ecisiones si una condiciones es verdadera o falsa 

- Cómo estos patrones se repiten en problemas de nómina, descuentos, préstamos, etc.
se repiten mucho para saber si una condicion o un valor es verdader o falso 

"""

#referencias 
"""
https://fastercapital.com/es/contenido/Garantizar-la-integridad-de-los-datos--validacion-de-entradas-en-aplicaciones-de-listado.html#:~:text=Implementar%20la%20validaci%C3%B3n%20de%20entradas%20en%20las%20aplicaciones%20de%20listado,usuarios%20interact%C3%BAen%20con%20los%20datos.
https://press.rebus.community/programmingfundamentals/chapter/boolean-data-type/#:~:text=A%20Boolean%20data%20type%20has,in%20the%20mid%2019th%20century.
https://platzi.com/blog/tipos-de-datos-en-python/#:~:text=Tipos%20de%20datos:,Verdadero)%20o%20False%20(Falso)
Tutoriales de Python sobre operadores aritméticos, relacionales y lógicos.
Libros o apuntes de algoritmos y programación básica.

"""