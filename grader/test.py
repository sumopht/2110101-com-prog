def read_data():
    x = input().split(", ")
    data = {'ID': x[0], 'Name': x[1], 'Birthdate': x[2]}
    return data


student1 = {"ID": "5830000021",
            "Name": "Pranpriya M.",
            "Birthdate": [27, 3, 1997]}
print(read_data())
