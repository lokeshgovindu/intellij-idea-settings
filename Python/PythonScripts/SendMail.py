import os
import sys
import argparse

# Import smtplib for the actual sending function
import smtplib

# Import the email modules we'll need
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

__INGRSMTP__    = 'smtp.intergraph.com'
__FROM__        = 'lgovindu@intergraph.com'
__TO__          = ['lgovindu@intergraph.com']

__FROM_MAIL_DEFAULT__   = 'no-reply@hexagongeospatial.com'

COMMASPACESEMICOLON = ';, '
COMMASPACE          = ', '

# ------------------------------------------------------------------------------
# SendTextMail
# ------------------------------------------------------------------------------
def SendTextMail(fromMail=None, fromMailText='', to=[], subject='Hello!', msgText='', label=None):
    """Send Mail"""

    if not to:              return 1

    if not fromMail:        fromMail        = 'no-reply@intergraph.com'
    if not fromMailText:    fromMailText    = 'InterGraph Consulting'
    if label:               subject         = '[' + label + '] ' + subject

    fromMailText = '{} <{}>'.format(fromMailText, fromMail)

    # Create the enclosing (outer) message
    msg = MIMEMultipart()

    msg['Subject']  = subject
    msg['To']       = COMMASPACE.join(to)
    msg['From']     = fromMailText
    msg.preamble    = 'You will not see this in a MIME-aware mail reader.\n'

    # Record the MIME types of parts - text/plain or text/html
    body = MIMEText(msgText, 'plain')

    # Attach parts into message container
    # According to RFC 2046, the HTML message is best and preferred.
    msg.attach(body)

    # Now send or store the message
    composed = msg.as_string()
    s = smtplib.SMTP(__INGRSMTP__)
    failed = s.sendmail(fromMail, to, composed)
    if failed:
        print('failed to send to [%s]' % failed)
    s.quit()

    return 0


# ------------------------------------------------------------------------------
# SendHtmlMail
# ------------------------------------------------------------------------------
def SendHtmlMail(fromMail=None, fromMailText='', to=[], subject='Hello!', msgText='', label=None):
    """Send Mail"""

    if not to:
        return 1

    if not fromMail:
        fromMail = __FROM_MAIL_DEFAULT__

    if not fromMailText:
        fromMailText = 'InterGraph Consulting'

    if label:
        subject = '[' + label + '] ' + subject

    fromMailText = '{} <{}>'.format(fromMailText, fromMail)

    # Create the enclosing (outer) message
    msg = MIMEMultipart()

    msg['Subject'] = subject
    msg['To'] = COMMASPACE.join(to)
    msg['From'] = fromMailText
    msg.preamble = 'You will not see this in a MIME-aware mail reader.\n'

    # # Record the MIME types of parts - text/plain or text/html
    # body = MIMEText(msgText, 'plain')

    # Create the body of the message (a plain-text and an HTML version).

    # Record the MIME types of both parts - text/plain and text/html.
    part2 = MIMEText(msgText, 'html')

    # Attach parts into message container
    # According to RFC 2046, the HTML message is best and preferred.
    # msg.attach(part1)
    msg.attach(part2)

    # Now send or store the message
    composed = msg.as_string()
    s = smtplib.SMTP(__INGRSMTP__)
    s.sendmail(fromMail, to, composed)
    s.quit()

    return 0


# ------------------------------------------------------------------------------
# Example_1
# ------------------------------------------------------------------------------
def Test_SendTextMail():
    SendTextMail(fromMailText='Lokesh Govindu',
                 fromMail='Lokesh.Govindu@hexagongeospatial.com',
                 to=['lgovindu@intergraph.com', 'lgovindu@ingrnet.com'],
                 label='LoGo',
                 subject='Hi', msgText='Hello Lokesh,\n\nHow are you?\n\nThanks,\nLokesh')
    return 0


def GetHtmlTable(table):
    ret = '<table>\n'
    for tr in table:
        ret += '<tr style=\'mso-yfti-irow:0;mso-yfti-firstrow:yes;height:15.75pt\'>'
        for i, td in enumerate(tr):
            if i == 0:
                ret += '<td width=99 style=\'width:74.0pt;border:solid windowtext 1.0pt;background:#D9D9D9;padding:0cm 5.4pt 0cm 5.4pt;height:15.75pt\'><b>{0}</b></td>'.format(td)
            else:
                ret += '<td width=789 style=\'width:592.0pt;border:solid windowtext 1.0pt;border-left:none;padding:0cm 5.4pt 0cm 5.4pt;height:15.75pt\'>{0}</td>'.format(td)
        ret += '</tr>\n'
    ret += '</table>\n'
    return ret


def Test_SendHtmlMail():
    table = []
    table.append([])
    table[-1].append('Source')
    table[-1].append(r'\\atltruck\Products\IDKs\Mainline\DesktopIDKs\DesktopIDKs_2014-10-25_0243_b2598')
    table.append([])
    table[-1].append('Target')
    table[-1].append(r'\\ingrnet.com\in\SGI\GeoSpatial\GS1\ERDAS\Products\IDKs\Mainline\DesktopIDKs\DesktopIDKs_2014-10-25_0243_b2598')
    table.append([])
    table[-1].append('Size')
    table[-1].append(r'6.25 GB (6,714,020,811 bytes)')
    table.append([])
    table[-1].append('Contains')
    table[-1].append(r'11 Files, 0 Folders')
    table.append([])
    table[-1].append('TimeTaken')
    table[-1].append('0:12:18.382000')

    htmlTable = GetHtmlTable(table)
    print(htmlTable)

    html = '<html>\n'
    html += '<style>\n'
    html += 'table, th, td {\n'
    html += 'border: 1px solid black;\n'
    html += 'border-collapse: collapse;\n'
    html += 'font-family: Calibri;\n'
    html += 'font-size: 11.0pt\n'
    html += '}\n'
    html += '</style>\n'
    html += '<body style="font-family:Calibri;font-size:11.0pt;">'
    html += htmlTable
    html += '</body>\n'
    html += '</html>\n'

    SendHtmlMail(fromMailText='Lokesh Govindu', fromMail=__FROM_MAIL_DEFAULT__, to=['lgovindu@intergraph.com'], label='LoGo', subject='Hi', msgText=html)

    return 0


def SendHappyBirthday():
    htmlText = ''
    happyBirthdayFile  = r'E:\Labs\Python\PythonScripts\BestWishes.html'
    # happyBirthdayFile  = r'E:\Labs\Python\PythonScripts\HBD.htm'
    # happyBirthdayFile  = r'E:\Labs\Python\PythonScripts\HappyBirthday.mht'
    fp = open(happyBirthdayFile)
    for line in fp.readlines():
        # print(line)
        htmlText += line
    print('Read completed!')
    fp.close()

    SendHtmlMail(fromMailText='Lokesh Govindu', fromMail=__FROM_MAIL_DEFAULT__, to=['lgovindu@intergraph.com'], label='LoGo', subject='Hi', msgText=htmlText)

    return 0


def SplitMailIds(mailids):
    """Split the string of mail-ids using seperators " ,;" (Quotes for clarity)
Seps : space, comma, semicolon"""
    return mailids.replace(' ', ';').replace(',', ';').split(";")


# ------------------------------------------------------------------------------
# SendMail Main Method
# ------------------------------------------------------------------------------
def main():
    #     example_1()
    parser = argparse.ArgumentParser(fromfile_prefix_chars='@', formatter_class=argparse.ArgumentDefaultsHelpFormatter,
                                     epilog="This script supports fromfile_prefix_chars ( \'@\' ).\
                                     \nArguments that start with any of the specified characters\
                                     \nwill be treated as files, and will be replaced\
                                     \nby the arguments they contain.")

    # Sender
    parser.add_argument('-s', '--sender', type=str, action='store', metavar='SENDER Email-ID', dest='sender',
                        help='The value of the From(Senders email-id): header (required)')

    # Message From Text
    parser.add_argument('--mf', '--msgfrom', '--mft', '--msgfromtext', type=str, action='store', metavar='MailFromText',
                        dest='msgfromtext', help='Text to be displayed in mail from field!')

    # Recipients
    parser.add_argument('-r', '--recipients', type=SplitMailIds, action='store', metavar='RECIPIENT', dest='recipients',
                        required=True,
                        help='A To: header value (at least one required). Seps : \' ,;\' ( Space, Comma & Semicolon )')

    # Subject
    parser.add_argument('--sub', '--subject', type=str, action='store', metavar='SUBJECT', dest='subject', default='Hi',
                        required=False, help='Subject of the mail')

    # Create a mutually exclusive group for text/text from file
    bodyGroup = parser.add_mutually_exclusive_group()

    # Body Text
    bodyGroup.add_argument('--text', '--msgtext', type=str, action='store', metavar='BODYTEXT', dest='text',
                           default='THANKS', required=False, help='Body of the mail')

    # Body Text from file
    bodyGroup.add_argument('--textfile', '--msgtextfile', type=file, action='store', metavar='FILE', dest='textfile',
                           help='TextFile for the body')

    # Mail Label
    parser.add_argument('-l', '--label', type=str, action='store', metavar='LABEL', dest='label', required=False,
                        help='Label for the mail')

    # Parse arguments
    opts = parser.parse_args()

    # Print input args on standard output
    print('Args = [%s]' % opts)

    # If use specified any text file, then body of the text file
    #  should be the contents of text file
    msgBody = opts.textfile.read() if opts.textfile else opts.text

    # Send Mail
    SendTextMail(fromMail=opts.sender, fromMailText=opts.msgfromtext, to=opts.recipients, subject=opts.subject,
             msgText=msgBody, label=opts.label)

    return None


if __name__ == '__main__':
    fileName = os.path.basename(sys.argv[0])
    info = ' ' + fileName + ' ' + 'Begin' + ' '
    print(info.center(80, '-'))
    # exitCode = main()
    # exitCode = Test_SendTextMail()
    exitCode = Test_SendHtmlMail()
    print('ExitCode = [%d]' % exitCode)
    info = ' ' + fileName + ' ' + 'End' + ' '
    print(info.center(80, '-'))
    sys.exit(exitCode)
