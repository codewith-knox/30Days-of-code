name = "Imaginary Irene"

# Print out the number of times the letter I is found
print(name.count("I"))
print(name.count("P"))                   #if letters is not in substring or string , it return 0;

# The number of letters I found in another string
print("Irreverent Irises in Islington".count("I"))

# The index of the substring Irene
print(name.find("Irene"))                              #Tells the where its start        (The word Irene starts at 10 index);

# This string has no such substring
print("A completely different string".find("Irene"))     #if substring not present in the string , it safely return -1;