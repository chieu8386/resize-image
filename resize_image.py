from PIL import Image
import glob
import os

def compress_images():
    input_folder = "input_data"
    output_folder = "output_data"
    
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
    extensions = ('*.jpg', '*.JPG', '*.JPEG', '*.jpeg', '*.PNG', '*.png')
    img_files = []
    for ext in extensions:
        img_files.extend(glob.glob(os.path.join(input_folder, ext)))
    if not img_files:
        print (f"Không có hình ảnh trong thư mục '{input_folder}'")
        return
    # input_file = img_files[0] #chỉ xử lý làn lượt 1 file khi chạy
    for input_file in img_files: # Dùng FOR để xử lý nhiều file
        base_name = os.path.basename(input_file)
        name, ext = os.path.splitext(base_name)
        output_file = os.path.join(output_folder, f"compress_{name}.jpg")
        print(f"Đang nén hình: {input_file}")
        try:
            with Image.open(input_file) as img:
                if img.mode in ("RGBA", "P"):
                    img = img.convert("RGB")
                width, height = img.size
                quality = 90
                scale_factor = 0.9
                while True:
                    img.save(output_file, "JPEG", quality = quality)
                    file_size = os.path.getsize(output_file)
                    if file_size <= 800 * 1024:
                        print(f"Hoàn tất {file_size / 1024:.2f} KB (Quality: {quality})")
                        break
                    quality -= 10
                    if quality < 40:
                        width = int (width * scale_factor)
                        height = int (height * scale_factor)
                        img = img.resize((width, height), Image.Resampling.LANCZOS)
                        quality = 80
                    if width < 10 or quality < 10:
                        break
                    #img.show()
        except Exception as e:
            print(f"Lỗi nén hình ảnh {e}")

if __name__ == "__main__":
    compress_images()
                    

