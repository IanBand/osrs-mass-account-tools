#NoEnv  ; Recommended for performance and compatibility with future AutoHotkey releases.
; #Warn  ; Enable warnings to assist with detecting common errors.
SendMode Input  ; Recommended for new scripts due to its superior speed and reliability.
SetWorkingDir %A_ScriptDir%  ; Ensures a consistent starting directory.

#SingleInstance force ;only one instance of the script can be run at a time

baseUserName := "goatlink+"
accountNumber := 0
handle := "@gmail.com"
passwd := "uIYmdgnF0ySZcjrAsuzP38X5oun78"
email := baseUserName . SubStr("0" . accountNumber, -1) . handle



MsgBox, %email%

^j::

Send, %email% ;%A_TAB% %passwd%
accountNumber++
email := baseUserName . accountNumber . handle
return
