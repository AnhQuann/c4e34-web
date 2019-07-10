from flask import Flask, render_template, redirect, request
from food_database import Foods
from bson.objectid import ObjectId

app = Flask (__name__)

@app.route("/foods")
def home():
    all_foods = Foods.find()
    return render_template("all_food.html", ALL_FOODS=all_foods)

@app.route("/foods/<id>")
def food_detail(id):
    food = Foods.find_one({"_id": ObjectId(id)})
    return render_template("food_detail.html", FOOD=food)

@app.route("/foods/delete/<id>")
def delete_food(id):
    deleted_food = Foods.find_one({"_id": ObjectId(id)})
    if deleted_food is not None:
        Foods.delete_one(deleted_food)
    else:
        return "Not found"
    return redirect("/foods")

@app.route("/foods/add_food", methods=["GET", "POST"])
def add_food():
    if request.method == "GET":
        return render_template("add_food.html")
    elif request.method == "POST":
        form = request.form
        title = form["title"]
        description = form["desc"]
        link = form["img_link"]
        food_type = form["food_type"]
        new_food = {
            "title": title,
            "description": description,
            "link": link,
            "type": food_type,
        }
        Foods.insert_one(new_food)
        return redirect("/foods")

@app.route("/foods/edit/<id>", methods=["GET", "POST"])
def edit_food(id):
    edited_food = Foods.find_one({"_id": ObjectId(id)})
    if request.method == "GET":
        return render_template("edit_food.html", EDITED_FOOD = edited_food)
    elif request.method == "POST":
        form = request.form
        new_food_info = {
            "title": form["title"],
            "description": form["desc"],
            "link": form["img_link"],
            "type": form["food_type"],
        }

        new_value = { "$set": new_food_info }

        Foods.update_one(edited_food, new_value)
        return redirect('/foods')
if __name__ == "__main__":
    app.run(debug=True)
