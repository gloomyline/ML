# -*- coding: utf-8 -*-
# @Author: 1211071880@qq.com
# @Date:   2018-05-25 12:00:13
# @Last Modified by:   Administrator
# @Last Modified time: 2018-05-28 16:27:14
import requests, itchat

# tuling robot api key and api url
API_KEY = '0a104fc9bbde4f089fe7395a5f9fa502'
API_URL = 'http://openapi.tuling123.com/openapi/api/v2'

# send requests to tuling robot server with capacity of msg
def get_res(msg):
  try:
    payload = {
      'userInfo': {
        'apiKey': API_KEY,
        'userId': '12312312'
      },
      'perception': {
        'inputText': {
          'text': msg
        }
      }
    }
    r = requests.post(API_URL, json=payload).json()
    return r.get('results')[0]['values']['text']
  except:
    return

# register msg type in itchat
@itchat.msg_register(itchat.content.TEXT)
def reply(msg):
  default_rep = 'I received: ' + msg['Text']
  reply_msg = get_res(msg['Text'])
  return reply_msg or default_rep

if __name__ == '__main__':
  itchat.auto_login()
  itchat.run()
