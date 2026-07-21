numbers = [2,5,6,7,78]
even = list(filter(lambda x:x+1,numbers))
print("numbers after increment of 1",even)



cities = ['chandigarh','ludhiana','zira','nangal']
sorted_cities = sorted(cities,key = lambda x : len(x))
print(sorted_cities)