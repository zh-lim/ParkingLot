# Basic Practice System Design Interview Question - Carpark System
Parking system created to ticket parked cars in the carpark.

## Test System
Running the 3 unit tests scripts to test each class
```
python -m unittest test/test_car.py
python -m unittest test/test_carpark.py
python -m unittest test/test_carpark_interface.py
```

## Run System
Two modes of running the program has been defined.
##### 1. File Mode
```
python main.py file.txt
```
##### 2. Shell Mode
```
python main.py
```

## About the System
#### Considerations
1. Input files are to be put into the *main.py* script folder. The input file will then be read by invoking the command for file mode.

2. Any user or file input commands which does not execute will be returned with a response.
> ***Invalid Input! Please check your input and try your command again.***
>> Invalid Commands include:
>> - Not enough arguments 
>> e.g. $ *create_parking_lot*
>> - Erroneous inputs
>> e.g. $ *create_parking_lot two*
>> - Wrong command
>> e.g. $ *create_car_park 6*

3. The program will not check the order of the argument inputs and just execute per normal.
> e.g. *park Red KA-1-HH-1234* will treat Red as the register no. and KA-1-HH-1234 as the colour.

4. The program does not validate/verify the inputs given. Any String input will be taken.
> e.g. *park KA-1-HH-1234 Fire* will take Fire to be the colour.

5. Creation of parking lot can only be executed once per running instance of the program. The below response will be given on the 2nd attempt at creation of parking lot.
> ***Parking lot already exists***

6. If slot number given for the leave command is not valid in the parking lot, the below response will be given.
> ***No such slot number in parking lot***
