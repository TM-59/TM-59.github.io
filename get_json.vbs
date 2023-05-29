' JSONファイルのパス
jsonPath = "\TM-59.github.io\example.json"

' ファイルを開く
Set fso = CreateObject("Scripting.FileSystemObject")
Set jsonFile = fso.OpenTextFile(jsonPath, 1)

' ファイルからテキストを読み込む
jsonText = jsonFile.ReadAll()

' JSONを解析してオブジェクトに変換する
Set jsonObj = JsonConverter.ParseJson(jsonText)

' オブジェクトのプロパティを表示する
For Each key In jsonObj.Keys
    WScript.Echo key & ": " & jsonObj(key)
Next
