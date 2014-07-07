from google.appengine.ext import db
from util import *
from time import strftime
class Post(db.Model):
    title = db.StringProperty(required = True)
    content = db.TextProperty(required = True)
    created = db.DateTimeProperty(auto_now_add = True)
    last_modified = db.DateTimeProperty(auto_now = True)
    def render(self,comments = ""):
        self._render_text = self.content.replace('\n', '')
        return render_str("post.html", p = self,comments = comments)
        
class Comment(db.Model):
    postid = db.IntegerProperty(required = True)
    content = db.TextProperty(required = True)
    username = db.StringProperty(required = True)
    created = db.DateTimeProperty(auto_now_add = True)
    
    
class User(db.Model):
    username = db.StringProperty(required = True)
    pw_hash = db.StringProperty(required = True)
    created = db.DateTimeProperty(auto_now_add=True)
    email = db.StringProperty()
    def put(self):
        ret = [False,False]
        if  self.email !="" and User.gql('WHERE email = :1', self.email).count() > 0:
            ret[0]=True
        if User.gql('WHERE username = :1', self.username).count() > 0:
            ret[1]=True
        if True in ret:
            return ret
        db.Model.put(self)
        return ret
    @classmethod
    def by_id(cls, uid):
        return User.get_by_id(uid)
    @classmethod
    def by_name(cls, username):
        return User.all().filter('username =', username).get()
    @classmethod
    def register(cls, username, pw, email = None):
        pw_hash = make_pw_hash(username, pw)
        return User(username = username, pw_hash = pw_hash, email = email)
    
    @classmethod
    def login(cls, username, pw):
        u = cls.by_name(username)
        if u and valid_pw(username,pw, u.pw_hash):
            return u
    

    
    
	
