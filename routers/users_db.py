# Users DB API

from fastapi import APIRouter, HTTPException, status
from db.models.user import User
from db.shemas.user import user_schema, users_schema
from db.client import db_client
from bson import ObjectId


router = APIRouter(prefix="/userdb",
                   tags=["userdb"], responses={status.HTTP_404_NOT_FOUND: {"message": "Not found"}})

# Start the server: fastapi dev users.py
# Stop the server: CTRL+C


@router.get("/", response_model=list[User])
async def users():

    return users_schema(db_client.users.find())


# http://127.0.0.1:8000/user/2  PATH
@router.get("/{id}")
async def user(id: str):
    return search_user("_id", ObjectId(id))


# http://127.0.0.1:8000/userquery/?id=2  QUERY
@router.get("/")
async def userquery(id: str):
    return search_user("_id", ObjectId(id))


@router.post("/", response_model=User, status_code=status.HTTP_201_CREATED)
async def userpost(user: User):
    if type(search_user(user, user.email)) == User:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="User already exist")
    # return {"error": "User already exist"}
    # else:
    #    users_list.append(user)
    user_dict = dict(user)
    del user_dict["id"]

    id = db_client.users.insert_one(user_dict).inserted_id
    new_user = user_schema(db_client.users.find_one({"_id": id}))
    return User(**new_user)


@router.put("/", response_model=User)
async def userput(user: User):
    user_dict = dict(user)
    del user_dict["id"]
    try:
        db_client.users.find_one_and_replace(
            {"_id": ObjectId(user.id)}, user_dict)
    except:
        return {"error": "User has not been updated"}

    return search_user("_id", ObjectId(user.id))


@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
async def userdelete(id: str):
    found = db_client.users.find_one_and_delete({"_id": ObjectId(id)})
    if not found:
        return {"error": "User has not been deleted"}


def search_user(field: str, key):
    try:
        user = db_client.users.find_one({field: key})
        print(user)
        return User(**user_schema(user))
    except:
        return {"error": "User not found"}
