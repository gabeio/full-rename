import argparse
import locale
import subprocess
import re

def relink(olduser):
    rex = re.compile(r"\d\d\:\d\d\ (.*)\ \-\>\ (.*)\n")
    # find the new user
    cmd = ["whoami"]
    newuser,error = subprocess.Popen(cmd, stdout=subprocess.PIPE).communicate()
    # newuser = subprocess.check_output(cmd)
    newuser = newuser.replace("\n","")
    print(newuser)
    # find all old (soft) links
    cmd = ['/bin/bash', '-c']
    cmd.append('find / -type l -ls 2>/dev/null | grep {olduser}'.format(olduser=olduser))
    print(cmd)
    found, error = subprocess.Popen(cmd, stdout=subprocess.PIPE).communicate()
    print(found)
    groups = rex.findall(found)
    print(groups)
    # go through all links
    for item in groups:
        dest = item[1].replace(olduser, newuser)
        # relink them to the new user
        cmd = ['/bin/bash', '-c']
        cmd.append('ln -nsf \"{destination}\" \"{origin}\"'.format(origin=item[0], destination=dest))
        print(cmd)
        out, error = subprocess.Popen(cmd, stdout=subprocess.PIPE).communicate()
        print(out)
        print(error)

if __name__ == '__main__':
    locale.setlocale(locale.LC_ALL, 'en_US.UTF-8')
    parser = argparse.ArgumentParser(description='Re-links olduser home directory to current user\'s home directory.')
    parser.add_argument('-u', '--user', dest='olduser', required=True,
                        help='The old user account which will need to relinked.')
    args = parser.parse_args()

    relink(args.olduser)
