import json
j={
	"msg": 1,
	"code": 0,
	"data": [{
		"tobuilding": "金创电商产业园",
		"touser": "测试",
		"qu": 2050,
		"modtime": "2020-05-19 17:36:44",
		"fromuserfk": 1,
		"tomobileext": "36666",
		"sheng": 1932,
		"bsareadtlfk": 1,
		"shi": 2049,
		"cretime": "2020-05-19 17:36:44",
		"fhshopfk": 1,
		"toaddr": "静福路25号",
		"fhuserfk": 2,
		"tolat4gcj": 1,
		"COUNT": 1,
		"id": 3,
		"tomobile": "13076636096",
		"todoorno": "11",
		"tolng4gcj": 1,
		"frommobile": 1}]}

a=json.dumps(j)
print(type(a))