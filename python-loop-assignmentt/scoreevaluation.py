scores = [ 70, 80, 35, 45, 99]

for score in scores:
    if score < 50:
        print("fail")
    else:
        print("pass")


for score in scores:
    if score < 50:
        continue