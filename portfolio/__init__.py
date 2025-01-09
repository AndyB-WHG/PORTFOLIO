from flask import Flask, render_template, abort

app = Flask(__name__)

projects = [
    {
        "name": "Boxing Club app with HTML and CSS",
        "thumb": "img/gym-pic.jpg",
        "hero": "img/gym-pic.jpg",
        "categories": ["HTML", "CSS"],
        "slug": "boxing-club",
        "prod": "https://andyb-whg.github.io/westhoughton-boxing-club/index.html",
    },
    {
        "name": "Habit tracking app with Python and MongoDB",
        "thumb": "img/habit-tracking.png",
        "hero": "img/habit-tracking-hero.png",
        "categories": ["python", "web"],
        "slug": "habit-tracking",
        "prod": "https://habit-tracker-igk0.onrender.com",
    },
    {
        "name": "Microblog app with Python and MongoDB",
        "thumb": "img/online-blog-freepic-dot-com-min.png",
        "hero": "img/online-blog-freepic-dot-com-min.png",
        "categories": ["python", "web"],
        "slug": "microblog",
        "prod": "https://python-web-microblog-1-3pe5.onrender.com"
    },
     {
        "name": "Online Retail Store",
        "thumb": "img/evolveHomePageFive.png",
        "hero": "img/evolveProductsPageThree.png",
        "categories": ["python", "web", "django", "Amazon AWS", "Stripe"],
        "slug": "evolve-retail",
        "prod": "https://e-volve-retail.herokuapp.com/",
    },
  
]

slug_to_project = {project["slug"]: project for project in projects}

print("Projects variable:") 
print("")
print(projects)
print("")
print("slug_to_project variable: ") 
print("")
print(slug_to_project)

@app.route("/")
def home():
    return render_template("home.html", projects=projects)


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/contact")
def contact():
    return render_template("contact.html")


@app.route("/project/<string:slug>")
def project(slug):
    if slug not in slug_to_project:
        abort(404)
    return render_template(f"project_{slug}.html", project=slug_to_project[slug])


@app.errorhandler(404)
def page_not_found(error):
    return render_template("404.html"),404
