import uuid

from datetime import datetime
import binascii
from typing import List

from Crypto.Hash import SHA256
from Crypto.PublicKey import RSA
from Crypto.Signature import PKCS1_v1_5

from urllib.parse import urlencode
# requests的并发版本
import grequests
# httpx 比 requests 好的地方在于不仅支持同步模式也支持异步模式
import httpx


class PATechGPTClient():

    def __init__(self, api_credential: str, api_private_key: str, app_key: str, secret_key: str, scene_id: str,
                 request_token_url: str = "http://eagw-gateway-sf.paic.com.cn:80/auth/token/apply",
                 dialog_url: str = "http://eagw-gateway-sf.paic.com.cn:80/chatgpt/dialog"):
        # param in eagw
        self.API_CREDENTIAL = api_credential
        self.API_PRIVATE_KEY = api_private_key

        self.REQUEST_TOKEN_URL = request_token_url
        self.DIALOG_URL = dialog_url

        # param in pingan gpt platform
        self.APP_KEY = app_key
        self.APP_SECRET = secret_key
        self.APP_DATA = {
            "appKey": self.APP_KEY,
            "appSecret": self.APP_SECRET
        }
        self.APP_DATA_ENCODE = urlencode(self.APP_DATA)
        self.SCENE_ID = scene_id




    @staticmethod
    def __get_sign(rsaPrivateKey, requestTime):
        '''
        根据秘钥生成签名
        '''
        # 将十六进制字符串转换为二进制字符串
        binary_key = binascii.a2b_hex(rsaPrivateKey)
        # 创建RSA公钥对象
        pkcs8_private_key = RSA.import_key(binary_key)
        # 注意这里签名用的是requestTime, 务必保证是同一个
        h = SHA256.new(requestTime.encode('utf-8'))
        signer = PKCS1_v1_5.new(pkcs8_private_key)
        #  是openApiSignature的值
        signature = signer.sign(h).hex().upper()
        return signature

    def __get_headers_template(self):
        request_time = str(int(datetime.now().timestamp() * 1000))
        headers = {
            "X-Auth-Type": "App_Token",
            "openApiCredential": self.API_CREDENTIAL,
            "openApiRequestTime": request_time,
            "openApiSignature": PATechGPTClient.__get_sign(self.API_PRIVATE_KEY, request_time)
        }
        return headers

    def get_headers_for_token_api(self):
        headers = self.__get_headers_template()
        headers['Content-Type'] = "application/x-www-form-urlencoded"
        headers['openApiCode'] = "API026878"
        return headers

    def __response_success(self, response):
        return response.status_code == 200

    def request_token(self):
        response = httpx.post(self.REQUEST_TOKEN_URL,
                              headers=self.get_headers_for_token_api(),
                              data=self.APP_DATA_ENCODE)
        try:
            if response.status_code == 200:
                return response.json().get("data").get("token")
            else:
                print(response.text)
                return None
        except Exception as error:
            print(error)
            return None

    def get_headers_for_dialog_api(self):
        headers = self.__get_headers_template()
        headers['Content-Type'] = "application/json"
        headers['openApiCode'] = "API026840"
        headers["access_token"] = self.request_token()
        return headers

    def pingan_gpt_inference(self, prompt: str,
                             temperature: float = 0.5,
                             top_p: float = 0.5,
                             session_id: str = None,
                             is_use_own_history: bool = False,
                             own_history: List[str] = [],
                             max_new_tokens: int = 1000,
                             timeout=120) -> str:
        try:
            response = httpx.post(self.DIALOG_URL,
                                  headers=self.get_headers_for_dialog_api(),
                                  json={
                                      "prompt": prompt,
                                      "sessionId": session_id if session_id else str(uuid.uuid4()),
                                      "sceneId": self.SCENE_ID,
                                      "isUseOwnHistory": is_use_own_history,
                                      "ownHistory": own_history,
                                      "max_new_tokens": max_new_tokens,
                                      "generateParam": {"temperature": temperature, "top_p": top_p}

                                  },
                                  timeout=timeout)
        except Exception as error:
            print(error)
            return None
        # httpx的response.json()只能执行一次
        if response.status_code == 200:
            return response.json()
        else:
            print(response.text)
            return None

    def pingan_gpt_batch_inference(self, prompts: List[str],
                                   temperature: float = 0.5,
                                   top_p: float = 0.5,
                                   session_id: str = None,
                                   is_use_own_history: bool = False,
                                   own_history: List[str] = [],
                                   max_new_tokens: int = 1000,
                                   timeout=120,
                                   concurrent=10) -> str:
        try:
            headers = self.get_headers_for_dialog_api()
            rs = [grequests.post(self.DIALOG_URL,
                                 headers=headers,
                                 json={
                                     "prompt": prompt,
                                     "sessionId": session_id if session_id else str(uuid.uuid4()),
                                     "sceneId": self.SCENE_ID,
                                     "isUseOwnHistory": is_use_own_history,
                                     "ownHistory": own_history,
                                     "max_new_tokens": max_new_tokens,
                                     "generateParam": {"temperature": temperature, "top_p": top_p}

                                 },
                                 timeout=timeout) for prompt in prompts]
            responses = grequests.map(rs, size=concurrent)
        except Exception as error:
            print(error)
            return len(prompts) * [None]
        return [response.json() if response else None for response in responses]

