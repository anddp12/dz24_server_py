print("Content-type text/html")
print("")

with open('index.html', 'r') as html:
    print(html.read())