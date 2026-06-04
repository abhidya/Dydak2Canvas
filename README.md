# Dydak2Canvas
Syncs Dydaks Urgent deadlines to the canvas calendar

## Archive status

This is an older Canvas automation demo. It is preserved for portfolio context; Canvas APIs, auth flows, and the original course website may have changed.

## Credential hygiene

Do not commit real Canvas usernames, passwords, auth tokens, or personal grade links. Use `config.ini` only as a template and keep real local credentials in an untracked copy.


## Offline demo

```bash
python3 test_form.py
```

The demo parses `fixtures/dydak_deadlines.html` and prints planned calendar
deadlines with `network_calls=0`. It does not log in to Canvas or call the
Canvas API.

# Historical setup

The original workflow asked users to download `test_form.exe` and edit `config.ini`.
That binary is retained only as an archive artifact; prefer the Python fixture
demo above when reviewing the repository.

Open the confi.ini file and add your information as follows 
```

[information]
Username: myusername
Password: REPLACE_WITH_LOCAL_PASSWORD
Link-to-Personal-Site: http://www.math.utk.edu/~dydak/251Sp18/Grades/poop.html
Canvas-Auth: REPLACE_WITH_CANVAS_TOKEN
```


Use your Canvas username and password

Use your personal Webpage that Dydak sent you

And use the Canvas auth token you generated 


# how to gen canvas auth token

https://i.imgur.com/suIYorc.gif


# how to run program

https://i.imgur.com/jgGvAgq.gifv
