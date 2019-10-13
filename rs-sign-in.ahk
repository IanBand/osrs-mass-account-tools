#NoEnv  ; Recommended for performance and compatibility with future AutoHotkey releases.
; #Warn  ; Enable warnings to assist with detecting common errors.
SendMode Input  ; Recommended for new scripts due to its superior speed and reliability.
SetWorkingDir %A_ScriptDir%  ; Ensures a consistent starting directory.
#SingleInstance force ;only one instance of the script can be run at a time



handle := "@gmail.com"
FileRead, passwd, %A_ScriptDir%\password.txt
FileRead, baseUserName, %A_ScriptDir%\user.txt

Input, accountID, L2, {Enter} ;L2 assumes account IDs can only be 00-99

email := baseUserName . {+} . accountID . handle

;MsgBox, %email%
Send, %email% 
Send, %A_TAB% 
Send, %passwd%

Q::
    Exit

;TODO: loop, switch windows, email regex

