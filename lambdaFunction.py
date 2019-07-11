import json
import base64
import boto3
import botocore
import cv2
import cgi
import email
from requests_toolbelt.multipart import decoder
import requests



s3 = boto3.resource("s3") 

def lambda_handler(event, context):
    
    #image = json.dumps(event['body'],indent=4)
    #data = json.loads(image.read())
    #image_str = image.str()
    #testEnrollResponse = requests.post(...)
    #multipart_data = decoder.MultipartDecoder.from_response(image)
    #content_type = "multipart/form-data; boundary =WebKitFormBoundarydEcEeQmqexmrrabx"
    #multipart_data = decoder.MultipartDecoder(image_str,content_type)
    
    if event :
        print("Event: ", event)
        
        content_type = event["headers"]["content-type"]
        print(content_type)
        
        file_obj = event["body"]
        print(file_obj)
        """
        b = email.message_from_string(file_obj)
        if b.is_multipart():
            for payload in b.get_payload():
                # if payload.is_multipart(): ...
                payload.get_payload(decode=True)
                print(payload.get_value("name"))
        else:
            
            b.get_payload()
        """
        
        #file_obj1 = file_obj.split('/r')
        #print(file_obj1)
        #file_obj2 = file_obj1.split("/n")
        #print(file_obj2)
        
        #print(type(file_obj))
        #print(file_obj.type())
        #print("FileOBJ:",file_obj)
        #content_type = "multipart/form-data; boundary ="+boundary+""
        multipart_data = decoder.MultipartDecoder(file_obj,content_type)
        print(multipart_data)
        for part in multipart_data.parts:
            print(part.content)
        
 
        #name = file_obj.request.get('name')
        #print(name)
        
        #testEnrollResponse = requests.post("https://q1205tf9ok.execute-api.us-east-1.amazonaws.com/prod/uploads3")
        #data = cgi.FieldStorage(file_obj)
        #multipart_data = decoder.MultipartDecoder.from_response(file_obj)
        #print(multipart_data)
        #for part in multipart_data.parts:
           # print("THIS",part.content)
       # print("FileOBJ:",file_obj)
        #filename = str(file_obj['s3']['object']['key'])
        #print("filename:",filename)
        
        #fileObj = s3.get_object(Bucket = 'captchabucket', Key = '5PWRU.png')
        
    
    
    #print(multipart_data)

    #for part in multipart_data.parts:
    #    print(part.content)  # Alternatively, part.text if you want unicode
    #    print(part.headers)
    
    
    return {
        'statusCode': 200,
        'body':data,
        #'isBase64Encoded':true
      
    }