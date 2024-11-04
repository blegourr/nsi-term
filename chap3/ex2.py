import datetime

"""----------------- ex 1 -----------------"""
class Fraction:
  """
  une fraction
  """
  def __init__(self, num, demon) -> None:
    if demon < 1:
      raise ValueError("demon n'est pas un entier > 0")

    self.num = num
    self.demon = demon

  def __str__(self) -> str:
    if self.demon == 1:
      return f"{self.num}"
    return f"{self.num}/{self.demon}"

  def __eq__(self, value: object) -> bool:
    return (self.num/self.demon) == value
  
  def __lt__(self, value: object) -> bool:
    return (self.num/self.demon) < (value.num/value.demon)

  def __add__(self, value: object) -> float:
    return (self.num/self.demon) + (value.num/value.demon)

  def __mul__(self, value: object) -> float:
    return (self.num/self.demon) * (value.num/value.demon)
  


# fraction1=Fraction(1,7)
# fraction2=Fraction(1,6)
# print(fraction1)
# if(fraction1==fraction2):
#   print("ce sont les deux même fractions")
# else:
#   print("les fractions sont différentes")
# if(fraction1 < fraction2):
#   print ("la fraction ",fraction1," est inférieur à la fraction",fraction2)
# print (fraction1+fraction2)
# print (fraction1*fraction2)


"""----------------- ex 2 -----------------"""
class Date():
  def __init__(self, year, month, day) -> None:
    if 1 <= month and month <= 12:
      raise ValueError("month n'est pas un entier compris entre 1 et 12")
    if 1 <= day and day <= 31:
      raise ValueError("day n'est pas un entier compris entre 1 et 31")
    
    self.year = year
    self.month = month
    self.day = day

  def __str__(self) -> str:
    if self.month == 2:
      month = "Février"
    elif self.month == 3:
      month = "Mars"
    elif self.month == 4:
      month = "Avril"
    elif self.month == 5:
      month = "Mai"
    elif self.month == 6:
      month = "Juin"
    elif self.month == 7:
      month = "Juillet"
    elif self.month == 8:
      month = "Août"
    elif self.month == 9:
      month = "Septembre"
    elif self.month == 10:
      month = "Octobre"
    elif self.month == 11:
      month = "Novembre"
    elif self.month == 12:
      month = "Décembre"
        
    return f"{self.day} {month} {self.year}"
  
  def __lt__(self, value: object) -> bool:
    dateA = datetime.timestamp(datetime.datetime(self.year, self.month, self.day))
    dateB = datetime.timestamp(datetime.datetime(value.year, value.month, value.day))

    return dateA < dateB
  
"""----------------- ex 3 -----------------"""
