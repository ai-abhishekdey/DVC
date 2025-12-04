## Data Versioning with DVC and Google Cloud Storage (GCS)

**Author: Abhishek Dey**

### Getting Started

* Initialise GIR

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

## Track the changes with git

```
git add data.dvc .gitignore

```

## Create a service account in Google Cloud Storage

* Go to **IAM**
	 -> **Service Accounts** 
	 -> **Create service account**
	 
* For **role**, select **Storage Object Admin**

* Once Service Account is created, go to **Actions** -> **Manage Keys** -> **Add Key** 

* Download the **KEY in JSON** and keep in a safe place
 

## Add Google Cloud Storage (GCS) as remote

* Install **Google Cloud CLI** following this [link](https://docs.cloud.google.com/sdk/docs/install-sdk#deb)

* Initialise gcloud cli

```
gcloud init

```

* If prompted for authentication, use

```
gcloud auth login --no-browser

```

* Add the GCS remote

```
dvc remote add -d gcs_remote gs://<bucket-name>/dvc_exp/

```

* Commit the remote configuration:

```
git add .dvc/config

git commit -m "Added GCS remote"

```

* Download service account credentials key 

```
gsutil -m cp gs://<bucket-name>/service_account_credentials.json ./

```

* Export service account credentials

```
export GOOGLE_APPLICATION_CREDENTIALS='service_account_credentials.json'

```

* Add service account credentials to .gitignore

```
echo "service_account_credentials.json" >> .gitignore

git add .gitignore

git commit -m "Ignore service account credentials"

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
  
````
