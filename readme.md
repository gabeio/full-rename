# Full Rename

First of all this focusing solely on OS X/macOS (this may apply to linux somewhat).

Follow the basics of renaming a user from Apple's own documentation:
https://support.apple.com/en-us/HT201548

If you are not a power user/developer you are likely done. If you are a power user/developer I suggest you continue.


## After renaming the user account and the user's home folder.

run: `python relink.py -u <the old username>`

In essence the scripts does a `find` to gather up all of the old user soft links and relinks them to the new user.

Currently this scripts looks for *all* soft symlinks on the entire root directory so make sure you untend to fully rename your username.