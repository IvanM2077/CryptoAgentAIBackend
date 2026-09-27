from flask import Flask, jsonify

from models.requestDto.coinRequestDto import CoinDetailRequestDto
from models.requestDto.simpleRequestDto import SupportedVsCurrenciesRequestDto
from services.apicaller import ApiCaller


app = Flask(__name__)

api = ApiCaller()


@app.route("/bitcoin")
def bitcoin():
    request = CoinDetailRequestDto(
        coin_id="bitcoin",
        market_data=True
    )
    data = api.call(request)
    return jsonify(data)

@app.route("/currencies")
def coins():
    request = SupportedVsCurrenciesRequestDto()
    data = api.call(request)
    return jsonify(data)

if __name__ == "__main__":
    app.run(debug=True)
