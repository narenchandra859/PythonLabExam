# Again taken from internet

def correct(text):
  import re
  # compress more white spaces into one
  new = re.sub(r'\s{2,}'," ",text)
  # inserts an extra space after . followed by letter
  new = re.sub(r'\.([a-zA-Z])', '. \\1', new)
  return new

print(correct("This is          very       funny   and cool.Indeed!"))