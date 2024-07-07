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
    
  - For additional technical information on CGI scripts, you can read the official
    Apache documentation at  https://httpd.apache.org/docs/2.4/howto/cgi.html#writing.
    Start at the section labeled "writing" as all the steps before have already been set up.

  - It's important to learn how to read official software documentation as there will be
    times during your software engineering career when no tutorials are available!

# Question 1

If you follow my instructional video (https://www.youtube.com/watch?v=KyN0DTeSE8A),
you would have successfully created test.sh.  Rename it to `q1.sh` and move it inside
**`/usr/lib/cgi-bin/web-admin-cgi-scripts/q1.sh`**

For q2 to q7, you will be writing scripts that are executable on your web server.
For example, we should be able to run your script by visiting:

```
curl http://<your ip>/cgi-bin/web-admin-cgi-scripts/q[1-7].sh
```

NOTE:  For the rest of the questions, I have also provided a running version so you can test
your against the answer key.  However, you are not allowed to use my script in your answer
(i.e. by doing a curl to my scripts)

# Question 2

Write a script called q2.sh that will tell the visitor a random joke.  The
output of this script can be found at http://learn.operatoroverload.com/~jmadar/1280/q2.sh
so you can check your output to see if it is correct.

You can get a new joke by doing a curl on https://icanhazdadjoke.com.  i.e.

```
$ curl https://icanhazdadjoke.com
What did the pirate say on his 80th birthday? Aye Matey!
```

HINT: The answer to this question is very simple.  When q2.sh is called, your
script will simply make a call to icanhazdadjoke.com and return the result.  

# Question 3

Write a script q3.sh that retrieves all titles from the current reddit home page.
A couple of things to note:

  - To retrieve the data that made up of a reddit page, use the following command:
  
    ```
    curl -s -H 'user-agent: asdf' https://old.reddit.com/.json | json_pp
    ```

  - A running version of the script can be found at
    https://learn.operatoroverload.com/~jmadar/1280/q3.sh  





