# Kai's Blog 
- Kai's blog website: http://kaiusgs.pythonanywhere.com/ 
## Deploy
1.  generated a random secret key by running the command below, and update config.py:
```
$ python -c 'import secrets; print(secrets.token_hex())'
```
config.py: 
```
SECRET_KEY = 'xxxxxxxxx'
```
2. start the flask app 
3. initialize the database by command: `init-db`
## Features 
### Existing features 
- Blogs list display 
- Blog operation: create, update, delete
- Database integration with SQLite 
- User authentication: signup, login, logout
### Upcoming features 
- debug the blog delete function
- finish unit test module
- Blog content display page
- Username password length check
- Blog title length check
- register limiting by fixed number
- merge templates for login and register into one
- merge templates for create and update into one
- image uploading 
- pagination
- rate limiting on login or comments
- authorization: admin vs normal user
- email verification or password reset
- admin panel & admin-only routes
- Migrate here my blogs in CSDN 
