import requests
import xml.etree.ElementTree as ET
import sys

# Cancel pickup request
# https://www.usps.com/business/web-tools-apis/package-pickup-api.pdf

# API credentials. Found in your signup/welcome email from USPS Web Tools.
api_username = ""
api_password = ""

address    = "1 Main Street"
city       = "Boston"
state      = "MA"
ZIP5       = "06660"
ZIP4       = "1337"

confirmation_number = "WTC9999999999999999999999"


xml = """
        <CarrierPickupCancelRequest USERID="{}" PASSWORD="{}">
        <FirmName></FirmName>
        <SuiteOrApt></SuiteOrApt>
        <Address2>{}</Address2>
        <Urbanization></Urbanization>
        <City>{}</City>
        <State>{}</State>
        <ZIP5>{}</ZIP5>
        <ZIP4>{}</ZIP4>
        <ConfirmationNumber>{}</ConfirmationNumber>
        </CarrierPickupCancelRequest>""".format(api_username, api_password,
                                                address, city, state, ZIP5,
                                                ZIP4, confirmation_number)

data = {
    'API': 'CarrierPickupCancel',
    'XML': xml
}

url = "https://secure.shippingapis.com/ShippingAPI.dll"

response = requests.post(url, data=data)

try:     # basic error handling:
    error_number      = root.find('Number').text
    error_source      = root.find('Source').text
    error_description = root.find('Description').text

    print("Error Number:", error_number)
    print("Error Source:", error_source)
    print("Error Description:", error_description)
except:
    print(response.text)  # dump the entire response to the screen.
