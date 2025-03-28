Program Features:

-Tkinter-based GUI with a futuristic dark theme
-Calculates compound interest for a specified number of trades
-Displays a detailed breakdown of each trade
-Shows final amount and total percentage gain
-Error handling for invalid inputs
-CSV Export Feature
	-Added "Export to CSV" button
	-Generates unique filenames using:
	-Base name: "compound_interest_calculation"
	-Timestamp
	-Incremental counter to prevent overwriting
	-Saves calculation details (trade number, amount, gain)


-The current script is a standalone desktop app
-Can be distributed using PyInstaller to create an executable
-Install PyInstaller: pip install pyinstaller
-Create executable: pyinstaller --onefile --windowed compound_interest_calculator.py

Screenshots

![ScreenShot of the app](assets/screenshot_compount_interest.jpg)  