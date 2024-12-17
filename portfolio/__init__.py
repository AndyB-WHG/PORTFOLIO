from flask import Flask, render_template, abort

app = Flask(__name__)

projects = [
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
        "thumb": "img/online-blog-freepic-dot-com.jpg",
        "hero": "img/online-blog-freepic-dot-com.jpg",
        "categories": ["python", "web"],
        "slug": "microblog",
        "prod": "https://python-web-microblog-1-3pe5.onrender.com"
    },
     {
        "name": "Personal finance tracking app with React",
        "thumb": "img/personal-finance.png",
        "hero": "img/personal-finance.png",
        "categories": ["react", "javascript"],
        "slug": "personal-finance",
    },
    {
        "name": "REST API Documentation with Postman and Swagger",
        "thumb": "img/rest-api-docs.png",
        "hero": "img/rest-api-docs.png",
        "categories": ["writing"],
        "slug": "api-docs",
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
