import webapp2
import os
import jinja2
import cgi
import re
import hashlib
import hmac
import string
import random
import binascii

template_dir = os.path.join(os.path.dirname(__file__),'templates')
jinja_env = jinja2.Environment(loader = jinja2.FileSystemLoader(template_dir),
                                autoescape = True)

#########################################
#signUp Input Validation
def valid_username(s):
    name_re = re.compile(r"^[a-zA-Z0-9_-]{3,20}$")
    return s and name_re.match(s)

def valid_password(s):
    pword_re = re.compile(r"^.{3,20}$")
    return s and pword_re.match(s)

def valid_email(s):
    email_re = re.compile(r"^[\S]+@[\S]+\.[\S]+$")
    return not s or email_re.match(s)
#########################################
#Escape html  
def escape_html(s):
    return cgi.escape(s,quote = True)

def escape_html_Rui(s):
    hs = [('&','&amp;'),('>', '&gt;'),('<','&lt;'),('"','&quot;')]
    tmp = s
    for h in hs:
        x,t=h
        tmp = tmp.replace(x,t)
    return tmp

def render_str(template, **params):
    t = jinja_env.get_template(template)
    return t.render(params)

secret = '507cbbabc5bd813b202c6fd887f5ac17995518941a50f9f79f7ab9e894befe70'
def hash_str(s):
    return hashlib.sha256(secret+s).hexdigest()
 
def make_secure_val(s):
    return "%s|%s" % (s, hash_str(s))
def check_secure_val(h):
    val = h.split("|")[0]
    if h == make_secure_val(val):
        return val

def make_pw_hash(name, pw, salt = None):
    if not salt:
        salt = binascii.b2a_hex(os.urandom(32))
        
    h = hashlib.sha256(name+pw+salt+secret).hexdigest()
    return"%s,%s" % (h,salt)
def valid_pw(name,pw,h):
    salt = h.split(',')[1]
    return h == make_pw_hash(name,pw, salt)
    
#Miscs  
def rot13(s):
    ret = ''
    for i in s:
        if i.isalpha():
            if 78<=ord(i)<91 or 110<=ord(i)<123:
                ret+=chr(ord(i)+13-90+65-1)
            elif ord(i)<78 or 96<ord(i)<110:
                ret+=chr(ord(i)+13)
        else:
            ret+=i             
    return ret
#########################################
#render helpers
def render_post(response, post):
    response.out.write('<b>' + post.subject + '</b><br>')
    response.out.write(post.content)