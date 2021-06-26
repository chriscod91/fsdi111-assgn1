from app import app #from our app package (foldert)
                    #import app variable
                    
@app.route("/")         #decorator that maps paths view functions
def hello():            #view function  
    return"<h1>Hello world!<h1>"#a simple return statement


@app.route("/aboutme")
def about():
    me = {
        "first_name": "chris",
        "last_name": "codina",
        "hobby": "grease monkey stuff",
        "ok": True
    }    
    return me

#pip3 freeze > requirements.txt

