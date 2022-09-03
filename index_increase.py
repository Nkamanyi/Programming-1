def main ():
  study_benefit = float(input("Enter the amount of the study benefits: "))
  index_raise = 1.17
  after_raise_1 = study_benefit * (1+1.17/100)
  after_raise_2 = study_benefit * (1+1.17/100)**2
  print(f"If the index raise is {index_raise} percent, the study benefit,")
  print(f"after a raise, would be {after_raise_1} euros")
  print("and if there was another index raise, the study")
  print(f"benefits would be as much as {after_raise_2} euros")
main ()
