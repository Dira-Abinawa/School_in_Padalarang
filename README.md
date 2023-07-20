# School_in_Padalarang

This is a REST API that provides a list of schools in Padalarang, Indonesia.

## Getting Started

To install the dependencies, run the following command:

pip install -r requirements.txt


To start the API, run the following command:

uvicorn main:app --reload


The API will be available on port 8000.

## API Endpoints

The API provides the following endpoints:

* `GET /schools`
    * Returns a list of all schools in Padalarang.
* `POST /schools`
    * Creates a new school.
* `PUT /schools/{id}`
    * Updates an existing school.
* `DELETE /schools/{id}`
    * Deletes an existing school.

## Example Requests

To get a list of all schools, you can use the following request:

GET http://localhost:8000/schools


To create a new school, you can use the following request:

POST http://localhost:8000/schools
Content-Type: application/json

{
"school_name": "SMP Negeri 1 Padalarang",
"basis_name": "Negeri",
"male_ambalan_name": "Gaharu",
"female_ambalan_name": "Melati"
}


To update an existing school, you can use the following request:

PUT http://localhost:8000/schools/1
Content-Type: application/json

{
"school_name": "SMA Negeri 1 Padalarang",
"basis_name": "Negeri",
"male_ambalan_name": "Bambu",
"female_ambalan_name": "Anggrek"
}


To delete an existing school, you can use the following request:

DELETE http://localhost:8000/schools/1


## Documentation

The API documentation is available at [http://localhost:8000/docs](http://localhost:8000/docs).