import hashlib
import base64
import requests
import json
import time

from urllib.parse import urlencode
from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad, pad


class AESCipher(object):
    key = b'ydsecret://query/key/B*RGygVywfNBwpmBaZg*WT7SIOUP2T0C9WHMZN39j^DAdaZhAnxvGcCY6VYFwnHl'
    iv = b'ydsecret://query/iv/C@lZe2YzHtZ2CYgaXKSVfsb7Y4QWHjITPPZ0nQp87fBeJ!Iv6v^6fvi2WN@bYpJ4'
    iv = hashlib.md5(iv).digest()
    key = hashlib.md5(key).digest()

    @staticmethod
    def decrypt(data):
        # AES解密
        cipher = AES.new(AESCipher.key, AES.MODE_CBC, iv=AESCipher.iv)
        decrypted = cipher.decrypt(base64.b64decode(data, b'-_'))
        unpadded_message = unpad(decrypted, AES.block_size).decode()
        return unpadded_message

    @staticmethod
    def encrypt(plaintext: str):
        # AES加密
        cipher = AES.new(AESCipher.key, AES.MODE_CBC, iv=AESCipher.iv)
        plaintext = plaintext.encode()
        padded_message = pad(plaintext, AES.block_size)
        encrypted = cipher.encrypt(padded_message)
        encrypted = base64.b64encode(encrypted, b'-_')
        return encrypted


def get_form_data(sentence, from_lang, to_lang):
    """
    构建表单参数
    :param :sentence:翻译内容
    :param from_lang:源语言
    :param to_lang:目标语言
    :return:
    """
    e = 'fsdsogkndfokasodnaso'
    d = 'fanyideskweb'
    u = 'webfanyi'
    m = 'client,mysticTime,product'
    p = '1.0.0'
    b = 'web'
    f = 'fanyi.web'
    t = time.time()

    query = {
        'client': d,
        'mysticTime': t,
        'product': u,
        'key': e
    }

    # 获取sign值 - -密钥值
    h = hashlib.md5(urlencode(query).encode('utf-8')).hexdigest()

    form_data = {
        'i': sentence,
        'from': from_lang,
        'to': to_lang,
        'domain': 0,
        'dictResult': 'true',
        'keyid': u,
        'sign': h,
        'client': d,
        'product': u,
        'appVersion': p,
        'vendor': b,
        'pointParam': m,
        'mysticTime': t,
        'keyfrom': f
    }
    return form_data


def translate(sentence, from_lang='auto', to_lang=''):
    """
    :param sentence:需翻译的句子
    :param from_lang:源语言
    :param to_lang:目标语言
    :return:
    """
    # 有道翻译网页请求参数
    url = 'https://dict.youdao.com/webtranslate'
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36',
        'referer': 'https://fanyi.youdao.com/',
        'cookie': 'OUTFOX_SEARCH_USER_ID=-805044645@10.112.57.88; OUTFOX_SEARCH_USER_ID_NCOO=818822109.5585971;'
    }
    params = get_form_data(sentence, from_lang, to_lang)

    try:
        res = requests.post(url, headers=headers, data=params)
        # 翻译结果进行AES解密
        cipher = AESCipher
        ret = json.loads(cipher.decrypt(res.text))
        tgt = ret['translateResult'][0][0]['tgt']
        return tgt
    except Exception as e:
        print('翻译失败：', e)
        return '翻译失败：' + sentence


if __name__ == '__main__':
    word = input("请输入你要翻译的文字: ")
    # result = translate(word)
    result = translate(word, 'auto', 'auto')
    print('翻译结果：\n', result)