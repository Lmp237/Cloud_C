apiVersion: v1
kind: Service
metadata:
  name: web
spec:
  type: LoadBalancer
  ports:
  - port: 5000
    targetPort: 5000
    protocol: TCP
  selector:
    app: tripmeal
    service: web
---
apiVersion: apps/v1
kind: Deployment
metadata:
  name: web
spec:
  replicas: 1
  selector:
    matchLabels:
      app: tripmeal
      service: web
  template:
    metadata:
      labels:
        app: tripmeal
        service: web
    spec:
      containers:
      - image: europe-west2-docker.pkg.dev/gq-cloud-computing/rfinal/app-photo/web
        name: web
        ports:
        - containerPort: 5000
          protocol: TCP
        env:
        - name: DATABASE_NAME
          value: "tripmealdb"
        - name: DATABASE_USER
          value: "root"
        - name: MYSQL_ROOT_PASSWORD
          value: "my-secret-pw"
        - name: DATABASE_HOST
          value: "db"
        - name: DATABASE_PORT
          value: "3306"
        - name: TRIPMEAL_KEY
          value: "my-secret-key"
        - name: SERVER_PORT
          value: "5000"
---
apiVersion: v1
kind: Service
metadata:
  name: db
spec:
  type: ClusterIP
  ports:
  - port: 3306
    protocol: TCP
  selector:
    app: tripmeal
    service: db
---
apiVersion: apps/v1
kind: StatefulSet
metadata:
  name: db
spec:
  selector:
    matchLabels:
      app: tripmeal
      service: db
  serviceName: db
  template:
    metadata:
      labels:
        app: tripmeal
        service: db
    spec:
      containers:
      - image: europe-west2-docker.pkg.dev/gq-cloud-computing/rfinal/app-photo/db
        name: db
        ports:
        - containerPort: 3306
        volumeMounts:
        - mountPath: /var/lib/mysql
          name: tripmeal-data
        env:
        - name: DATABASE_NAME
          value: "tripmealdb"
        - name: DATABASE_USER
          value: "root" 
        - name: MYSQL_ROOT_PASSWORD
          value: "my-secret-pw"
  volumeClaimTemplates:
  - metadata:
      name: tripmeal-data
    spec:
      accessModes:
      - ReadWriteOnce
      resources:
        requests:
          storage: 100Mi
