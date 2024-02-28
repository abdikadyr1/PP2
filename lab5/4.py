import re
l_str = "dsAbdikadyr.;sdAmire8df"
x = re.findall("[A-Z][a-z]+", l_str)
if x:
    print("Sequences:", x)
else:
    print("Didn't match")