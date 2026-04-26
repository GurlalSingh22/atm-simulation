from datetime import datetime

class Statement:

    def __init__(self):
   
        self.history = []

    def add_record(self, txn_type, amount, bal):
       
        record = {
            "type" : txn_type,
            "amount" : amount,
            "balance" : bal,
            "time" : datetime.now().strftime("%d-%m-%Y %H:%M:%S")
        }
        self.history.append(record)

    def show(self):
        if len(self.history) == 0:
            print("\n  📭 No transactions found.")
            return

        print("\n" + "="*52)
        print("         🧾  MINI STATEMENT")
        print("="*52)
        print(f"  {'#':<4} {'Type':<12} {'Amount':>10}  {'Balance':>10}  Time")
        print("-"*52)

        i = 1
        for t in self.history:
            if t["type"] == "Deposit":
                sign = "+"
            else:
                sign = "-"
            print(f"  {i:<4} {t['type']:<12} {sign}Rs.{t['amount']:>6}  Rs.{t['balance']:>8}  {t['time']}")
            i = i + 1

        print("="*52)
