from flask import jsonify
def api_response(status_code, data=None, message=""):
      return jsonify({
         "status": {
               "code": status_code,
               "message": message
         },
         "data": data
      }), status_code
# def api_response(data=None, status_code=200, message=""):
#     return {
#         "data": data,
#         "status": {"message": message, "status_code": status_code},
#     }, status_code
