# How to use
you visit the pingan gpt model through eagw system.
you have to get the auth token to call the dialog api.

the get auth token api from eagw is:
prd: "http://eagw-gateway-sf.paic.com.cn:80/auth/token/apply"
testing: "http://eagw-gateway-sf-stg.paic.com.cn:80/auth/token/apply"

the dialog api from eagw is:
prd: "http://eagw-gateway-sf.paic.com.cn:80/chatgpt/dialog"
testing: "http://eagw-gateway-sf-stg.paic.com.cn:80/chatgpt/dialog"


app key, secret key, scene id are from:
https://isps-gpt-console-prd-sz.paic.com.cn/ -》大模型服务-》应用接入管理
for example: https://isps-gpt-console-prd-sz.paic.com.cn/#/modelService/appDetail?id=${app_id}

api credential and private key are from:
eagw系统（ https://eagw-admin.paic.com.cn ） -》开放接口-》凭据管理-》（选择对应的服务）-》凭据编码(api credential) and 密钥管理(private key)