
# Python web.py框架开发web抽奖系统

V 1.8版 web抽奖系统-取消URL传参改为Session验证，增加接口过滤验证

# 计划2017年8月第一周的周末：

1.接入短信验证码平台（阿里大于），考虑到可实施性和其他原因未接入，Python SDK包已测试通过。

2.实现Session验证，取消通过url传参入参的形式，测试并验证通过，增加接口判断主要通过Session保存用户信息。


# Python项目部署运行篇：


本地调试模式：

        1.命令>>Python lucky.py，如果运行正常的话本地默认开启服务端口8080，打开浏览器访问127.0.0.1:8080即可
        
        2.命令>>Python lucky.py 80,选择开启80端口，如果没有端口冲突的问题开启正常，打开浏览器访问127.0.0.1即可
                   
                   
产品环境部署：


        1.推荐配置：Nginx作为HTTP代理服务器处理静态文件，Gunicorn作为应用处理服务器，Supervisor管理应用进程
        
        2.配置安装篇，建议自行BaiDu、Google解决
        
        3.Nginx.conf配置段：
        
        
              server {
                  listen       80;
                  server_name  localhost;
                  location / {
                      proxy_pass http://127.0.0.1:5000; # 此处为Gunicorn本地运行的端口
                      proxy_redirect off;
                      proxy_set_header Host $host:80;
                      proxy_set_header X-Real-IP $remote_addr;
                      proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
                 }
                 location /static {
                    root /var/www/lucky;
                 }
              }
             
        
        
              
       4.Gunicorn命令解析：
       
           1.>>gunicorn -w 8 -b 127.0.0.1:5000 lucky:app
            
           2.参数说明：-w为启动进程数；-b为端口端口和访问方式，0.0.0.0为公开访问，而127.0.0.1为本地访问；lucky:app,lucky为运行的py文件,app为调用方法名
            
            
       5.Supervisor.conf配置段：
          
       
          [program:myapp]
            directory = /var/www/lucky
            command = gunicorn -w 8 -b 127.0.0.1:5000 lucky:app
          [inet_http_server]
            port = 0.0.0.0:9001
            
          1.运行>>supervisord -c supervisord.conf
          
          2.inet_http_server为应用web管理页面的地址，查看并管理当前正在运行的gunicorn程序
          
          3.设置开机执行脚本命令，测试通过，一套部署Python运行的服务器就搭建好了
          

    
