# ABOUT THE PROJECT
The project was created by me to get the list of county name and the population of any zipcode in the USA and its minor islands.
The source of the data is mentioned in source.txt file present in data folder. The population data is from the US Census Bureau of year 2016. Their are two csv files used to gather this data-

1. The county_data.csv file contains the county name and the zipcode.
2. The population_data.csv file contains the population of the zipcode.

These two csv files are merged together and pushed to mongodb using ingest_data.py file. The connection to the mongoDB instance in written in mongo_connection.py file.

The main file app.py listens to one single POST method route called "/create_phrase". The username and the zipcode will be passed from the front end. The username is extracted from the JSON object and pig_latin_translate function is called which will find the pig latin name of the name provided in the requests. Similarly the zipcode is extracted from the JSON object that zipcode is looked up in the mongoDB if that zipcode is found then the population, county, pig_latin name and zipcode is returned in response else an error "zipcode not found is returned".


# How to run

1. Just run the command python app.py in the terminal.
2. In case you want to create your own mongoDB instance then run the mongo_connection.py file and later run the ingest_data.py file to insert data in the mongoDB.

# Tests 
Few test cases are provided in the test.py file such as to check the status code, check if population, county, pig_latin name and zipcode is returned in the response and equal to the expected values.

# File Descrption
1. app.py- main file of the project. It contains the route "/create_phrase" which is used to return the response.
2. mongo_connection.py- file to connect to the mongoDB instance.
3. ingest_data.py- file to insert data in the mongoDB.
4. test.py- file to test the app.py file.
5. source.txt- file to mention the source of the data.
6. utils.py- file to convert the username into the pig latin name.
7. requirements.txt- file to mention the requirements of the project.

