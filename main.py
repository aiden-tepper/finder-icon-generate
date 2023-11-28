import os
from openai import OpenAI
from applescript import tell

client = OpenAI(
    api_key="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",
)

def generate_image(prompt):
    response = client.images.generate(
        prompt=prompt,
        size="256x256",
        n=1
    )

    image_url = response.date[0].url

    return image_url

def change_icon(folder_path, image_url):
    script = f"""
    tell application "Finder"
        set iconFile to POSIX file "{image_url}" as alias
        set folderToChange to POSIX file "{folder_path}" as alias
        set icon of folderToChange to iconFile
    end tell
    """
    tell(script)

def main():
    # Replace with the actual paths of the folders you want to change
    folders = ['/path/to/folder1', '/path/to/folder2']

    for folder in folders:
        # Use the folder name as the prompt for DALL-E
        folder_name = os.path.basename(folder)

        # Generate an image based on the folder name
        image_url = generate_image(folder_name)

        # Change the folder's icon to the generated image
        change_icon(folder, image_url)
