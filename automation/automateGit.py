import bpy
import subprocess
from datetime import date

today = date.today()

# Get the project directory automatically
project_directory = bpy.path.abspath("//")
print(bpy.data.scenes.keys())

# Get the current Blender file name
blend_file_name = bpy.data.filepath.split("/")[-1]

# Commit Message
with open(bpy.path.abspath("//documentaion"), 'r') as object:
    lines = object.readlines()
    print(bpy.path.abspath("//documentaion"))

    commit_message = lines[-1] + today.strftime("%B %d, %Y")


def push_blendfile_to_github(dummy):
    # Add only the Blender file
    # subprocess.run(["git", "-C", project_directory, "add", blend_file_name])

    # Add every file in the directory
    subprocess.run(["git", "-C", project_directory, "add", "."])
    # Commit
    subprocess.run(["git", "-C", project_directory, "commit", "-m", commit_message])
    # Push
    subprocess.run(["git", "-C", project_directory, "push"])


# Register the function to execute when the file is saved
bpy.app.handlers.save_post.append(push_blendfile_to_github)

# Run the function once to ensure the initial commit
# push_blendfile_to_github(None)
