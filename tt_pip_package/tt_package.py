import json
import requests
import logging
from urllib.parse import urljoin
from tt_pip_package import responses
from http import HTTPStatus

class DB_API():
    def __init__(self):
        self.base_url = 'https://jsonplaceholder.typicode.com/users/'
        self.headers = {'content-type': 'application/json; charset=UTF-8'}
        self.user_template = [{"id": None,
                               "name": None,
                               "username": None,
                               "email": None,
                               "address": {
                                   "street": None,
                                   "suite": None,
                                   "city": None,
                                   "zipcode": None,
                                   "geo": {
                                       "lat": None,
                                       "lng": None
                                   }
                               },
                               "phone": None,
                               "website": None,
                               "company": {
                                   "name": None,
                                   "catchPhrase": None,
                                   "bs": None
                               }
                               }, ]

    def check_status_code(self, r):
        if r.status_code in [HTTPStatus.OK, HTTPStatus.CREATED, HTTPStatus.ACCEPTED]:
            return True
        elif r.status_code == HTTPStatus.UNAUTHORIZED:
            raise SystemExit(logging.error("Unauthorized"))
        else:
            raise SystemExit(logging.error("Some Unexpected Error: ", r.status_code))

    def get_users(self):
        try:
            r = requests.get(self.base_url, timeout=5)
            if self.check_status_code(r):
                try:
                    return [responses.User(user) for user in r.json()]
                except json.JSONDecodeError:
                    return r
                except ValueError:
                    return r
        except requests.exceptions.ConnectionError as err:
            raise SystemExit(logging.error(err))
        except Exception as ex:
            raise SystemExit(logging.error(ex))


    def get_user(self, id):
        try:
            r = requests.get(url=urljoin(self.base_url, str(id)), timeout=5)
            if self.check_status_code(r):
                try:
                    return responses.User(r.json())
                except json.JSONDecodeError:
                    return r
                except ValueError:
                    return r
        except requests.exceptions.ConnectionError as err:
            raise SystemExit(logging.error(err))
        except Exception as ex:
            raise SystemExit(logging.error(ex))

    def add_user(self, name, username, email,  phone, website):
        new_user = self.user_template[0]
        new_user['name'] = name
        new_user['username'] = username
        new_user['email'] = email
        new_user['phone'] = phone
        new_user['website'] = website

        try:
            r = requests.post(url=self.base_url, data=json.dumps(new_user), headers=self.headers, timeout=5)
            if self.check_status_code(r):
                try:
                    return responses.User(r.json())
                except json.JSONDecodeError:
                    return r
                except ValueError:
                    return r
        except requests.exceptions.ConnectionError as err:
            raise SystemExit(logging.error(err))
        except Exception as ex:
            raise SystemExit(logging.error(ex))

    def update_user(self, id, name, username, email,  phone, website):
        new_user = self.user_template[0]
        new_user['id'] = id
        new_user['name'] = name
        new_user['username'] = username
        new_user['email'] = email
        new_user['phone'] = phone
        new_user['website'] = website
        try:
            r = requests.put(url=urljoin(self.base_url, str(id)), data=json.dumps(new_user), headers=self.headers, timeout=5)
            if self.check_status_code(r):
                try:
                    return responses.User(r.json())
                except json.JSONDecodeError:
                    return r
                except ValueError:
                    return r
        except requests.exceptions.ConnectionError as err:
            raise SystemExit(logging.error(err))
        except Exception as ex:
            raise SystemExit(logging.error(ex))

    def delete_user(self, id):
        try:
            r = requests.delete(url=urljoin(self.base_url, str(id)), timeout=5)
            if self.check_status_code(r):
                return r.json()
        except requests.exceptions.ConnectionError as err:
            raise SystemExit(logging.error(err))
        except Exception as ex:
            raise SystemExit(logging.error(ex))
