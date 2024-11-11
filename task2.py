from typing import Callable

from decimal import Decimal

import re

def generator_numbers(text: str):  
    # ідентифікування всіх дійсних чисел
    pattern = r"\d+\.\d+"
    matches = re.findall(pattern, text)

    for match in matches:        
        yield match  

def sum_profit(text: str, generator: Callable[[str], str]): 
    # обчислення загального прибутку
    income = Decimal(0.00)
    for number in generator(text):        
        income += Decimal(number).quantize(Decimal("0.00"))
        
    return income

text = "Загальний дохід працівника складається з декількох частин: 1000.01 як основний дохід, доповнений додатковими надходженнями 27.45 і 324.00 доларів."
total_income = sum_profit(text, generator_numbers)
print(f"Загальний дохід: {total_income}")
