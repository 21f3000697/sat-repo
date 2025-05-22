import json

def handler(request, response):
    response.headers["Access-Control-Allow-Origin"] = "*"
    response.headers["Content-Type"] = "application/json"

    with open("q-vercel-python.json") as f:
        data = json.load(f)

    names = request.query.getlist("name")
    marks = [data.get(name, None) for name in names]

    return response.json({"marks": marks})
