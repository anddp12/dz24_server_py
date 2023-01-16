print("Content-type text/html")
print("")

with open('master.html', 'r') as html:
    print(html.read())
    
title = "Personal_data"
print(f"<title>{title}</title>")

with open('head.html', 'r') as html:
    print(html.read())
        
with open('personal_data.html', 'r') as html:
        print(html.read())
        
with open('footer.html', 'r') as html:
    print(html.read())