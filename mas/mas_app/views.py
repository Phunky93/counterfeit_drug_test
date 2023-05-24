from django.shortcuts import render
from .models import *
import json
from django.core import serializers
from django.http import HttpResponse, JsonResponse
from django.db.models import Q
from django.db.models import Count
import re
import os
from django.views.decorators.cache import never_cache
from django.core.files.storage import FileSystemStorage
from blockchain import *
from datetime import date
from datetime import datetime
import geocoder
from django.views.decorators.csrf import csrf_exempt
# Create your views here.


@never_cache
def show_index(request):
    return render(request, "index.html", {})


@never_cache
def logout(request):
    if 'uid' in request.session:
        del request.session['uid']
    return render(request,'index.html')

def register(request):
	username=request.POST.get("username")
	password=request.POST.get("password")
	user_type=request.POST.get("u_type")
	mobile=request.POST.get("mobile")
	p_address=request.POST.get("p_address")

	print(username,password,user_type,mobile,p_address)

	if not verify_adr(p_address):
		return HttpResponse("<script>alert('Public Key does not belong to blockchain');window.location.href='/show_index/';</script>")
	else:
		if user_type=="Select":
			return HttpResponse("<script>alert('Please Select UserType');window.location.href='/show_index/'</script>")

		else:
			obj10=Requests.objects.filter(mobile=mobile,username=username,password=password,p_address=p_address,user_type=user_type)
			co=obj10.count()
			if co==1:
				return HttpResponse("<script>alert('Request is in Pending list');window.location.href='/show_index/'</script>")

			else:
				obj1=Requests(mobile=mobile,username=username,password=password,p_address=p_address,user_type=user_type)
				obj1.save()
				return HttpResponse("<script>alert('Request sent, Wait For Approval');window.location.href='/show_index/'</script>")




def check_login(request):
	username = request.POST.get("username")
	password = request.POST.get("password")

	print(username)
	print(password)

	if username == 'admin' and password == 'admin':
		request.session["uid"] = "admin"
		return HttpResponse("<script>alert('Admin Login Successful');window.location.href='/show_home_admin/'</script>")
	

	else:
		obj1=Manufacturer.objects.filter(username=username,password=password)
		c1=obj1.count()
		if c1==1:
			ob=Manufacturer.objects.get(username=username,password=password)
			request.session["uid"] = ob.u_id
			request.session["username"]=ob.username
			request.session["pub_key"]=ob.p_address
			return HttpResponse("<script>alert('Manufacturer Login Successful');window.location.href='/show_home_manufacturer/'</script>")

		else:
			obj2=Distributor.objects.filter(username=username,password=password)
			c2=obj2.count()
			if c2==1:
				ob9=Distributor.objects.get(username=username,password=password)
				request.session["uid"] = ob9.u_id
				request.session["username"]=ob9.username
				request.session["pub_key"]=ob9.p_address
				return HttpResponse("<script>alert('Distributor Login Successful');window.location.href='/show_home_distributor/'</script>")
			else:
				obj3=Pharmacy.objects.filter(username=username,password=password)
				c3=obj3.count()
				if c3==1:
					ob8=Pharmacy.objects.get(username=username,password=password)
					request.session["uid"] = ob8.u_id
					request.session["username"]=ob8.username
					request.session["pub_key"]=ob8.p_address
					return HttpResponse("<script>alert('Pharmacy Login Successful');window.location.href='/show_home_pharmacy/'</script>")
				else:
					return HttpResponse("<script>alert('Invalid');window.location.href='/show_index/'</script>")


@never_cache
###############ADMIN START
def show_home_admin(request):
	if 'uid' in request.session:
		print(request.session['uid'])
		return render(request,'home_admin.html') 
	else:
		return render(request,'index.html')

@never_cache
def show_request_admin(request):
	if 'uid' in request.session:
		print(request.session['uid'])
		req_list=Requests.objects.all()

		return render(request,'view_request_admin.html',{'req': req_list}) 
	else:
		return render(request,'index.html')


def approve(request):
	r_id=request.POST.get('r_id')
	username=request.POST.get('username')
	password=request.POST.get('password')
	mobile=request.POST.get('mobile')
	user_type=request.POST.get('user_type')
	p_address=request.POST.get('p_address')

	if user_type=="Manufacturer":
		obj1=Manufacturer(mobile=mobile,username=username,password=password,p_address=p_address)
		obj1.save()
		obj2=Manufacturer.objects.get(mobile=mobile,username=username,password=password,p_address=p_address)
		user_id=obj2.u_id
		print("User id : ",user_id)
		#Adding to blockchain
		add_manufacturer1(user_id,username,password,mobile,p_address)

		obj3=Requests.objects.get(r_id=int(r_id))
		obj3.delete()
		return HttpResponse("<script>alert('Approved Successfully');window.location.href='/show_request_admin/'</script>")
	
	elif user_type=="Distributor":
		obj1=Distributor(mobile=mobile,username=username,password=password,p_address=p_address)
		obj1.save()
		obj2=Distributor.objects.get(mobile=mobile,username=username,password=password,p_address=p_address)
		user_id=obj2.u_id
		print("User id : ",user_id)
		#Adding to blockchain
		add_distributor1(user_id,username,password,mobile,p_address)

		obj3=Requests.objects.get(r_id=int(r_id))
		obj3.delete()
		return HttpResponse("<script>alert('Approved Successfully');window.location.href='/show_request_admin/'</script>")

	elif user_type=="Pharmacy":
		obj1=Pharmacy(mobile=mobile,username=username,password=password,p_address=p_address)
		obj1.save()
		obj2=Pharmacy.objects.get(mobile=mobile,username=username,password=password,p_address=p_address)
		user_id=obj2.u_id
		print("User id : ",user_id)
		#Adding to blockchain
		add_pharmacy1(user_id,username,password,mobile,p_address)

		obj3=Requests.objects.get(r_id=int(r_id))
		obj3.delete()
		return HttpResponse("<script>alert('Approved Successfully');window.location.href='/show_request_admin/'</script>")

	else:
		obj1=Customer(mobile=mobile,username=username,password=password,p_address=p_address)
		obj1.save()
		obj2=Customer.objects.get(mobile=mobile,username=username,password=password,p_address=p_address)
		user_id=obj2.u_id
		print("User id : ",user_id)
		#Adding to blockchain
		add_customer1(user_id,username,password,mobile,p_address)

		obj3=Requests.objects.get(r_id=int(r_id))
		obj3.delete()
		return HttpResponse("<script>alert('Approved Successfully');window.location.href='/show_request_admin/'</script>")

def reject(request):
	r_id=request.POST.get('r_id')
	obj1=Requests.objects.get(r_id=int(r_id))
	obj1.delete()
	return HttpResponse("<script>alert('Rejected');window.location.href='/show_request_admin/'</script>")


@never_cache
def display_view_manufacturers(request):
	if 'uid' in request.session:
		print(request.session['uid'])
		obj=get_manufacturers()
		return render(request,'view_manufacturers_admin.html',{'obj':obj}) 
	else:
		return render(request,'index.html')

@never_cache
def display_view_distributors(request):
	if 'uid' in request.session:
		print(request.session['uid'])
		obj=get_distributors()
		return render(request,'view_distributors_admin.html',{'obj':obj}) 
	else:
		return render(request,'index.html')

@never_cache
def display_view_pharmacys(request):
	if 'uid' in request.session:
		print(request.session['uid'])
		obj=get_pharmacys()
		return render(request,'view_pharmacys_admin.html',{'obj':obj}) 
	else:
		return render(request,'index.html')

@never_cache
def display_view_customers(request):
	if 'uid' in request.session:
		print(request.session['uid'])
		obj=get_customers()
		return render(request,'view_customers_admin.html',{'obj':obj}) 
	else:
		return render(request,'index.html')


@never_cache
def show_home_manufacturer(request):
	if 'uid' in request.session:
		print(request.session['uid'])
		return render(request,'home_manufacturer.html') 
	else:
		return render(request,'index.html')

@never_cache
def show_home_distributor(request):
	if 'uid' in request.session:
		print(request.session['uid'])
		return render(request,'home_distributor.html') 
	else:
		return render(request,'index.html')


@never_cache
def show_home_pharmacy(request):
	if 'uid' in request.session:
		print(request.session['uid'])
		return render(request,'home_pharmacy.html') 
	else:
		return render(request,'index.html')

@never_cache
def display_add_medicine(request):
	if 'uid' in request.session:
		return render(request,'add_medicine.html') 
	else:
		return render(request,'index.html')

import zlib
#zlib.crc32() method, we can compute the checksum for crc32 (Cyclic Redundancy Check) to a particular data. 
#It will give 32-bit integer value as a result by using zlib.crc32() method.
def crc_32(med_name,ingredients,exp_date,quantity,dstbtr_lat,dstbtr_long,username):
	print("***************************")
	print(type(exp_date))
	#making a string
	out="%s_%s_%s_%s_%s_%s_%s"%(med_name,ingredients,exp_date,quantity,dstbtr_lat,dstbtr_long,username)
	# print(out)
	#convert it to bytes for crc32
	s = bytes(out, 'utf-8')
	# print(s)
	# print(type(s))

	t = zlib.crc32(s)
	  
	# print(t)
	return t

import pyqrcode
import png
from pyqrcode import QRCode
def generate_qrcode(get_hash,username,med_name):
	print("^^^^^^^^^^^^^^^^^^")
	print(type(get_hash))
	get_hash=str(get_hash)
	print(type(get_hash))
	#String which represents the QR code
	s = get_hash


	  
	# Generate QR code
	url = pyqrcode.create(s)
	
	if not os.path.isdir("mas_app/static/generated_qr_codes/"+username):
		os.makedirs("mas_app/static/generated_qr_codes/"+username)
	# # Create and save the svg file naming "myqr.svg"
	# url.svg("myqr.svg", scale = 8)
	  
	# Create and save the png file naming "myqr.png"
	url.png("mas_app/static/generated_qr_codes/"+username+"/"+med_name+".png", scale = 6)


def add_medicine(request):
	med_name=request.POST.get("med_name")
	ingredients=request.POST.get("ingredients")
	exp_date=request.POST.get("exp_date")
	quantity=request.POST.get("quantity")
	dstbtr_lat=request.POST.get("lat")
	dstbtr_long=request.POST.get("long")
	private_key=request.POST.get("private_key")
	d_public_key=request.POST.get("d_pub_key")

	username=request.session["username"]

	obj1=Manufacturer.objects.get(username=username)
	public_key=obj1.p_address

	verify_result=verify_key(public_key,private_key,1)
	if(verify_result=="No"):
		return HttpResponse("<script>alert('Key Error');window.location.href='/display_add_medicine/'</script>")
	else:
		get_hash=crc_32(med_name,ingredients,exp_date,quantity,dstbtr_lat,dstbtr_long,username)
		get_hash=str(get_hash)
		print("type(get_hash) : ",type(get_hash))
		if Medicine.objects.filter(hash_value=get_hash).exists():
			return HttpResponse("<script>alert('Medicine Already Added');window.location.href='/display_add_medicine/'</script>")
		else:
			status="shipped"
			obj4=Medicine(med_name=med_name,ingredients=ingredients,exp_date=exp_date,quantity=quantity,dstbtr_lat=dstbtr_lat,dstbtr_long=dstbtr_long,d_public_key=d_public_key,manufacturer_name=username,hash_value=get_hash,avail_quantity=quantity,status="shipped")
			obj4.save()

			obj5=Medicine.objects.get(med_name=med_name,ingredients=ingredients,exp_date=exp_date,quantity=quantity,dstbtr_lat=dstbtr_lat,dstbtr_long=dstbtr_long,d_public_key=d_public_key,manufacturer_name=username,hash_value=get_hash,avail_quantity=quantity,status="shipped")
			my_m_id=obj5.m_id
			print("m_id : ",my_m_id)
			generate_qrcode(get_hash,username,med_name)
			add_medicine1(my_m_id,med_name,ingredients,exp_date,quantity,dstbtr_lat,dstbtr_long,username,get_hash,status)
			# get_medicines()
			return HttpResponse("<script>alert('Medicine Added Successfully');window.location.href='/display_add_medicine/'</script>")

@never_cache
def display_view_medicine(request):
	if 'uid' in request.session:
		get_name=request.session["username"]
		med_list=Medicine.objects.filter(manufacturer_name=get_name)
		return render(request,'view_medicine.html',{'med':med_list}) 
	else:
		return render(request,'index.html')

@never_cache
def get_medicine_request_dis(request):
	if 'uid' in request.session:
		get_pub_key=request.session["pub_key"]
		med_list=Medicine.objects.filter(d_public_key=get_pub_key,status="shipped")
		return render(request,'get_medicine_request_dis.html',{'med':med_list}) 
	else:
		return render(request,'index.html')

@never_cache
def get_collected_medicine_dis(request):
	if 'uid' in request.session:
		get_pub_key=request.session["pub_key"]
		med_list=Medicine.objects.filter(d_public_key=get_pub_key,status="collected")
		return render(request,'get_collected_medicine_dis.html',{'med':med_list}) 
	else:
		return render(request,'index.html')

def collect_med_dis(request):
	m_id=request.POST.get("m_id")
	med_name=request.POST.get("med_name")
	ingredients=request.POST.get("ingredients")
	exp_date=request.POST.get("exp_date")
	quantity=request.POST.get("quantity")
	dstbtr_lat=request.POST.get("dstbtr_lat")
	dstbtr_long=request.POST.get("dstbtr_long")
	manufacturer_name=request.POST.get("manufacturer_name")
	hash_value=request.POST.get("hash_value")
	status="collected"
	g = geocoder.ip('me')
	get_current_lat=str(g.latlng[0])
	get_current_long=str(g.latlng[1])
	
	if (dstbtr_lat==get_current_lat) and (dstbtr_long==get_current_long):
		blk1=Medicine.objects.get(m_id=int(m_id))
		blk1.status=status
		blk1.save()
		m_id=int(m_id)
		add_medicine1(m_id,med_name,ingredients,exp_date,quantity,dstbtr_lat,dstbtr_long,manufacturer_name,hash_value,status)
		return HttpResponse("<script>alert('Collected Successfully');window.location.href='/get_collected_medicine_dis/'</script>")
	else:
		return HttpResponse("<script>alert('Location doesnt match');window.location.href='/get_medicine_request_dis/'</script>")

def distribute(request):
	m_id=request.POST.get("m_id")
	med_name=request.POST.get("med_name")
	ingredients=request.POST.get("ingredients")
	exp_date=request.POST.get("exp_date")
	quantity=request.POST.get("quantity")
	avail_quantity=request.POST.get("avail_quantity")
	hash_value=request.POST.get("hash_value")
	pharmacy_pub_key=request.POST.get("pharmacy_pub_key")
	dist_private_key=request.POST.get("dist_private_key")
	dist_pub_key=request.session["pub_key"]
	status="Distributed"

	if not verify_adr(pharmacy_pub_key):
		return HttpResponse("<script>alert('Pharmacy Public Key does not belong to blockchain');window.location.href='/get_collected_medicine_dis/';</script>")
	else:
		verify_result=verify_key(dist_pub_key,dist_private_key,1)
		if(verify_result=="No"):
			return HttpResponse("<script>alert('Distributer Key Error');window.location.href='/get_collected_medicine_dis/'</script>")
		else:
			blk1=Distributed_items(m_id=m_id,med_name=med_name,ingredients=ingredients,exp_date=exp_date,quantity=quantity,avail_quantity=avail_quantity,hash_value=hash_value,pharmacy_pub_key=pharmacy_pub_key,dist_pub_key=dist_pub_key,status=status)
			blk1.save()

			blk2=Medicine.objects.get(m_id=int(m_id))
			blk2.status=status
			blk2.save()
			m_id=int(m_id)
			add_distributed_items1(m_id,med_name,ingredients,exp_date,quantity,avail_quantity,hash_value,pharmacy_pub_key,dist_pub_key,status)
			return HttpResponse("<script>alert('Distributed Successfully');window.location.href='/get_collected_medicine_dis/'</script>")


@never_cache
def display_medicine_stock_pharmacy(request):
	if 'uid' in request.session:
		get_pub_key=request.session["pub_key"]
		print("get_pub_key : ",get_pub_key)
		dist_list=Distributed_items.objects.filter(pharmacy_pub_key=get_pub_key)
		print(dist_list)
		return render(request,'display_medicine_stock_pharmacy.html',{'dist':dist_list}) 
	else:
		return render(request,'index.html')

#####

@csrf_exempt
def customer_register(request):
	username=request.POST.get("username")
	phone=request.POST.get("phone")
	public_key=request.POST.get("public_key")
	password=request.POST.get("password")

	print(username,phone,password,public_key)

	response_data={}
	try:
		if not verify_adr(public_key):
			response_data['msg'] = "Public Key does not belong to blockchain"
		else:
			d = Customer.objects.filter(username=username)
			c = d.count()
			if c == 1:
				response_data['msg'] = "Already registered"
			else:
			    ob=Customer(username=username,mobile=phone,p_address=public_key,password=password)
			    ob.save()

			    response_data['msg'] = "yes"
	except:
	    response_data['msg'] = "no"
	return JsonResponse(response_data)


@csrf_exempt
def find_login(request):
	username=request.POST.get("username")
	password=request.POST.get("password")

	print(username,password)
	
	try:
		ob=Customer.objects.get(username=username,password=password)

		data={"msg":"Customer"}
		return JsonResponse(data,safe=False)
	except:
		data={"msg":"no"}
		return JsonResponse(data,safe=False)

@csrf_exempt
def get_info(request):
	hash_value=request.POST.get("value")
	username=request.POST.get("username")
	print("hash_value : ",hash_value)
	# get_medicines()
	blk1=Distributed_items.objects.get(hash_value=hash_value)
	m_id=blk1.m_id
	med_name=blk1.med_name
	ingredients=blk1.ingredients
	exp_date=blk1.exp_date
	avail_quantity=blk1.avail_quantity


	data={}
	respdata={}
	resplist=[]
	data["m_id"]=m_id
	data["med_name"]=med_name
	data["ingredients"]=ingredients
	data["exp_date"]=exp_date
	data["avail_quantity"]=avail_quantity
	print("^^^^^^^^^^^^^^^^^^^^^^^")
	print(data)
	resplist.append(data)

	respdata["data"]=resplist


	return JsonResponse(respdata,safe=False)

@csrf_exempt
def do_payment(request):
	wanted_quantity=request.POST.get("w_quantity")
	available_quantity=request.POST.get("a_quantity")
	m_id=request.POST.get("m_id")
	username=request.POST.get("username")
	private_key=request.POST.get("private_key")
	response_data={}

	if(int(wanted_quantity)>int(available_quantity)):
		response_data['msg'] = "Quantity not available"
	else:
		obj1=Customer.objects.get(username=username)
		public_key=obj1.p_address
		verify_result=verify_key(public_key,private_key,1)
		if(verify_result=="No"):
			response_data['msg'] = "key Error"
		else:
			w_quantity=int(wanted_quantity)
			a_quantity=int(available_quantity)
			final_quantity=a_quantity-w_quantity
			print("final_quantity : ",final_quantity)
			blk1=Distributed_items.objects.get(m_id=int(m_id))
			blk1.avail_quantity=final_quantity
			blk1.save()
			response_data['msg'] = "yes"
	return JsonResponse(response_data)
