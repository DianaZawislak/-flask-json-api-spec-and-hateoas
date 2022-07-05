# Flask JSON API SPEC and HATEOAS

### Name: <Insert Here>

### UCID: <Insert Here>

## Introduction

The purpose of this unit is to introduce you the JSON API spec, which defines an industry standard specification for the
implementation of a REST API. JSON API helps you implement HATEOAS, which is required to develop APIs that can adequetly
support API clients especially ones written using SPA frameworks like REACT and Angular. You need to be able to do this
so that you can create apps that correctly browse resources.

### Unit Video - [Watch Here](https://youtu.be/kb7DwRuwYFQ)

### Readings

1. [History of REST API - MUST READ](https://blog.readme.com/the-history-of-rest-apis/)
2. [Understanding HATEOAS](https://dzone.com/articles/rest-api-what-is-hateoas)
3. [What is JSON API Spec](https://nordicapis.com/the-benefits-of-using-json-api/)
4. [Flask JSON API  SPEC Quick Start](https://flask-rest-jsonapi.readthedocs.io/en/latest/quickstart.html)

### Assignment Tasks

For this assignment you need to fix the API to have it pass the tests

1. Change the route for listing cities and countries, so that they are named correctly.
2. Change the route for retrieving individual cities and countries, so they are named correctly

## Steps to Complete the Assignment

1. Clone the repo, do pip install -r requirements.txt, and then pytest --pylint all the tests pass
2. Put your name in the README.MD as indicated above. If you don't do this you will get a 0.
3. Run pytest --pylint to see that the test tasks are failing currently and that you need to complete them
4. Setup Pycharm run configuration for flask ![Pycharm Flask Run Configuration](flask-run-config.png)
5. Put the 5 assignment task tests in their respective test file i.e. put task 1 in test_task1.py
   You get 20 points for each task.
6. Submit a link to your GitHub Classroom repository to the Canvas assignment i.e. the one with your github ID in it

### References and Articles used for Assignment

1. [Flask Documentation](https://flask.palletsprojects.com/en/2.1.x/)
2. [Flask RestX](https://flask-restx.readthedocs.io/en/latest/)
3. [Open API Spec Home Page](https://www.openapis.org)
4. [Mashmallow JSON API](https://marshmallow-jsonapi.readthedocs.io/en/latest/)
5. [Complete Project I used for code reference](https://github.com/marshmallow-code/marshmallow-jsonapi/blob/dev/examples/flask_example.py)