import click
import subprocess


@click.group(help="CLI tool to manage learning branches in your python project.")
def app():
   pass

def save_old_branch_name(name):
    """Save the old branch name to a file."""
    with open('old_branch_name.txt', 'w') as f:
        f.write(name)

def load_old_branch_name():
    """Load the old branch name from a file."""
    try:
        with open('old_branch_name.txt', 'r') as f:
            name = f.read().strip()
            subprocess.run(["rm", "old_branch_name.txt"])
            return name
    except FileNotFoundError:
        return None


@click.command(help="Create a new learning branch, from main branch.")
@click.option('--name', '-n' ,prompt='Enter the branch to create', help='The name of the new branch you want to learn for this project')
def sl(name: str):
    """
    Create a new branch, install Jupyter Notebook, and create a new Jupyter Notebook file.

    Args:
        newBranchName (str): The name of the new branch.

    Returns:
        None
    """
    
    oldBranchName = subprocess.run(["git", "branch", "--show-current"], capture_output=True, text=True).stdout.strip()
    save_old_branch_name(oldBranchName)
    subprocess.run(["git", "checkout", "-b", "learn"+name])
    subprocess.run(["pip", "install", "-r", "jypter.txt"])
    subprocess.run(["touch", name+".ipynb"])


@click.command(help='Merge the changes from the learn branch to the main branch')
def ml():
    """
    Merge the changes from the current branch to the production branch.

    This function checks if the current branch contains the word "learn" in its name.
    If it does, it removes the "learn" prefix from the branch name, uninstalls the "jupyter" and "notebook" packages,
    deletes the corresponding notebook file, checks out the "production" branch, pulls the latest changes from the remote "production" branch,
    merges the changes from the learning branch to the "production" branch, and finally deletes the learning branch.

    If the current branch does not contain the word "learn" in its name, it displays a message indicating that it is not a learning branch.
    """
    oldBranchName = load_old_branch_name()
    if(oldBranchName == "None"):
        click.echo("You are not in learn branch")
        return
    currentBranch = subprocess.run(["git", "branch", "--show-current"], capture_output=True, text=True).stdout.strip()
    if("learn" in currentBranch):
        currentBranch = currentBranch[5:]
        subprocess.run(["pip", "uninstall", "-r", "jypter.txt", "-y"])
        subprocess.run(["rm", currentBranch+".ipynb"])
        try:
            subprocess.run(["git", "checkout", oldBranchName])
        
        except Exception as e:
            click.echo(str(e))
            
        subprocess.run(["git", "pull", "origin", oldBranchName])

        subprocess.run(["git", "merge", "learn"+currentBranch])
        subprocess.run(["git", "branch", "-d", "learn"+currentBranch])
    else:
        click.echo("You are not in a learning branch")
    

app.add_command(ml)
app.add_command(sl)


