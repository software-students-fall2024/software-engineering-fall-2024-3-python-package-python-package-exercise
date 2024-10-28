import smtplib
from typing import Union, List
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

"""
referenced from: https://realpython.com/python-send-email/
"""
def send_fortune_email(recipient_email: str, fortunes_with_numbers: Union[str, List[str]]
                       , sender_email: str = "garage.swe.team@gmail.com", sender_password: str = "gnjf kukg pqca htnv"):
    """
    Send an email to the recipient with the provided fortunes and lucky numbers.

    Args:
        recipient_email (str): Email address of the recipient.
        fortunes_with_numbers (Union[str, List[str]]): A single fortune and lucky number or a list of fortunes and lucky numbers.
        sender_email (str): Sender's email address.
        sender_password (str): Password for the sender's email account.
    """

    # email body content
    email_content = f"""
Hi {recipient_email.split('@')[0].capitalize()},

I hope this email finds you well and brings a little sparkle to your day!

I've been diving into some fun fortune-telling and lucky number insights lately, and I thought I'd share a bit of positivity and good vibes with you.

"""

    # handle single or multiple fortunes
    if isinstance(fortunes_with_numbers, str):
        email_content += f"{fortunes_with_numbers}\n\n"
    elif isinstance(fortunes_with_numbers, list):
        for fortune in fortunes_with_numbers:
            email_content += f"{fortune}\n\n"
    else:
        raise ValueError("The fortunes_with_numbers argument must be either a string or a list of strings.")
    
    # closing content append
    email_content += """
✨ Fun Tip: Try incorporating your lucky number into your daily routine this week. Whether it's wearing something with that number, scheduling important tasks on the date, or simply keeping an eye out for its appearance, it could add an extra layer of positivity to your days.

Wishing you a week filled with luck, joy, and wonderful surprises!

Feel free to reply and share your thoughts or your own lucky numbers. I'd love to hear from you!

Take care and stay lucky! 🍀

Best wishes,
Garage Team
"""

    msg = MIMEMultipart()
    msg["From"] = sender_email
    msg["To"] = recipient_email
    msg["Subject"] = "Your Fortune and Lucky Numbers 🍀"

    # attach the body text to the email
    msg.attach(MIMEText(email_content, "plain"))

    try:
        with smtplib.SMTP("smtp.gmail.com", 587) as server:
            server.starttls()
            server.login(sender_email, sender_password)
            server.sendmail(sender_email, recipient_email, msg.as_string())
            print("Email sent successfully.")
    except Exception as e:
        print(f"Failed to send email: {e}")


# some testing
fortune = "你好我是奶龙"
fortune1 = "Opportunities are on the horizon."

single_fortune = f"🔮 Your Fortune: {fortune}\n🍀 Your Lucky Number: 7"
multiple_fortunes = [
    f"🔮 Your Fortune: {fortune}\n🍀 Your Lucky Number: 7",
    f"🔮 Your Fortune: {fortune1}\n🍀 Your Lucky Number: 15"
]

if __name__ == "__main__":
    send_fortune_email("ys4689@nyu.edu", single_fortune)
    send_fortune_email("ys4689@nyu.edu", multiple_fortunes)