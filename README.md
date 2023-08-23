
# Cherry Leaves Mildew Detection

Powdery Mildew Detector is an app that can predict whether a cherry leaf is healthy or is infected
with powdery mildew. 
The app is capable of predicting on new image data of a given cherry leaf is healthy or infected.

The app has been built using an ML model based on a supervised learning and single-label binary classification. 
A binary classifier is been used as the output to predict a result. 

[View the live project here](https://mildew-detector-cherry-leaves-7ca9c643cfca.herokuapp.com/)

## Introduction


## Dataset Content

* The source of the dataset is [Kaggle](https://www.kaggle.com/codeinstitute/cherry-leaves). For this project, fictitious user stories and business requirements where predictive analytics can be applied to a real-world workplace project or situation.
* The dataset contains +4 thousand images taken from the client's crop fields. The images show healthy cherry leaves and cherry leaves that have powdery mildew.
* The cherry plantation crop is one of the finest products in their portfolio. Infected cherry leaves contain powdery mildew, which is a fungal disease that affects a widerange of plants. This presents a major problem to the busiess as the disease can severely compromise the product quality and output.

The full dataset can be found [here](https://www.kaggle.com/datasets/codeinstitute/cherry-leaves)

![Kaggle Screenshots]()
![Kaggle Screenshots]()

## Business Requirements

- Farmy & Foods is facing a challenge in their main plantation, where their cherry crops have been presenting powdery mildew. Currently, the process is manual verification if a given cherry tree contains powdery mildew. An employee can spend around 30 minutes in each tree, taking a few samples of tree leaves and verifying visually if the leaf tree is healthy or has powdery mildew. If there is powdery mildew, the employee must apply a specific compound to kill the fungus. The time spent applying this compound is 1 minute. The company has thousands of cherry trees, located on multiple farms across the country. As a result, this manual process is not scalable due to the time spent in the manual process inspection.

- To increase efficiency in this process, the IT team suggested an ML system that detects instantly, using a leaf tree image, if it is healthy or has powdery mildew. A similar manual process is in place for other crops for detecting pests, and if this initiative is successful, there is a realistic opportunity to replicate this project for all other crops to further improve business processes. 
- The dataset is a collection of cherry leaf images provided by the client, taken from their crops.

**Therefore, the client is interested in developing an app that has the capability to:**

* 1 - Visually differentiate a healthy cherry leaf from one with powdery mildew.
* 2 - Predict if a cherry leaf is healthy or contains powdery mildew.

## Hypotheses and Validation

1.  Cherry leaves that are infected with powdery mildew have white spots or areas on the leaf surface, or plant stems.
2. The infection of powdery mildew would gradually spread, to eventually cover the plant to have a white powdery/fuzzy appearance all over.
3. This appearance of an infected plant should be a sufficient difference from a healthy leaf, to be able to trian an ML model to detect and predict the presence of powdery mildew on new leaf image data. This can help the client decrease time and labour costs associated with manual detection.
4. The ML model will be able to distinush between a healthy cherry leaf, and one which has been infected with powdery mildew, with an **accuracy of at least 97%.**


## Rationale to map the business requirements to the Data Visualisations and ML tasks

### Business Requiment 1: Data Visualisation

### Business Requirement 2: Classification of Images 



## ML Business Case
* In the previous bullet, you potentially visualised an ML task to answer a business requirement. You should frame the business case using the method we covered in the course.

## Project Methodologies

- Kanban etc - insert info & screenshot & link to github project board. 
- CRISP-DM

## Jupyter Notebooks Process

## Dashboard Design & App Features 
* List all dashboard pages and their content, either blocks of information or widgets, like buttons, checkboxes, images, or any other items, that your dashboard library supports.
* Finally, during the project development, you may revisit your dashboard plan to update a given feature (for example, at the beginning of the project, you were confident you would use a given plot to display an insight, but later, you chose another plot type).


## Project Testing
- Insert test cases 

## Technologies Used

### Languages
- Python

### Data Visualisation & ML Libraries 
- [Pandas](https://pandas.pydata.org/) - Used for data structuring and analysis.
- [Numpy](https://numpy.org/) - Provides mathematical functions to operate with and manipulate arrays.
- [Matplotlib](https://matplotlib.org/) - Used for data visualisation.
- [Seaborn](https://seaborn.pydata.org/#) - Used for statistical graphics, and the stuling of these using themes. 
- [Plotly](https://plotly.com/python/) - Used for plotting data and functions. 
- [Scikit-learn](https://scikit-learn.org/stable/index.html#) - Adopted tools for data processing and predictive analysis. used in this project speicicifically top train the ML Model for the binary classification output. 
- [Tensorflow](https://www.tensorflow.org/) - Used to process and clean the data to search for non-image files. 
- [Keras](https://keras.io/) - Used for the Classification model, and ML pipeline. The neural learning multi-layer network was built using Keras. 
- [Joblib](https://joblib.readthedocs.io/en/latest/) - Used for loading and saving files generated in the project. 

### Version Control 
- Git - Used as a version control for this project. 
- [GitHub](https://github.com/) - The project repository stored here. 

### Development & Hosting
- [Jupyter Notebooks](https://jupyter.org/) - the main development source for running and executing the ML pipelines. 
- [Codeanywhere](https://codeanywhere.com/) - Used as the workspace and development environment for this project. 
- [Streamlit](https://streamlit.io/) - UI host for the dashboard.
- [Heroku](https://www.heroku.com/) - Used to deploy the project. 


## Useful Learning Links about this data 

- [WSU Page on Cherry Powdery Mildew](https://treefruit.wsu.edu/crop-protection/disease-management/cherry-powdery-mildew/)
- [Royal Horticultrual Society Page on Powdery Mildew plant Fungi](https://www.rhs.org.uk/disease/powdery-mildews)
- [Wikipedia Page on Powdery Mildew](https://en.wikipedia.org/wiki/Powdery_mildew)



## Unfixed Bugs
* You will need to mention unfixed bugs and why they were unfixed. This section should include shortcomings of the frameworks or technologies used. Although time can be a significant variable for consideration, paucity of time and difficulty understanding implementation is not a valid reason to leave bugs unfixed.

## Deployment
### Heroku

* The App live link is: https://mildew-detector-cherry-leaves-7ca9c643cfca.herokuapp.com/ 
* Set the runtime.txt Python version to a [Heroku-20](https://devcenter.heroku.com/articles/python-support#supported-runtimes) stack currently supported version.
* In the IDE, using the Heroku CLI, set the Heroku stack to 20. 
* The project was deployed to Heroku using the following steps.

1. Log in to Heroku and create an App
2. At the Deploy tab, select GitHub as the deployment method.
3. Select your repository name and click Search. Once it is found, click Connect.
4. Select the branch you want to deploy, then click Deploy Branch.
5. The deployment process should happen smoothly if all deployment files are fully functional. Click now the button Open App on the top of the page to access your App.
6. If the slug size is too large then add large files not required for the app to the .slugignore file. 


## Main Data Analysis and Machine Learning Libraries
* Here you should list the libraries used in the project and provide an example(s) of how you used these libraries.


## Credits 

LINK TO MALARIA DETECTOR PROJECT
TEMPLATE used 
Streamlit CI lessons
Tensorflow lssons
Wikipedia etc 
* In this section, you need to reference where you got your content, media and from where you got extra help. It is common practice to use code from other repositories and tutorials. However, it is necessary to be very specific about these sources to avoid plagiarism. 
* You can break the credits section up into Content and Media, depending on what you have included in your project. 

### Content 

- The text for the Home page was taken from Wikipedia Article A.
- Instructions on how to implement form validation on the Sign-Up page were taken from [Specific YouTube Tutorial](https://www.youtube.com/).
- The icons in the footer were taken from [Font Awesome](https://fontawesome.com/).

### Media

- The photos used on the home and sign-up page are from This Open-Source site.
- The images used for the gallery page were taken from this other open-source site.



## Acknowledgements (optional)
* Mentor - add detail
* Peers at code institute 
* Neil - add details 