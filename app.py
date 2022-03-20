from flask import Flask, request, jsonify
from flask_cors import CORS, cross_origin

from utils import pig_latin_translate
from mongo_connection import get_collection


# Instantiate flask app
app = Flask(__name__)
cors = CORS(app)

# Basic config for flask app
app.config["SEND_FILE_MAX_AGE_DEFAULT"] = 0
app.secret_key = "my-secret-key"
app.config["SESSION_TYPE"] = "filesystem"
app.config['CORS_HEADERS'] = 'Content-Type'


@app.route("/create_phase", methods=['POST'])
@cross_origin()
def index():
    """
    Get the request type and the data from the request.
    """
    if request.method == "POST":
        val = request.json

        name_key = "name"
        zip_key = "zip"
        pig_latin_name_key = "pig_latin_name"
        county_key = "county"
        population_key = "population"
        """
        Check if the request doesn't have the required keys.
        """
        if name_key not in val or zip_key not in val:
            return jsonify({"Error": "'name' and 'zip' are required inputs"})
        """
        Translate the name to pig latin.
        """
        pig_latin_name = pig_latin_translate(val[name_key].lower())

        """
        Get the county and population from the database.
        """
        collection = get_collection("zip_county_data")

        document = collection.find_one({"zipcode": val[zip_key]})

        if not document:
            return jsonify({"Error": "Zipcode not found"})

        res_dict = {
            pig_latin_name_key: pig_latin_name,
            zip_key: val[zip_key],
            county_key: document[county_key],
            population_key: document[population_key]
        }

        return jsonify(res_dict)


if __name__ == "__main__":
    app.run(port=8080)