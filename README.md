
# Python web.py框架开发web抽奖系统

记录爬坑脱坑的全过程

2017-7-17 23:24:25 1.0版本 web抽奖系统-前端静态版本

2017-7-18 23:25:00 1.1版本 web抽奖系统-Python后端服务端bug超级多的版




Python项目部署运行篇：

本地调试模式：

        1.命令>>Python lucky.py，如果运行正常的话本地默认开启服务端口8080，打开浏览器访问127.0.0.1:8080即可；
        
        2.命令>>Python lucky.py 80,选择开启80端口，如果没有端口冲突的问题开启正常，打开浏览器访问127.0.0.1即可；
        
        
产品环境部署：

        1.推荐配置：Nginx作为HTTP代理服务器处理静态文件，Gunicorn作为应用处理服务器，Supervisor管理应用进程；
        
        2.配置安装篇，建议自行BaiDu、Google解决；
        
        3.Nginx.conf配置段：
        
        
              server {
                  listen       80;
                  server_name  localhost;
                  location / {
                      proxy_pass http://127.0.0.1:5000; 
                      proxy_redirect off;
                      proxy_set_header Host $host:80;
                      proxy_set_header X-Real-IP $remote_addr;
                      proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
                 }
                 location /static {
                    root /var/www/lucky;
                 }
              }
             
        
        
              
       4.Gunicorn配置段：
       
            1.>>gunicorn -w 8 -b 127.0.0.1:5000 lucky:app
            
            2.-w为启动进程数,-b为端口端口和访问方式，0.0.0.0为公开访问，而127.0.0.1为本地访问，lucky:app,lucky为运行的py文件,app为调用方法名；
            
            
       5.Supervisor配置段：
          
