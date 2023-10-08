### Solution Approach
For this solution the stack used is **Python**, **Pytest** and **Selenium Web driver**.

Check in your local if you already have these configurations, otherwise you can install
with the following configurations described below.

**Check Python**

First check if you already have Python installed in your system
```
# Check the Python 3 version
$ python3 --version
```
Install python

```
$ sudo apt-get update
$ sudo apt-get install python3.8 python3-pip
```

**Install Selenium**
With the following command line :
```
pip install selenium
```
Install Chromedriver to handle the window browser, for this test we use Chrome Browser.


**Install pytest**

pytest
```
pip install pytest
```
You can run testcases from terminal using pytest
```
pytest TestHatsMen.py
```

### Fronted exercise specification
1. Go to https://www.amazon.com
2. Search for "hats for men"
3. Add first hat to Cart with quantity 2
4. Open cart and assert total price and quantity are correct
5. Search for "hats for women"
6. Add first hat to Cart with quantity 1
7. Open cart and assert total price and quantity are correct
8. Change the quantity for item selected at step 3 from 2 to 1 item in Cart
9. Assert total price and quantity are changed correctly


