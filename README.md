# backend

This repository hosts the model and other files necessary for the AirBnb application to make predictions. The data used to create the model is hosted on Kaggle 
and can be found [here](https://www.kaggle.com/rudymizrahi/airbnb-listings-in-major-us-cities-deloitte-ml).

### File Structure
    .
    ├── data
    │   ├── test.csv             # Testing data
    │   ├── train.csv            # Training data
    ├── model                    
    │   ├── .gitignore            # Ignored files
    │   ├── model.ipynb           # Model for predictions
    │   ├── model_tools_class.py  # Functions needed for data prep
    │   ├── model_visualizations.py  # Functions needed for data prep
    │   └── requirements.text     # Required packages
    └── README.md
    
   
### Installation

First, you need to clone the repository with the method of you choice (zip download or https). 
Next, in your command line, navigate to the model directory. Then you can install the required packages with the following command:
```
pip3 install -r requirements.txt
```
If you use a diffrerent package manager like conda, you should use that command in place of ```pip3```.
