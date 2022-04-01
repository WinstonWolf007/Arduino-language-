from Official.Main.cleans import Cleans

code = ['if', '"1 1"', '==', '"1 1"']

clean = Cleans(code)
code = clean.cleans_code_string()

print(code)
