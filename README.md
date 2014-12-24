blog
====
Update:
- What's new: 2014.12.23
  - Begin writing blog api on Google Endpoint or Flask RESTful.


A blog sample, written in Python, based on Google App Engine

Here's a sample website of this templates:
http://taste-your-recipe-test.appspot.com/
- *Some of the functions are still testing.

=====

Available functions:
- signup
  - /signup
- login
  - /login 
- logout
  - /logout 
- post blog
  - /newpost
- add and remove cookie 

app.yaml
- This file is used by Google App Engine to recognize which file is the main Python file to handle.
  In my code, blog.py is this file.
  
templates
- In this directory, there are several html files. These files are used by 'blog.py', functioning as a template of website.
  These templates are handled by Jinja2.





