import os
import sys
import Skype4Py

StatusOffline   = 'OFFLINE'
StatusOnline    = 'ONLINE'
StatusInvisible = 'INVISIBLE'
StatusAway      = 'AWAY'
StatusDND       = 'DND'

def main():
    # Create an instance of the Skype class.
    skype = Skype4Py.Skype()

    # Connect the Skype object to the Skype client.
    skype.Attach(Wait=True)

    # Obtain some information from the client and print it out.
    print('Your skype account : [%s (%s)]' % (skype.CurrentUser._Handle, skype.CurrentUser.FullName))
    print('CurrentUserStatus  : [%s]' % skype.CurrentUserStatus)

    # Switch the status
    if skype.CurrentUserStatus == StatusOnline:
        skype.CurrentUserStatus = StatusOffline
    elif skype.CurrentUserStatus == StatusOffline:
        skype.CurrentUserStatus = StatusOnline
    else:
        skype.CurrentUserStatus = StatusInvisible

    print('Status modified to : [%s]' % skype.CurrentUserStatus)

    return 0

if __name__ == '__main__':
    fileName = os.path.basename(sys.argv[0])
    info = ' ' + fileName + ' ' + 'Begin' + ' '
    print(info.center(79, '-'))
    exitCode = main()
    print('ExitCode = [%d]' % exitCode)
    info = ' ' + fileName + ' ' + 'End' + ' '
    print(info.center(79, '-'))
    sys.exit(exitCode)
