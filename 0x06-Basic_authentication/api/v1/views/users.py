#!/usr/bin/env python3
""" module docs """
from api.v1.views import app_views
from flask import abort, jsonify, request
from models.user import User


@app_views.route('/users', methods=['GET'], strict_slashes=False)
def view_all_users() -> str:
    """ method docs"""
    all_users = [user.to_json() for user in User.all()]
    return jsonify(all_users)


@app_views.route('/users/<user_id>', methods=['GET'], strict_slashes=False)
def view_one_user(user_id: str = None) -> str:
    """ method docs """
    if user_id is None:
        abort(404)
    user = User.get(user_id)
    if user is None:
        abort(404)
    return jsonify(user.to_json())


@app_views.route('/users/<user_id>', methods=['DELETE'], strict_slashes=False)
def delete_user(user_id: str = None) -> str:
    """ method docs """
    if user_id is None:
        abort(404)
    user = User.get(user_id)
    if user is None:
        abort(404)
    user.remove()
    return jsonify({}), 200


@app_views.route('/users', methods=['POST'], strict_slashes=False)
def create_user() -> str:
    """ method docs """
    request_json = None
    e_msg = None
    try:
        request_json = request.get_json()
    except Exception as e:
        request_json = None
    if request_json is None:
        e_msg = "Wrong format"
    if e_msg is None and request_json.get("email", "") == "":
        e_msg = "email missing"
    if e_msg is None and request_json.get("password", "") == "":
        e_msg = "password missing"
    if e_msg is None:
        try:
            user = User()
            user.email = request_json.get("email")
            user.password = request_json.get("password")
            user.first_name = request_json.get("first_name")
            user.last_name = request_json.get("last_name")
            user.save()
            return jsonify(user.to_json()), 201
        except Exception as e:
            e_msg = "Can't create User: {}".format(e)
    return jsonify({'error': e_msg}), 400


@app_views.route('/users/<user_id>', methods=['PUT'], strict_slashes=False)
def update_user(user_id: str = None) -> str:
    """ method docs """
    if user_id is None:
        abort(404)
    user = User.get(user_id)
    if user is None:
        abort(404)
    request_json = None
    try:
        request_json = request.get_json()
    except Exception as e:
        request_json = None
    if request_json is None:
        return jsonify({'error': "Wrong format"}), 400
    if request_json.get('first_name') is not None:
        user.first_name = request_json.get('first_name')
    if request_json.get('last_name') is not None:
        user.last_name = request_json.get('last_name')
    user.save()
    return jsonify(user.to_json()), 200
