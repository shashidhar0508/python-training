# prints default value 'Norway' function caller doesn't pass any value
def location(country = "Norway"):
  print("I am from " + country)

location("Sweden")
location("India")
location()
location("Brazil")