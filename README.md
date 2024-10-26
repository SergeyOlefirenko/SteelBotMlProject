# SteelBot
Telegramm Bot
## UI Link: https://t.me/SteelBot_bot
## URL: www.steelbot.org
# Short description
This project is a full-fledged application for working with the Telegram UI (Telegram bot), allowing the user to promptly handle data on the mass of various products made from different metals and alloys.
It utilizes machine learning models based on RandomForestRegressor and RandomForestClassifier to predict the assortment and volume of the most in-demand products based on user requests.

It also provides values for area and volume, for example, for spherical objects, enabling quick retrieval of data on load changes in equipment calculations, construction works, logistics, and so on.
The application can also be useful for trading organizations and departments involved in material asset accounting. 
The main advantage of this project is that, primarily, for calculations, it uses 1 or 2 main parameters, for example:
To get the mass of 1 m² of a circle or square, you only need to enter 1 parameter - the diameter or the size of one side. For rectangular sections, the algorithm works in such a way that using the same
logic as for a square - the second parameter, which is, for a square, the length - for a rectangle will be the second side's size, and the length will be the third parameter, absent in the square.
The same logic applies to calculations for sheets, strips, etc. Similar logic is implemented in calculations for square and rectangular pipes.
To calculate the mass of a sphere, only 1 parameter is used - the diameter.
This allows for very quick manipulation of the necessary data when calculating loads during the design of, for example, milling equipment for thermal power plants.

The interaction between the Python server-side and the Telegram UI occurs through a generated API token stored in environment variables.
The interaction between the Telegram UI and the MongoDB database is also carried out through the server using an API.
The user's interaction with the server and the database occurs asynchronously.
## The "data" package contains JSON files:
### "grades.json" 
- contains information about the density of metals and alloys.
### "language-message.json" 
- contains informational messages displayed to the user during registration, depending on the language code of the device using Telegram.
## The "database" package contains:
- "init.py" files defining imports from the "mongoDB_database.py" file
- "mongoDB_database.py" file, where the logic of interacting with the database is defined.
## The "keyboards" package contains:
- "languages" package, which includes language files for keyboards displayed to the user through the API on the Telegram UI, depending on the language code of the device or the language selected by the user.
It also contains "init.py" files defining imports and logic files with the ".py" extension.
__________________________________________________________________________________________________________
# SteelBot
Telegram Bot
## UI Link: https://t.me/SteelBot_bot
## URL: www.steelbot.org
# Short description
This project is a fully functional application designed as a Telegram bot interface, enabling users to quickly process data about the weight of various items made from different metals and alloys. It also provides surface area and volume calculations, for instance, for spherical objects, allowing users to swiftly retrieve data on load changes for equipment design, construction work, logistics, and other processes.

The application can be useful for trading organizations and departments involved in tracking material assets. The main advantage of the project is that calculations require only 1 or 2 primary parameters. For example: to get the mass of 1 m² of a circle or square, it is sufficient to enter just one parameter—either the diameter or the side length. For rectangular sections, the algorithm works similarly, with the second parameter, which for a square is the side length, becoming the width, and the length becoming the third parameter, not needed for squares. The same logic is applied for sheets, strips, etc. The same principle is implemented for calculating the mass of square and rectangular tubes. For spheres, only one parameter—the diameter—is required.
This allows for very quick data retrieval in load calculations, such as in the design of milling equipment for thermal power plants.

## Technical Details
The interaction between the Python backend and the Telegram interface is facilitated by an API token, which is stored in environment variables. Communication between Telegram and the MongoDB database also occurs via the server using the API, and all interactions between the user, server, and database are asynchronous.

## Package Descriptions
## The "data" package contains JSON files:
### "grades.json" 
- contains information about the density of metals and alloys.
### "language-message.json" 
- contains informational messages displayed to the user during registration, depending on the language code of the device using Telegram.
## The "database" package contains:
- "init.py" files defining imports from the "mongoDB_database.py" file
- "mongoDB_database.py" file, where the logic of interacting with the database is defined.
## The "keyboards" package contains:
- "languages" package, which includes language files for keyboards displayed to the user through the API on the Telegram UI, depending on the language code of the device or the language selected by the user.
It also contains "init.py" files defining imports and logic files with the ".py" extension.
## Package "ml"
Includes files responsible for the machine learning model and generating forecast graphs displayed to the user.

## Project Selection: Project Idea/Dataset

## Project Description

This project is a full-fledged application built as a Telegram bot interface, allowing users to quickly process data on the weight of various products made from different metals and alloys. It uses a machine learning model based on RandomForestRegressor and RandomForestClassifier to forecast the nomenclature and volume of the most in-demand products based on user requests. This project was chosen because of its multitasking and multifunctionality, which enables the implementation of various tasks in code and the opportunity to work with real-world, intuitive data to develop machine learning skills.

## What Was Done: Workflow and Process

The first step was to implement the application in Python as a set of calculators for calculating the weight of various engineering products, along with logging user requests into a database.

Once the essential functionality was established, data preparation for the machine learning model began. The method log_result() in the main.py file was updated to call the method analyze_data() from pipe_train_model.py, where data preparation logic for the round_pipe_data_analysis table is implemented. This table is dynamically updated with new data from the primary results table in the 'database' database and provides a DataFrame for machine learning logic. Additional data processing and preparation logic is handled in mongoDB_database.py.

When the program is launched (main.py), it calls the ProductForecast() class, which checks for the minimum required data for model training. This class also contains methods responsible for machine learning: train_regressor, train_classifier, train_all_models, among others.

RandomForestRegressor was chosen as the machine learning model because classification was necessary to determine the target variable. The following classifiers were implemented:


self.classifiers = {
    'nomenclature': self.load_model('classifier_nomenclature.pkl'),
    'material': self.load_model('classifier_material.pkl'),
    'diameter': self.load_model('classifier_diameter.pkl'),
    'wall_thickness': self.load_model('classifier_wall_thickness.pkl')
}

A linear regression model was not suitable because there was no linear relationship between the parameters in the DataFrame, and LinearRegressor did not fit the purpose. Additionally, a forecast graph needed to display the nomenclature, which includes three key parameters: material, diameter, and wall_thickness. Currently, the project focuses on various nomenclatures for round pipes only.

## Project Outcome, Impact, and Real-World Applications

The application can be valuable for trading organizations and departments involved in inventory management of physical assets. The main advantage of this project is that it only requires one or two key parameters for calculations. For instance, to find the weight of a 1 m² circle or square, users only need to enter the diameter or the length of one side. The algorithm works similarly for rectangular sections, with the difference that a second dimension is needed, along with a third parameter, the length, if the shape is a rectangle. The same logic applies to sheets, strips, etc. A similar approach is used for calculating the weight of square and rectangular pipes. For spheres, only the diameter is required. This allows for quick access to essential data when calculating loads, such as in the design of milling equipment for thermal power plants.

As a result of implementing the machine learning model, the application can now forecast product nomenclature and volume based on user requests. The core concept is that each time a user performs calculations, the results are saved in the results table in the database and are dynamically processed in tables used by the machine learning model. These tables are updated whenever the results table data changes. With this data, the model can predict demand for certain products and volumes in specific countries, as user input reflects their interests. The model then tracks the count of requests for each product type, using this as the target variable for classification.

## Challenges or Obstacles and Solutions

The main challenge was displaying a graph where the target variable required multiple parameters. This was resolved by using a classification approach.

### Conclusion: Possible Future Improvements and Project Applications

Potential future improvements include extending the project to support calculations for the full range of products specified in the project. Additional data for the full product range will also be added for use in the machine learning model.

The project could be used by manufacturing and trading companies for production or sales planning based on machine learning-powered forecasts for specific product lines.

For me personally, this project has been an excellent practice for developing a deeper understanding of data analysis and machine learning logic, which I look forward to applying in future projects.














