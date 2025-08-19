import os
def create_file(file_name,content=""):
    if os.path.exists(file_name):
        print(f"File already exists: {file_name}")
        return
    try:
        with open(file_name,'w') as f:
            f.write(content)
        print(f"Created: {file_name}")
    except Exception as e:
        print(f"Error with {file_name}:{e}")
if __name__=="__main__":
    folder=os.path.dirname(__file__)
    files_to_create={
        "main.tf":"#Terraform configuration file\n",
        "variables.tf":"#Terraform variables\n",
        "outputs.tf":"#Terraform outputs\n",
        "README.md":"#tf-infra Setup\n This folder contains Terraform code.",
        "setup.hcl":"env = \"dev\"\nregion=\"ap-south-1\"",
        "notes.txt":"Deployment notes and TODOs."
    }
    for name, content in files_to_create.items():
        path=os.path.join(folder,name)
        create_file(path,content)
