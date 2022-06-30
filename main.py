sta = ["Aland Islands", "Albania", "Andorra", "Armenia", "Austria", "Azerbaijan", "Belarus", "Belgium", "Bosnie and Herzegovina", "Bulgaria", "Croatia", "Cyprus", "Czechia", "Denmark", "England", "Estonia", "Faroe Islands", "Finland", "France", "Georgia", "Germany", "Gibraltar", "Greece", "Guernsey", "Hungary", "Iceland", "Irland", "Isle of Man", "Italy", "Jersey", "Kazakhstan", "Kosovo", "Latvia", "Liechtenstein", "Lithuania", "Luxembourg", "Malta", "Moldovo", "Monaco", "Montenegro", "Netherlands", "North Macedonia", "Northen Irland", "Norway", "Poland", "Portugal", "Romania", "Russia", "San Marino", "Scotland", "Serbia", "Slovakia", "Slovenia", "Spain", "Sweden", "Switzerland", "Turkey", "Ukraine", "Vatican City", "Wales"]
cap = ["Mariehamn", "Tirana", "Andorra la Vella", "Yerevan", "Vienna", "Baku", "Minsk", "Brussels", "Sarajevo", "Sofia", "Zagreb", "Nicosia", "Prague", "Copenhagen", "London", "Tallinn", "Torshavn", "Helsinki", "Paris", "Tbilis", "Berlin", "Gibraltar", "Athens", "Saint Peter Port", "Budapest", "Reykjavik", "Dublin", "Douglas", "Rome", "Saint Helier", "Nur-Sultan", "Pristina", "Riga", "Vanduz", "Vilnius", "Luxembourg City", "Valleta", "Chisinau", "Monaco", "Podgorica", "Amsterdam", "Skopje", "Belfast", "Oslo", "Warsaw", "Lisbon", "Bucharest", "Moscow", "San Marino", "Edinburgh", "Belgrade", "Bratislava", "Ljubljana", "Madrid", "Stockholm", "Bern", "Ankara", "Kyiv", "Vatican City", "Cardiff"]
correct = 0
print("Europe's Capitals Quiz \n")
print("""Note: Type the capitals' and countries' names with capital letters! \n""")
yes_no = int(input("Table of results -> Press -1\nFind the capital -> Press 1\nFind the country -> Press 2\n"))
if yes_no == -1:
  for i in range(60):
    print(cap[i] + " is the capital of " + sta[i])
  print("\nTo start click on Run!")
elif yes_no == 1:
  print("\nLET'S START!\n")
  for i in range(60):
    input1 = input("Enter the capital of " + str(sta[i]) + ": ")
    if input1 == cap[i]:
      print("Correct!")
      correct += 1
    else:
      print("Incorrect! It's "+ str(cap[i]) + ".")
  print("You scored " + str(correct) + "/60!")
elif yes_no == 2:
  print("\nLET'S START!\n")
  for i in range(60):
    input1 = (input("Enter the country of " + str(cap[i]) + ": "))
    if input1 == sta[i]:
      print("Correct!")
      correct += 1
    else:
      print("Incorrect! It's "+ str(sta[i]) + ".")
  print("You scored " + str(correct) + "/60!")