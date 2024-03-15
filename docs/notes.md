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

## Create function with service account
```sh
# gcloud functions deploy funcion-tutorial-productor --entry-point producir --runtime python39 --trigger-http --allow-unauthenticated --memory 128MB --region us-central1 --timeout 60 --min-instances 0 --max-instances 1 --service-account "misw-das-productor@<PROJECT_ID>.iam.gserviceaccount.com" --set-env-vars LOCATION_ID=us-central1,PROJECT_ID=<PROJECT_ID>,QUEUE_ID=cola-cloud-task-tutorial,URL_FUNCTION=https://us-central1-<PROJECT_ID>.cloudfunctions.net/funcion-tutorial-consumidor
$ gcloud functions deploy function-produce-http --entry-point produce --runtime python39 --trigger-http --allow-unauthenticated --memory 128MB --region us-central1 --timeout 60 --min-instances 0 --max-instances 1 --service-account "miso-cloud-producer@miso-cloud-native-414617.iam.gserviceaccount.com" --set-env-vars LOCATION_ID=us-central1,PROJECT_ID=miso-cloud-native-414617,QUEUE_ID=queue-cloud-task,URL_FUNCTION=https://us-central1-miso-cloud-native-414617.cloudfunctions.net/function-consume-http
```