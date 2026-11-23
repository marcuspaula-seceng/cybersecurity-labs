from collections import Counter
from pathlib import Path

log = Path(__file__).with_name("auth.log")
failures = Counter()
pending = Counter()
alerts = []

for line in log.read_text(encoding="utf-8-sig").splitlines():
    if not line.strip():
        continue
    time, *fields = line.split()
    event = dict(field.split("=", 1) for field in fields)
    account_and_ip = (event["user"], event["src"])

    if event["result"] == "failed":
        failures[event["src"]] += 1
        pending[account_and_ip] += 1
    elif event["result"] == "success":
        count = pending.pop(account_and_ip, 0)
        if count >= 2:
            alerts.append((time, *account_and_ip, count))

print("Falhas por IP:")
for ip, count in sorted(failures.items()):
    print(f"  {ip}: {count}")

print("Sessões para investigação:")
for time, user, ip, count in alerts:
    print(f"  {time} | conta {user} | IP {ip} | sucesso após {count} falhas")
if not alerts:
    print("  Nenhuma sessão atingiu o limiar de duas falhas seguidas de sucesso.")
