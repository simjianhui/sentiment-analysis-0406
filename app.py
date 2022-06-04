#!/usr/bin/env python
# coding: utf-8

# In[7]:


from textblob import TextBlob


# In[8]:


from flask import Flask


# In[9]:


from flask import render_template, request


# In[10]:


app = Flask(__name__)


# In[11]:


@app.route("/", methods =["GET", "POST"])
def index():
    if request.method == "POST":
        text = request.form.get("text")
        print(text)
        r = TextBlob(text).sentiment
        return(render_template("index.html", result=r))
    else:
        return(render_template("index.html", result="waiting.."))


# In[ ]:


if __name__ == "__main__":
    app.run()


# In[ ]:




