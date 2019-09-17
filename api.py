import requests
from bs4 import BeautifulSoup
import csv


class DecisionLogicApi():
	def __init__(self, serviceKey, siteUserGuid, profileGuid):
		self.serviceKey = serviceKey
		self.siteUserGuid = siteUserGuid
		self.profileGuid = profileGuid

	def test(self):
		""" Post test request"""
		url = "https://integration.decisionlogic.com/Integration-v2.asmx"
		headers = {"Content-Type" : "text/xml; charset=utf-8",
				   'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.90 Safari/537.36',
				   }
		data = """<?xml version="1.0" encoding="utf-8"?>
					<soap:Envelope xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/">
					  <soap:Body>
					    <HelloWorld xmlns="https://integration.decisionlogic.com" />
					  </soap:Body>
					</soap:Envelope>
				</soap:Envelope>
				"""
		r = requests.post(url, headers=headers, data=data)
		soup = BeautifulSoup(r.text, "lxml")
		return soup.find("soap:body").text


	def SearchBanksByCountry(self, country_code):
		"""
			Search banks by country
		"""
		url = "https://integration.decisionlogic.com/integration.asmx"
		headers = {"Content-Type" : "text/xml; charset=utf-8",
				   'User-Agent' : 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.90 Safari/537.36',
				   "SOAPAction" : "http://www.decisionlogic.com/SearchBanksByCountry",
				   }
		data = f"""<?xml version="1.0" encoding="utf-8"?>
					<soap:Envelope xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/">
					  <soap:Body>
					    <SearchBanksByCountry xmlns="http://www.decisionlogic.com/">
					      <serviceKey>{self.serviceKey}</serviceKey>
					      <countryCode>{country_code}</countryCode>
					    </SearchBanksByCountry>
					  </soap:Body>
					</soap:Envelope>"""
		r = requests.post(url, headers=headers, data=data)
		return r

	def CreateRequest4(self,
					  firstName=None,
					  lastName=None,
					  accountNumber=None,
					  routingNumber=None,
					  customerId=None,
					  contentServiceId=0,
					  emailAddress=''):
		url = "https://integration.decisionlogic.com/Integration-v2.asmx"
		headers  = { "Content-Type" : "application/soap+xml; charset=utf-8"}

		data = 	f"""<?xml version="1.0" encoding="utf-8"?>
					<soap12:Envelope xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns:soap12="http://www.w3.org/2003/05/soap-envelope">
					  <soap12:Body>
					    <CreateRequest4 xmlns="https://integration.decisionlogic.com">
					      <serviceKey>{self.serviceKey}</serviceKey>
					      <siteUserGuid>{self.siteUserGuid}</siteUserGuid>
					      <profileGuid>{self.profileGuid}</profileGuid>
					      <customerId>{customerId}</customerId>
					      <firstName>{firstName}</firstName>
					      <lastName>{lastName}</lastName>
					      <accountNumber>{accountNumber}</accountNumber>
					      <routingNumber>{routingNumber}</routingNumber>
					      <contentServiceId>{contentServiceId}</contentServiceId>
					      <emailAddress>{emailAddress}</emailAddress>
					    </CreateRequest4>
					  </soap12:Body>
					</soap12:Envelope>"""
		r = requests.post(url, headers=headers, data=data)
		return r

	def create_request_and_verify(self,
					  firstName=None,
					  lastName=None,
					  accountNumber=None,
					  routingNumber=None,
					  customerId=None,
					  contentServiceId=0,
					  emailAddress=None):
		url = "https://integration.decisionlogic.com/Integration-v2.asmx"
		headers  = { "Content-Type" : "text/xml; charset=utf-8"}

		data = 	f"""<?xml version="1.0" encoding="utf-8"?>
	<soap:Envelope xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/">
	  <soap:Body>
	    <CreateAndVerifyRequest xmlns="https://integration.decisionlogic.com">
	      <serviceKey>{self.serviceKey}</serviceKey>
	      <siteUserGuid>{self.siteUserGuid}</siteUserGuid>
	      <profileGuid>{self.profileGuid}</profileGuid>
	      <customerId>{customerId}</customerId>
	      <firstName>{firstName}</firstName>
	      <lastName>{lastName}</lastName>
	      <accountNumber>{accountNumber}</accountNumber>
	      <routingNumber>{routingNumber}</routingNumber>
	      <contentServiceId>{contentServiceId}</contentServiceId>
	      <emailAddress>{emailAddress}</emailAddress>
	      <MatchRequestType>{MatchRequestType}</MatchRequestType>
	      <MatchFirstName>{MatchFirstName}</MatchFirstName>
	      <MatchLastName>{MatchLastName}</MatchLastName>
	      <MatchAdressStreet>{MatchAdressStreet}</MatchAdressStreet>
	      <MatchAddressCity>{MatchAddressCity}</MatchAddressCity>
	      <MatchAddressState>{MatchAddressState}</MatchAddressState>
	      <MatchAddressZip>{MatchAddressZip}</MatchAddressZip>
	      <MatchPhoneNumber>{MatchPhoneNumber}</MatchPhoneNumber>
	      <MatchSocialSecurityNumber>{MatchSocialSecurityNumber}</MatchSocialSecurityNumber>
	    </CreateAndVerifyRequest>
	  </soap:Body>
	</soap:Envelope>"""
		print(data)
		r = requests.post(url, headers=headers, data=data)
		return r


	def get_profiles(self):
		url = "https://www.decisionlogic.com/integration.asmx"
		headers = {"Content-Type": "text/xml; charset=utf-8",
				"SOAPAction": "http://www.decisionlogic.com/GetProfiles"}
		data = f"""<?xml version="1.0" encoding="utf-8"?>
			<soap:Envelope xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/">
			  <soap:Body>
			    <GetProfiles xmlns="http://www.decisionlogic.com/">
			      <serviceKey>{self.serviceKey}</serviceKey>
			    </GetProfiles>
			  </soap:Body>
			</soap:Envelope>"""
		r = requests.post(url, headers=headers,data=data)
		return r

	def get_multiple_report_details_from_request_code7(self, request_code):
		url = "https://integration.decisionlogic.com//Integration-v2.asmx"
		headers  = {"Content-Type" : "text/xml; charset=utf-8",
				"SOAPAction": "https://integration.decisionlogic.com/GetMultipleReportDetailsFromRequestCode7"}
		data = f"""<?xml version="1.0" encoding="utf-8"?>
				<soap12:Envelope xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns:soap12="http://www.w3.org/2003/05/soap-envelope">
				  <soap12:Body>
				    <GetMultipleReportDetailsFromRequestCode7 xmlns="https://integration.decisionlogic.com">
				      <serviceKey>{self.serviceKey}</serviceKey>
				      <requestCode>{request_code}</requestCode>
				    </GetMultipleReportDetailsFromRequestCode7>
				  </soap12:Body>
				</soap12:Envelope>"""
		r = requests.post(url, data=data, headers=headers)
		return r

	def search_report_summary(self,
							  siteUserGuid=None,
							  siteUserGuidMode=0,
							  profileGuid=None,
							  profileGuidMode=0,
							  fromDateCreated="1970-06-12T00:00:00",
							  toDateCreated="2100-06-12T00:00:00",
							  timeZoneOffset=8,
							  dateCreatedMode=0,
							  customerIdentifier=None,
							  customerIdentifierMode=0,
							  holderName=None,
							  holderNameMode=0,
							  emailAddress=None,
							  emailAddressMode=0,
							  institution=None,
							  institutionMode=0,
							  routingNumber=None,
							  routingNumberMode=0,
							  accountNumber=None,
							  accountNumberMode=0,
							  status=99,
							  statusMode=0,
							  processStatus=0,
							  processStatusMode=0):
		url = "https://integration.decisionlogic.com/Integration-v2.asmx" 
		headers = {"Content-Type": "application/soap+xml; charset=utf-8"}
		data = f"""<?xml version="1.0" encoding="utf-8"?>
					<soap12:Envelope xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns:soap12="http://www.w3.org/2003/05/soap-envelope">
  					<soap12:Body>
    				<SearchReportSummaryAdvanced4 xmlns="https://integration.decisionlogic.com">
				      <serviceKey>{self.serviceKey}</serviceKey>
				      <siteUserGuid>{siteUserGuid}</siteUserGuid>
				      <siteUserGuidMode>{siteUserGuidMode}</siteUserGuidMode>
				      <profileGuid>{profileGuid}</profileGuid>
				      <profileGuidMode>{profileGuidMode}</profileGuidMode>
				      <fromDateCreated>{fromDateCreated}</fromDateCreated>
				      <toDateCreated>{toDateCreated}</toDateCreated>
				      <dateCreatedMode>{dateCreatedMode}</dateCreatedMode>
				      <timeZoneOffset>{timeZoneOffset}</timeZoneOffset>
				      <customerIdentifier>{customerIdentifier}</customerIdentifier>
				      <customerIdentifierMode>{customerIdentifierMode}</customerIdentifierMode>
				      <holderName>{holderName}</holderName>
				      <holderNameMode>{holderNameMode}</holderNameMode>
				      <emailAddress>{emailAddress}</emailAddress>
				      <emailAddressMode>{emailAddressMode}</emailAddressMode>
				      <institution>{institution}</institution>
				      <institutionMode>{institutionMode}</institutionMode>
				      <routingNumber>{routingNumber}</routingNumber>
				      <routingNumberMode>{routingNumberMode}</routingNumberMode>
				      <accountNumber>{accountNumber}</accountNumber>
				      <accountNumberMode>{accountNumberMode}</accountNumberMode>
				      <status>{status}</status>
				      <statusMode>{statusMode}</statusMode>
				      <processStatus>{processStatus}</processStatus>
				      <processStatusMode>{processStatusMode}</processStatusMode>
				    </SearchReportSummaryAdvanced4>
				  </soap12:Body>
				</soap12:Envelope>"""

		r = requests.post(url, data=data, headers=headers)
		return r


	def get_result(self, request_code):
		r = self.get_multiple_report_details_from_request_code7(request_code)
		soup = BeautifulSoup(r.text, "lxml")
		customer_name = soup.find('nameentered').text
		request_status = soup.find('statustext').text
		print(f"{customer_name}, request_code: {request_code}")
		if request_status != "Successful":
			print(f"Current request status: {soup.find('statustext').text}")
			return
		all_transactions = soup.find_all('transactionsummary5')
		all_transactions = sum([float(t.find('amount').text) for t in all_transactions])
		all_totaldebits = soup.find_all('totaldebits')
		all_totaldebits = sum([float(debits.text) for debits in all_totaldebits])
		all_totalcredits = soup.find_all('totalcredits')
		all_totalcredits = sum([float(credit.text) for credit in all_totalcredits])
		if all_totalcredits/3 < 30000:
			print(f"Decline: client has less than 30000k/month (average {all_totalcredits/3}).")
			return
		if all_totalcredits/3 > 100000:
			print(f"Accept: client has more than 100000k/month (average {all_totalcredits/3}).")
			return
		if all_totalcredits + all_totaldebits > 0:
			print(f"Accept: total debits({all_totaldebits}) more that total credits(average {all_totalcredits/3})")
			return


	def save_report(self, request_code):
		r = get_multiple_report_details_from_request_code7(self.serviceKey, request_code)
		soup = BeautifulSoup(r.text, "lxml")
		reports = soup.find_all("reportdetail5")
		for report in reports:
			elements = report.findChildren()
			names = [el.name for el in elements]
			d = {el.name: el.text for el in elements}
			with open("get_multiple_report_details_from_request_code7.csv", "a+") as file:
				writer = csv.writer(file)
				writer.writerow([k for k in d])
				writer.writerow([d[k] for k in d])


