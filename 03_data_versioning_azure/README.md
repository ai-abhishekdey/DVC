## Data Versioning with DVC and Azure Blob Storage

**Author: Abhishek Dey**

## Getting Started

* Install Azure cli

```

curl -sL https://aka.ms/InstallAzureCLIDeb | sudo bash


sudo apt-get update && sudo apt-get install --only-upgrade -y azure-cli

```

* Check installed Azure CLI version

```
az --version

```

* Login 

```
az login --use-device-code

```

* List of Storage Accounts / Blobs

```
az storage account list -o table

```


## Initialise dvc project in root repo

```

cd ../

dvc init

cd 03_data_versioning_azure

touch .gitignore

```

## Add a dataset

```

mkdir data

echo "hello" > data/sample.txt

dvc add data

```

## Check data.dvc

cat data.dvc

```
outs:
- md5: 7b682103c6f8bdb875c3d39b43c847c5.dir
  size: 6
  nfiles: 1
  hash: md5
  path: data

```

## Add data.dvc to .gitignore

```

git add data.dvc .gitignore

git commit -m "Dataset v1 azure"

```


## Add azure storage remote & push data

```

dvc remote add -d azure_remote azure://<container>/<path>

dvc remote modify azure_remote account_name <storage_account_name>

dvc remote modify --local azure_remote account_key <storage_account_key>

git add .dvc/config     

git commit -m "Configure Azure DVC remote"

git push

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
git commit -m "Dataset v2 azure: Updated sample"
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
git checkout 27298b390fe1bf7f1fc679d5d5ffcfe4be5c434erwd

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









