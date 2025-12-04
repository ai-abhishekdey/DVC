## Data Versioning with DVC and Google Cloud Storage (GCS)

**Author: Abhishek Dey**


## Create a service account in Google Cloud Storage

* Go to **IAM**
	 -> **Service Accounts** 
	 -> **Create service account**
	 
* For **role**, select **Storage Admin**

* Once Service Account is created, go to **Actions** -> **Manage Keys** -> **Add Key** 

* Download the **KEY in JSON** and keep in a safe place
 
* Download service account credentials key 

```
gsutil -m cp gs://<bucket-name>/service_account_credentials.json /home/user/

```

* Export service account credentials

```
export GOOGLE_APPLICATION_CREDENTIALS='/home/user/service_account_credentials.json'

```

## Setup Google Cloud CLI

* Install **Google Cloud CLI** following this [link](https://docs.cloud.google.com/sdk/docs/install-sdk#deb)

* Initialise gcloud cli

```
gcloud init

```

* If prompted for authentication, use

```
gcloud auth login --no-browser

```

## Getting Started

* Initialise Git

```
git init

```

* Initialise DVC

```
dvc init

```

```
Initialized DVC repository.

You can now commit the changes to git.

+---------------------------------------------------------------------+
|                                                                     |
|        DVC has enabled anonymous aggregate usage analytics.         |
|     Read the analytics documentation (and how to opt-out) here:     |
|             <https://dvc.org/doc/user-guide/analytics>              |
|                                                                     |
+---------------------------------------------------------------------+

What's next?
------------
- Check out the documentation: <https://dvc.org/doc>
- Get help and share ideas: <https://dvc.org/chat>
- Star us on GitHub: <https://github.com/treeverse/dvc>

```

```
git status

```

```
On branch master

No commits yet

Changes to be committed:
  (use "git rm --cached <file>..." to unstage)
	new file:   .dvc/.gitignore
	new file:   .dvc/config
	new file:   .dvcignore

Untracked files:
  (use "git add <file>..." to include in what will be committed)
	README.md

```

### Create sample data

```
mkdir data

echo "Hello World" > data/sample.txt

```

### Track data folder

```
dvc add data

```

* This will create **data.dvc**

* check the data.dvc

```

cat data.dvc

```

```
outs:
- md5: ef25b58ba3f203fd9c6531eacf9fbd03.dir
  size: 12
  nfiles: 1
  hash: md5
  path: data
```

### Track the changes with git

```
git add data.dvc .gitignore

```

* Add the GCS remote

```
dvc remote add -d gcs_remote gs://<bucket-name>/dvc_exp/

```

* Commit the remote configuration:

```
git add .dvc/config

git commit -m "Dataset v1: Initial sample"

```

* Push dataset to GCS

```
dvc push

```

## Make a new dataset version

* Add a new line

```
echo "New version of data" >> data/sample.txt

```

* Check the updated text file

cat data/sample.txt 

```
Hello World
New version of data

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
- md5: fff0a0c87a3172113a812e525049260f.dir
  size: 32
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
git checkout 37f466b193aebd7513b1f0a46bf91cda6012803a

```

* Pull the data from gcs

```

dvc pull

```

* Check the downloaded data

```
cat data/sample.txt 


Hello World

```
