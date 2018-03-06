import ImageAPI as imapi

base_path = ''
bin_dir = "binaries"
image_dir = "images"
image_urls = []
image_file_path = "imageurls/imageurls.txt"

imapi = imapi.ImageAPI(image_file_path, base_path, bin_dir, image_dir)

download_paths = imapi.download_images()
imapi.load_images(download_paths)

