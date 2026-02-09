import json
import subprocess
import yaml
import sys

# Configuration
USERNAME = "atharvved09"
OUTPUT_FILE = "_data/projects.yml"
# Repos to include can be managed here, or we can fetch everything
# For now, we will fetch everything and filter by this list if it's not empty, 
# or just include everything if the user wants. 
# The user asked to "include all private repos", so we might want to be broader.
# But sticking to the initial list + enabling easy addition is safer.
INCLUDE_REPOS = [
    "Bioinformatics-DB",
    "cas-offinder",
    "CRISPRitz",
    "CRISPRme",
    "examples-scikit-bio",
    "sort_animation",
    "openclaw",
    "atharvved09.github.io"
]

def fetch_repos_gh_cli():
    """Fetches repositories using GitHub CLI (gh)."""
    # specific fields to fetch
    fields = "name,description,url,homepageUrl,primaryLanguage,stargazerCount,updatedAt,visibility"
    cmd = [
        "gh", "repo", "list", USERNAME,
        "--limit", "200",
        "--json", fields
    ]
    
    try:
        result = subprocess.run(cmd, capture_output=True, text=True, check=True)
        return json.loads(result.stdout)
    except subprocess.CalledProcessError as e:
        print(f"Error running gh cli: {e}")
        print(f"Standard Error output:\n{e.stderr}")
        print("Ensure 'gh' is installed and you are authenticated (gh auth login).")
        return []
    except FileNotFoundError:
        print("GitHub CLI ('gh') not found. Please install it.")
        return []

# Load enhancements
try:
    with open("_data/repo_enhancements.yml", "r") as f:
        REPO_ENHANCEMENTS = yaml.safe_load(f) or {}
except FileNotFoundError:
    REPO_ENHANCEMENTS = {}

def generate_summary(repo):
    """
    Generates a 'rosey' summary for the repository.
    """
    name = repo["name"]
    
    # Check if we have an enhanced summary
    if name in REPO_ENHANCEMENTS:
        return REPO_ENHANCEMENTS[name].get("summary", "")

    language = (repo.get("primaryLanguage") or {}).get("name", "Unknown")
    description = repo.get("description") or f"A project developed using {language}."
    
    return description

def update_data():
    """Updates the _data/projects.yml file."""
    print("Fetching repositories via GitHub CLI...")
    repos = fetch_repos_gh_cli()
    
    if not repos:
        print("No repositories found or error occurred.")
        return

    projects = []
    print(f"Found {len(repos)} repositories.")

    for repo in repos:
        # If we stick to the allow-list:
        is_private = repo.get("visibility") == "PRIVATE"

        # Include if it is in the allow-list OR if it is a private repository
        # This addresses the user's request to "cover the work in private repos"
        if repo["name"] not in INCLUDE_REPOS and not is_private:
            continue

        print(f"Processing {repo['name']}...")
        
        
        # Get description from enhancements if available, otherwise from repo
        enhanced_data = REPO_ENHANCEMENTS.get(repo["name"], {})
        description = enhanced_data.get("description", repo.get("description", ""))

        project = {
            "name": repo["name"],
            "description": description,
            "summary": generate_summary(repo),
            "url": None if is_private else repo["url"],
            "homepage": repo.get("homepageUrl", ""),
            "language": (repo.get("primaryLanguage") or {}).get("name", ""),
            "stars": repo.get("stargazerCount", 0),
            "updated_at": repo.get("updatedAt", ""),
            "featured": repo["name"] in ["Bioinformatics-DB", "sort_animation"],
            "visibility": "Private" if is_private else "Public"
        }
        projects.append(project)

    # Write to YAML
    with open(OUTPUT_FILE, "w") as f:
        yaml.dump(projects, f, sort_keys=False)
    
    print(f"Successfully updated {OUTPUT_FILE} with {len(projects)} projects.")

if __name__ == "__main__":
    update_data()
