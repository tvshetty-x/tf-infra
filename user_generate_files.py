import os
print("Script started")
def create_file(path, content=""):
    if os.path.exists(path):
        print(f"[!] File already exists: {path}")
        return
    try:
        with open(path, 'w') as f:
            f.write(content)
        print(f"[✓] Created: {path}")
    except Exception as e:
        print(f"[✗] Error creating {path}: {e}")
def get_extension_choice():
    extensions = {
        "1": (".txt", "Text file"),
        "2": (".tf", "Terraform file"),
        "3": (".md", "Markdown"),
        "4": (".hcl", "HCL config"),
        "5": (".py", "Python file"),
        "6": (".log", "Log file")
    }
    print("\nChoose file type:")
    for key, (ext, desc) in extensions.items():
        print(f"  {key}. {ext}  →  {desc}")
    choice = input("Enter the number of the file type: ").strip()
    return extensions.get(choice, (None, None))
if __name__ == "__main__":
    folder = os.path.dirname(__file__)
    print("\n Welcome to Friendly File Creator!")
    while True:
        name = input("\n Enter file name (without extension) or type 'exit' to stop: ").strip()
        if name.lower() == "exit":
            print(" Exiting program.")
            break
        if not name:
            print(" File name cannot be empty.")
            continue
        ext, desc = get_extension_choice()
        if not ext:
            print("Invalid choice. Please try again.")
            continue
        full_name = f"{name}{ext}"
        full_path = os.path.join(folder, full_name)
        default_content = f"# This is a {desc} named {full_name}\n"
        create_file(full_path, default_content)