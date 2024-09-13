# Keda Playground


## TODO (priorities)

* Port forwarding vs. NodePort (LoadBalancer?)
* Overriding metrics-api (image)
* Condense READMEs

### Quickstart (MacOS)

* Tooling: `brew install minikube helm`
* Helm plugins: `helm repo add kedacore https://kedacore.github.io/charts && helm repo update`
* Start minikube: `minikube start`
* Deploy KEDA in minikube: `helm install keda kedacore/keda --namespace keda --create-namespace`
* Deploy **Hello-World App**: `kubectl apply -f k8s/hello-world.yaml`
* Deploy **Metris-API**: `kubectl apply -f k8s/metrics-api.yaml`
    * **Optional:** Expose to localhost for REST invocations to change response: `kubectl port-forward svc/metrics-api-service 7051`.
    * `POST http://localhost:7051/value` with request body. Inspected KEDA value will be overwritten to whatever is supplied in the request body.
* Deploy **KEDA** configs: `kubectl apply -f k8s/keda.yaml`

#### Teardown

* Teardown manifests with `kubectl delete -f <file>`.
* KEDA uninstall [instructions here](https://keda.sh/docs/2.14/deploy/#uninstall)
* `minikube stop`
* **Optional:** `minikube delete` for hard-destroying minikube.
