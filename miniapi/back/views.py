
import http.client
import json
import ssl
from django.shortcuts import render
from django.conf import settings
import requests

from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt

def home(request):
	return render(request, 'back/home.html')


@csrf_exempt
def request_res(request):
	print("irsen")
	print("irsen")
	print("irsen")
	print("irsen")

	HEADERS = {
	    'Content-type': 'application/xml',
	}


	body = '''
		<Document>
			<GrpHdr>
		   		<MsgId>5000691545452</MsgId>
			   <CreDtTm>3/1/2022 9:28:08 AM</CreDtTm>
			   <TxsCd>5003</TxsCd>
			   <NbOfTxs>1</NbOfTxs>
			   <InitgPty>
			      <Id>
			         <OrgId>
			            <AnyBIC>49</AnyBIC>
			         </OrgId>
			      </Id>
			   </InitgPty>
			   <Crdtl>
			      <Lang>0</Lang>
			      <RoleID>4</RoleID>
			      <LoginID>test_3115</LoginID>
			      <Pwds>
			         <PwdType>1</PwdType>
			         <Pwd>Ankle@123</Pwd>
			      </Pwds>
			   </Crdtl>
			</GrpHdr>
			<EnqInf>
				<IBAN>400016370</IBAN>
				<Ccy>MNT</Ccy>
			</EnqInf>
		</Document>


	'''

	host = '172.29.2.91'
	key = 'C:/Users/delgermaa.s/Desktop/cgw/corptdb.key'
	certificate_secret = 'C:/Users/delgermaa.s/Desktop/cgw/public_key.key'
	# pem = 'C:/Users/delgermaa.s/Desktop/cgw/corptdb.pem'
	certificate_file = 'C:/Users/delgermaa.s/Downloads/corptdb.pem'

	request_url = 'https://172.29.2.91:8080/api/trusted'

	# certificate_file = pem
	# certificate_secret= public_key
	 
	 
	context = ssl.SSLContext(ssl.PROTOCOL_SSLv23)
	context.load_cert_chain(certfile=certificate_file, password=certificate_secret)
	 
	connection = http.client.HTTPSConnection(host, port=8080, context=context)
	 
	connection.request(method="POST", url=request_url, headers=HEADERS, body=body)
	 
	response = connection.getresponse()
	# print(response.status, response.reason)
	data = response.read()
	if isinstance(data, bytes):
	        data = data.decode()

	return render(request, 'back/response.html', {"response": data, 'status': response.status})



def request_with_user_pass(request_url, api_name):

	HEADERS = {
	    'Content-type': 'application/xml',
	}

		# 	JSON_HEADERS = {
	#     'accept': 'application/json',
	#     'Content-type': 'application/json',
	# }

	AUTH = requests.auth.HTTPBasicAuth(
	        "OMS",
	        "TWCMS2019oms#prod",
	    )
  # <PRODUCTID>40757677</PRODUCTID>


	REQUEST_FUNCTION_BODYS = {
		'GetPersonalinfo': 'C:\\Users\\delgermaa.s\\Desktop\\FORAPI\\createrequests\\getPersonInfo.txt',
		'GetAccountinfo': 'C:\\Users\\delgermaa.s\\Desktop\\FORAPI\\createrequests\\getAccountInfo.txt',
		'GetCardinfo': 'C:\\Users\\delgermaa.s\\Desktop\\FORAPI\\createrequests\\getCardInfo.txt',

		'CreateCustomer': 'C:\\Users\\delgermaa.s\\Desktop\\FORAPI\\createrequests\\create_user_xml.txt',
		'CreateAccount': 'C:\\Users\\delgermaa.s\\Desktop\\FORAPI\\createrequests\\create_account_xml.txt',
		'CreateCard': 'C:\\Users\\delgermaa.s\\Desktop\\FORAPI\\createrequests\\create_card_account.txt',
		'ReIssue': 'C:\\Users\\delgermaa.s\\Desktop\\FORAPI\\createrequests\\reissue_request.txt'
	}


	f = open(REQUEST_FUNCTION_BODYS[api_name], "r")
	body = f.read()
	rsp = requests.post(url=request_url, data=body, headers=HEADERS)
	print("rsp")
	print("rsp")
	print("rsp")
	print("rsp", rsp.status_code)
	print("rsp", rsp.text)


host_options = {
	"twcms": "http://172.29.2.105:8888",
	"two": "http://172.29.2.5:2721",
}
	 
request_with_user_pass(host_options['twcms'], "CreateAccount")