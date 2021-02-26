from seek import max_page, extract_jobs
from save import save_to_file

end_page = max_page()

jobs = extract_jobs(end_page)

save_to_file(jobs)

