import csv

def save_to_file(jobs):
    file = open("jobs.csv", mode="w")
    writer = csv.writer(file)
    writer.writerow(['Title','Company','Location','Salary','Description','link'])

    for job in jobs:
        writer.writerow(list(job.values()))

    return
