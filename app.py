import os
from flask import Flask
from env import MoveToBeacon1D
from flask_restful import reqparse, abort, Api, Resource

app = Flask(__name__)
api = Api(app)

# create new simulation object and reset 
simulation = MoveToBeacon1D()
simulation.reset()

# argument parsing
parser = reqparse.RequestParser()
parser.add_argument('input',type=int)

class PredictSentiment(Resource):
    def get(self):
        # use parser and find the user's query
        args = parser.parse_args()
        user_query = args['input']
        # Get output from model
        print(type(user_query))
        if type(user_query)==int:
            output_1, output_2 = simulation.step(user_query)
        else:
            output_1 = 'Error'
            output_2 = 'Error'
        # create JSON object
        output = {'Output_1': output_1, 'Output_2': output_2}
        return output
        
# Setup the Api resource routing here
# Route the URL to the resource
api.add_resource(PredictSentiment, '/')


#if __name__ == '__main__':
#    app.run(debug=True)
    
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='127.0.0.1',port=port)