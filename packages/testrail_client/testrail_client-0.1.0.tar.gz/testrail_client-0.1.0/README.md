# Muffin
Using the testrail-api package, you can fetch information for all test cases under a specific suite. This information is useful for automated testing purposes.

## Requirements
```
python 3.10.13
```

## PR Rules
- PR title:   `type: subject`
- commit msg: `type: subject`
- branch:  `type/subject-title-1234`

type可分為 fix, docs, refactor, test, feature

| type     | commit                                  | body                                                                                                                                                                                              |
| -------- | --------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| fix      | fix: upload s3 number data fail         | 問題:<br><br>1. upload s3 number data fail<br>2. …<br><br>原因:<br><br>1. 沒有執行到 upload_number_data function<br>2. …<br><br>調整:<br><br>1. 加上 pytest tag @pytest.mark.usefixtures("upload_number_data") |
| docs     | docs: add README                        | …自由發揮….                                                                                                                                                                                           |
| refactor | refactor: adjust log convention         | …自由發揮….                                                                                                                                                                                           |
| test     | test: add search spoof number cases     | 1. test_spoof_number<br><br>驗證各類偽照號碼格式<br>+886、886、09、+2、+0、02<br>並確認 "name_source": "SPOOF",                                                                                                     |
| feature  | feature: upload test report to testrail | 需求:<br>調整:                                                                                                                                                                                        |


