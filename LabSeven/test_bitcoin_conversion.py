import unittest
import bitcoin_conversion
from unittest import TestCase
from unittest.mock import patch

class TestBitcoinConversion(TestCase):

    @patch('bitcoin_conversion.request_rates')
    def test_btc_to_target(self, mock_rates):
        mock_rate = 11437.8983
        example_api_response = {"time":{"updated":"Oct 14, 2020 08:43:00 UTC","updatedISO":"2020-10-14T08:43:00+00:00","updateduk":"Oct 14, 2020 at 09:43 BST"},"disclaimer":"This data was produced from the CoinDesk Bitcoin Price Index (USD). Non-USD currency data converted using hourly conversion rate from openexchangerates.org","bpi":{"USD":{"code":"USD","rate":"11,449.2583","description":"United States Dollar","rate_float":mock_rate}}}
        mock_rates.side_effect = [example_api_response]
        converted = bitcoin_conversion.convert_bitcoin_to_target(1,'USD')
        expected = 11437.8983
        self.assertEqual(expected, converted)

    @patch('requests.get')
    def test_btc_to_target_2(self, mock_requests_get):
        mock_rate = 11437.8983
        example_api_response = {"time":{"updated":"Oct 14, 2020 08:43:00 UTC","updatedISO":"2020-10-14T08:43:00+00:00","updateduk":"Oct 14, 2020 at 09:43 BST"},"disclaimer":"This data was produced from the CoinDesk Bitcoin Price Index (USD). Non-USD currency data converted using hourly conversion rate from openexchangerates.org","bpi":{"USD":{"code":"USD","rate":"11,449.2583","description":"United States Dollar","rate_float":mock_rate}}}

        mock_requests_get().json.return_value = example_api_response

        converted = bitcoin_conversion.convert_bitcoin_to_target(1,'USD')
        expected = 11437.8983
        self.assertEqual(expected, converted)