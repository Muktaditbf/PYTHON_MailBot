import smtplib

# 1. Setup Variables (Use Quotes!)
my_email = "USE YOUR EMAIL HERE"
my_password = "USE YOUR PASSWORD HERE(not the email pass its app authenticator pass)" # Keep the spaces
receiver_mail = "USE RECEIVER EMAIL HERE"

# 2. Connect to Gmail's Door (Port 587)
server = smtplib.SMTP("smtp.gmail.com", 587)
server.starttls() # Encrypt the connection

# 3. Login
server.login(my_email, my_password)

# 4. Create Message
message = "Subject: Hello from Python\n\n This is an auto email."

# 5. Send
server.sendmail(my_email, receiver_mail, message)

print("Email sent successfully!")