# Introduction

Bash scripts can be called by a special URL on a web server.

For this assignment, put all your scripts inside
the `/usr/lib/cgi-bin/web-admin-cgi-scripts/` directory.

## NOTES

You will need to use sudo for some of the commands because you will be writing
files / creating links in privileged areas of the filesystems.  Make sure you
review sudo and the file systems from the follow videos (optional but good to
know):

  - https://ww.linkedin.com/learning/learning-linux-command-line-2/user-roles-and-sudo?u=57075641

  - https://www.linkedin.com/learning/learning-linux-command-line-2/the-linux-filesystem?u=57075641

  - The most important directory is `/usr/lib/cgi-bin/`.  If you put an executable file here,
    it can be called from the web via `http://${your_server_ip}/cgi-bin/<script file name>`

  - Put your work inside the `/usr/lib/cgi-bin/web-admin-cgi-scripts/` directory

  - Your script can be accessed by anyone on the Internet!!!
    
  - For scripts to be runnable by the web server, the output requires a couple of special lines.
    Below is the example script:

    ```
    #!/bin/bash
    # need to start with a line identifying the output mime type
    # this is part of the HTTP response header
    echo "content-type: text/plain"

    # an empty line to indicate the end of header and the start
    # of the content
    echo 

    # you can now write the rest of your script below
    echo "Hello World"
    ```









