from flask import Flask
import os
from env import MoveToBeacon1D
from flask_restful import reqparse, abort, Api, Resource

import numpy as np

app = Flask(__name__)
api = Api(app)

# create new simulation object and reset 
simulation = MoveToBeacon1D()
simulation.reset()

# argument parsing
parser = reqparse.RequestParser()
parser.add_argument('query')

class PredictSentiment(Resource):
    def get(self):
        # use parser and find the user's query
        args = parser.parse_args()
        user_query = args['query']

        # vectorize the user's query and make a prediction
        input = np.array([user_query])
        output_1, output_2 = simulation.step(input)
        
        # create JSON object
        output = {'Location of agent on the x axis': output_1, 'Current reward experienced by the agent': output_2}
        
        return output

# Setup the Api resource routing here
# Route the URL to the resource
api.add_resource(PredictSentiment, '/')


if __name__ == '__main__':
    app.run(debug=True)
    
#if __name__ == "__main__":
#    port = int(os.environ.get("PORT", 5000))
#    app.run(debug=True,host='0.0.0.0',port=port)