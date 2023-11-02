places = [["Sydney", "NSW, Australia"], ["Denver", "CO, USA"], ["Prauge", "Czech Republic"], ["Cozumel", "Mexico"], ["Tornoto", "ON, Canada"], ["Berlin", "Germany"], ["Ripley", "WV, USA"]]
location = " "
first = True
print("Places to visit:")
for place in places:
    for cell in place:
        if first == True:
            location += cell + ", "
            first = False
        else:
            location += cell
            first = True
    print(location)
    location = " "