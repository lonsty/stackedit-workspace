# 快递查询

查询网址：[https://www.ickd.cn/yunda.html](https://www.ickd.cn/yunda.html)

![eUPyod.md.png](https://s2.ax1x.com/2019/08/01/eUPyod.png)

1. 输入单号，点击查询，会弹出验证框
	**此时再按F12打开浏览器的开发者模式，选中 network > js，然后完成验证**
	![eUPOS0.md.png](https://s2.ax1x.com/2019/08/01/eUPOS0.png)
	
2. 验证成功后，会查询快递信息，看下图中出现了一条以单号开头的请求记录

	![eUiVOO.md.png](https://s2.ax1x.com/2019/08/01/eUiVOO.png)

	需要的信息在里面
	![eUisXT.md.png](https://s2.ax1x.com/2019/08/01/eUisXT.png)

4. 复制请求的URL
	![eUiD10.md.png](https://s2.ax1x.com/2019/08/01/eUiD10.png)
	
	> https://biz.trace.ickd.cn/yunda/3848991454726?mailNo=3848991454726&ticket=t02xULvc4qUJJAHzQP3vNW_b8kM9JxoLLHb8-UoowVCNsXVuaRMt6O5ojfUDxo36poflCG3dWCC4xnVmLTo38WjU3U22e1sqBGFLBTNRM6D2ZgtvCgmpGBVvw**&randstr=%40vF6&tk=806d4b8b&tm=1564621583977&callback=_jqjsp&_1564621583978=

5. 把复制的内容用浏览器打开，会得到新的快递数据
	*虽然每次请求的都是同一个URL，但是返回的快递单号内容都是随机的，应该是有些变化的参数没有跟服务器对应上。不过正好，都不用自己生成单号了*
	![eUiX4A.md.png](https://s2.ax1x.com/2019/08/01/eUiX4A.png)

[![eUiVOO.md.png](https://s2.ax1x.com/2019/08/01/eUiVOO.md.png)
<!--stackedit_data:
eyJoaXN0b3J5IjpbMjExODY3ODVdfQ==
-->