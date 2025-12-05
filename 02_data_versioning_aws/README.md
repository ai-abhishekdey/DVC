## Data Versioning with DVC and AWS S3

**Author : Abhishek Dey**

##  Getting Started

* Install aws-cli

```

sudo apt-get install awscli

```

* Configure aws-cli

```
aws configure

```

```

AWS Access Key ID [None]: A******************F
AWS Secret Access Key [None]: B**********/***/***P
Default region name [None]: us-east-1
Default output format [None]: json

```

## Initialise dvc project in root repo 

```
cd ../

dvc init

cd 02_data_versioning_aws

touch .gitignore

```

## Add a dataset

```

mkdir data

echo "hello" > data/sample.txt

dvc add data

```

## Check  data.dvc

cat data.dvc

```
outs:
- md5: 7b682103c6f8bdb875c3d39b43c847c5.dir
  size: 6
  nfiles: 1
  hash: md5
  path: data

````

## Add data.dvc to .gitignore

```
git add data.dvc .gitignore

git commit -m "Dataset v1"

```


## Add S3 bucket remote & push data

```
dvc remote add -d s3remote s3://ad-workspace/dvc_exp

dvc push

```

## Make a new dataset version

* Add a new line

```
echo "New version of data" >> data/sample.txt

```

## Track changes again:

```
dvc add data
git add data.dvc
git commit -m "Dataset v2: Updated sample"
dvc push

```
* Updated data.dvc file

```
outs:
- md5: cc727b82ff74d2d9d398231c43d3080e.dir
  size: 26
  nfiles: 1
  hash: md5
  path: data
  
```

## To download an older version of the data

* Check the commit-id in the git log

```
git log

```

* git checkout to the older version commit

```
git checkout 56cbfa64ad012f7162792c5e1e58e443f76258b2

```

* Pull the data from gcs

```
dvc pull

```

* Check the downloaded data

```
cat data/sample.txt 

hello

```

