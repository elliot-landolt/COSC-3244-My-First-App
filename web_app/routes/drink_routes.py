from flask import Blueprint, render_template, flash
from app.drinks import get_drinks

drink_routes = Blueprint("drink_routes", __name__)

@drink_routes.route("/drinks")
def drink_list():
    try:
        drinks = get_drinks()
        flash('Success!', "success")
        return render_template("drinks.html", drinks=drinks)
    except Exception as e:
        print('error', e)

        flash(f'An Error Occurred', "danger")