 # Evaluate student's ability by using Machine learning model
 
## TABLE OF CONTENT
1. [INTRODUCTION](#1-Introduction)
2. [PROJECT STRUCTURE](#2-PROJECT-STRUCTURE)
3. [DEMO](#3-DEMO)


### INTRODUCTION
This project is built to evaluate and select the best machine learning model based on metrics like accuracy, F1-score, precision, etc. To predict student's ability 
some Machine Learning models used are:
+ Decision Tree
+ Random Forest
+ Gradient boosting
+ Linear Regression
+ XGBRegressor

### PROJECT-STRUCTURE
- **source:** 
  - **components**
    - **data_ingestion**
    - **data_model_trainer**
    - **data_trainsformation**
  - **pipeline**  
    - ****
    - **predict_pipeline.py**
    - **train_pipeline.py**
  - **exception.py**
  - **logger.py**
  - **utils.py**
- **Notebook:** Log results on running our work
  - **catboost_info**
  - **data**
     - **stud.csv**
  - student_processing.ipynb
  - Training_model.ipynb
- **templates:**
  - **home.html** Front-end code
  - **index.html** 
- **env_DE:** Just virtual environment
- **artifacts:** include train, test, raw data and model has been trained 
- **Analyst_and_Choosing_the_best_model_project.egg-info:** information about author, project, dependency, require, etc.
- **logs:** Log results on running our work
- LICENSE
- .gitignore
- app.py
- readme.md
- requirements.txt
- setup.py
### DEMO
To run appli cation 
Firstly install dependancies.
- Install dependencies:
```bash
pip install -r requirements.txt
```
Secondly, Run project:
```bash
#using venv in windows
env_DE\Scripts\activate
# using venv in linux
source env_DE/bin/activate
#run application
python app.py
```
Finally
open webbrowser at site [http://127.0.0.1:5000/predictdata](http://127.0.0.1:5000/predictdata)
Then choose specifications and our system will provide the prediction of the student

