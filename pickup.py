import requests
import xml.etree.ElementTree as ET
import sys

# This software only includes (most) of the "required" parameters.
# It doesn't do everything. See the documentation for additional possible fields:
# https://www.usps.com/business/web-tools-apis/package-pickup-api.pdf

# API credentials. Found in your signup/welcome email from USPS Web Tools.
api_username = ""
api_password = ""

first_name = "Super"
last_name  = "User"
address    = "1 Main Street"
city       = "Anytown"
state      = "MA"
ZIP5       = "10101"
ZIP4       = "1881"
phone      = "5558880000"

# PACKAGES - not complete. See documentation.
# Valid package types:
#   PriorityMailExpress
#   PriorityMail
#   ExpressMail
#   GroundAdvantage
#   Returns
#   International
#   OtherPackages
service_type = "GroundAdvantage"
count        = "1"
weight       = "5"
location     = "Front Door"
# Valid package locations: (not complete. See documentation.)
#   Front Door
#   Back Door
#   Side Door
#   Knock on Door/Ring
#   Bell
#   Mail Room
#   Office
#   Reception
#   In/At Mailbox


xml = """
        <CarrierPickupScheduleRequest USERID="{}" PASSWORD="{}">
        <FirstName>{}</FirstName>
        <LastName>{}</LastName>
        <FirmName></FirmName>
        <SuiteOrApt></SuiteOrApt>
        <Address2>{}</Address2>
        <Urbanization></Urbanization>
        <City>{}</City>
        <State>{}</State>
        <ZIP5>{}</ZIP5>
        <ZIP4>{}</ZIP4>
        <Phone>{}</Phone>
        <Extension></Extension>
        <!-- package contaier -->
        <Package>
        <ServiceType>{}</ServiceType>
        <Count>{}</Count>
        </Package>
        <!-- duplicate the above container for more packages -->
        <EstimatedWeight>{}</EstimatedWeight>
        <PackageLocation>{}</PackageLocation>
        <SpecialInstructions></SpecialInstructions>
        </CarrierPickupScheduleRequest>""".format(api_username, api_password,
                                                  first_name, last_name,
                                                  address, city, state,
                                                  ZIP5, ZIP4, phone,
                                                  service_type, count, weight,
                                                  location)

# To add additional packages, duplicate the <Package></Package> tags. Example:
#        <Package>
#        <ServiceType>GroundAdvantage</ServiceType>
#        <Count>56</Count>
#        </Package>
#        <Package>
#        <ServiceType>PriorityMail</ServiceType>
#        <Count>23</Count>
#        </Package>

data = {
    'API': 'CarrierPickupSchedule',
    'XML': xml
}

url = "https://secure.shippingapis.com/ShippingAPI.dll"

response = requests.post(url, data=data)

print(response.text)
sys.exit()

root = ET.fromstring(response.text)

try:     # basic error handling:
    error_number      = root.find('Number').text
    error_source      = root.find('Source').text
    error_description = root.find('Description').text

    print("Error Number:", error_number)
    print("Error Source:", error_source)
    print("Error Description:", error_description)

except:  # if no error:
    firm_name     = root.find('FirmName').text
    suite_or_apt  = root.find('SuiteOrApt').text
    address       = root.find('Address2').text
    urbanization  = root.find('Urbanization').text
    city          = root.find('City').text
    state         = root.find('State').text
    zip5          = root.find('ZIP5').text
    zip4          = root.find('ZIP4').text
    day_of_week   = root.find('DayOfWeek').text
    date          = root.find('Date').text
    carrier_route = root.find('CarrierRoute').text

    print(" Suite or Apt: {}".format(suite_or_apt))
    print("      Address: {}".format(address))
    print(" Urbanization: {}".format(urbanization))
    print("         City: {}".format(city))
    print("        State: {}".format(state))
    print("         ZIP5: {}".format(zip5))
    print("         ZIP4: {}".format(zip4))
    print("  Day of Week: {}".format(day_of_week))
    print("         Date: {}".format(date))
    print("Carrier Route: {}".format(carrier_route))

