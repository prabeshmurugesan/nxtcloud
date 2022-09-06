from django.shortcuts import render
import mysql.connector
import boto3
import boto
from django.conf import settings
# Create your views here.

def index(request):
    mydb = mysql.connector.connect(username='root', password="rjga#tb*MJcW*H+Pkqf9e(&",
                                   host='nextcloud.chhqwpjaxwun.ap-south-1.rds.amazonaws.com', port=3306)

    db = mydb.cursor()

    if request.method=='POST':
        Username = request.POST['username']
        Password = request.POST['password']
        clientdb = request.POST['dbname']
        Bucketname = request.POST['bucketname']

        db.execute(f'create database {clientdb}')

        db.execute(f'create user "{Username}" IDENTIFIED BY "{Password}"')

        db.execute(f'GRANT ALL PRIVILEGES ON  {clientdb}.* TO "{Username}"')

        #conn = boto.connect_s3()

        s3 = boto3.client("s3",
                aws_access_key_id="AKIA54IUGKM6ZSDISBFW",
                aws_secret_access_key="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",
                region_name="ap-south-1",
        )
        creation = s3.create_bucket(Bucket=Bucketname,CreateBucketConfiguration={"LocationConstraint": "ap-south-1"})

        return render(request, 'dbs3/successful.html')
    else:
        return render(request, 'dbs3/index.html')





