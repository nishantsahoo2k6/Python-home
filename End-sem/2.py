capitals = {'Bangladesh':"Dhaka",
            'Nepal':"Kathmandu",
            'Bhutan':"Thinmphu",
            'Sri Lanka':"Colombo",
            'Pakistan':"Karachi"}
print(capitals)

country =  input("Enter the country name: ")
if country in capitals:
    print(capitals[country])
else:
    print("Invalid Country")

capitals['India']="Delhi"
print(capitals)
