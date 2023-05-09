Option Explicit

Dim objShell, filePath
Set objShell = CreateObject("WScript.Shell")

If WScript.Arguments.Count = 1 Then
    filePath = WScript.Arguments.Item(0)
    If LCase(Right(filePath, 5)) = ".html" Then
        objShell.Run """C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"" """ & filePath & """", 1, True
        'objShell.Run """C:\Program Files\Mozilla Firefox\firefox.exe"" -new-tab """ & filePath & """", 1, True
        'objShell.Run """C:\Program Files (x86)\Google\Chrome\Application\chrome.exe"" --new-tab """ & filePath & """", 1, True
    Else
        WScript.Echo "Invalid file type. Please specify an HTML file."
    End If
Else
    WScript.Echo "Please drag and drop an HTML file onto this script to open it in Microsoft Edge."
End If
