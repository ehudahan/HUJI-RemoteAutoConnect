# HUJI CONNECT AUTOMATION
import pexpect as pp
import sys
import pyotp as qr
import getpass


host = 'hm-01'  #river / bagel / aquarium/ waffle...
user = "" # your CS user name
ssh_command = "ssh -CX "+user+"%"+host+"@gw.cs.huji.ac.il"
my_secret = ""   # scan QR of google authenticator to get this
my_pass = getpass.getpass('IDng:')

otp_flag = "OTP"
psw_flag = "IDng"

totp = qr.TOTP(my_secret)
totp = totp.now()

tunnel = pp.spawn(ssh_command)
tunnel.expect(otp_flag)
tunnel.sendline(totp)
tunnel.expect(psw_flag)
tunnel.sendline(my_pass)

tunnel.interact()
