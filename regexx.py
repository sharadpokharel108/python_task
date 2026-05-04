import re

string="Hello Hello Hellos  World"

pattern=r'\b(Hello)\b \1'
matches=re.findall(pattern,string)
print(matches)
