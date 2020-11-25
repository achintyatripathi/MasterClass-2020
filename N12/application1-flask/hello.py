from flask import Flask,render_template
app = Flask(__name__)


# making list of pokemons 
Pokemons =["Pikachu", "Charizard", "Squirtle", "Jigglypuff",  
           "Bulbasaur", "Gengar", "Charmander", "Mew", "Lugia", "Gyarados"] 

@app.route('/')
def index():
   return "<h1>Hi I am the first page</h1>"


@app.route('/hi/<name>')
def name(name):
    return render_template('hello.html',name=name)



# defining pokemon page 
@app.route('/pokemon') 
def pokemon(): 
  
# returning index.html and list 
# and length of list to html page 
    return render_template("index.html", len = len(Pokemons), Pokemons = Pokemons) 
if __name__ == '__main__':
   app.run(debug = True)
