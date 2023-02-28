#!/bin/python3

import js2py

# Just some redundant get functions for values that are reused throughout PoC scripts

def get_cookie():
    
    # Cookies seem to be generated and checked for legitimacy but aren't checked for ACTUAL authentication or authorization
 
    valid_cookie = {"connect.sid": "s%3A3aw2F_O7wq8y1jM2S4ms-JIOOWIj9S1s.v3CLHjDhza6uCsWrIM%2BzgD5dopSOTsTonzb3lSn04NM"}

    return valid_cookie

def get_proxy():

    proxy = { "http":"http://127.0.0.1:8080" }

    return proxy

def get_date_string():

    get_date_string_internal = js2py.eval_js('function get_date_string(){ const raw_date = new Date();var year = raw_date.getFullYear();var month = ("0" + (raw_date.getMonth()+1)).slice(-2);var date = ("0" + (raw_date.getDate()+1)).slice(-2);var hour = ("0" + (raw_date.getHours()+1)).slice(-2);var minute = ("0" + (raw_date.getMinutes()+1)).slice(-2);var second = ("0" + (raw_date.getSeconds()+1)).slice(-2);var formatted_date_string = year + "-" + month + "-" + date + " " + hour + ":" + minute + ":" + second;return formatted_date_string;}')
    date_string = get_date_string_internal()

    return date_string