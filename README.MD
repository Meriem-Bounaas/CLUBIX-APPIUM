## About Clubix :
Clubix is a mobile application specially crafted for the efficient administration and organization of the gym/fitness center. 

### Screenshot of the application : 
<img src="./src/media/Screenshot_0.png"> 
<img src="./src/media/Screenshot_1.png">
<img src="./src/media/Screenshot_2.png">
<img src="./src/media/Screenshot_3.png">
<img src="./src/media/Screenshot_4.png">
<img src="./src/media/Screenshot_5.png">
<img src="./src/media/Screenshot_6.png">
<img src="./src/media/Screenshot_7.png">
<img src="./src/media/Screenshot_8.png">
<img src="./src/media/Screenshot_9.png">
<img src="./src/media/Screenshot_10.png">
<img src="./src/media/Screenshot_11.png">
<img src="./src/media/Screenshot_12.png">
<img src="./src/media/Screenshot_13.png">
<img src="./src/media/Screenshot_14.png">
<img src="./src/media/Screenshot_15.png">
<img src="./src/media/Screenshot_16.png">


### Test Cases : 
1. Registration, followed by login and configuration
2. adding sports
3. adding groups
4. adding members
5. Logout

### Allure Report : 


### Technology used :
- Appium
- Python
- Pytest

### Tests execution :
1- Create a virtual environment

    python -m venv venv
2- Activate the environment
    
    .\venv\Scripts\Activate.ps1
3- Install the libraries

    pip install -r requirements.txt
4- Run the tests

    pytest <test_name>
5- Run allure-pytest

    pytest --alluredir=allure-results <test_name>
6- Launch the Allure server to view the results

    allure serve allure-results