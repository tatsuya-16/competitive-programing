s = str(input()).replace("eraser", "").replace("erase", "").replace("dreamer", "").replace("dream", "").replace("","")
if len(s) == 0:
  print("YES")
else:
  print("NO")