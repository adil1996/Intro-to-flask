from flask import Flask, render_template

app = Flask(__name__)

expression_kwargs ={
    "color": "brown",
    "animal_one":"fox",
    "animal_two":"dog",
    "orange_amount": 10,
    "apple_amount": 15,
    "donate_amount": 5,
    "first_name": "Saiyyad Mohammad",
    "last_name": "Adil"

}

movies = [
    "ABC","XYZ","ZXC"
]

car = {
    "brand": "Audi",
    "model": "Audi23A",
    "year": "2022"
}

class moon:
    def __init__(self, first, second, third, fourth) -> None:
        self.first = first
        self.second = second
        self.third = third
        self.fourth = fourth

todos = {
    ('Get Milk',False),
    ('Learn Programming', True)

}

@app.route("/")
def hello_world():
    return render_template('firstPage.html', title= 'Firstpage')

@app.route("/fancy")
def hello_word_fancy():
    return render_template('secondPage.html', title = "SecondPage")

@app.route('/jinja')
def load_jinja():
    return render_template('jinjaIntro.html', name='Saiyyad Mohammad Adil', template_name = "jinja", title = "JinjaIntro")

@app.route('/expression')
def load_expression():
    return render_template('expressions.html', **expression_kwargs, title = "Expression")

@app.route('/datastructure')
def load_dataStructure():
    moons = moon('A','B','C','D')
    kwargs = {
        "movies": movies,
        "car": car,
        "moons": moons
    }
    return render_template('data_structures.html', **kwargs, title = "DataStructure")

@app.route('/condition')
def load_condition():
    company = "Microsoft"
    return render_template('conditionals_basics.html', company=company, title= "Conditional")

@app.route('/setvariable')
def load_set():
    return render_template('setExpression.html', todos=todos)


#API using with the path variable.
@app.route('/todos/<string:todo>')
def load_path_variable(todo: str):
    for text, completed in todos:
        if text == todo:
            completed_text = "[x]" if completed else "[]"
            title = f"{completed_text} - Todos"
            return render_template('todo.html', completed=completed, text=text, title=title)
    else:
        return render_template("not-found.html", title="Not found", text=todo)