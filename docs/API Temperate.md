# 人力工时统计系统

## RESTful API

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
		"employee_name": "王五",
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

根据给定时间段查询过去一段时间内某员工的所有工时信息

### 3. 获取部门所有员工当天（/历史）工时统计

### 4. 获取生产线所有员工当天（/历史）工时统计

## MQTT topics

### 订阅特定员工工号

```
topics/manhours/<employee_ID>
```

每当后台服务同步并计算得到员工的工时信息，会立即发布消息，client 端订阅服务会收到如下示例信息：

```
'{"code": 0, "msg": "success", "data": {"employee_id": "G1234567", "employee_name": "\\u738b\\u4e94", "date": "2020-07-01", "records": [{"production_line": "LINE-5", "schedule_start": "2020-07-01 08:00:00", "actually_start": "2020-07-01 07:53:37", "schedule_end": "2020-07-01 12:00:00", "actually_end": "2020-07-01 12:02:45"}, {"production_line": "LINE-4", "schedule_start": "2020-07-01 14:00:00", "actually_start": "2020-07-01 14:05:25", "schedule_end": "2020-07-01 18:00:00", "actually_end": "2020-07-01 19:54:21"}], "manhours": {"total": 8, "detail": [{"type": 1, "manhours": 4}, {"type": 2, "manhours": 4}]}}}'
```

### 订阅所有员工工号

```
topics/manhours/#
```
<!--stackedit_data:
eyJoaXN0b3J5IjpbMTU5NDg4NzE4OV19
-->