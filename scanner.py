#!/usr/bin/env python3
"""
Docker Security Scanner
A containerized vulnerability scanner for web applications
"""

import socket
import requests
import sys
from datetime import datetime

class SecurityScanner:
    def __init__(self, target):
        self.target = target
        self.results = []
        
    def banner(self):
        print("=" * 50)
        print("DOCKER SECURITY SCANNER v1.0")
        print("Target:", self.target)
        print("Scan started:", datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
        print("=" * 50)
    
    def port_scan(self):
        """Scan common ports"""
        print("\n[+] Scanning common ports...")
        common_ports = [21, 22, 23, 25, 80, 443, 3306, 3389, 8080]
        open_ports = []
        
        for port in common_ports:
            try:
                sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                sock.settimeout(1)
                result = sock.connect_ex((self.target, port))
                if result == 0:
                    open_ports.append(port)
                    print(f"    [OPEN] Port {port}")
                sock.close()
            except:
                pass
        
        self.results.append(f"Open ports: {open_ports}")
        return open_ports
    
    def check_http_headers(self):
        """Check HTTP security headers"""
        print("\n[+] Checking HTTP security headers...")
        try:
            response = requests.get(f"http://{self.target}", timeout=5)
            headers = response.headers
            
            security_headers = {
                'X-Frame-Options': 'Clickjacking protection',
                'X-Content-Type-Options': 'MIME sniffing protection',
                'Strict-Transport-Security': 'HTTPS enforcement',
                'Content-Security-Policy': 'XSS protection',
            }
            
            for header, purpose in security_headers.items():
                if header in headers:
                    print(f"    [GOOD] {header} present")
                else:
                    print(f"    [WARN] {header} missing ({purpose})")
                    self.results.append(f"Missing: {header}")
        except Exception as e:
            print(f"    [ERROR] Could not check headers: {e}")
    
    def generate_report(self):
        """Generate scan report"""
        print("\n" + "=" * 50)
        print("SCAN COMPLETE")
        print("=" * 50)
        print(f"\nFindings: {len(self.results)}")
        for finding in self.results:
            print(f"  - {finding}")
        print("\nRecommendation: Review findings and implement security best practices")
    
    def run(self):
        """Run full scan"""
        self.banner()
        self.port_scan()
        self.check_http_headers()
        self.generate_report()

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python scanner.py <target_domain_or_ip>")
        sys.exit(1)
    
    target = sys.argv[1]
    scanner = SecurityScanner(target)
    scanner.run()