#you have been haxed!
muy = "shervin drawing business"
muy = muy.split(" ", 1)[1]
new_muy = ""
new_dict = {}
print(muy)
for count, i in enumerate(muy, start=0):
    if (i == " "):
        break
    else:
        new_muy = new_muy + i
    new_dict.update({count : i})
print(new_dict)
print(new_muy)

print(list(new_dict.keys())[-1])
print(new_dict)