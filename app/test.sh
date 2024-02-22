curl -X POST http://192.168.45.136:8001/route1/multi \
    -F "files=@model.py" -F 'requests={"in1": "string","in2": true}' \
    -F "files=@model.py" -F 'requests={"in1": "string","in2": true}'