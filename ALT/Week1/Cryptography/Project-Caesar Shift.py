# Read the instructions to see what you need to do here!

alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

def caesar_encode(text, n):
  encoded = ""
  for letter in text:
    index = alpha.index(letter)+n
    encoded += alpha[index%len(alpha)]
  return encoded


def caesar_decode(text, n):
  decoded = ""
  for letter in text:
    index = alpha.index(letter)-n
    decoded += alpha[index%len(alpha)]
  return decoded


test = "HELLOWORLD"
shift = 5
enc = caesar_encode(test, shift)
dec = caesar_decode(enc, shift)
print(enc)
print(dec)
# If this worked, dec should be the same as test!