import csv
hours_per_month = 730
def load_vms(filename:str):
    vms=[]
    with open(filename, newline="") as f:   
        reader=csv.DictReader(f)
        for row in reader:
            row["cpu"] = int(row["cpu"])
            row["ram_gb"] = int(row["ram_gb"])
            row["cost_per_hour"] = float(row["cost_per_hour"])  
            vms.append(row)
    return vms
def filter_prod_vms(vms): 
    return [vm for vm in vms if vm["environment"]=="prod"]  
def calculate_monthly_cost(vms):
    """Total monthly cost for all given VMs."""
    return sum(vm["cost_per_hour"] * hours_per_month for vm in vms)

def sort_vm_top_n(vms,n=3):
    return sorted(vms, key=lambda vm: vm["cost_per_hour"], reverse=True)[:n]

if __name__ == "__main__":
    all_vms = load_vms("vms.csv")
    prod_vms = filter_prod_vms(all_vms)
    total_cost = calculate_monthly_cost(prod_vms)
    print(f"Total monthly cost for production VMs: ${total_cost}")
    print("number of vms", len(prod_vms))
    top_vms = sort_vm_top_n(prod_vms, n=3)
    print("top 3 most expensive VMs:")
    for vm in top_vms:
        print (f" -{vm['name']}: ${vm['cost_per_hour']}/hour")
    