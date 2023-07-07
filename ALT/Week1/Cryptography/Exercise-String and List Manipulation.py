# Write code to accomplish each question as written in instructions.md.  Replace the empty string in each return statement with the correct return.

def question01(s):
  return s[2]

def question02(s):
  return s[4]

def question03(s):
  return len(s)

def question04(s):
  return s[0]

def question05(s):
  return s[-1]

def question06(s):
  return s[-2]

def question07(s):
  return s[3:8]

def question08(s):
  return s[-5:]

def question09(s):
  return s[3:]

def question10(s):
  return s.lower()

def question11(s):
  return s.upper()

def question12(s):
  return list(s)

def question13(s):
  return s[:len(s)-1]

def question14(s):
  return s[1:]

def question15(s):
  cnt = 0
  for i in range(len(s)):
    if "e" == s[i]:
      cnt += 1
  return cnt

def question16(s):
  cnt = 0
  L = s.lower()
  for i in range(len(L)):
    if "e" == L[i]:
      cnt += 1
  return cnt
  
def question17(s):
  cnt = 0
  L = s.lower()
  for i in range(len(L)):
    if L[i] == "a" or L[i] == "e" or L[i] == "i" or L[i] == "o" or L[i] == "u":
      cnt += 1
  return cnt

def question18(s):
  vowels = []
  L = s.lower()
  for i in range(len(L)):
    if L[i] == "a" or L[i] == "e" or L[i] == "i" or L[i] == "o" or L[i] == "u":
      vowels.append(s[i])
  return vowels

def question19(s):
  return s[::2]

def question20(s):
  return s[1::2]

def question21(s):
  list = []
  for i in range(len(s)-1):
    list.append(s[i:i+2])
  return list

def question22(s):
  string = ""
  for i in range(len(s)):
    if i%3 == 0:
      string += "!"
    else:
      string += s[i]
  return string

def question23(s):
  string = ""
  for i in range(len(s)):
    if i%3 == 2:
      string += "!"
    else:
      string += s[i]
  return string

#CHANGE THIS to do other tests!
st = "ExampleString"  

print("#1:", question01(st))
print("#2:", question02(st))
print("#3:", question03(st))
print("#4:", question04(st))
print("#5:", question05(st))
print("#6:", question06(st))
print("#7:", question07(st))
print("#8:", question08(st))
print("#9:", question09(st))
print("#10:", question10(st))
print("#11:", question11(st))
print("#12:", question12(st))
print("#13:", question13(st))
print("#14:", question14(st))
print("#15:", question15(st))
print("#16:", question16(st))
print("#17:", question17(st))
print("#18:", question18(st))
print("#19:", question19(st))
print("#20:", question20(st))
print("#21:", question21(st))
print("#22:", question22(st))
print("#23:", question23(st))