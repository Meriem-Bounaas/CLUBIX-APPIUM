## About Clubix :
Clubix is a mobile application specially crafted for the efficient administration and organization of the gym/fitness center. 

### Screenshot of the application : 
<div style="display: flex; justify-content: space-between;">
    <img src="./src/media/Screenshot_0.png" alt="Image 0" style="width: 200px; height: auto;">
    <img src="./src/media/Screenshot_1.png" alt="Image 1" style="width: 200px; height: auto;">
    <img src="./src/media/Screenshot_2.png" alt="Image 2" style="width: 200px; height: auto;">
    <img src="./src/media/Screenshot_3.png" alt="Image 2" style="width: 200px; height: auto;">
</div>
<div style="display: flex; justify-content: space-between;">
    <img src="./src/media/Screenshot_4.png" alt="Image 0" style="width: 200px; height: auto;">
    <img src="./src/media/Screenshot_5.png" alt="Image 1" style="width: 200px; height: auto;">
    <img src="./src/media/Screenshot_6.png" alt="Image 2" style="width: 200px; height: auto;">
    <img src="./src/media/Screenshot_7.png" alt="Image 2" style="width: 200px; height: auto;">
</div>
<div style="display: flex; justify-content: space-between;">
    <img src="./src/media/Screenshot_8.png" alt="Image 0" style="width: 200px; height: auto;">
    <img src="./src/media/Screenshot_9.png" alt="Image 1" style="width: 200px; height: auto;">
    <img src="./src/media/Screenshot_10.png" alt="Image 2" style="width: 200px; height: auto;">
    <img src="./src/media/Screenshot_11.png" alt="Image 2" style="width: 200px; height: auto;">
</div>
<div style="display: flex; justify-content: space-between;">
    <img src="./src/media/Screenshot_12.png" alt="Image 0" style="width: 200px; height: auto;">
    <img src="./src/media/Screenshot_13.png" alt="Image 1" style="width: 200px; height: auto;">
    <img src="./src/media/Screenshot_14.png" alt="Image 2" style="width: 200px; height: auto;">
    <img src="./src/media/Screenshot_15.png" alt="Image 2" style="width: 200px; height: auto;">
</div>
<div style="display: flex; justify-content: space-between;">
    <img src="./src/media/Screenshot_16.png" alt="Image 0" style="width: 200px; height: auto;">
</div>


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