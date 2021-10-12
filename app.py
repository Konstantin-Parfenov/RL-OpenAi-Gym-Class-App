import os
from flask import Flask
from env import MoveToBeacon1D
from flask_restful import reqparse, abort, Api, Resource

app = Flask(__name__)
api = Api(app)

class PerformStep(Resource):
    '''
    Recieve input value by parsing GET request. If the value in not (-1) or (1), send Error message.
    '''
    def get(self):
        # use parser and find the user's input
        args = parser.parse_args()
        user_query = args['input']
        # Get output from model
        if user_query == -1 or user_query == 1 :
            # Get output values from MoveToBeacon1D instance step.
            output_1, output_2 = simulation.step(user_query)
            # create JSON object
            output = {'Location of agent on the x axis': output_1, 'Current reward experienced by the agent': output_2}
            return output
        else:
            output = {'Error': 'Wrong value input.Allowed values -1 and 1'}
            return output
            
class Restart(Resource):
    '''
    Restart the environment and send INFO message.
    '''
    def get(self):
        simulation.reset
        reset_message = {'INFO': 'Simulation state has been rest'}
        return reset_message
        
        

# create new simulation object and reset 
simulation = MoveToBeacon1D()
simulation.reset()

# argument parsing
parser = reqparse.RequestParser()
# allow only int values in the input
parser.add_argument('input',type=int)
        
# Setup the Api resource routing here
# Route the URL to the resource
api.add_resource(PerformStep, '/')
api.add_resource(Restart, '/restart')

    
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0',port=port)