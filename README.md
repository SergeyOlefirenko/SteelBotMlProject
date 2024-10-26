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
