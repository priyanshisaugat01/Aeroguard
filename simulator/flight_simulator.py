import random
import time
from datetime import datetime

def generate_flight_metrics():
    """Generate fake airline server metrics"""
    
    metrics = {
        'timestamp': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
        'cpu_usage': round(random.uniform(20, 60), 2),
        'memory_usage': round(random.uniform(30, 70), 2),
        'api_response_time': round(random.uniform(100, 300), 2),
        'active_flights': random.randint(50, 200),
        'passengers_checked_in': random.randint(500, 2000),
        'network_latency': round(random.uniform(5, 20), 2),
        'db_query_time': round(random.uniform(10, 50), 2),
        'status': 'NORMAL ✅'
    }
    
    # 15% chance of anomaly
    if random.random() < 0.15:
        metrics['cpu_usage'] = round(random.uniform(85, 99), 2)
        metrics['api_response_time'] = round(random.uniform(2000, 5000), 2)
        metrics['network_latency'] = round(random.uniform(500, 1000), 2)
        metrics['status'] = 'ANOMALY DETECTED! 🚨'
    
    return metrics

def display_metrics(metrics):
    """Display metrics in nice format"""
    print("\n" + "="*50)
    print(f"✈️  AEROGUARD - Flight Operations Monitor")
    print("="*50)
    print(f"🕐 Time: {metrics['timestamp']}")
    print(f"💻 CPU Usage: {metrics['cpu_usage']}%")
    print(f"🧠 Memory: {metrics['memory_usage']}%")
    print(f"⚡ API Response: {metrics['api_response_time']}ms")
    print(f"✈️  Active Flights: {metrics['active_flights']}")
    print(f"👥 Passengers: {metrics['passengers_checked_in']}")
    print(f"🌐 Network Latency: {metrics['network_latency']}ms")
    print(f"🗄️  DB Query: {metrics['db_query_time']}ms")
    print(f"📊 Status: {metrics['status']}")
    print("="*50)

# Main program
print("🛡️ AeroGuard Starting...")
print("✈️ Monitoring Flight Operations...")
print("Press Ctrl+C to stop\n")

while True:
    metrics = generate_flight_metrics()
    display_metrics(metrics)
    time.sleep(3)