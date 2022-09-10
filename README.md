# Pharmaceutical_sales_prediction
**Data and Features**
- The data for this challenge can be found here. Or you can find it also here: Rossmann Store Sales | Kaggle

**Data fields**
 
Most of the fields are self-explanatory. The following are descriptions for those that aren't.
  - **Id **- an Id that represents a (Store, Date) duple within the test set
   - **Store -** a unique Id for each store
   -** Sales** - the turnover for any given day (this is what you are predicting)
   - **Customers **- the number of customers on a given day
   - **Open **- an indicator for whether the store was open: 0 = closed, 1 = open
   - **StateHoliday **- indicates a state holiday. Normally all stores, with few exceptions, are closed on state holidays. Note that all schools are closed on public holidays and weekends. a = public holiday, b = Easter holiday, c = Christmas, 0 = None
   - **SchoolHoliday **- indicates if the (Store, Date) was affected by the closure of public schools
   - **StoreType** - differentiates between 4 different store models: a, b, c, d
   - **Assortment** - describes an assortment level: a = basic, b = extra, c = extended. Read more about assortment here
   - **CompetitionDistance** - distance in meters to the nearest competitor store
   - **CompetitionOpenSince[Month/Year] **- gives the approximate year and month of the time the nearest competitor was opened
   - **Promo **- indicates whether a store is running a promo on that day
   - **Promo2 -** Promo2 is a continuing and consecutive promotion for some stores: 0 = store is not participating, 1 = store is participating
   - **Promo2Since[Year/Week] **- describes the year and calendar week when the store started participating in Promo2
   - **PromoInterval** - describes the consecutive intervals Promo2 is started, naming the months the promotion is started anew. E.g. "Feb,May,Aug,Nov" means each round starts in February, May, August, November of any given year for that store

**Project Structure**
- **images:**
 - images/ the folder where all snapshot for the project are stored.
- logs:
 - logs/ the folder where script logs are stored.
**- mlruns:**
 - mlruns/0/ the folder that contain auto generated mlflow runs.
**- data:**
 - .dvc the folder where the dataset versioned csv files are stored.
- **.dvc:**
- .dvc/: the folder where dvc is configured for data version control.
- .github:
 - .github/: the folder where github actions and CML workflow is integrated.
-** .vscode:**
 - .vscode/: the folder where local path fix are stored.
-** models:**
 - 09-009-2022-00-23-23-53.91%.pkl: the folder where model pickle files are stored.
- **notebooks:**
   - notebook fiel used to preprocessing and modeling notebook
**- src:**
 - a python script for cleaning pandas dataframes.
- **tests:**
 - **tests/: **the folder containing unit tests for the scripts.
- requirements.txt: a text file lsiting the projet's dependancies.
-** README.md:** Markdown text with a brief explanation of the project and the repository structure.
- **Dockerfile:** build users can create an automated build that executes several command-line instructions in a container.
 ** Installation guide**
 The project covers the following:
            
      - Data preprocessing
      - EDA( Exploratory Data Analysis)
      - Sklearn Pipleine 
      - Machine Learning modelning
      - Deep Learning (LSTM) modeling
  **To install**
  git clone https://github.com/BirhanuGebisa/Pharmaceutical_sales_prediction.git