import os
import requests

# Configuration
folder_path = '/Users/ethanhumphreys/Desktop/photos'
webhook_url = 'https://discord.com/api/webhooks/1247172560278257664/gTM-YDVeVGyXSvZ-5bq2JqzWpS87tBdpG_CSCnbJ7dslWh1s1Wy2XgsgTEzSgF48o0YP'

def post_image_to_discord(image_path, webhook_url):
    with open(image_path, 'rb') as image_file:
        files = {'file': image_file}
        response = requests.post(webhook_url, files=files)
        if response.status_code == 204:
            print(f'Successfully posted {image_path}')
        else:
            print(f'Failed to post {image_path}. Status code: {response.status_code}')

def main():
    if not os.path.exists(folder_path):
        print(f'Folder path {folder_path} does not exist.')
        return

    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)
        if os.path.isfile(file_path):
            post_image_to_discord(file_path, webhook_url)
            
if __name__ == '__main__':
    main()
