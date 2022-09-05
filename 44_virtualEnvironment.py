# Virtual Environment & Requirements.txt
# So, guys in this tutorial our introduction will be a little different than usual as we are not going be to using Pycharm. 
# Instead today we are going to work with PowerShell. It may be a little unusual but don't worry, as I am here to guide you through every step.

# So, let's get started. First, we will create a new folder. After opening the folder we will now open our PowerShell window using shift + mouse right-click




# Our PowerShell window will appear like this:



# Note that the path it is showing is of our current folder. That is actually the benefit of using shift + mouse right-click.

# Now let us move on to some theoretical concept.

# A virtual environment is a tool or an aid provided to us by Python to keep the dependencies that we have utilized earlier in a few projects, constant. 
# In simple terms, after some duration, Python keeps on launching and upgrading its versions. 
# The new versions yet being better can have certain disadvantages for few users, 
# because, in every new update, new functions are added to the modules, and previous ones may be upgraded. 
# So, there is a chance that a function that used to work earlier will not work as it used to.

# To save ourselves from such situations, Python has allowed us to use of a virtual environment.

# What virtual environment does?
# Virtual Environment saves the current state of our compiler along with the state of their modules and libraries. 
# So in this way even if Python has made certain changes in its module, our virtual environment can still work as before even after years. 
# We can also install different packages and “dataframes” in our virtual environment.

# To be more clear, the virtual environment works exactly the same way as the Python we have installed on our windows/mac/Linux currently because a 
# virtual environment is just a clone of the original product.

# Using Virtual Environments
# To get started, install the virtualenv tool with pip:

# $ pip install virtualenv


# virtualenv is a tool. It is used to create isolated Python environments. 

# To assign a name to your virtual environment, use command

# $ virtualenv virtualenv_name
# After running this command, a directory named folder_name will be created. 
# This directory will contain all the necessary executables to use the packages that the Python project would need. 
# Python packages will be installed in this directory.



# Now, after creating a virtual environment, you need to activate it. When you open the directory, 
# it contains folders like include, lib, script, and tcl. When you open the script folder, you'll find a file activate.bat. 
# You can activate the virtual environment by simply clicking on this file or using the command prompt and writing the following command.

# $ .\virtualenv_name\Scripts\activate


# Once the virtual environment is activated, the name of your virtual environment will appear on the terminal's left side.

# When you are done working in the virtual environment for the moment, you can deactivate it:

# (virtualenv_name)$ deactivate
# Now moving onto requirement.txt. When we run a certain command pip freeze > requirement.txt, 
# a file will be generated in the directory where our virtual environment is based. 
# The file will contain all the details related to the external packages that we have installed along with their versions. 
# By having the requirement.txt file, we can create our virtual machine again easily by downloading all the same libraries, 
# having the same versions by a simple command. 

# freeze > requirement.txt


# The requirement.txt folder will contain data like this:



# We can install all the packages one by one by a command:

# pip install package_name == version


# But in case we have a large number of libraries installed, 
# this will take a massive amount of time as we have to install each one by one so we have another method by which we can install 
# all the packages at once by using the requirement.txt file. The syntax would be:

# pip install -r .\requirements.txt
 

# Code file as described in the video
# numpy==1.15.4
# scikit-learn==0.20.1
# scipy==1.1.0
# sklearn==0.0
