# capitalize()
name = "tERMINAL"
print( name.capitalize() )

# casefold()
name = "tERMINAL"
print( name.casefold() )

# center()
name = "Terminal"
print( name.center(12, "-") )
 
# count()
name = "casa"
print( name.count("a") )

# endswith()
name = "Terminal"
print( name.endswith("nal") )

# find()
name = "Terminal"
print( name.find("i") )

# format()
name = "Eu {} {} Python!"
print( name.format(" ", "amar") )

# format_map()
name = {'a': 'Python', 'b': 'curto'}
print( 'Eu {b} {a}'.format_map(name) )

# isalnum()
name = "plan9"
print( name.isalnum() )

# isalpha()
name = "plan9"
print( name.isalpha() )

# isdecimal()
name = "9.36"
print( name.isdecimal() )

# isdigit()
name = "936"
print( name.isdigit() )

# islower()
name = "somos minúsculos..."
print( name.islower() )

# isspace()
name = " "
print( name.isspace() )

# isupper()
name = "TERMINAL"
print( name.isupper() )

# ljust()
name = "Terminal"
print( name.ljust(11, '>') )

# lower()
name = "TeRmInAl RoOt"
print( name.lower() )

# upper()
name = "TeRmInAl RoOt"
print( name.upper() )

# replace()
name = "Terminal User"
print( name.replace("User", "Root") )

# strip()
name = " Terminal Root "
print( name.strip() )

# title()
name = "tErminAl rOOt pYthon"
print( name.title() )

# zfill()
name = ".936"
print( name.zfill(6) )

# removesuffix()
name = "Terminal"
print( name.removesuffix("inal") )

# swapcase()
name = "TERMINAL root"
print( name.swapcase() )

# istitle()
name = "Terminal Root Python"
print( name.istitle() )