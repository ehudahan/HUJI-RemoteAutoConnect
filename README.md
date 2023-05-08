Sure, here's an example readme file:

# Automate SSH Connection Script for HUJI

## Description

This script automates the SSH connection and passwords for accessing HUJI remote servers. It uses the `pyotp` Python package to generate One-Time Passwords (OTP) and automatically fills in the user credentials, so you won't have to type them each time. 

**IMPORTANT NOTE: This script cancels both passwords needed to connect to your user, so do not share it with anyone.**

## Installation

1. Open the terminal and install the `pyotp` package using either of the following commands:
   ```
   pip3 install pyotp
   ```
   ```
   pip install pyotp
   ```
2. Reset your secret by following these steps:
   - Go to https://registrar.cs.huji.ac.il/hotp and select HOTP.
   - Connect to your HUJI CS user and follow the on-screen instructions until a QR code is displayed.
   - Check your phone to obtain a message with a URL in the format `otpauth://totp/user?secret=XXXXXXXXXXXXXXXX&issuer=CSE`.
   - Copy the orange part (the OTP secret) to the script as described in Step 3.
3. Open the script in a text editor and fill in your credentials:
   - `ssh_command`: the command you type to initiate the SSH remote connection.
   - `my_secret`: the OTP secret obtained in Step 2.
   - `my_pass`: your HUJI CS user password.
4. Save the script and run it with the command:
   ```
   python3 <path_to_script>
   ```
   Note that you should also scan the QR code with the Google Authenticator app in order to have access to your new OTP (the old one will be invalidated).
