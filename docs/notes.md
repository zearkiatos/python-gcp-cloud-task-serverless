# GCP create cloud task

## Create permission to the user account
```sh
# gcloud iam service-accounts create misw-das-productor --description="Cuenta de servicio para el tutorial de cloud task" --display-name="Productor tutorial cloud task"
$ gcloud iam service-accounts create miso-cloud-producer --description="Cuenta de servicio para el tutorial de cloud task" --display-name="Productor tutorial cloud task"
```

## Adding the permission

```sh
# gcloud projects add-iam-policy-binding <PROJECT_ID> --member="serviceAccount:miso-cloud-producer@<PROJECT_ID>.iam.gserviceaccount.com" --role="roles/cloudtasks.enqueuer"
$ gcloud projects add-iam-policy-binding miso-cloud-native-414617 --member="serviceAccount:miso-cloud-producer@miso-cloud-native-414617.iam.gserviceaccount.com" --role="roles/cloudtasks.enqueuer"
```

## Create Cloud task
```sh
# gcloud tasks queues create cola-cloud-task-tutorial --location=us-central1
$ gcloud tasks queues create queue-cloud-task --location=us-central1
```