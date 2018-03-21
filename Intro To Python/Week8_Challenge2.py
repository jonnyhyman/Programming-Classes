''' Launch a website on your web browser with python!

                    REMEMBER

    ... With great power comes great responsibility...

    Challenges:

        1. Make it go to a different website
        2. Make it open as a new WINDOW, instead of new TAB

'''



import webbrowser
webbrowser.open('http://google.com', new=2)

# SPOILER ALERT
# new = 0? browser decides
# new = 1? new window
# new = 2? new tab

# How do I know this? Go here and scroll down a bit and read
'''https://docs.python.org/3.6/library/webbrowser.html'''
