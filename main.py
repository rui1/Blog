#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
from util import *
from database import *
#from time import sleep
import time
from time import sleep
import logging

class Handler(webapp2.RequestHandler):
    def write(self, *a, **kw):
        self.response.out.write(*a,**kw)
    def render_str(self, template, **params):
        t = jinja_env.get_template(template)
        return t.render(params)
    def render(self, template, **kw):
        self.write(self.render_str(template,**kw))
    def set_secure_cookies(self, name, val):
        cookie_val = make_secure_val(val)
        self.response.headers.add_header('Set-Cookie','%s=%s;Path =/' %(name, cookie_val))
    def read_secure_cookies(self,name):
        cookie_val = self.request.cookies.get(name)
        return cookie_val and check_secure_val(cookie_val)
    def login(self, user):
        self.set_secure_cookies('user_id',str(user.key().id()))
        self.set_secure_cookies('username',str(user.username))
    def logout(self):
        #self.set_secure_cookies('user_id','')
        self.response.headers.add_header('Set-Cookie', 'user_id=; Path=/')
        self.response.headers.add_header('Set-Cookie', 'username=; Path=/')
    def initialize(self, *a, **kw):
        webapp2.RequestHandler.initialize(self,*a,**kw)
        uid = self.read_secure_cookies('user_id')
        self.user = uid and User.by_id(int(uid))
    def visits_count(self,visit_cookie_str):
        visits = 0
        visit_cookie_str= self.request.cookies.get('visits')
        if visit_cookie_str:
            cookie_val = check_secure_val(visit_cookie_str)
            if cookie_val:
                visits = int(cookie_val)
        visits+=1
        self.set_secure_cookies('visits',str(visits))
        self.set_secure_cookies('timeStamp',str(time.time()))
        if not visits%100:
            return "Congratulations! You are the "+str(visits)+"th visitors!"
        else:
            return "You've Been here "+ str(visits)+" times!"
     
def render_post(response, post):
    response.out.write('<b>' + post.subject + '</b><br>')
    response.out.write(post.content)

		
class MainPage(Handler):
    def get(self):
        self.posts = Post.all().order('-created') 
        visit_cookie_str= self.request.cookies.get('visits')
        self.visits = self.visits_count(visit_cookie_str)
        username = self.read_secure_cookies('username')
        if not username:
            self.logout()
        self.render("blog.html", username=username, posts = self.posts,visits= self.visits)

    def post(self):
        username = self.request.get('username')
        password = self.request.get('password')
        u = User.login(username, password)
        if u:
            self.login(u)
            self.redirect('/')
        else:
            msg = 'Invalid Login'
            self.render('login-form.html',error_login = msg)
 

class NewPost(Handler):
    def get(self):
        if self.user:
            self.render("newpost.html")
        else:
            self.redirect("/login")

    def post(self):
        if not self.user:
            self.redirect('/')
        title = self.request.get("title")
        content = self.request.get("content")

        if title and content:
            a = Post(title=title, content = content)
            a.put()
            sleep(1)
            self.redirect("/"+str(a.key().id()))
        else: 
            error="title and content, please!"
            self.render("newpost.html", title = title, content = content, error = error)   

class Permalink(Handler):
    def get(self,postid = ''):
        key = db.Key.from_path('Post',int(postid))
        username = self.request.cookies.get('username').split('|')[0]
        selected = db.get(key)
        if not selected:
            self.error(404)
            return
        self.render("permalink.html",  post = selected,username=username)

        
class SignUp(Handler):

    def get(self):
        self.render("signup-form.html")

    def post(self):
        have_error = False
        self.username = self.request.get('username')
        self.password = self.request.get('password')
        self.verify = self.request.get('verify')
        self.email = self.request.get('email')

        self.params = dict(username = self.username,
                      email = self.email)
        #key = db.Key.from_path('User',username)
        #selected = db.get(key)
        if not valid_username(self.username):
            self.params['error_username'] = "That's not a valid username."
            have_error = True

        if not valid_password(self.password):
            self.params['error_password'] = "That wasn't a valid password."
            have_error = True
        elif self.password != self.verify:
            self.params['error_verify'] = "Your passwords didn't match."
            have_error = True

        if not valid_email(self.email):
            self.params['error_email'] = "That's not a valid email."
            have_error = True

        if have_error:
            self.render('signup-form.html', **self.params)
        else:
            self.done()
        '''
            h = make_pw_hash(username, password)
            a=User(username = username,pw_hash = h,email =email)
            existed = a.put()
            sleep(1)
            if True not in existed:
                self.login(a)
                h1 = self.read_secure_cookies('user_id')
                #h1= self.request.cookies.get('username')
                if h1:
                    self.redirect('/welcome' )
                else:
                    self.render('signup-form.html')
                    self.response.out.write("I am watching!")
            else:
                if existed[0]==True:
                    params['error_email']='This email address has been used!'
                if existed[1]==True:
                    params['error_username']='This username has been used!'
                self.render('signup-form.html',**params)
        '''
    def done(self, *a, **kw):
        raise NotImplementedError
    
class register(SignUp):
    def done(self):
        a = User.register(self.username, self.password, self.email)
        existed = a.put()
        if True not in existed:
            self.login(a)
            self.redirect('/')
            '''
            h1 = self.read_secure_cookies('user_id')
            if h1:
                self.redirect('/')
            else:
                self.render('signup-form.html')
                self.response.out.write("Don't change the cookies!")
            '''
        else:
            if existed[0]==True:
                self.params['error_email']='This email address has been used!'
            if existed[1]==True:
                self.params['error_username']='This username has been used!'
            self.render('signup-form.html',**self.params)
                
        
    

class login(Handler):
    def get(self):
        self.render('login-form.html')

    def post(self):
        username = self.request.get('username')
        password = self.request.get('password')
        u = User.login(username, password)
        if u:
            self.login(u)
            self.redirect('/')
        else:
            msg = 'Invalid Login'
            self.render('login-form.html',error = msg)
          
        '''   
        params = dict(username = username)
        have_error = False
        new_cookie_val1=str(make_secure_val(username))
        self.response.headers.add_header('Set-Cookie','username=%s' % new_cookie_val1)
        user = db.GqlQuery("select * from User where username ='%s'" % username).get()
        if not user:
            params['error_username'] = "This username can't be found."
            params['username']=''
            have_error=True
        else:
            h1= self.request.cookies.get('username')
            if not valid_pw(username,password,user.password):
                params['error_password'] = "Incorrect password."
                have_error=True
            if not check_secure_val(h1):
                have_error = True
        if have_error:
            params['error_login']="This is invalid login!"
            self.render('login-form.html',**params)
        else:
            self.redirect('/welcome')
        '''
 
class logout(Handler):
    def get(self):
        #self.response.headers.add_header('Set-Cookie','username=%s' % "")
        #self.response.headers.add_header('Set-Cookie', 'username=%s; Path=/' % '')
        #self.redirect('/signup')
        self.logout()
        self.redirect('/')
class inprogress(Handler):
    def get(self):
        self.render('InProcess.html')

class home(Handler):
    def get(self):
        self.posts = Post.all().order('-created') 
        visit_cookie_str= self.request.cookies.get('visits')
        self.visits = self.visits_count(visit_cookie_str)
        username = self.read_secure_cookies('username')
        if not username:
            self.logout()
        self.render("home.html", username=username,visits= self.visits)

    def post(self):
        username = self.request.get('username')
        password = self.request.get('password')
        u = User.login(username, password)
        if u:
            self.login(u)
            self.redirect('/')
        else:
            msg = 'Invalid Login'
            self.render('login-form.html',error_login = msg)

        
class Welcome(Handler):
    def get(self):
        cookies_val = self.request.cookies.get('username')
        if cookies_val is not None:
            username = cookies_val.split("|")[0]
            if valid_username(username) and check_secure_val(cookies_val):
                self.render('welcome.html', username = username)
            else:
                self.redirect('/signup')
        else:
            self.redirect('/signup')
            
app = webapp2.WSGIApplication([('/', home),
                               ('/algorithm',MainPage),
                                ('/newpost',NewPost),
								(r'/(\d+)',Permalink),
                                ('/signup',register),
                               ('/welcome',Welcome),
                               ('/login',login),
                               ('/logout',logout),
                               ('/inprogress',inprogress),
                               ('/home',home)], debug=True)
