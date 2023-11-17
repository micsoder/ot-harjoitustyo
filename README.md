## Atlas

#### Purpose
This program will create an interactive map for game development where the admin can create NPCs, and quests and add information about the world.

#### Current stage
Up to this stage, the program enables users to both create an account and log in. Upon logging in, users are welcomed with a visually engaging placeholder page adorned with vibrant shades of green. I am aware that now the account creation comes before the login page which is opposite from what I planned in the functional_requirements file but I am currently thinking about how I want it so it is purpose like that.


### Documentation
- [Requirements](Documentation/functional_requirements.md)
- [Record of working hours](Documentation/working_hours_record.md)
- [Changelog](Documentation/changelog.md)

### Installation guide

#### 1. Open up the terminal and check that Python and Poetry are installed and their version, otherwise install those.
```
python3 --version
```
```
python --version
```
```
poetry --version
```

#### 2. Clone the repository
```
git clone https://github.com/micsoder/ot-harjoitustyo.git
```

#### 3. Go to the directory
```
cd ot-harjoitustyo
```

#### 4. Install the dependencies from Poetry
```
poetry install
```

#### 5. Set the virtual environment
```
poetry shell
```

#### 6. Start the program by running 
```
poetry run invoke start
```

### Command Line Operations

#### To launch the program
The program can be launched from the terminal with the following command:
```
poetry run invoke start
```

#### To test the program
The program can be tested from the terminal with the following command:
```
poetry run invoke test
```

#### To get a coverage report of the tests 
The following command gives a coverage report of the tests
```
poetry run invoke coverage-report
```
