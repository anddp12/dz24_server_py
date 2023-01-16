print("Content-type text/html")
print("")

with open('master.html', 'r') as html:
    print(html.read())
    
title = "Resume"
print(f"<title>{title}</title>")

with open('head.html', 'r') as html:
    print(html.read())
    
with open('menu.html', 'r') as html:
    print(html.read())
    
with open('footer.html', 'r') as html:
    print(html.read())