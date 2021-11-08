num = list(input())

def rot(num_list):
  new_num_list = []
  check = True
  for one_num in num_list:
    if one_num == '6' and check:
      new_num_list.append('9')
      check = False
    else:
      new_num_list.append(one_num)
  return(''.join(new_num_list))

print(rot(num))

