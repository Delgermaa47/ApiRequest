
import os
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
		'GetPersonalinfo': 'C:\\Users\\delgermaa.s\\Desktop\\sys\\TMCMS doc\\FORAPI\\createrequests\\getPersonInfo.txt',
		'Getaccntnoinfo': 'C:\\Users\\delgermaa.s\\Desktop\\sys\\TMCMS doc\\FORAPI\\createrequests\\getaccntnoInfo.txt',
		'GetCardinfo': 'C:\\Users\\delgermaa.s\\Desktop\\sys\\TMCMS doc\\FORAPI\\createrequests\\getCardInfo.txt',

		'CreateCustomer': 'C:\\Users\\delgermaa.s\\Desktop\\sys\\TMCMS doc\\FORAPI\\createrequests\\create_user_xml.txt',
		'Createaccntno': 'C:\\Users\\delgermaa.s\\Desktop\\sys\\TMCMS doc\\FORAPI\\createrequests\\create_accntno_xml.txt',
		'CreateCard': 'C:\\Users\\delgermaa.s\\Desktop\\sys\\TMCMS doc\\FORAPI\\createrequests\\create_card_accntno.txt',
		'ReIssue': 'C:\\Users\\delgermaa.s\\Desktop\\sys\\TMCMS doc\\FORAPI\\createrequests\\reissue_request.txt'
	}


	body = utils.read_data(REQUEST_FUNCTION_BODYS[api_name])
	rsp = requests.post(url=request_url, data=body, headers=HEADERS)
	print("rsp")
	print("rsp")
	print("rsp")
	print("rsp", rsp.status_code)
	print("rsp", rsp.text)

# request_url = "http://17
# 2.29.2.105:8888"
# api_name =  'CreateCustomer'
# request_with_user_pass(request_url, api_name)
def request_with_ebarimt(function_name):

	JSON_HEADERS = {
	    'accept': 'application/json',
	    'Content-type': 'application/json',
	}

	body = {
		   "data":{
		      "allamount":"1000.00",
		      "cashAmount":"0.00",
		      "nonCashAmount":"1000.00",
		      "customerNo":"",
		      "billType":"1",
		      "returnBillId":"",
		      "invoiceId":"",
		      "stock_code":"22",
		      "rrn":"111111111999",
		      "bankId":"04",
		      "terminalId":"95000011",
		      "approvalCode":"930912",
		      "amount":"1000.00"
		   }
		}

	request_url = "http://172.29.2.23/posapp/" + function_name
	rsp = requests.post(url=request_url, data=json.dumps(body), headers=JSON_HEADERS)

# select 
#     rec.recno,
#     rec.invstatus,
#     rec.rectype,
#     rec.invno,
#     sent.INVSTATUS,
#     sent.invtype
# from vbismiddle.invoicerec rec
# inner join vbismiddle.invoicesent sent
# on rec.invno=sent.invno
# where rec.recno=45


def tdb_invioce(key, name):
	
	body1 = {
		"invno": "",
		"custno": "90400005627",
		"fname": "Дэлгэрмаа Санжжав",
		"amount": "5001",
		"accntno": "400016379",
		"handphone": "999999",
		"invdesc": "test1",
		"rec_datas": json.dumps([
		 		{
			"recno": "",
			"fname": "Мөнхнаран",
			"custno": "90459013017",
			"accntno": "469017000",
			"amount": "2500",
			"handphone": "88888888",
		}
		])
		
	}

	body2 = {
		"invno": "",
		"custno": "90400005627",
		"fname": "Дэлгэрмаа",
		"amount": "5001",
		"accntno": "400016379",
		"handphone": "999999",
		"invdesc": "test2",
		"rec_datas": json.dumps([
		 			{
			"recno": "",
			"fname": "Мөнхнаран",
			"custno": "90459013017",
			"amount": "2500",
			"accntno": "469017000",
			"handphone": "88888888",
		},
		{
			"recno": "",
			"custno": "90400005018",
			"fname": "Жавхлан",
			"amount": "2500",
			"accntno": "400012440",
			"handphone": "89898989",
		}
		])
		
	}

	body3 = {
		"invno": "",
		"custno": "90400005018",
		"fname": "Мөнхнаран",
		"amount": "5001",
		"accntno": "400012440",
		"handphone": "89898989",
		"invdesc": "test3",
		"rec_datas": json.dumps([
		 	{
				"recno": "",
				"custno": "90400005627",
				"fname": "Дэлгэрмаа",
				"amount": "2500",
				"accntno": "400016379",
				"handphone": "999999",
			},
		])
		
	}
	
	rec_request = {
		"invoice_save": 'invoice-save',
		"invoice_template": 'invoice-template-save',
	}

	data ={
		"body1": body1,
		"body2": body2,
		"body3": body3,
	}
	url = 'http://localhost/api/{}'.format(rec_request[key])
	rsp = requests.post(url=url, data=data[name])
	print("hel")
	print("hel")
	print("hel")
	print("hel")
	print("hel")
	print(rsp.status_code)
	# print(rsp.json())
	print(rsp.text)


def invoice_edit(id):
	
	body = {
		"invno":"155",
		"amount":"6000",
		"custno":"90400005627",
		"accntno":"400016379",
		"invdesc":"testing_edit",
		"created_at":"12-APR-22 06.04.28.946150 PM",
		"updated_at":"12-APR-22 06.04.28.946150 PM",
		"rec_datas": json.dumps([
			{
				"recno":"57",
				"invno":"155",
				"amount":"2500",
				"custno":"90459013017",
				"accntno":"469017000",
				"handphone":"88888888",
				"created_at":"12-APR-22 06.04.28.954385 PM",
				"updated_at":"12-APR-22 06.04.28.954385 PM"
			}
		])
		}
	request_url = 'http://localhost/api/invoice-edit/' + str(id)
	rsp = requests.post(url=request_url, data=body)
	print("hel")
	print("hel")
	print("hel")
	print("hel")
	print("hel")
	print(rsp.status_code)
	print(rsp.json())


def invoice_rec_list(key, body):
	rec_request = {
		"inv_list": 'invoice-sent-list',
        'invsent_history': "invsent-history",
        'invrec_history': "invrec-history",
        'invtemplate_list': "invtemplate-list",
		'invoice_recieve_list': "invoice-recieve-list"
	}

	request_url = 'http://localhost/api/{}'.format(rec_request[key])
	rsp = requests.post(url=request_url, data=body)
	print("hel")
	print("hel")
	print("hel")
	print("hel")
	print("hel")
	print(rsp.status_code)
	print(rsp.text)
	# print(rsp.json())


def get_to_ivn_function(key, get_type):
	rec_request = {
		"paid": 'invoice-recieve-paid',
		"rec_detail": 'invoice-rec-detail',
		"approve": 'approve-rec-invoice',
		"revoke": 'delete-recieve-invoice',
		
		"get_fname": 'get-fname',

		"invoice_detail": 'invoice-detail',
		"invoice_remove": 'delete-sent-invoice',
		   
        # 'invsent_history_detail': "invsent-history-detail",
        # 'invrec_history_detail': "invrec-history-detail",

        # 'invtemplate_detail': "invtemplate-detail",

	}
	request_url = 'http://localhost/api/{}/{}'.format(rec_request[get_type], key)
	print("bla")
	print("bla")
	print("bla", request_url)
	rsp = requests.get(url=request_url)
	print("res")
	print("res")
	print("res")
	print(rsp.status_code)
	print(rsp.text)
	# print(rsp.json())

key='invoice_template'
key='invoice_save'
name="body2"
# tdb_invioce(key, name)


# invoice_edit(id)


body = {
	"perpage": 20,
	"last_id": "",
	"is_prev_page": False,
	"sort_name": "invno",
	"sort_type": "asc",
	"custom_query":""
}
key = 'invoice_recieve_list'
# invoice_rec_list(key, body)

id = 31
name = 'invoice_detail'
get_to_ivn_function(id, name)