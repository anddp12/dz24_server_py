print("Content-type text/html")
print("")

with open('master.html', 'r') as html:
    print(html.read())
    
title = "Resume Taran A. I. "
print(f"<title>{title}</title>")

with open('head.html', 'r') as html:
    print(html.read())
    
    
    
with open('personal_data.html', 'r') as html:
    print(html.read())
    
# with open('education.html', 'r') as html:
#     print(html.read())
    
# with open('experience.html', 'r') as html:
#     print(html.read())
    
# with open('additional_information.html', 'r') as html:
#     print(html.read())
    
# with open('about_myself.html', 'r') as html:
#     print(html.read())
    
# with open('skills.html', 'r') as html:
#     print(html.read())
    
with open('footer.html', 'r') as html:
    print(html.read())
    

    