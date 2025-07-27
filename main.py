from flask import Flask, render_template, redirect, url_for, request, session
from flask_bootstrap import Bootstrap5
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Float
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, FloatField
from wtforms.validators import DataRequired, NumberRange
import requests
import os


MOVIE_DB_API_KEY = os.environ.get("MOVIE_DB_API_KEY")
MOVIE_DB_SEARCH_URL = "https://api.themoviedb.org/3/search/movie"
MOVIE_DB_INFO_URL = "https://api.themoviedb.org/3/movie"
MOVIE_DB_IMAGE_URL = "https://image.tmdb.org/t/p/w500"
MOVIE_DB_AUTHORIZATION_KEY = os.environ.get("MOVIE_DB_AUTH_KEY")

app = Flask(__name__)
app.config['SECRET_KEY'] = os.environ.get("FLASK_KEY")
Bootstrap5(app)

# CREATE DB
class Base(DeclarativeBase):
    pass


app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get("MOVIE_DB_URI", "sqlite:///movies.db")
db = SQLAlchemy(model_class=Base)
db.init_app(app)


class MovieForm(FlaskForm):
    rating = FloatField('Your Rating Out of 10', validators=[DataRequired(), NumberRange(min=0, max=10, message="Rating must be between 0 and 10")])
    review = StringField('Your Review', validators=[DataRequired()])
    submit = SubmitField("Done")

class AddMovieForm(FlaskForm):
    title = StringField('Movie Title', validators=[DataRequired()])
    submit = SubmitField("Add Movie")

# CREATE TABLE
class Movie(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    title: Mapped[str] = mapped_column(String(250), unique=True, nullable=False)
    year: Mapped[int] = mapped_column(Integer, nullable=False)
    description: Mapped[str] = mapped_column(String(500), nullable=False)
    ranking: Mapped[int] = mapped_column(Integer, nullable=True)
    rating: Mapped[float] = mapped_column(Float, nullable=True)
    review: Mapped[str] = mapped_column(String(250), nullable=True)
    image_url: Mapped[str] = mapped_column(String(250), nullable=False)

with app.app_context():
    db.create_all()

@app.route("/")
def home():
    # order movies in the database by rating given
    result = db.session.execute(db.select(Movie).order_by(Movie.rating))
    all_movies = result.scalars().all()
    for i in range(len(all_movies)):
        all_movies[i].ranking = len(all_movies) - i
    db.session.commit()
    return render_template("index.html", movies_list=all_movies)

# add rating and review to the chosen movie
@app.route("/edit", methods=["POST","GET"])
def rate_movie():
    form = MovieForm()
    movie_id = request.args.get('id')
    movie = db.get_or_404(Movie, movie_id)
    if form.validate_on_submit():
        movie.rating = request.form["rating"]
        movie.review = request.form["review"]
        db.session.commit()
        return redirect(url_for('home'))
    return render_template("edit.html", movie=movie, form=form)


@app.route("/delete")
def delete():
    movie_id = request.args.get('id')
    movie_to_delete = db.get_or_404(Movie, movie_id)
    db.session.delete(movie_to_delete)
    db.session.commit()
    return redirect(url_for('home'))

# make a list of movies in the search result to choose from
@app.route("/select")
def find_movie():
    movie_api_id = request.args.get("id")
    if movie_api_id:
        movie_api_url = f"{MOVIE_DB_INFO_URL}/{movie_api_id}"
        response = requests.get(movie_api_url, params={
            "api_key": MOVIE_DB_API_KEY, "language": "en-US"})
        data = response.json()
        new_movie = Movie(
            title=data["original_title"],
            description=data["overview"],
            year=data["release_date"],
            image_url=f"{MOVIE_DB_IMAGE_URL}{data['poster_path']}",
        )
        db.session.add(new_movie)
        db.session.commit()
        return redirect(url_for("rate_movie", id=new_movie.id))


#search for a movie by its title
@app.route("/add", methods=["POST", "GET"])
def add_movie():
    form = AddMovieForm()
    if form.validate_on_submit():
        movie_title = request.form['title']
        headers = {
            "accept": "application/json",
            "Authorization": MOVIE_DB_AUTHORIZATION_KEY
        }
        parameters = {
            "query": movie_title
        }
        response = requests.get(MOVIE_DB_SEARCH_URL, params=parameters, headers=headers)
        response.raise_for_status()
        data = response.json()
        movies = data["results"]
        return render_template("select.html", movies = movies)
    return render_template("add.html", form=form)


if __name__ == "__main__":
    app.run(debug=False, use_reloader=False)
