import consul

def discover_service(service_name):
    c = consul.Consul(host="consul-server1")
    
    index, services = c.health.service(service_name, passing=True)
    
    if services:
        for service in services:
            service_id = service['Service']['ID']
            service_address = service['Service']['Address']
            service_port = service['Service']['Port']
            print(f"Found service: {service_id} at {service_address}:{service_port}")
    else:
        print(f"No healthy instances of {service_name} found")

if __name__ == "__main__":
    discover_service("example-service")