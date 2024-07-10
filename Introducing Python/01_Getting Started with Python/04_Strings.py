# Concatenation
print("Sai" + " Teja")
print("-----------------")
# Replication
print("Sai"*3)
print("-"*30)
print("-----------------")
# Length
print(len("Sai Teja"))
print("-----------------")
# Slicing
print("Sai Teja"[0:3])
name = "Sai Teja"
print(name[2:8])
print(name[-8:0])
print(name[0:])
print(name[:7])
print("-----------------")
# Case Conversion
print(name)
print(name.lower())
print(name.upper())
print("-----------------")
# Stripping --> All the whiteSpaces are removed from start and end
print("       Sai Teja      ".strip())
print("       Sai    Teja      ".strip()) # Middle white spaces are not removed
print("       Sai Teja      ".lstrip())
print("       Sai Teja      ".rstrip())
print("-----------------")
# Replacing
String = "All the whiteSpaces are removed from start and end"
print(String.replace("the","or"))
print("-----------------")
# Count
print(String.count("t"))
print(String.count("z"))
print(String.count("l"))
print("-----------------")
# Find
print(String.find("and")) # 1st Index number will be printed
print("-----------------")
# Check
print("Sai Teja".isalpha())
print("SaiTeja".isalpha())
print("123".isnumeric())
print("saiteja".islower())
print("SAITEJA".isupper())
print("-----------------")
# Capitalization
print(String.capitalize()) # Capitalizize the first letter that is A
print(String.title()) # all the letters after space are capitalized 
print("-----------------")
# Formatting
print("{} {} {}".format("Sai teja","is a good","boy"))
print("{2} {0} {1}".format("Saiteja","is a good","boy"))
print("-----------------")
# Start and end
print("Strings".startswith("s"))
print("Strings".endswith("s"))
print("-----------------")

print("Strings".center(20,"*"))
print("Strings".ljust(20,"*"))
print("Strings".rjust(20,"*"))