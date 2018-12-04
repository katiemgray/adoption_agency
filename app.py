"""Animal Adoption application."""

from flask import Flask, request, redirect, render_template, flash
from models import db, connect_db, Pet
from form import AddPetForm, PetForm
from pet_finder import random_pet

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///adoption'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True

connect_db(app)
db.create_all()

from flask_debugtoolbar import DebugToolbarExtension
app.config['SECRET_KEY'] = "SECRET!"
debug = DebugToolbarExtension(app)


@app.route('/')
def show_homepage():
    """render the homepage for animal adoption"""
    pets = Pet.query.all()
    randpet = random_pet()
    print(randpet)
    return render_template('homepage.html', pets=pets, randpet=randpet)


@app.route("/add", methods=["GET", "POST"])
def handle_add_pet():
    """Pet add form; handle adding."""

    form = AddPetForm()

    if form.validate_on_submit():
        name = form.name.data
        species = form.species.data
        photo_url = form.photo_url.data
        age = form.age.data
        notes = form.notes.data

        # new_pet= Pet(**form.data)

        new_pet = Pet(
            name=name,
            species=species,
            photo_url=photo_url,
            age=age,
            notes=notes)
        db.session.add(new_pet)
        db.session.commit()

        return redirect('/')

    else:
        return render_template("pet_add_form.html", form=form)


@app.route("/pets/<int:pet_id_number>", methods=["GET", "POST"])
def show_pet_details(pet_id_number):
    """Show pet details."""

    pet = Pet.query.get_or_404(pet_id_number)
    form = PetForm(obj=pet)

    # import pdb
    # pdb.set_trace()

    if form.validate_on_submit():
        pet.photo_url = form.photo_url.data
        pet.notes = form.notes.data
        pet.available = form.available.data
        db.session.commit()
        flash(f"Pet {pet_id_number} updated!")
        return redirect(f"/pets/{pet_id_number}")

    else:
        return render_template("pet_details.html", pet=pet, form=form)
