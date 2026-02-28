import etl
import subprocess
if __name__ == "__main__":
    etl.run_etl()
    subprocess.run(["python", "dashboard.py"])
