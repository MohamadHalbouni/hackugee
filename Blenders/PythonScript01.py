import bpy
import subprocess

# Get the project directory automatically
project_directory = bpy.path.abspath("//")
    
# Get the current Blender file name
blend_file_name = bpy.data.filepath.split("/")[-1]

# Commit Message
commit_message = "ThisIsBlender"


def push_blendfile_to_github(dummy):
    
    # Add only the Blender file
    #subprocess.run(["git", "-C", project_directory, "add", blend_file_name])
    
    # Add every file in the directory
    subprocess.run(["git", "-C", project_directory, "add", "."])
    # Commit
    subprocess.run(["git", "-C", project_directory, "commit", "-m", commit_message ])
    # Push
    subprocess.run(["git", "-C", project_directory, "push"])
    
# Register the function to execute when the file is saved
bpy.app.handlers.save_post.append(push_blendfile_to_github)

# Run the function once to ensure the initial commit
#push_blendfile_to_github(None)
