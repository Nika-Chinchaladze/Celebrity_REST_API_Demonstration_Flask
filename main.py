from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap
from form_class import QuickForm, AddForm, ChangeForm, UpdateForm
from api_class import CelebrityApi

app = Flask(__name__)
app.config["SECRET_KEY"] = "TommyShelby"
Bootstrap(app)


@app.route("/")
def home_page():
    tool = CelebrityApi()
    my_data = tool.get_all()
    return render_template("index.html", celebrity_list=my_data)


@app.route("/random")
def random_page():
    tool = CelebrityApi()
    my_data = tool.get_random()
    return render_template("random.html", celebrity=my_data)


@app.route("/search", methods=["GET", "POST"])
def search_page():
    # Check Submit State and Return Desired Results:
    form = QuickForm()
    if form.validate_on_submit():
        tool = CelebrityApi()
        my_data = tool.get_search(
            category=form.category.data,
            defined_value=form.valueField.data,
            operator=form.operator.data
        )
        return render_template("index.html", celebrity_list=my_data)
    # Standard Way - Just Open Search Page:
    return render_template("search.html", form=form)


@app.route("/add", methods=["GET", "POST"])
def add_page():
    # Check Submit State and Return Desired Results:
    form = AddForm()
    if form.validate_on_submit():
        tool = CelebrityApi()
        tool.add_celebrity(
            first_name=form.first_name.data,
            last_name=form.last_name.data,
            gender=form.gender.data,
            age=form.age.data,
            movie_genre=form.movie_genre.data,
            followers=form.followers.data,
            img_url=form.img_url.data
        )
        return redirect(url_for("home_page"))
    # Standard Way - Just Open Add Page:
    return render_template("add.html", form=form)


@app.route("/update", methods=["GET", "POST"])
def update_page():
    # Check Submit State and Return Desired Results:
    form = UpdateForm()
    if form.validate_on_submit():
        chosen_id = request.args.get("id")
        tool = CelebrityApi()
        tool.update_celebrity(
            celebrity_id=chosen_id,
            category=form.category.data,
            defined_value=form.valueField.data
        )
        return redirect(url_for("home_page"))
    # Standard Way - Just Open Add Page:
    return render_template("update.html", form=form)


@app.route("/change", methods=["GET", "POST"])
def change_page():
    # Check Submit State and Return Desired Results:
    form = ChangeForm()
    if form.validate_on_submit():
        celebrity_id = request.args.get("id")
        tool = CelebrityApi()
        tool.change_celebrity(
            celebrity_id=celebrity_id,
            first_name=form.first_name.data,
            last_name=form.last_name.data,
            gender=form.gender.data,
            age=form.age.data,
            movie_genre=form.movie_genre.data,
            followers=form.followers.data,
            img_url=form.img_url.data
        )
        return redirect(url_for("home_page"))
    # Standard Way - Just Open Change Page:
    return render_template("change.html", form=form)


@app.route("/delete")
def delete_page():
    chosen_id = request.args.get("id")
    tool = CelebrityApi()
    tool.delete_celebrity(celebrity_id=chosen_id)
    return redirect(url_for("home_page"))


if __name__ == "__main__":
    app.run(debug=True)
