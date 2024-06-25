<h2>BruteForcePy</h2>
This project is a simple brute force password cracker implemented in Python. It uses the random module to generate password guesses and the pyautogui module to optionally prompt the user for a password. The script attempts to guess the password by generating random combinations of characters until it finds a match.

<h2>Features</h2>

- **Password Input Options:** Users can either provide a password via command line arguments or be prompted to enter a password through a GUI dialog.

- **Brute Force Algorithm:** The script generates random password guesses and checks each guess against the target password.

- **Attempt Logging:** Each guess is printed to the console along with the attempt number.

<h2>Requirements</h2>

- **Python 3.x**
  
- **pyautogui module**

<h2>Installation</h2>

1. Clone the repository:
 ```bash
git clone https://github.com/Its-harin-05/BruteForcePy.git
```
```bash
cd BruteForcePy
```

2. Install the required packages:
```bash
pip install pyautogui
```

<h2>Usage</h2>    

1. Run the application with a password as an argument:
```bash
python app.py -p yourpassword
```

2. Run the application without a password argument to prompt for password input:
```bash
python app.py
```

<h2>Contribution</h2>

Contributions are welcome! Please open an issue or submit a pull request for any improvements or bug fixes.   
