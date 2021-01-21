# with Evernote  


``` applescript
--Variablesset recipientName to "John Doe"set recipientAddress to "nobody@nowhere.com"set theSubject to "AppleScript Automated Email"set theContent to "This email was created and sent using AppleScript!"--Mail Tell Blocktell application "Mail"		--Create the message	set theMessage to make new outgoing message with properties {subject:theSubject, content:theContent, visible:true}	end tell
```

![code](https://i.imgur.com/OgSFr4j.png)
![result](https://i.imgur.com/V5yTVN2.png)


## Get type of object 

```applescript 
set a to "some text variable"
return class of a
```

## alias to string 

``` applescript
set f to f as stringtell note1 to append text f
```
![alias to string](https://i.imgur.com/w9IUBmp.png)

## Thanks 

* [The Ultimate Beginner's Guide To AppleScript](The Ultimate Beginner's Guide To AppleScript
)
* [APPLESCRIPT: GET NAME OF FILES IN A FOLDER WITHOUT EXTENSION](https://www.geekality.net/2010/11/26/applescript-get-name-of-files-in-a-folder-without-extension/)
