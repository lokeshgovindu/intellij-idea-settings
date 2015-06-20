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
    skype.Attach()
    currentUser = skype.CurrentUser

    # Obtain some information from the client and print it out.
    print('Your skype account : [%s (%s)]' % (currentUser.Handle, currentUser.FullName))
    print('CurrentStatus : [%s]' % skype.CurrentUserStatus)

    # skype.SendMessage('madhu.sameena', 'TestMessage!')
    # chat = skype.CreateChatWith('madhu.sameena')
    # chat.SendMessage('GMAL :-)')

    mad = skype.User('madhu.sameena')
    while True:
        if mad._GetOnlineStatus() == StatusOnline:
            chat = skype.CreateChatWith('madhu.sameena')
            chat.SendMessage('GMAL :-)')
            break

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
