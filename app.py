#!/usr/bin/env python
# coding: utf-8

# In[28]:


from flask import Flask


# In[29]:


app = Flask(__name__)


# In[30]:


from flask import request, render_template
import joblib

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        Nikkei = request.form.get("Nikkei")
        print(Nikkei)
        model1 = joblib.load("STI_REG")
        pred1 = model1.predict([[Nikkei]])
        str1 = "The prediction for STI using Regression is : " + str(pred1)
        return(render_template("index.html", result1=str1))
    else:
        return(render_template("index.html", result1="2"))


# In[ ]:


if __name__ == "__main__":
    app.run()


# In[ ]:





# In[ ]:




