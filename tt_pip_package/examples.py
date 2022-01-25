from tt_package import DB_API
import json
import requests

def main():
    DB = DB_API()

    #GET /posts
    users = DB.get_users()
    print('ALL USERS:', users)
    print('USER NAME ID=3:', users[3-1].name)

    #users.sort(key=lambda x: x['name'])
    #print(users)

    #GET /posts/{id}
    user = DB.get_user(id=1)
    print("USER ID=1:", user)

    #POST /posts
    added_user = DB.add_user(name='Iwar', username='iwar999', email='iwar999@mqil.com', phone='123', website='iwar999.com')
    print("ADDED USER:", added_user)

    #PUT /posts/{id}
    updated_user = DB.update_user(id=3, name='Iwar', username='iwar999', email='iwar999@mqil.com', phone='123', website='iwar999.com')
    #print("UPDATED USER ID=3:", updated_user)
    print("UPDATED USER NAME:", updated_user.name)

    #DELETE /posts/{id}
    deleted_user = DB.delete_user(id=5)
    print("DELETED USER:", deleted_user)



if __name__ == '__main__':
    main()