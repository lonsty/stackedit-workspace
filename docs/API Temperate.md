# 人力工时统计系统

### 1. 获取员工当天工时信息

#### 请求地址

```
/api/v1/manhour/today/<employee ID>
```

#### 请求方式

`GET`

#### 传入参数

TBD

#### 传参举例

```
/api/v1/manhour/today/G1234567
```

#### 返回参数

TBD

#### 返回举例

```json
{
	"code": 0,
	"msg": "success",
	"data": {
		"employee_id": "G1234567",
		"employee_name": "王五"，
		"date": "2020-07-01",
		"records": [
			{	
				"production_line": "LINE-5",
				"schedule_start": "2020-07-01 08:00:00",
				"actually_start": "2020-07-01 07:53:37",
				"schedule_end": "2020-07-01 12:00:00",
				"actually_end": "2020-07-01 12:02:45",
			},
			{	
				"production_line": "LINE-4",
				"schedule_start": "2020-07-01 14:00:00",
				"actually_start": "2020-07-01 14:05:25",
				"schedule_end": "2020-07-01 18:00:00",
				"actually_end": "2020-07-01 19:54:21",
			},
		],
		"manhours": {
			"total": 8,
			"detail": [
				{
					"type": 1,
					"manhours": 4
				},
				{
					"type": 2,
					"manhours": 4
				},
			]
		}
	}
}
```

### 2. 获取员工历史工时信息

根据给定时间段查询过去一段时间内的
<!--stackedit_data:
eyJoaXN0b3J5IjpbLTE2MjYyNTU1MDNdfQ==
-->