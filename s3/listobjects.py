import boto3

# API de High Level
s3 = boto3.resource('s3')

bucket_name = "iansergio2005"
bucket = s3.Bucket(bucket_name)

for obj in bucket.objects.all():
    print(f"Objeto: {obj.key} | Tamanho: {obj.size} B")
