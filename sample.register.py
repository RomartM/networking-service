import consul
import socket

def register_service(service_name, service_port):
    c = consul.Consul(host="consul-server1")
    
    service_id = f"{service_name}-{socket.gethostname()}"
    
    c.agent.service.register(
        name=service_name,
        service_id=service_id,
        address=socket.gethostname(),
        port=service_port,
        check=consul.Check.tcp(socket.gethostname(), service_port, "10s")
    )
    
    print(f"Service {service_name} registered with Consul")

if __name__ == "__main__":
    register_service("example-service", 8080)