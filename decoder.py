# Here is the code in Python

def decode(message_file):
  init_dict = {}
  with open(message_file) as f:
    for line in f:
      (key.val) = line.split()
      init_dict[int(key)] = val
  f.close()

  sorted_dict = dict(sorted(init_dict.items()))

  lengh_dict = len(sorted_dict)
  full_string = ""

  counter = 1

  for i in range(0, length_dict):
    for j in range(0, i+1):
      if i==j:
        full_string += str(sorted_dict[counter]) + " "
      counter += 1
    if counter > length_dict:
      break
  return full_string


decode("message_file.txt")
