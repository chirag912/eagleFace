import json
import base64


import boto3
import botocore

#sR = boto3.client("s3")

#imp = sR.get_object(Bucket="captchabucket", Key = "package.zip")

#import sys
#sys.path.insert(0, imp)

#from imp import numpy as np
#from imp import cv2
s3 = boto3.resource("s3") 

def lambda_handler(event, context):
    # TODO implement
    
    #name1 = json.dumps(event['queryStringParameters']['username'],indent=4)
    image = json.dumps(event['body'],indent=4)
    data = json.loads(image)
    print("DATA : ",data)
    #image2 = image.load({"name"})
    #image2 = image.strip('\"')
    #image3 = base64.b64decode(data)
    
    #name1 = data[:-17123]
    #name2 = name1[89:]
    #name2 = name1[:-850]
    
    
    #image2 = data[210:]
    #image3 = image2[:-192]
    #image4 = image3.strip()
    #image5 = base64.b64decode(image4)
    
    #bucket_name = "captchabucket"
    #file_name = name2 +".jpg"
    #lambda_path = ".images/" + file_name
    #s3_path = "images_new/" + name2
    
    #s3.Bucket(bucket_name).put_object(Key=s3_path, Body=image3)
    
    #Bucket = "captchabucket"
    #Key = "5PWRU.png"
    #outPutName = '/tmp/'+ "5PWRU.png"
    
    #s3 = boto3.client("s3")

    #data_stream = io.BytesIO()
    #s3.meta.client.download_fileobj(Bucket,Key,data_stream)
    
    # List all key in a  S3 bucket
    
    #conn = client('s3')  # again assumes boto.cfg setup, assume AWS S3
    #for key in s3.list_objects(Bucket='eaglefaces3')['Contents']:
    #    print(key['Key'])
    
    """
    
    if event :
        print("Event: ", event)
        
        file_obj = event["body"]
        print("FileOBJ:",file_obj)
        filename = str(file_obj['s3']['object']['key'])
        print("filename:",filename)
        
        fileObj = s3.get_object(Bucket = 'captchabucket', Key = '5PWRU.png')
        
        #print(fileObj)
        
        
        
        
        #file_content = base64.b64encode(fileObj['Body'].read())
        #print(file_content)
        
    """    
    
    """
    
    try:
        #s3.Bucket(Bucket).download_file(Key,outPutName)
        
        fileObj = s3.get_object(Bucket = 'captchabucket', Key = '5PWRU.png')
        
        file_content = fileObj['Body'].read().decode('utf-8')
        
        print("success")

        
    except botocore.exceptions.ClientError as e:
        if e.response['Error']['Code'] == "404":
            print("The object does not exist.")
        else:
            raise
    """

    #image2 = image.loads(image)
    
    #image2 = json.dumps(image['image'], indent=4)
    #image2 = json.load(image)
    #image3 = image['image']
    
    
    #image2 = image.load({"name"})
    #image2 = image.strip('\"')
    #image3 = base64.b64decode(data)
    #image2 = data[210:]
    #image3 = image2[:-190]
    #image4 = base64.b64decode(image3)
    """
    env = {
        'REQUEST_METHOD': 'POST',
        'CONTENT_TYPE': 'multipart/form-data; boundary=KQNTvuH-itP09uVKjjZiegh7',
        'CONTENT_LENGTH': len(image),
    }
    fs = cgi.FieldStorage(fp=io.BytesIO(image), environ=env)
    """

  
        
    #name  = json.dumps(event['queryStringParameters'],indent=4)
    #image1 = image[7:]#
    
    
    #s3 = boto3.resource("s3") 
    
    #name1 = "chirag11"
    #bucket_name = "eaglefaces3"
    #file_name = "RRR4"+".jpg"
    #lambda_path = ".images/" + file_name
    #s3_path = "images_new/" + file_name
    
    #s3.Bucket(bucket_name).put_object(Key=s3_path, Body=image4)

    


    
    return {
        'statusCode': 200,
        'body':data
      
    }
