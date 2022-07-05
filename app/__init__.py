from flask import Flask, request, jsonify
from flask_restx import Api, Resource, fields
from werkzeug.middleware.proxy_fix import ProxyFix
from marshmallow_jsonapi import fields as mfields
from marshmallow_jsonapi.flask import Relationship, Schema

app = Flask(__name__)
app.config["DEBUG"] = True
api = Api(app, version='1.0', title='Geography API', description='A simple Geography API')
app.wsgi_app = ProxyFix(app.wsgi_app)
ns = api.namespace('Geography', description='Geography operations')


class Model:
    def __init__(self, **kwargs):
        for key, val in kwargs.items():
            setattr(self, key, val)


class City(Model):
    pass


class Country(Model):
    pass


city1 = City(id=1, city_ascii="New York")
city2 = City(id=3, city_ascii="Ottawa")

country1 = Country(
    id=1,
    country_ascii="United States",
    cities=[city1],

)

country2 = Country(
    id=2,
    country_ascii="Canada",
    cities=[city2],

)
db = {"countries": [country1, country2], "cities": [city1, city2]}


class CountriesSchema(Schema):
    id = mfields.Str(dump_only=True)
    country_ascii = mfields.Str()
    cities = Relationship(
        related_view="city",
        related_view_kwargs={"city_id": "<id>", "_external": True},
        many=True,
        include_data=True,
        type_="cities",
    )

    class Meta:
        type_ = "country"
        self_view = "countries"
        self_view_kwargs = {"country_id": "<id>"}
        self_view_many = "countries"


class CitySchema(Schema):
    id = mfields.Str(dump_only=True)
    city_ascii = mfields.Str()

    class Meta:
        type_ = "city"
        self_view = "city"
        self_view_kwargs = {"city_id": "<id>"}
        self_view_many = "cities"


def j(*args, **kwargs):
    """Wrapper around jsonify that sets the Content-Type of the response to
    application/vnd.api+json.
    """
    response = jsonify(*args, **kwargs)
    response.mimetype = "application/vnd.api+json"
    return response


@api.route("/counties/", methods=["GET"])
class Countries(Resource):
    @ns.doc('get_countries')
    def get(self):
        countries = db["countries"]
        data = CountriesSchema(many=True).dump(countries)
        return j(data)


@api.route("/counties/<int:country_id>", methods=["GET"])
class Country(Resource):
    @ns.doc('get_country')
    def get(self, country_id):
        countries = db["countries"][country_id - 1]
        data = CountriesSchema().dump(countries)
        return j(data)


@api.route("/cites/", methods=["GET"])
class Cities(Resource):
    @ns.doc('get_cities')
    def get(self):
        cities = db["cities"]
        data = CitySchema(many=True).dump(cities)
        print(data)
        return j(data)


@api.route("/cies/<int:city_id>", methods=["GET"])
class City(Resource):
    @ns.doc('get_city')
    def get(self, city_id):
        city = db["cities"][city_id - 1]
        data = CitySchema(many=False).dump(city)
        return j(data)


if __name__ == "__main__":
    app.run()


