d, m, y = input().split("/")
if m == "1":
    m = "January"
elif m == "2":
    m = "February"
elif m == "3":
    m = "March"
elif m == "4":
    m = "April"
elif m == "5":
    m = "May"
elif m == "6":
    m = "June"
elif m == "7":
    m = "July"
elif m == "8":
    m = "August"
elif m == "9":
    m = "September"
elif m == "10":
    m = "October"
elif m == "11":
    m = "November"
else:
    m = "December"
print(m, d + ", " + y)
