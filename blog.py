import os
import jinja2
import webapp2

from google.appengine.ext import db

template_dir = os.path.join(os.path.dirname(__file__), 'templates')
jinja_env = jinja2.Environment(loader = jinja2.FileSystemLoader(template_dir), autoescape = True)



class Handler(webapp2.RequestHandler):
	def write(self, *a, **kw):
		self.response.out.write(*a, **kw)

	def render_str(self, template, **params):
		t = jinja_env.get_template(template)
		return t.render(params)

	def render(self, template, **kw):
		self.write(self.render_str(template, **kw))

class Blog(db.Model):
	subject = db.StringProperty(required = True)
	blog = db.TextProperty(required = True)
	created = db.DateTimeProperty(auto_now_add = True)

class MainPage(Handler):
	def render_index(self, subject="", blog="", error=""):
		blogs = db.GqlQuery("SELECT * FROM Blog ORDER BY created DESC")

		self.render("index.html", subject=subject, blog=blog, error=error, blogs=blogs)

	def get(self):
		self.render_index();


class PostPage(Handler):
	def render_post(self, subject="", blog="", error=""):
		blogs = db.GqlQuery("SELECT * FROM Blog ORDER BY created DESC")

		self.render("post.html", subject=subject, blog=blog, error=error, blogs=blogs)

	def get(self):
		self.render_post()

	def post(self):
		subject = self.request.get('subject')
		blog = self.request.get('blog')

		if subject and blog:
			b = Blog(subject=subject, blog=blog)
			b_key = b.put()

			self.redirect("/blog/%d" % b_key.id())
		else:
			error = "please enter both subject and blog!"
			self.render_post(subject, blog, error)

class Permalink(MainPage):
	def get(self, blog_id):
		s = Blog.get_by_id(int(blog_id))
		self.render("index.html", blogs=[s])



application = webapp2.WSGIApplication([('/', MainPage), 
									   ('/newpost', PostPage), 
									   ('/blog/(\d+)', Permalink)], 
									   debug=True)




