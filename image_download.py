from google_images_download import google_images_download

#test example
Keyword = ["car", "roads", "Ford Motor Company", "Karl Benz", "19ß8 Model T"]

# downloads images from google_images by list elements
def keywordPictures(List):
    for i in List:
        response = google_images_download.googleimagesdownload()
        arguments = {"keywords": i, "limit": 1, "print_urls": True, format:"jpg"}
        response.download(arguments)


