#def earthquake_magnitude(filename):
    # Read the csv file.
    # For each magnitude (1-7), keep track of the total number of earthquakes
    # Magnitude#1: (0 - 1)
    # Magnitude#2: (>1 - 2)
    # Magnitude#3: (>2 - 3)
    # Magnitude#4: (>3 - 4)
    # Magnitude#5: (>4 - 5)
    # Magnitude#6: (>5 - 6)
    # Magnitude#7: (>7)


dict = earthquake_magnitude("Lecture16_Home_Eqs.csv")
print(dict.keys())
print(dict.values())


# Expected Output:
#dict_keys(['1', '2', '3', '4', '5', '6', '7'])
#dict_values([2914, 4126, 1494, 265, 740, 77, 1])


