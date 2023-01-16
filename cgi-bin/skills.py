print("Content-type text/html")
print("")

with open('master.html', 'r') as html:
    print(html.read())
    
title = "Skills"
print(f"<title>{title}</title>")

with open('head.html', 'r') as html:
    print(html.read())
            
with open('skills.html', 'r') as html:
    print(html.read())
    
with open('footer.html', 'r') as html:
    print(html.read())
    

    