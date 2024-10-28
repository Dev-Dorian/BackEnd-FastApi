from fastapi import APIRouter, HTTPException, status
from pydantic import BaseModel

router = APIRouter(prefix="/users",
                   tags=["users"], responses={status.HTTP_404_NOT_FOUND: {"message": "Not found"}})

# Start the server: fastapi dev users.py
# Stop the server: CTRL+C


class User(BaseModel):
    id: int
    name: str
    surname: str
    url: str
    age: int


users_list = [User(id=1, name="Dorian", surname="DorianDEV", url="https://doriandv.com/", age=29),
              User(id=2, name="Carlos", surname="CarlosDEV",
                   url="https://carlosdev.com/", age=22),
              User(id=3, name="Maria", surname="MariaDEV", url="https://mariadev.com/", age=30)]


@router.get("/usersjson")
async def usersjson():
    return [{"name": "Dorian", "surname": "DorianDEV", "url": "https://doriandev.com/", "age": 29},
            {"name": "Carlos", "surname": "CarlosDEV",
                "url": "https://carlosdev.com/", "age": 22},
            {"name": "Maria", "surname": "MariaDEV", "url": "https://mariadev.com/", "age": 30}]


@router.get("/users")
async def users():
    return users_list


# http://127.0.0.1:8000/user/2  PATH
@router.get("/user/{id}")
async def user(id: int):
    return search_user(id)


# http://127.0.0.1:8000/userquery/?id=2  QUERY
@router.get("/userquery/")
async def userquery(id: int):
    return search_user(id)


@router.post("/user/", status_code=201)
async def userpost(user: User):
    if type(search_user(user.id)) == User:
        raise HTTPException(status_code=404, detail="User already exist")
        # return {"error": "User already exist"}
    else:
        users_list.append(user)
        return user


@router.put("/user/")
async def userput(user: User):
    found = False
    for index, saved_user in enumerate(users_list):
        if saved_user.id == user.id:
            users_list[index] = user
            found = True
    if not found:
        return {"error": "User has not been updated"}
    else:
        return user


@router.delete("/user/{id}")
async def userdelete(id: int):
    found = False
    for index, saved_user in enumerate(users_list):
        if saved_user.id == id:
            del users_list[index]
            found = True
    if not found:
        return {"error": "User has not been deleted"}
    else:
        return user


def search_user(id: int):
    users = filter(lambda user: user.id == id, users_list)
    try:
        return list(users)[0]
    except:
        return {"error": "User not found"}
