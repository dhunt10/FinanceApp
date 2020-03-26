from flask import Flask, request, Response
from flask_restful import Resource, Api, reqparse
from getter import quoteGetter


app = Flask(__name__)
api = Api(app)
class StockTrade(Resource):
    def __init__(self):
        parser = reqparse.RequestParser(bundle_errors=True)
	parser.add_argument('stock',
			    type=str,
			    required=True)
	self.parser = parser

    def get(self):
        args = self.parser.parse_args()
	result = quoteGetter(stock=args.stock.upper())
	return result

api.add_resource(StockTrade, '/trade')

if __name__ == '__main__':
    app.run(host='localhost', port='8080')
