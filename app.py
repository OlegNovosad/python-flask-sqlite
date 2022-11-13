from flask import Flask, request, redirect, url_for, render_template

app = Flask(__name__)

class Movie():
    def __init__(self, id, title, seen):
        self.id = id
        self.title = title
        self.seen = seen
        
movies = [
    Movie(1, "Coco", True),
    Movie(2, "Titanic", True),
    Movie(3, "Врятувати рядового Раяна", False)
]

@app.route("/")
def index():
    return render_template("index.html", movies=movies)

@app.route("/add", methods=["POST"])
def add():
    title = request.form.get("title")
    if len(movies) == 0:
        id = 1
    else:
        id = movies[len(movies) - 1].id + 1
    movie = Movie(id, title, False)
    movies.append(movie)
    return redirect(url_for("index"))

@app.route("/update/<int:id>")
def update(id: int):
    for movie in movies:
        if movie.id == id:
            movie.seen = not movie.seen
            break
    return redirect(url_for("index"))

@app.route("/delete/<int:id>")
def delete(id: int):
    for index, movie in enumerate(movies):
        if movie.id == id:
            del movies[index]
            break
    return redirect(url_for("index"))

app.run(debug=True)