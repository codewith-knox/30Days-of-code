name = "In Search Of Lost Typing"
author = "Marcel Pythons"
year = 1992

# combine in the tuple
book = (name,author,year)
#  print the name of the book
print("name:",book[0],"\n"+"author:",book[1],"\n"+"year:",book[2])


# combine with the Dictionary
book = {"name":name,"author":author,"year":year}
print(book["name"])