import argparse
import imaplib
import email
import sqlite3
from datetime import datetime, timedelta

def create_table():
    conn = sqlite3.connect('emails.db')
    c = conn.cursor()

    # create table if it doesn't exist
    c.execute('''CREATE TABLE IF NOT EXISTS emails (id INTEGER PRIMARY KEY AUTOINCREMENT,from_email TEXT, subject TEXT, date TEXT)''')

    conn.commit()
    conn.close()

def insert_email(from_email, subject, date):
    conn = sqlite3.connect('emails.db')
    c = conn.cursor()

    # insert email into database
    c.execute('INSERT INTO emails (from_email, subject, date) VALUES (?, ?, ?)',(from_email, subject, date))

    conn.commit()
    conn.close()

def get_emails(name, duration):
    # connect to IMAP server
    mail = imaplib.IMAP4_SSL('imap.gmail.com')
    mail.login('vinz223665@gmail.com', 'ugyltbuxtnpmzijl')
    mail.select('inbox')

    # search for emails by name or time duration
    if name:
        search_criteria = f'(FROM "{name}")'
    elif duration:
        date_since = (datetime.now() - timedelta(days=duration)).strftime('%d-%b-%Y')
        search_criteria = f'(SINCE "{date_since}")'
    else:
        raise ValueError('Either name or duration must be provided')

    # fetch emails that match the search criteria
    _, data = mail.search(None, search_criteria)
    emails = []
    for num in data[0].split():
        _, msg_data = mail.fetch(num, '(RFC822)')
        email_data = email.message_from_bytes(msg_data[0][1])
        from_email = email_data['From']
        subject = email_data['Subject']
        date = email_data['Date']

        insert_email(from_email, subject, date)

        emails.append({
            'From': from_email,
            'Subject': subject,
            'Date': date
        })

    # disconnect from IMAP server
    mail.close()
    mail.logout()

    return emails

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Fetch emails by name or time duration')
    parser.add_argument('--name', type=str, help='Fetch emails by name of sender')
    parser.add_argument('--duration', type=int, help='Fetch emails by time duration (in days)')

    args = parser.parse_args()

    create_table()

    emails = get_emails(args.name, args.duration)

    for email in emails:
        print(f"From: {email['From']}\nSubject: {email['Subject']}\nDate: {email['Date']}\n")
