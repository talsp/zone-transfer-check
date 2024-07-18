import dns.resolver

def get_dns_servers(domain):
    try:
        ns_records = dns.resolver.resolve(domain, 'NS')
        dns_servers = [str(ns.target) for ns in ns_records]
        return dns_servers
    except Exception as e:
        print(f"An error occurred: {e}")
        return []

domain = input("[+] Please enter the domain name: ")
dns_servers = get_dns_servers(domain)
if dns_servers:
    for server in dns_servers:
        try:
            print(f"[+] Checking zone transfer for {server}")
            zone = dns.zone.from_xfr(dns.query.xfr(server, domain))
            names = zone.nodes.keys()
            for name in names:
                print(zone[name].to_text(name))
        except Exception as e:
            print(f"[-] Zone transfer failed: {e}")
else:
    print(f"[-] No DNS servers found for {domain}")
