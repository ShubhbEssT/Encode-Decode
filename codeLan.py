import random as rd

#Code

letters = [
    "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o",
    "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"
]

#Encode


def encode(a: str):
  a = a.lower()
  output = ""
  lastWrd = ""
  if len(a) >= 3:
    for letter in a:
      if a.index(letter) != 0:
        output = f"{output}{letter}"
      else:
        lastWrd = letter
    output = f"{output}{lastWrd}"
    q = rd.choice(letters)
    w = rd.choice(letters)
    e = rd.choice(letters)
    r = rd.choice(letters)
    t = rd.choice(letters)
    y = rd.choice(letters)
    output = f"{q}{w}{e}{output}{r}{t}{y}"
  else:
    output = a[::-1]
  return output


#Decode


def decode(a: str):
  if len(a) >= 3:
   output = ""
   output = a[3:-3]
   output = f"{output[-1]}{output[0:-1]}"

  else:
    output = a[::-1]

  return output