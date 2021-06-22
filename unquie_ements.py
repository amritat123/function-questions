def uni_value(elements):
  my_list = []
  for i in elements:
    if i not in my_list:
      my_list.append(i)
  return my_list
print(uni_value([1,2,3,3,3,3,4,5]))