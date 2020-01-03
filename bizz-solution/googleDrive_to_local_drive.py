





import requests

def download_file_from_google_drive(id, destination):
    URL = "https://docs.google.com/uc?export=download"

    session = requests.Session()

    response = session.get(URL, params = { 'id' : id }, stream = True)
    token = get_confirm_token(response)

    if token:
        params = { 'id' : id, 'confirm' : token }
        response = session.get(URL, params = params, stream = True)

    save_response_content(response, destination)    

def get_confirm_token(response):
    for key, value in response.cookies.items():
        if key.startswith('download_warning'):
            return value

    return None

def save_response_content(response, destination):
    CHUNK_SIZE = 32768

    with open(destination, "wb") as f:
        for chunk in response.iter_content(CHUNK_SIZE):
            if chunk: # filter out keep-alive new chunks
                f.write(chunk)
file_id1 = '1-An-Bwm43j5XdjPflRyY4bnXnlKGVQJI'
file_id2 = '1PccBznZbXTbRHeKOl_KXjaCM34Mxm8iy'
file_id3 = '1vPhv7O8LSvpK2hL4I2OTUnVSg5g9cgyO'
file_id4 = '11NKLPeEQL8TFsTWBydQDzzE08mxgd5Dm'
file_id5 = '1I2SF79AmhtKtg56GHNsBqHxwW5XeZIQ2'
destination1 = 'google_drive/⁩days_of_order_in_a_week.png'
destination2 = 'google_drive/⁩top_20_prod.csv'
destination3 = 'google_drive/⁩books_read.png'
destination4 = 'google_drive/⁩file1.csv'
destination5 = 'google_drive/⁩myfile.ext'

download_file_from_google_drive(file_id1, destination1)   
download_file_from_google_drive(file_id2, destination2)   
download_file_from_google_drive(file_id3, destination3)   
download_file_from_google_drive(file_id4, destination4)   
download_file_from_google_drive(file_id5, destination5)   

