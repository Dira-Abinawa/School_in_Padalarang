from fastapi import APIRouter, Request
from config.db import connection
from schemas.schools import SchoolPadalarang, SchoolsPadalarang
from models.schools import School
from bson import ObjectId
import pymongo

sch = APIRouter()

@sch.get('/')
async def find_all_schools():
    school_cursor = connection.local.school.find()
    school_list = list(school_cursor)
    if not school_list:
        return "Data not Found"
    result = [SchoolPadalarang(school) for school in school_list]
    return result

@sch.post('/')
async def create_schools(school : School):
    connection.local.school.insert_one(dict(school))
    return SchoolsPadalarang(connection.local.school.find())

@sch.put('/{id}')
async def update_school(id, school: School):
    updated_school = connection.local.school.find_one_and_update(
        {"_id": ObjectId(id)},
        {"$set": dict(school)},
        return_document=pymongo.ReturnDocument.AFTER
    )
    return SchoolPadalarang(updated_school)

@sch.delete('/{id}')
async def delete_school(id):
    school = connection.local.school.find_one_and_delete({"_id": ObjectId(id)})
    if school:
        return SchoolPadalarang(school)
    else:
        return {"message": "Student not found"}
