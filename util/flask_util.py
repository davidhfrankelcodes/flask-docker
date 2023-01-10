from flask import request

def get_format_param():
    return request.args.get('format', 'app')
