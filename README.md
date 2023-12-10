## Atlas

#### Purpose
This program will create an interactive map for game development where the admin can create NPCs, and quests and add information about the world.

#### Current stage
Up to this stage, the program enables users to both create an account and log in. Upon logging in, the user sees a placeholder image of villages, a dashboard, and a bar. Into the dashboard, a title and a description can be added, by pressing the save button at the bottom, the information is saved so that the next time the user opens the program, the same information appears. On the top of the window, there is a bar with two functions. If the user presses the **Add zone** button, then a pop-up window will appear where the user can add the title of the new zone, the filename of the image, and a description and then by pressing the **save button**, the zone is saved. If the user then chooses from the bar, **Show zone**, then the user can choose which zone to show by selecting one of the options from the dropdown menu. The user can all the time change the title and description in the dashboard by updating them and then pressing the **save button**. 


**PS. 1)** My original idea was that a new zone is added so that the user mouse clicks on the map and a polygon is created around that area and then that area would have been shown by clicking on that area on the map. Unfortunately, I wasn't able to get it to work now so I made it a bit more static with the bar functions. 

**PS. 2)** I am aware that now the account creation comes before the login page which is opposite from what I planned in the functional_requirements file but I am currently thinking about how I want it so it is purpose like that.

**PS. 3)** I have made the map itself on the [inkarnate](https://inkarnate.com/maps/) website.


### Documentation
- [Instructions](Documentation/instruction_manual.md)
- [Requirements](Documentation/functional_requirements.md)
- [Record of working hours](Documentation/working_hours_record.md)
- [Changelog](Documentation/changelog.md)
- [Architecture](Documentation/architecture.md)
- [Week 5 release](https://github.com/micsoder/ot-harjoitustyo/releases/tag/week5)

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

#### To check the formatting of the program
The formatting can be fixed with autopep8 and a report about the Pylint grade printed with the following command: 
```
poetry run invoke lint
```
