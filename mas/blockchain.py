import random
import sys
import base64

import json

from web3 import Web3
from solcx import compile_standard

import solcx
# solcx.install_solc()

compiled_sol = compile_standard({
     "language": "Solidity",
     "sources": {
         "phb.sol": {
             "content": '''
                 pragma solidity >=0.4.0 <0.8.21;
               

                contract PHB {

                    struct Manufacturer
                    {            
                        int user_id;
                        string username;
                        string password;
                        string mobile;
                        string p_address;
                    }

                    Manufacturer []manus;

                    function addManufacturer(int user_id,string memory username,string memory password,string memory mobile,string memory p_address) public
                    {
                        Manufacturer memory e
                            =Manufacturer(user_id,
                                    username,
                                    password,
                                    mobile,
                                    p_address);
                        manus.push(e);
                    }

                    function getManufacturer(int user_id) public view returns(
                            string memory,
                            string memory,
                            string memory,
                            string memory
                            )
                    {
                        uint i;
                        for(i=0;i<manus.length;i++)
                        {
                            Manufacturer memory e
                                =manus[i];
                            
                            if(e.user_id==user_id)
                            {
                                return(e.username,
                                    e.password,
                                    e.mobile,
                                    e.p_address
                                   
                                   );
                            }
                        }
                        
                        
                        return("Not Found",
                                "Not Found",
                                "Not Found",
                                "Not Found"
                               );
                    }

                    function getManufacturerCount() public view returns(uint256)
                    {
                        return(manus.length);
                    }


                    struct Distributor
                    {
       
                        int user_id;
                        string username;
                        string password;
                        string mobile;
                        string p_address;
                    }

                    Distributor []dis;

                    function addDistributor(int user_id,string memory username,string memory password,string memory mobile,string memory p_address) public
                    {
                        Distributor memory e
                            =Distributor(user_id,
                                    username,
                                    password,
                                    mobile,
                                    p_address);
                        dis.push(e);
                    }


                    function getDistributor(int user_id) public view returns(
                            string memory,
                            string memory,
                            string memory,
                            string memory
                            )
                    {
                        uint i;
                        for(i=0;i<dis.length;i++)
                        {
                            Distributor memory e
                                =dis[i];
                                 
                            
                            if(e.user_id==user_id)
                            {
                                return(e.username,
                                    e.password,
                                    e.mobile,
                                    e.p_address
                                   );
                            }
                        }
                        
                        
                        return("Not Found",
                                "Not Found",
                                "Not Found",
                                "Not Found");
                    }

                    function getDistributorCount() public view returns(uint256)
                    {
                        return(dis.length);
                    }

                    struct Pharmacy
                    {
       
                        int user_id;
                        string username;
                        string password;
                        string mobile;
                        string p_address;
                    }

                    Pharmacy []pharms;

                    function addPharmacy(int user_id,string memory username,string memory password,string memory mobile,string memory p_address) public
                    {
                        Pharmacy memory e
                            =Pharmacy(user_id,
                                    username,
                                    password,
                                    mobile,
                                    p_address);
                        pharms.push(e);
                    }


                    function getPharmacy(int user_id) public view returns(
                            string memory,
                            string memory,
                            string memory,
                            string memory
                            )
                    {
                        uint i;
                        for(i=0;i<pharms.length;i++)
                        {
                            Pharmacy memory e
                                =pharms[i];
                                 
                            
                            if(e.user_id==user_id)
                            {
                                return(e.username,
                                    e.password,
                                    e.mobile,
                                    e.p_address
                                   );
                            }
                        }
                        
                        
                        return("Not Found",
                                "Not Found",
                                "Not Found",
                                "Not Found");
                    }

                    function getPharmacyCount() public view returns(uint256)
                    {
                        return(pharms.length);
                    }

                    struct Customer
                    {
       
                        int user_id;
                        string username;
                        string password;
                        string mobile;
                        string p_address;
                    }

                    Customer []custm;

                    function addCustomer(int user_id,string memory username,string memory password,string memory mobile,string memory p_address) public
                    {
                        Customer memory e
                            =Customer(user_id,
                                    username,
                                    password,
                                    mobile,
                                    p_address);
                        custm.push(e);
                    }


                    function getCustomer(int user_id) public view returns(
                            string memory,
                            string memory,
                            string memory,
                            string memory
                            )
                    {
                        uint i;
                        for(i=0;i<custm.length;i++)
                        {
                            Customer memory e
                                =custm[i];
                                 
                            
                            if(e.user_id==user_id)
                            {
                                return(e.username,
                                    e.password,
                                    e.mobile,
                                    e.p_address
                                   );
                            }
                        }
                        
                        
                        return("Not Found",
                                "Not Found",
                                "Not Found",
                                "Not Found");
                    }

                    function getCustomerCount() public view returns(uint256)
                    {
                        return(custm.length);
                    }




                    struct Medicine
                    {            
                        int m_id;
                        string med_name;
                        string ingredients;
                        string exp_date;
                        string quantity;
                        string dstbtr_lat;
                        string dstbtr_long;
                        string manufacturer_name;
                        string hash_value;
                        string status;

                    }

                    Medicine []med;

                    function addMedicine(int m_id,string memory med_name, string memory ingredients, string memory exp_date,string memory quantity,string memory dstbtr_lat,string memory dstbtr_long,string memory manufacturer_name,string memory hash_value,string memory status) public
                    {
                        Medicine memory e
                            =Medicine(m_id,
                                    med_name,
                                    ingredients,
                                    exp_date,
                                    quantity,
                                    dstbtr_lat,
                                    dstbtr_long,
                                    manufacturer_name,
                                    hash_value,
                                    status);
                        med.push(e);
                    }

                    function getMedicine(int m_id) public view returns(
                           
                            string memory,
                            string memory,
                            string memory,
                            string memory,
                            string memory,
                            string memory,
                            string memory,
                            string memory,
                            string memory
                            )
                    {
                        uint i;
                        for(i=0;i<med.length;i++)
                        {
                            Medicine memory e
                                =med[i];
                            
                            if(e.m_id==m_id)
                            {
                                return(e.med_name,
                                    e.ingredients,
                                    e.exp_date,
                                    e.quantity,
                                    e.dstbtr_lat,
                                    e.dstbtr_long,
                                    e.manufacturer_name,
                                    e.hash_value,
                                    e.status
                                   );
                            }
                        }
                        
                        
                        return("Not Found",
                                "Not Found",
                                "Not Found",
                                "Not Found",
                                "Not Found",
                                "Not Found",
                                "Not Found",
                                "Not Found",
                                "Not Found"
                               );
                    }

                    function getMedicineCount() public view returns(uint256)
                    {
                        return(med.length);
                    }

                    struct Distributed_items
                    {
                        int m_id;
                        string med_name;
                        string ingredients;
                        string exp_date;
                        string quantity;
                        string avail_quantity;
                        string hash_value;
                        string pharmacy_pub_key;
                        string dist_pub_key;
                        string status;
                    }
                    Distributed_items []d_items;

                    function addDistributed_items(int m_id,string memory med_name,string memory ingredients,string memory exp_date,string memory quantity,string memory avail_quantity,string memory hash_value,string memory pharmacy_pub_key,string memory dist_pub_key,string memory status)public
                    {
                        Distributed_items memory t=Distributed_items(m_id,
                                                        med_name,
                                                        ingredients,
                                                        exp_date,
                                                        quantity,
                                                        avail_quantity,
                                                        hash_value,
                                                        pharmacy_pub_key,
                                                        dist_pub_key,
                                                        status);
                        d_items.push(t);
                    }

                    function getDistributed_items(int m_id) public view returns(string memory,
                                                                            string memory,
                                                                            string memory,
                                                                            string memory,
                                                                            string memory,
                                                                            string memory,
                                                                            string memory,
                                                                            string memory,
                                                                            string memory)
                    {
                        uint j;
                        for(j=0;j<d_items.length;j++)
                        {
                            Distributed_items memory t=d_items[j];

                            if(t.m_id==m_id)
                            {
                                return(t.med_name,
                                        t.ingredients,
                                        t.exp_date,
                                        t.quantity,
                                        t.avail_quantity,
                                        t.hash_value,
                                        t.pharmacy_pub_key,
                                        t.dist_pub_key,
                                        t.status);
                            }

                        }

                        return("Not Found",
                                "Not Found",
                                "Not Found",
                                "Not Found",
                                "Not Found",
                                "Not Found",
                                "Not Found",
                                "Not Found",
                                "Not Found");
                    }
                    function getDistributed_itemsCount() public view returns(uint256)
                    {
                        return(d_items.length);
                    }


                }

               '''
         }
     },
     "settings":
         {
             "outputSelection": {
                 "*": {
                     "*": [
                         "metadata", "evm.bytecode"
                         , "evm.bytecode.sourceMap"
                     ]
                 }
             }
         }
 })


# web3.py instance



def verify_key(adr1,key,amount):
    try:
        ganache_url = "http://127.0.0.1:7545"
        web3 = Web3(Web3.HTTPProvider(ganache_url))
        web3.eth.enable_unaudited_features()
        nonce = web3.eth.getTransactionCount(adr1)

        tx = {
            'nonce': nonce,
            'to': adr1,
            'value': web3.toWei(1, 'ether'),
            'gas': 200000,
            'gasPrice': web3.toWei(amount, 'gwei'),
        }
        signed_tx = web3.eth.account.signTransaction(tx,key)
        tx_hash = web3.eth.sendRawTransaction(signed_tx.rawTransaction)
        #print(web3.toHex(tx_hash))
        return "Yes"
    except Exception as e:
        print(e)  
        return "No"  



def create_contract():
    blockchain_address = 'http://127.0.0.1:7545'
    # # Client instance to interact with the blockchain
    w3 = Web3(Web3.HTTPProvider(blockchain_address))

    print(w3.isConnected())
    #w3 = Web3(Web3.EthereumTesterProvider())

    # set pre-funded account as sender
    w3.eth.defaultAccount = w3.eth.accounts[0]
    # get bytecode
    bytecode = compiled_sol['contracts']['phb.sol']['PHB']['evm']['bytecode']['object']

    # # get abi
    abi = json.loads(compiled_sol['contracts']['phb.sol']['PHB']['metadata'])['output']['abi']

    pb = w3.eth.contract(abi=abi, bytecode=bytecode)

    # # Submit the transaction that deploys the contract
    tx_hash = pb.constructor().transact()

    # # Wait for the transaction to be mined, and get the transaction receipt
    tx_receipt = w3.eth.getTransactionReceipt(tx_hash)
    print("tx_receipt.contractAddress: ",tx_receipt.contractAddress)
    f=open('contract_address.txt','w')
    f.write(tx_receipt.contractAddress)
    f.close()


def add_manufacturer1(user_id,username,password,mobile,p_address):
    f=open('contract_address.txt','r')
    address=f.read()
    f.close()
    blockchain_address = 'http://127.0.0.1:7545'
    # # Client instance to interact with the blockchain
    w3 = Web3(Web3.HTTPProvider(blockchain_address))

    print(w3.isConnected())
    #w3 = Web3(Web3.EthereumTesterProvider())

    # set pre-funded account as sender
    w3.eth.defaultAccount = w3.eth.accounts[0]
    print(type(w3.eth.accounts[0]))

	# get bytecode
    # bytecode = compiled_sol['contracts']['phb.sol']['PHB']['evm']['bytecode']['object']

    # # get abi
    abi = json.loads(compiled_sol['contracts']['phb.sol']['PHB']['metadata'])['output']['abi']

    
    p1 = w3.eth.contract(
        address=address,
        abi=abi
    )
    tx_hash = p1.functions.addManufacturer(user_id,username,password,mobile,p_address).transact()
    tx_receipt = w3.eth.getTransactionReceipt(tx_hash)

    #print(tx_hash) 
    print(tx_receipt)

    

def get_manufacturer(id1):
    id1=int(id1)
    p1=get_contract()
    store = p1.functions.getManufacturer(id1).call()
    print("store : ",store)
    return store

def get_manufacturers():
    c=get_manufacturer_count()
    c_names=['username','password','mobile','p_address']
    dict1={}
    for i in range(1,c+1):
        d=get_manufacturer(i)
        dict2={}
        for j in range(len(c_names)):
            # print("j : ",j)
            # print(type(j))
            # if(j==4):
            #     print("entered")
            #     dict2[c_names[j]]=d[6]
            # else:
            dict2[c_names[j]]=d[j]
        dict1[i]=dict2

    print(dict1)
    return dict1        

def get_manufacturer_count():
    p1=get_contract()
    store = p1.functions.getManufacturerCount().call()
    print(store)
    return int(store)


def add_distributor1(user_id,username,password,mobile,p_address):
    f=open('contract_address.txt','r')
    address=f.read()
    f.close()
    blockchain_address = 'http://127.0.0.1:7545'
    # # Client instance to interact with the blockchain
    w3 = Web3(Web3.HTTPProvider(blockchain_address))

    print(w3.isConnected())
    #w3 = Web3(Web3.EthereumTesterProvider())

    # set pre-funded account as sender
    w3.eth.defaultAccount = w3.eth.accounts[0]
    print(type(w3.eth.accounts[0]))
    abi = json.loads(compiled_sol['contracts']['phb.sol']['PHB']['metadata'])['output']['abi']
    p1 = w3.eth.contract(
        address=address,
        abi=abi
    )
    # c=get_patient_count()+1
    tx_hash = p1.functions.addDistributor(user_id,username,password,mobile,p_address).transact()
    tx_receipt = w3.eth.getTransactionReceipt(tx_hash)
    print(tx_hash)



def get_distributor(id1):
    id1=int(id1)
    p1=get_contract()
    print(id1,'============')
    store = p1.functions.getDistributor(id1).call()
    print(store)
    return store

def get_distributors():
    c=get_distributor_count()
    c_names=['username','password','mobile','p_address']
    dict1={}
    for i in range(1,c+1):
        d=get_distributor(i)
        dict2={}
        for j in range(len(c_names)):
            # if j==5:
            #     dict2[c_names[j]]=d[7]
            # else:
            dict2[c_names[j]]=d[j]
        dict1[i]=dict2

    print(dict1)
    return dict1     


def get_distributor_count():
    p1=get_contract()
    store = p1.functions.getDistributorCount().call()
    print(store)
    return int(store)

def add_pharmacy1(user_id,username,password,mobile,p_address):
    f=open('contract_address.txt','r')
    address=f.read()
    f.close()
    blockchain_address = 'http://127.0.0.1:7545'
    # # Client instance to interact with the blockchain
    w3 = Web3(Web3.HTTPProvider(blockchain_address))

    print(w3.isConnected())
    #w3 = Web3(Web3.EthereumTesterProvider())

    # set pre-funded account as sender
    w3.eth.defaultAccount = w3.eth.accounts[0]
    print(type(w3.eth.accounts[0]))
    abi = json.loads(compiled_sol['contracts']['phb.sol']['PHB']['metadata'])['output']['abi']
    p1 = w3.eth.contract(
        address=address,
        abi=abi
    )
    # c=get_patient_count()+1
    tx_hash = p1.functions.addPharmacy(user_id,username,password,mobile,p_address).transact()
    tx_receipt = w3.eth.getTransactionReceipt(tx_hash)
    print(tx_hash)



def get_pharmacy(id1):
    id1=int(id1)
    p1=get_contract()
    print(id1,'============')
    store = p1.functions.getPharmacy(id1).call()
    print(store)
    return store

def get_pharmacys():
    c=get_pharmacy_count()
    c_names=['username','password','mobile','p_address']
    dict1={}
    for i in range(1,c+1):
        d=get_pharmacy(i)
        dict2={}
        for j in range(len(c_names)):
            # if j==5:
            #     dict2[c_names[j]]=d[7]
            # else:
            dict2[c_names[j]]=d[j]
        dict1[i]=dict2

    print(dict1)
    return dict1     


def get_pharmacy_count():
    p1=get_contract()
    store = p1.functions.getPharmacyCount().call()
    print(store)
    return int(store)

#^^^^^^^^^^^


def add_customer1(user_id,username,password,mobile,p_address):
    f=open('contract_address.txt','r')
    address=f.read()
    f.close()
    blockchain_address = 'http://127.0.0.1:7545'
    # # Client instance to interact with the blockchain
    w3 = Web3(Web3.HTTPProvider(blockchain_address))

    print(w3.isConnected())
    #w3 = Web3(Web3.EthereumTesterProvider())

    # set pre-funded account as sender
    w3.eth.defaultAccount = w3.eth.accounts[0]
    print(type(w3.eth.accounts[0]))
    abi = json.loads(compiled_sol['contracts']['phb.sol']['PHB']['metadata'])['output']['abi']
    p1 = w3.eth.contract(
        address=address,
        abi=abi
    )
    # c=get_patient_count()+1
    tx_hash = p1.functions.addCustomer(user_id,username,password,mobile,p_address).transact()
    tx_receipt = w3.eth.getTransactionReceipt(tx_hash)
    print(tx_hash)



def get_customer(id1):
    id1=int(id1)
    p1=get_contract()
    print(id1,'============')
    store = p1.functions.getCustomer(id1).call()
    print(store)
    return store

def get_customers():
    c=get_customer_count()
    c_names=['username','password','mobile','p_address']
    dict1={}
    for i in range(1,c+1):
        d=get_customer(i)
        dict2={}
        for j in range(len(c_names)):
            # if j==5:
            #     dict2[c_names[j]]=d[7]
            # else:
            dict2[c_names[j]]=d[j]
        dict1[i]=dict2

    print(dict1)
    return dict1     


def get_customer_count():
    p1=get_contract()
    store = p1.functions.getCustomerCount().call()
    print(store)
    return int(store)

##############################
def add_medicine1(m_id,med_name,ingredients,exp_date,quantity,dstbtr_lat,dstbtr_long,username,hash_value,status):                      
    f=open('contract_address.txt','r')
    address=f.read()
    f.close()
    blockchain_address = 'http://127.0.0.1:7545'
    # # Client instance to interact with the blockchain
    w3 = Web3(Web3.HTTPProvider(blockchain_address))

    print(w3.isConnected())
    #w3 = Web3(Web3.EthereumTesterProvider())

    # set pre-funded account as sender
    w3.eth.defaultAccount = w3.eth.accounts[0]
    print(type(w3.eth.accounts[0]))
    abi = json.loads(compiled_sol['contracts']['phb.sol']['PHB']['metadata'])['output']['abi']
    p2 = w3.eth.contract(
        address=address,
        abi=abi
    )
    # c=get_patient_count()+1
    tx_hash = p2.functions.addMedicine(m_id,med_name,ingredients,exp_date,quantity,dstbtr_lat,dstbtr_long,username,hash_value,status).transact()
    #tx_receipt = w3.eth.getTransactionReceipt(tx_hash)
    print(tx_hash)


def get_medicine(id1):
    id1=int(id1)
    p1=get_contract()
    store = p1.functions.getMedicine(id1).call()
    print("store : ",store)
    return store

def get_medicines():
    c=get_medicine_count()
    c_names=['med_name','ingredients','exp_date','quantity','dstbtr_lat','dstbtr_long','manufacturer_name','hash_value']
    dict1={}
    for i in range(1,c+1):
        d=get_medicine(i)
        dict2={}
        for j in range(len(c_names)):
            dict2[c_names[j]]=d[j]
        dict1[i]=dict2

    print("File dictionary :::>",dict1)
    return dict1        

def get_medicine_count():
    p1=get_contract()
    store = p1.functions.getMedicineCount().call()
    print(store)
    return int(store)


def get_contract():
    f=open('contract_address.txt','r')
    address=f.read()
    f.close()
    blockchain_address = 'http://127.0.0.1:7545'
    # # Client instance to interact with the blockchain
    w3 = Web3(Web3.HTTPProvider(blockchain_address))

    print(w3.isConnected())
    #w3 = Web3(Web3.EthereumTesterProvider())

    # set pre-funded account as sender
    w3.eth.defaultAccount = w3.eth.accounts[0]#'0x3529A6ee990639C32bEe5F841a9649cdd0c6e0FD'
    print(type(w3.eth.accounts[0]))

	# get bytecode
    # bytecode = compiled_sol['contracts']['phb.sol']['PHB']['evm']['bytecode']['object']

    # # get abi
    abi = json.loads(compiled_sol['contracts']['phb.sol']['PHB']['metadata'])['output']['abi']

    p1 = w3.eth.contract(
        address=address,
        abi=abi
    )
    return p1



def verify_adr(s):
    blockchain_address = 'http://127.0.0.1:7545'
    # # Client instance to interact with the blockchain
    w3 = Web3(Web3.HTTPProvider(blockchain_address))

    print(w3.isConnected(),"##########")
    #w3 = Web3(Web3.EthereumTesterProvider())

    # set pre-funded account as sender
    adrs = w3.eth.accounts
    print(adrs)

    if s in adrs:
        return True
    else:
        return False    

def bverify_transaction(tx):
    blockchain_address = 'http://127.0.0.1:7545'
    # # Client instance to interact with the blockchain
    w3 = Web3(Web3.HTTPProvider(blockchain_address))

    print(w3.isConnected(),"##########")
    #w3 = Web3(Web3.EthereumTesterProvi
    x=w3.eth.getTransaction(tx)
    print(x)
    if x==None:
        print('Fake')
        return False
    else:
        print('Real')
        return True


###################
def add_distributed_items1(m_id,med_name,ingredients,exp_date,quantity,avail_quantity,hash_value,pharmacy_pub_key,dist_pub_key,status):
    f=open('contract_address.txt','r')
    address=f.read()
    f.close()
    blockchain_address = 'http://127.0.0.1:7545'
    # # Client instance to interact with the blockchain
    w3 = Web3(Web3.HTTPProvider(blockchain_address))

    print(w3.isConnected())
    #w3 = Web3(Web3.EthereumTesterProvider())

    # set pre-funded account as sender
    w3.eth.defaultAccount = w3.eth.accounts[0]
    print(type(w3.eth.accounts[0]))

    # get bytecode
    # bytecode = compiled_sol['contracts']['phb.sol']['PHB']['evm']['bytecode']['object']

    # # get abi
    abi = json.loads(compiled_sol['contracts']['phb.sol']['PHB']['metadata'])['output']['abi']

    
    p1 = w3.eth.contract(
        address=address,
        abi=abi
    )
    tx_hash = p1.functions.addDistributed_items(m_id,med_name,ingredients,exp_date,quantity,avail_quantity,hash_value,pharmacy_pub_key,dist_pub_key,status).transact()
    tx_receipt = w3.eth.getTransactionReceipt(tx_hash)

    #print(tx_hash) 
    print(tx_receipt)

    

def get_d_items(id1):
    id1=int(id1)
    p1=get_contract()
    store = p1.functions.getDistributed_items(id1).call()
    print("store : ",store)
    return store

def get_distributed_items():
    c=get_distributed_items_count()
    c_names=['med_name','ingredients','exp_date','quantity','avail_quantity','hash_value','pharmacy_pub_key','dist_pub_key','status']
    dict1={}
    for i in range(1,c+1):
        d=get_d_items(i)
        dict2={}
        for j in range(len(c_names)):
            dict2[c_names[j]]=d[j]
        dict1[i]=dict2

    print(dict1)
    return dict1        

def get_distributed_items_count():
    p1=get_contract()
    store = p1.functions.getDistributed_itemsCount().call()
    print(store)
    return int(store)



def transfer(adr1,adr2,key,amount,sender_name,receiver_name,title):
    try:
        ganache_url = "http://127.0.0.1:7545"
        web3 = Web3(Web3.HTTPProvider(ganache_url))
        web3.eth.enable_unaudited_features()
        nonce = web3.eth.getTransactionCount(adr1)

        tx = {
            'nonce': nonce,
            'to': adr2, #artist_address
            'value': web3.toWei(amount, 'ether'),
            'gas': 2000000,
            'gasPrice': web3.toWei(amount, 'gwei'),
        }
        signed_tx = web3.eth.account.signTransaction(tx,key)
        tx_hash = web3.eth.sendRawTransaction(signed_tx.rawTransaction)
        print(web3.toHex(tx_hash))
        generated_hash=web3.toHex(tx_hash)
        print("generated_hash : ",generated_hash)
        return generated_hash

    except Exception as e:
        print(e)  
        return False



if __name__=="__main__":
    pass

     #create_contract()




