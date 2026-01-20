def main():
    pounds = pounds_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to charge? "))
    charge = pounds * percent
    print(f"Charge £{charge:.2f}")


def pounds_to_float(d):
  pounds = d.removeprefix("£")
  output1 = float(pounds)
  return output1

def percent_to_float(p):
 percent = p.removesuffix("%")
 output2 = float(percent)
 output2 = output2 / 100 
 return output2

main()
