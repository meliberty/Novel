
# coding: utf-8

# In[94]:


import random 
import markovify 
import dominate
from dominate.tags import *
import pdfkit
# import wkhtmltopdf

novel = ''

with open('A_Christmas_Carol.txt', 'r') as f:
    text = f.read()

text_model = markovify.Text(text)

for i in range(3605):
   

    novel += str(text_model.make_sentence()) + " "
    
    r = random.randint(0,100)
    
    if (r < 36):
        novel += "\n\n"
    
#print(novel)

chunked = novel.split("\n\n")

doc = dominate.document(title='Christmas')

with doc.head:
    style("body {background-color: black; color: white; font-size:25pt}")
    
with doc: 
    
    h1("Christmas Novel")
    p("A NaNoGenMo Novel by Megan Liberty")
    
    for s in chunked:
        p(s)
     
    
    
pdfkit.from_string(str(doc.render()), 'Christmas.pdf')
print(doc)


# In[93]:


print(doc)


# In[95]:


len(novel.split(" "))

