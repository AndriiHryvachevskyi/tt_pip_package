# Test Tasks: Andrew's PIP Package

Installation

`pip install git+https://github.com/AndriiHryvachevskyi/tt_pip_package.git`

Use case

'''python
from tt_package import DB_API
import json
import requests

def main():
    DB = DB_API()
    #GET /posts
    users = DB.get_users()
    print('ALL USERS:', users)
    print('USER NAME ID=3:', users[3-1].name)

if __name__ == '__main__':
    main()
'''
