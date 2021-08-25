# Cars API

Car API is a simple Django API that allows you to manage a database containing makes and models of different cars.

## Installation

1. Clone the repository
2. Navigate to the main folder
3. Run
4. You might now need to wait about 45 seconds for the application to start
```bash
docker-compose up --build
```
The app should now be running locally at your PC at <http://localhost:8000/>

## Usage

You can visit this working API at <http://netguru-cars-api-kalek.herokuapp.com>

### Available paths are
* POST /cars/ - send a POST request that will create a new car with body {"make" : "Ford", "model" : "Focus"}. Make and model must be valid, data is checked against the <https://vpic.nhtsa.dot.gov/api/vehicles/getmodelsformake/Ford?format=json> API
* POST /rate/ - send a POST request that will rate an existing car with body {"car_id" : 5, "rating" : 5}. car_id must be valid id of a car and rating must be in the range from 1 to 5
* DELETE /cars/id/ - send a DELETE request that will delete an existing car where id is a valid id of a car
* GET /cars/- get the list of all authors
* GET /popular/- get the list of 5 most popular cars (based on the amount of ratings)

### Testing
Tests are available in api/tests directory so you can navigate to this folder with 'docker-compose up' running and run 
```bash
pytest
```
