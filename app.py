from flask import Flask, render_template, request
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField
from wtforms.validators import DataRequired
from nhtsa_api import get_car_info, get_car_ratings
import os

# Collaborators: Edward Mendieta, Matias Jorquera, Jonathan Insua, Jonathan Jesion

app = Flask(__name__)
app.config["SECRET_KEY"] = os.urandom(16)

years = [(str(i), str(i)) for i in range(1985, 2025)]


class CarSearch(FlaskForm):
    car_make = StringField("What is your Car Make: ", [DataRequired()])
    car_model = StringField("What is your Car Model: ", [DataRequired()])
    make_year = SelectField("What year is your vehicle: ", [DataRequired()], choices=years)
    submit = SubmitField("Get Safety Ratings")


@app.route('/', methods=['GET', 'POST'])
def home():
    form = CarSearch()
    if request.method == "POST":
        make = form.car_make.data
        model = form.car_model.data
        year = form.make_year.data
        car_id = get_car_info(year, make, model)
        if car_id == True:
            error = f"No results for {year} {make} {model}"
            return render_template("no_results.html", error=error)
        data = get_car_ratings(car_id)
        return render_template("search_success.html", data=data)
    return render_template("car_search.html", form=form)


if __name__ == '__main__':
    app.run(debug=True)
