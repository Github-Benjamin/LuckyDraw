
# Python web.py框架开发web抽奖系统

这一个版本呢，实现了后端抽奖，前端利用ajax进行数据交互。


# 1.2版抽奖接口说明：

1.host:/luckynumber；
接口仅用查询用户剩余抽奖次数查询，返回JSON数据；

示例数据：
	{
		luckynnumber: 0
	}
	
2.host:/lucky；
抽奖接口，请求接口进行随机抽奖并返回JSON数据；

示例数据1：
	{
	  "playnum": -1, 
	  "id": "Null", 
	  "angles": 0, 
	  "name": "抽奖次数不足"
	}	

	
示例数据2：
	{
	  "playnum": -1, 
	  "id": "Null", 
	  "angles": 0, 
	  "name": "抽奖次数不足"
	}	
