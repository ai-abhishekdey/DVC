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

## Initialise dvc project

```

git init

dvc init

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
