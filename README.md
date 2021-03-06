# DSCI560_HW2


## DOI Badge
  [![DOI](https://zenodo.org/badge/296792612.svg)](https://zenodo.org/badge/latestdoi/296792612)

## Lanch the notebook
  [![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/Ueny/DSCI560_HW2/master?filepath=DSCI560_HW2.ipynb)
  
## Project Description
  This project aims to visualize 1000 data points, and each one of them comes from our generalization. The X is generated by random numbers ranged from 0 to 100,     and the Y is generated based on X. The function y = 3x + 6 is implemented on each number of X, so we have Y. With the cordinates represented by X and Y, we are     able to build up a scattered plot of data distribution.
  
## Scripts Introductions
  We have 3 scripts which need to be run in order, and the introductions are as follows.
  
1. random_numbers.py:
   
   We use a random package to generate uniform numbers repeatedly, and the range of the random number is from 0 to 100. The process will be repeated for 1000 times. We are able to have a visualization about the distribution of the 1000 random numbers. The X axis represents the number ID from 1 to 1000, and the y axis represents number values.
    
2. update_numbers.py:
  
   Based on previous 1000 random numbers, we implement a function y = 3x + 6 on each one, so we have new numbers from 6 to 306. We are also able to have a visualization about the distribution of the 1000 numbers. The X axis represents the number ID from 1 to 1000, and the y axis represents new values.
    
3. visualization.py:
  
   Based on the previous data from *1.* and *2.*, we are going to have a data visualization with random numbers (*1.*) as X and after-function numbers (*2.*) as Y. We'll have a scattered plot.


## DSCI560_HW2.ipynb:
  Run all the scripts in order, ans show up all the results with explanations.


## Execute Instructions
#### Note: the instructions are based on the Mac OS environment and Python3

### Step 1: create a virtual environment
  - Clone the code to a local repository
  - In the same directory, run the command `pip install virtualenv` in your command to install the environment management tool.
  - Run the command `virtualenv dsci560H4` to create a virtual environment called *dsci560H4*
    ![image](https://user-images.githubusercontent.com/54614822/97098068-1d446a00-1636-11eb-87f9-016e2a61003b.png)

### Step 2: activate the virtual environment and check dependencies
  - Run the command `source dsci560H4/bin/activate` to activate this virtual environment
  
    ![image](https://user-images.githubusercontent.com/54614822/97098217-909aab80-1637-11eb-8ec5-3dc03d27b2ea.png)
    
  - In the virtual environment, by running the command `pip freeze > requirements_original.txt` to extract dependencies.
  
    ![image](https://user-images.githubusercontent.com/54614822/97098395-9abda980-1639-11eb-8068-490622c9ea54.png)
    
    ![image](https://user-images.githubusercontent.com/54614822/97098440-30f1cf80-163a-11eb-8b9d-2f678d3b478d.png)  
    
    We can see that, there is no dependency.
    
  - However, considering we need the *matplotlib* package to help us do the visualization, we need to run the command first `pip install matplotlib`. 
  
    ![image](https://user-images.githubusercontent.com/54614822/97098471-9cd43800-163a-11eb-9cad-a4092063e8b3.png)
    
  - And then let's check the dependencies again.
  
    ![image](https://user-images.githubusercontent.com/54614822/97098493-b5445280-163a-11eb-8c8c-7d1dde748b4c.png)
    
    ![image](https://user-images.githubusercontent.com/54614822/97098497-c1301480-163a-11eb-91b7-c177d39e4f19.png)
    
    So we know that, we'll have a list of dependencies after an installation of a package.
  
### Step 3: run the scripts
   (Note: Please have a python3 and install a package matplotlib)
   - Run the script *random_numbers.py* first. Run the command `python3 random_numbers.py`. And we can see the result, 1000 generated random numbers.
   
     ![image](https://user-images.githubusercontent.com/54614822/97098716-972c2180-163d-11eb-83cd-4aabcf772336.png)
     
   - Run the script *update_numbers.py* then. Run the command `python3 update_numbers.py`
   
   - Run the script *visualization.py* finally. RUn the command `python3 visualization.py`
 
## The final visualization result
  ![image](https://github.com/Ueny/DSCI560_HW/blob/master/visualization.jpg)
