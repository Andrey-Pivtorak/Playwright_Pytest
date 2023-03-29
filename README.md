# Playwright_Pytest project

## Clone the repository. Run the command in command line:
* _https://github.com/Andrey-Pivtorak/Playwright_Pytest.git_


## Move to playwright_pytest folder:
* _cd playwright_pytest_

## Run the commands in command line:
* _python -m pip install --upgrade pip_
* _pip install pipenv_
* _pip install playwright pytest-playwright_
* _playwright install chromium_
* _pip install allure-pytest_

## Use command to run all the tests:
* _pytest_

## Use command to run all the tests in parallel:
* _pytest -n auto_

## Use command to run all the tests with different browsers:
* _pytest --test-browser=chrome_
* _pytest --test-browser=firefox_
* _pytest --test-browser=edge_

## Run allure report:
* _allure serve reports_

## Test results:
![](https://github.com/Andrey-Pivtorak/Playwright_Pytest/blob/master/data/report.png)

