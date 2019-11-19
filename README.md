```
https://github.com/passionsjin/simple_django_app.git
```
#### docker build -t django-simple-app .
#### kubectl apply -f deployment.yml
#### kubectl expose deploy django-simple-app-deployment --type=NodePort
```buildoutcfg
apiVersion: apps/v1
kind: Deployment
metadata:
  name: django-simple-app-deployment
  labels:
    app: django-simple-app
spec:
  replicas: 1
  selector:
    matchLabels:
      app: simple-app
  template:
    metadata:
      labels:
        app: simple-app
    spec:
      containers:
      - name: django-simple-app
        image: django-simple-app
        imagePullPolicy: IfNotPresent
        ports:
        - containerPort: 8000
```

## Deployment of new versions of the application
 - Make changes in to the app
 - `docker build -t kubernetes-django:v2 .`
 - Update image at the `deployment.yml` file `spec.template.spec.containers.image` to the `kubernetes-django:v2`
 - `kubectl apply -f deployment.yml`
 - App should be updated to the new version now.