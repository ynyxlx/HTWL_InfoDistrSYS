from flask  import Flask, request
from flask_restful import reqparse, abort, Api, Resource
import json

app = Flask(__name__)
api = Api(app)

from  config import MODUL_DICT
from InformationMidware import MessageHandle


import logging

MessageHandle(MODUL_DICT)


class Message(Resource):
    def post(self):
        logging.info("getting message")


        get_data = request.get_data()
        logging.info("message:{}".format(get_data))
        
        

        message_dict=json.loads(get_data)
        
        
        
        return MessageHandle.send(message_dict)


'''
@app.route('/message', methods=['POST'])
def send_message(message_json):
    message_dict=json.loads(message_json)
        
    return MessageHandle.send(message_dict)
'''
api.add_resource(Message, '/message')


if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG,
                format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
                datefmt='%a, %d %b %Y %H:%M:%S',
                filename='MessageServer.log',
                filemode='w')	

    logging.info('start')
    app.run(debug=True)
