### Image Compression 
## English
# A lightweight Python script that automatically compresses images to meet specific file size requirements (under 800KB). It supports batch processing for multiple image formats.

Key Features:

  - Auto-compression: Iteratively reduces quality and resolution until the file size is below 800KB.
  
  - Batch Processing: Automatically scans the input_data folder for supported image formats.
  
  - Flexible Formats: Supports JPG, JPEG, and PNG.
  
  - Format Standardization: Converts all images to JPG during the compression process.

Folder Structure:

  - input_data/: Place your original images here.
  
  - output_data/: The folder where compressed images will be saved.
  
  - resize_image.py: The main script to execute the compression.

Requirements:

  - Python 3.x
  
  - Pillow library: pip install Pillow

Usage:

  - Install the requirement: pip install Pillow
  
  - Place your images into the input_folder.
  
  - Run the script: python resize_image.py.
  
  - Your compressed images will be ready in the output_folder.

## Tiếng Việt
# Một script Python nhỏ gọn giúp tự động nén hình ảnh để đạt được kích thước tệp mong muốn (dưới 800KB). Hỗ trợ xử lý hàng loạt nhiều định dạng ảnh khác nhau.

Tính năng chính:

  - Tự động nén: Tự động điều chỉnh chất lượng và kích thước ảnh cho đến khi tệp nhỏ hơn 800KB.
  
  - Xử lý hàng loạt: Tự động quét thư mục input_data để tìm và nén tất cả ảnh có sẵn.
  
  - Định dạng đa dạng: Hỗ trợ JPG, JPEG, và PNG.
  
  - Chuẩn hóa định dạng: Chuyển đổi tất cả ảnh sang định dạng JPG sau khi nén.

Cấu trúc thư mục:

  - input_folder/: Nơi chứa các ảnh gốc cần nén.
  
  - output_folder/: Nơi lưu trữ ảnh sau khi đã nén.
  
  - resize_image.py: Script chính thực hiện quá trình nén ảnh.

Yêu cầu:

  - Python 3.x
  
  - Thư viện Pillow: pip install Pillow

Cách sử dụng:

  - Cài đặt thư viện: pip install Pillow
  
  - Đặt các ảnh cần nén vào thư mục input_data/.
  
  - Chạy script: python resize_image.py.
  
  - Nhận ảnh đã nén tại thư mục output_data/
